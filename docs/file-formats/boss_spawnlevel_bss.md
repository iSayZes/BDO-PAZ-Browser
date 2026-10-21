# `boss_spawnlevel.bss` Format

## Purpose

The difficulty levels of the Guild Boss Summon window
(`panel_guild_bosssummon_all`): per guild boss, one 21-byte entry per level
with the reward item, the window image and the boss character. The window
reads an entry through `ToClient_bossSpawnOptionWrapper(bossKey, level)`
(`getImagePath()`, `getItemEnchantKey()`). The boss key is the key of
[`boss_spawn.bss`](boss_spawn_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records           | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ----------------- | --------- |
| 2      | 3473 and later | 3474    | `boss_spawnlevel.bss` | 1,070 | 24 Entry, 6 Group | 21        |
| 1      | 1485 to 3251   | 3251    | `boss_spawnlevel.bss` | 761   | 20 Entry, 5 Group | 19        |

| Layout | File                  | Known         | Unknown       |
| ------ | --------------------- | ------------- | ------------- |
| 2      | `boss_spawnlevel.bss` | 926 B (86.5%) | 144 B (13.5%) |
| 1      | `boss_spawnlevel.bss` | 641 B (84.2%) | 120 B (15.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 2 |
| 3473   | Layout 2 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. Character names come from LOC type 6, reward names from LOC type 0.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type               | Field        | Notes                                                      |
| ------------------- | ------------------ | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]            | magic        | `PABR`                                                     |
| `+0x04`             | u32                | group_count  | `6` on client 3464, one group per boss                     |
| `+0x08`             | Group[group_count] | groups       | Variable size; the last ends where the string table starts |
| `groups+0x00`       | String Table       | string_table | Counted string table (`_common/pabr_strings.py`), UTF-16 image paths |
| `string_table+0x00` | u32                | table_start  | Offset of the string table                                 |
| `string_table+0x04` | u32                | zero         |                                                            |

### Group (variable: 4 bytes + entries)

| Offset  | Type                 | Field       | Notes              |
| ------- | -------------------- | ----------- | ------------------ |
| `+0x00` | u32                  | entry_count | `4` on every group |
| `+0x04` | Entry[entry_count]   | entries     | See Entry          |

### Entry (21 bytes)

| Offset  | Type | Field          | Notes                                                                  |
| ------- | ---- | -------------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | boss_key       | `boss_spawn.bss` key; the same on every entry of a group               |
| `+0x04` | u8   | level          | `0` to `3`, the second argument of `ToClient_bossSpawnOptionWrapper`   |
| `+0x05` | u16  | unknown_05     | `1` on every entry                                                     |
| `+0x07` | u16  | unknown_07     | Falls by 1 per level within a group (65308 to 65305 for Ferrid); see Open Questions |
| `+0x09` | u32  | reward_item_id | `getItemEnchantKey()`: the boss's Small, Medium, Large and Extra Large Reward |
| `+0x0D` | u32  | image          | String index: `getImagePath()`, relative to `ui_texture/`              |
| `+0x11` | u16  | unknown_11     | A character ID; equals `character_id` except on Khan and Gumiho & Duoksini |
| `+0x13` | u16  | character_id   | The boss character, LOC type 6                                        |

The groups on client 3464:

| Key | Boss              | character_id (levels 0 to 3) | Rewards          |
| --- | ----------------- | ---------------------------- | ---------------- |
| 1   | Ferrid            | 28856 to 28853               | 756210 to 756213 |
| 2   | Moghulis          | 29700 to 29697               | 756214 to 756217 |
| 3   | Giant Mudster     | 28852 to 28849               | 756206 to 756209 |
| 4   | Org               | 29696 to 29693               | 756275 to 756278 |
| 5   | Khan              | 23843 to 23840               | 756218 to 756221 |
| 8   | Gumiho & Duoksini | 27897, 27895, 27894, 29539   | 790880, 790877, 790878, 790879 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                  |
| ------- | ------------------ | ------------ | -------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                      |
| `+0x04` | pstr[string_count] | strings      | Image paths; `image` indexes this list |

## Layout 1

On client 1784 the entry ends after `unknown_11`: it is 19 bytes and has no
`character_id`. Only the Entry differs from Layout 2.

### Entry (19 bytes)

| Offset  | Type | Field          | Notes                                                              |
| ------- | ---- | -------------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | boss_key       |                                                                    |
| `+0x04` | u8   | level          |                                                                    |
| `+0x05` | u16  | unknown_05     |                                                                    |
| `+0x07` | u16  | unknown_07     |                                                                    |
| `+0x09` | u32  | reward_item_id |                                                                    |
| `+0x0D` | u32  | image          |                                                                    |
| `+0x11` | u16  | unknown_11     | Key 4 holds 27198, 27197, 27196 and 27186, the Khan values of `unknown_11` on client 3473 |

Client 1784 has 4 groups (keys 1 to 4) of 4 entries.

## Notes

- `unknown_11` on Khan is 27198, 27197, 27196 and 27186, a "Khan" with the model
  `monster/partyleader/ocean_bellj_boss_ghost`, while `character_id` is the
  Khan of `monster/m0423_ocean_boss_junior_boss`. On Gumiho & Duoksini
  `unknown_11` is the `monster/guildraidboss/mainreward_guildraid` character
  and `character_id` the nine-tailed fox (`m0498_ninetailedfox_guildraid`).
- The string table has one image per group, in group order; the client
  ships more `GuildBoss_Renewal_*` images (`Gamos`) than the file uses.
- The window prints the level with `LUA_GUILD_BOSSSUMON_DIFFICULTYCOUNT`.

## Open Questions

### unknown_07

Two runs of values: 65301 to 65316 on Ferrid, Giant Mudster and Khan, and
62810 to 62856 on Moghulis, Org and Gumiho & Duoksini, falling by 1 per
level. They are not character IDs or `guildquest.dbss` keys, and the four
checked in LOC (65308, 62856, 65316, 62813) only match unrelated type 0
item names.

### unknown_11

A character ID that equals `character_id` on four of the six bosses. On
Khan and Gumiho & Duoksini it is a different character (a party leader
ghost, a main reward object), which may be the character the summon places
first, but no Lua call names it.
