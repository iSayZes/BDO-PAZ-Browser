# `bossinfostaicstatusmanager.bss` Format

## Purpose

The bosses of the Boss Info window (`panel_worldmap_bosslist_all`, opened
from the world map): one variable-length record per boss with its tab, its
character, an optional reinforced form, the window's two images, the main
rewards, a world position and, for world bosses, the weekly spawn times. The
window reads a record through `ToClient_getBossStaticStatus(index)`. On
client 3464 the 28 records are 14 World bosses, the 5 Field bosses, 6 Dark
Rift bosses and 3 Hunting/Sniper bosses. The file name spells "staic" for
"static".

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes | Records                                                    | Row bytes               |
| ------ | -------------- | ------- | -------------------------------- | ----- | ---------------------------------------------------------- | ----------------------- |
| 1      | 3473 and later | 3474    | `bossinfostaicstatusmanager.bss` | 7,396 | 58 Group List, 29 Boss Record, 52 Group, 8 Reinforced Form | 4 to 126, 32 on average |

| Layout | File                             | Known           | Unknown     |
| ------ | -------------------------------- | --------------- | ----------- |
| 1      | `bossinfostaicstatusmanager.bss` | 7,367 B (99.6%) | 29 B (0.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3473   | Layout 1 |
| 3251   | No file  |
| 3002   | No file  |
| 2519   | No file  |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                                                 | Required | Role                                                                 |
| ---------------------------------------------------- | -------- | -------------------------------------------------------------------- |
| `stringtable.bss`                                    | Optional | Tab names, keys `LUA_WORLDMAP_BOSSLIST_TOOLTIP_<boss_info_type>`     |
| `ui_texture/texturestringkey/texturestring_combine.xml` | Optional | Resolves the texture keys to a DDS file and a UV rectangle           |
| `languagedata_en.loc`                                | Optional | LOC type 6 boss names, LOC type 0 reward item names                  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                      | Field        | Notes                                                          |
| ------------------- | ------------------------- | ------------ | -------------------------------------------------------------- |
| `+0x00`             | char[4]                   | magic        | `PABR`                                                         |
| `+0x04`             | u32                       | record_count | `28` on client 3464                                            |
| `+0x08`             | Boss Record[record_count] | records      | Variable size; the last one ends where the string table starts |
| `records+0x00`      | String Table              | string_table | Counted string table (`_common/pabr_strings.py`)               |
| `string_table+0x00` | u32                       | table_start  | Offset of the string table                                     |
| `string_table+0x04` | u32                       | zero         |                                                                |

### Boss Record (variable: 30 bytes + lists and reinforced form)

| Offset               | Type                               | Field             | Notes                                                                 |
| -------------------- | ---------------------------------- | ----------------- | --------------------------------------------------------------------- |
| `+0x00`              | Group List                         | spawn_times       | See Group List; empty on every non-World record                       |
| `spawn_times+0x00`   | Group List                         | unknown_ids       | Same groups and lengths as `spawn_times`, one ID per time; see Open Questions |
| `unknown_ids+0x00`   | u32                                | reward_item_count | Number of `reward_items`                                              |
| `unknown_ids+0x04`   | u32[reward_item_count]             | reward_items      | Item IDs: the "Main Rewards" row of the window                        |
| `reward_items+0x00`  | u32                                | main_texture      | String index of the large boss image (`Img_` key)                     |
| `reward_items+0x04`  | u32                                | list_texture      | String index of the list entry image; always `main_texture + 1`       |
| `reward_items+0x08`  | u16                                | character_id      | `characterstatic.dbss` character ID, LOC type 6                       |
| `reward_items+0x0A`  | u8                                 | has_reinforced    | `0` or `1`; when `1`, the Reinforced Form follows                     |
| `reward_items+0x0B`  | Reinforced Form if has_reinforced = 1 | reinforced     | See Reinforced Form                                                   |
| `reinforced+0x00`    | f32[3]                             | position          | World position; the second value is the height                       |
| `reinforced+0x0C`    | u8                                 | boss_info_type    | Window tab, see [Boss Info Types](#boss-info-types)                   |
| `reinforced+0x0D`    | u8                                 | unknown_flag      | `1` on the 14 World records, `0` on the rest                          |
| `reinforced+0x0E`    | u8                                 | is_event_boss     | `1` only on 21878 Gift Box; see Notes                                 |

### Reinforced Form (variable: 14 bytes + rewards)

| Offset                          | Type                              | Field                        | Notes                                                           |
| ------------------------------- | --------------------------------- | ---------------------------- | --------------------------------------------------------------- |
| `+0x00`                         | u16                               | reinforced_character_id      | The reinforced form (23172 Nightmarish Kzarka for 23001 Kzarka) |
| `+0x02`                         | u32                               | reinforced_main_texture      | String index                                                    |
| `+0x06`                         | u32                               | reinforced_list_texture      | String index                                                    |
| `+0x0A`                         | u32                               | reinforced_reward_item_count | Number of `reinforced_reward_items`                             |
| `+0x0E`                         | u32[reinforced_reward_item_count] | reinforced_reward_items      | Item IDs                                                        |

The reinforced form stores its textures before its rewards, the reverse of
the Boss Record's `reward_items`, `main_texture` and `list_texture`.

### Group List (variable: 4 bytes + groups)

| Offset  | Type               | Field       | Notes                        |
| ------- | ------------------ | ----------- | ---------------------------- |
| `+0x00` | u32                | group_count | `0`, or `2` on World records |
| `+0x04` | Group[group_count] | groups      | See Group                    |

The group keys are `0` then `1` on every record that has groups.

### Group (variable: 5 bytes + values)

| Offset  | Type             | Field       | Notes                 |
| ------- | ---------------- | ----------- | --------------------- |
| `+0x00` | u8               | group_key   | `0` or `1`            |
| `+0x01` | u32              | value_count | Number of `values`    |
| `+0x05` | u32[value_count] | values      | The group's values    |

### String Table (variable: 4 bytes + strings)

The string table holds the texture keys, an `Img_` key followed by the list
key for each image set (`Combine_Etc_WorldMap_BossList_Img_Begg`,
`Combine_Etc_WorldMap_BossList_Begg`): 60 strings for 30 sets on client
3464.

| Offset  | Type               | Field        | Notes                                    |
| ------- | ------------------ | ------------ | ---------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                        |
| `+0x04` | pstr[string_count] | strings      | Texture keys; the texture fields index this list |

## Boss Info Types

The window tab, named by `stringtable.bss` key
`LUA_WORLDMAP_BOSSLIST_TOOLTIP_<n>`.

| Value | Tab            | Records (client 3464)                                                    |
| ----- | -------------- | ------------------------------------------------------------------------ |
| 0     | World          | 14: Gift Box, Kzarka, Nouver, Karanda, Kutum, Offin, Garmoth, Vell, Quint, Muraka, Bulgasal, Uturi, Sangoon, Golden Pig King |
| 1     | Field          | 5: Dastard Bheg, Red Nose, Dim Tree Spirit, Giant Mudster, Katzvariak    |
| 2     | Dark Rift      | 6: Red Nose, Dastard Bheg, Muskan, Dim Tree Spirit, Ferrid, Griffon (25501 to 25531) |
| 3     | Hunting/Sniper | 3: Rawr-Rawr, Blue Whale, Fugitive Khalk                                 |
| 4     | Event          | None in the file                                                         |

`TOOLTIP_5` is "Hunting", the console name of tab 3.

## Notes

- The Lua calls on a record are `getBossInfoType()`,
  `getCharacterKeyRaw(isReinforce)`, `getCharacterName(isReinforce)`,
  `getMainTextureID(isReinforce)`, `getSubTextureID(isReinforce)`,
  `getRewardItemKeyListSize(isReinforce)` / `getRewardItemKeyByIndex`,
  `getPosition()`, `getNextSpawnLeftTime(serverUtc)` and `isEventBoss()`.
  `ToClient_isReinforceBoss(index)` picks the form.
- A record without spawn times is the window's "Random Spawn"
  (`LUA_WORLDMAP_BOSSLIST_RANDOM_APPEAR`): the Lua shows it when
  `getNextSpawnLeftTime` returns `-1`, and all five Field bosses show it in
  game while their `spawn_times` are empty.
- Dastard Bheg's 12 `reward_items` (11015 Bheg's Gloves, 8904 Concentrated
  Boss Crystal, 42435 Latent Boss Aura, 44926 Awakening Weapon Box, 15992
  Liverto Weapon Bundle, 15606 Ancient Magic Crystal of Crimson Flame -
  Power, 757010 Mythical Feather, 721002 Ancient Spirit Dust, 17839 and
  17829 Advice of Valks (+40) and (+30), 752023 Mass of Pure Magic, 768495
  Ode to Heroes of Yore) are the window's Main Rewards row in order.
- `is_event_boss` drives the event tag on a list entry
  (`eventTag:SetShow(bossInfo:isEventBoss() == true)`); 21878 Gift Box, the
  one record with it set, is an event boss with its own `Gift` image set.
- Quint and Muraka have the same `spawn_times` and the same `unknown_ids`
  (`158, 139` and `556, 560`), the only IDs shared by two records. They
  spawn together in game.
- The 8 reinforced forms have their own reward lists; 23001 Kzarka's
  reinforced list adds 4 items and drops 4. All reward values are below
  `2^24`, so they are item IDs with no enhancement level.
- Both groups of a World record hold the same number of times, but only
  Garmoth (13 of 14 times) and Vell have group 1 at group 0 minus 420
  minutes; the other bosses' groups are two unrelated timetables.
- The four Land of the Morning Light bosses (Bulgasal, Uturi, Sangoon,
  Golden Pig King) each have their own reinforced character (28733 to
  28736), all named Dark Bonghwang with the same model and the
  `Blackphoenix` image set.
- Khalk's two texture keys are spelled differently
  (`Combine_Etc_WorldMap_BossList_Img_Kalk`, `..._Kark`); both resolve in
  `texturestring_combine.xml`, so the pairing is by string index, not name.
- `fieldboss.dbss` holds every Field record's character, but it is a
  different list (694 characters); see [fieldboss](fieldboss_dbss.md).

## Open Questions

### unknown_ids

One u32 per spawn time, `101` to `1102` on client 3464, unique except for
the Quint and Muraka pair. The boss alert Lua (`panel_bossalert_alarm`)
works from character keys and times only, so nothing in Lua names these.

### unknown_flag

`1` on exactly the World records. The Lua only enables the Boss
Notification button on the World tab, but it decides that by tab, not by a
record field, so the byte cannot be told apart from the tab.

## In-Game Checks

### spawn_times as Minutes of the Week

Needs zone: anywhere with the world map

Every value is below 10,080, the minutes in a week. Open the world map,
then Boss Info on the World tab, and note the clock time with the countdown
of Kzarka, Garmoth and Vell. If each countdown ends on a value of one group
read as day `value // 1440` and minute of day `value % 1440` from the same
week start, `spawn_times` are minutes of the week; the group that matches
is the one this client's region uses (the other may be the second service
region of the same client), and the offset gives the week start.
