# `guildbossfieldinfo.bss` Format

## Purpose

A world position per guild boss, keyed by the [`boss_spawn.bss`](boss_spawn_bss.md)
key. The Guild Boss Summon window (`panel_guild_bosssummon_all`) offers to
enter or leave the guild boss field (a mirror field,
`__eMirrorFieldContentsKey_GuildBossField`) only where
`ToClient_IsInGuildBossFieldPos(bossKey)` is true, and
`ToClient_CheckUseGuildBossField(bossKey)` tells whether a boss uses one.
On client 3474 the file has 6 rows, one for each `boss_spawn.bss` boss,
each near that boss's spawn point. The file is a u32 count and fixed rows,
with no PABR magic and no string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | ------- | --------- |
| 1      | 2107 and later | 3474    | `guildbossfieldinfo.bss` | 148   | 6 Row   | 24        |

| Layout | File                     | Known         | Unknown      |
| ------ | ------------------------ | ------------- | ------------ |
| 1      | `guildbossfieldinfo.bss` | 124 B (83.8%) | 24 B (16.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                               |
| --------------------- | -------- | ------------------------------------------------------------------ |
| `boss_spawnlevel.bss` | Optional | The boss character of each key, for the Boss column               |
| `languagedata_en.loc` | Optional | Character names (LOC type 6)                                       |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (24 bytes)

| Offset  | Type | Field              | Notes                                                          |
| ------- | ---- | ------------------ | -------------------------------------------------------------- |
| `+0x00` | u32  | boss_spawn_key     | A `boss_spawn.bss` key; `8` down to `1` on client 3474          |
| `+0x04` | f32  | x                  | World position, in the units of the `boss_spawn.bss` point     |
| `+0x08` | f32  | y                  | Height                                                         |
| `+0x0C` | f32  | z                  |                                                                |
| `+0x10` | u32  | boss_spawn_key_dup | Equal to `boss_spawn_key`                                      |
| `+0x14` | f32  | unknown_14         | `20000` on every row of client 3474                            |

The positions on client 3474, against the `boss_spawn.bss` spawn point of
the same key:

| Key | Boss          | x       | z        | Distance to the spawn point (x, z) |
| --- | ------------- | ------- | -------- | ---------------------------------- |
| 8   | Gumiho        | -64376  | 53858    | 0                                  |
| 5   | Khan          | -89743  | 602896   | 12,222                             |
| 4   | Org           | -50574  | -124111  | 1                                  |
| 3   | Giant Mudster | 32259   | -112131  | 0                                  |
| 2   | Moghulis      | 241677  | 15375    | 6,813                              |
| 1   | Ferrid        | 275038  | -29073   | 0                                  |

## Field Names

`boss_spawn_key` is the `bossKey` of the Lua calls above: all 6 keys of
client 3474 are `boss_spawn.bss` keys, and 4 of the 6 points lie within
1 unit of that boss's spawn point (x and z). The file is not in client
1784, and no sheet of a private server's `DataSheets.bexcel` on client 1784
holds it; the 2016 client's debug symbols have no guild boss field type.

## Open Questions

### unknown_14

`20000` on all 6 rows, a f32 after the key's copy. The two points that are
off their spawn point (Khan 12,222 units, Moghulis 6,813) are still within
20,000 units of it, so it may be the radius `ToClient_IsInGuildBossFieldPos`
checks; no Lua reads the value.
