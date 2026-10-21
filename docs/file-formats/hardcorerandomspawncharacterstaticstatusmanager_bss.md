# `hardcorerandomspawncharacterstaticstatusmanager.bss` Format

## Purpose

The characters that spawn at random on the Hardcore channel, one 19-byte
row each: the character, five string-table references (world map icon,
boss icon, notice background and two notice keys) and a random spawn key.
Two key lists follow the rows, the bosses and the NPCs, then a list of
string-table indexes. On client 3474 the 12 rows are four Wandering
Merchants and six Lights of Offering on the NPC list, and the bosses
Laytenn and Ancient Puturum. The characters are
[`characterstatic.dbss`](characterstatic_dbss.md) keys.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                                  | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------------------------------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `hardcorerandomspawncharacterstaticstatusmanager.bss` | 1,620 | 12 Row  | 19        |

| Layout | File                                                  | Known           | Unknown      |
| ------ | ----------------------------------------------------- | --------------- | ------------ |
| 1      | `hardcorerandomspawncharacterstaticstatusmanager.bss` | 1,516 B (93.6%) | 104 B (6.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | No file  |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                    |
| --------------------- | -------- | ----------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Character names (LOC type 6); notice text, LOC type 37 under the RESOURCE sheet key hash |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                   | Type                          | Field                 | Notes                                                                |
| ------------------------ | ----------------------------- | --------------------- | -------------------------------------------------------------------- |
| `+0x00`                  | char[4]                       | magic                 | ASCII `PABR`                                                         |
| `+0x04`                  | u32                           | row_count             | Number of rows                                                       |
| `+0x08`                  | Row[row_count]                | rows                  | See Row; byte-packed                                                 |
| `rows+0x00`              | u32                           | boss_count            | Number of `boss_keys`                                                |
| `rows+0x04`              | u16[boss_count]               | boss_keys             | `random_spawn_key` of each boss row; `ToClient_getHardCoreBossKeyByIndex` |
| `boss_keys+0x00`         | u32                           | npc_count             | Number of `npc_keys`                                                 |
| `boss_keys+0x04`         | u16[npc_count]                | npc_keys              | `random_spawn_key` of each NPC row                                   |
| `npc_keys+0x00`          | u32                           | unknown_str_ref_count | Number of `unknown_str_refs`; equals `string_count` on client 3474   |
| `npc_keys+0x04`          | u32[unknown_str_ref_count]    | unknown_str_refs      | String-table indexes `0` to `15` in order on client 3474             |
| `unknown_str_refs+0x00`  | String Table                  | string_table          | See String Table                                                     |
| `string_table+0x00`      | u32                           | table_start           | Offset of the string table, where `unknown_str_refs` ends            |
| `string_table+0x04`      | u32                           | zero                  | Always `0`                                                           |

### Row (19 bytes)

| Offset  | Type | Field                 | Notes                                                                                                    |
| ------- | ---- | --------------------- | -------------------------------------------------------------------------------------------------------- |
| `+0x00` | u16  | character_key         | [`characterstatic.dbss`](characterstatic_dbss.md) key; `ToClient_getHardCoreCharaterKeyByRandomSpawnCharaterKey` |
| `+0x02` | i16  | world_map_icon_ref    | String-table index of the world map icon texture (`Combine_WorldMap_HardcoreServer_*`)                   |
| `+0x04` | i16  | boss_icon_ref         | String-table index of the boss info icon texture, `-1` on the NPC rows; `ToClient_getHardCoreBossUIIconTextureID` |
| `+0x06` | i16  | notice_background_ref | String-table index of the notice background texture (`Combine_Etc_HardcoreServer_*_NakBG`)                |
| `+0x08` | i16  | notice_ref            | String-table index of the RESOURCE sheet key of the spawn notice (`PANEL_BIGNAK_HARDCOREMESSAGE_<n>`)     |
| `+0x0A` | i16  | reveal_notice_ref     | String-table index of the RESOURCE sheet key of the "World Map location revealed" notice, `-1` on the NPC rows |
| `+0x0C` | u8   | unknown_0c            | `1` on the NPC rows, `0` on the boss rows                                                                |
| `+0x0D` | u32  | random_spawn_key      | Random spawn key, unique; the key the two lists hold                                                     |
| `+0x11` | u16  | unknown_11            | Always `0`                                                                                               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                  |
| ------- | ------------------ | ------------ | ------------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings; `16` on client 3474                 |
| `+0x04` | pstr[string_count] | strings      | UTF-16LE texture IDs and RESOURCE sheet keys            |

## Random Spawns

Client 3474, with the notice text of LOC type 37:

| `random_spawn_key` | Character (key)            | List | Spawn notice                              | Reveal notice                 |
| ------------------ | -------------------------- | ---- | ----------------------------------------- | ----------------------------- |
| `1` to `4`         | Wandering Merchant (62223 to 62226) | NPC  | The Wandering Merchant Visits     |                               |
| `11` to `16`       | Light of Offering (62200)  | NPC  | Light of Offering                         |                               |
| `21`               | Laytenn (29496)            | Boss | Laytenn, the Ancient Destroyer (World Map reveal in 5 min.) | World Map location revealed |
| `22`               | Ancient Puturum (29497)    | Boss | Frenzied Ancient Puturum (World Map reveal in 5 min.) | World Map location revealed |

## Field Names

The Hardcore channel is newer than client 1784: no sheet of a private
server's `DataSheets.bexcel` on that client and no string of its server
dump has `HardCore` in the name. The world map of client 3474
(`grand_worldmap_mainpanel.luac`, `PaGlobalFunc_UpdateHardCoreBossListUI`)
walks the bosses with `ToClient_getHardCoreBossKeyByIndex(index)`, turns
each random spawn key into a character with
`ToClient_getHardCoreCharaterKeyByRandomSpawnCharaterKey(key)` and that
character's `getName()`, and sets the boss image with
`ToClient_getHardCoreBossUIIconTextureID(key)`. The boss list holds the
`random_spawn_key` of the two boss rows, and those rows' `boss_icon_ref`
strings are the `..._Map_BossInfoIcon_Raiten` and `..._Puturum` textures.
The other refs are named by their strings: a world map icon, a notice
background (`NakBG`, "big nak" being the client's name for its large
centre-screen notice) and two `PANEL_BIGNAK_HARDCOREMESSAGE_<n>` keys,
whose LOC text announces the spawn and, for a boss, the reveal on the world
map.

## Notes

- The file is byte-identical on clients 3002, 3251 and 3474; clients 1784
  and 2519 do not ship it.
- The row refs index the string table directly, and `unknown_str_refs` maps
  every index to itself, so both readings give the same string on client
  3474.
- The compass widget (`panel_widget_compass_hardcore_1.luac`) builds one
  icon per `ToClient_getHardCoreMaxRandomNpcCount()` and per
  `ToClient_getHardCoreMaxBossCount()`; the NPC and boss lists hold 10 and
  2 keys on client 3474.
- The parser is `_bss/hardcorerandomspawncharacterstaticstatusmanager/parser.py`.
  The preview shows each row with its character name, its list, the four
  texture and key strings and the LOC text of both notices.

## Open Questions

### Row Flag and String Index List

What `unknown_0c` and `unknown_str_refs` are. `unknown_0c` is `1` exactly
on the rows of the NPC list, so it may be the list a row goes on, which the
two lists also give. `unknown_str_refs` lists each string once in table
order; whether the row refs go through it or straight to the table cannot
be told while it maps every index to itself.
