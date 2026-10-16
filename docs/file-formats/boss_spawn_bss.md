# `boss_spawn.bss` Format

## Purpose

The guild bosses of the Guild Boss Summon window
(`panel_guild_bosssummon_all`): one 43-byte row per summonable boss with its
spawn key, the number of difficulty levels, where it spawns and the spawn
range. The window reads a row through `ToClient_bossSpawnList()` and, by
`BossSpawnKey`, `ToClient_bossSpawnPosition`, `ToClient_bossSpawnRange` and
`ToClient_bossSpawnMaxLevel`. The per-level reward and image are in
[`boss_spawnlevel.bss`](boss_spawnlevel_bss.md), which uses the same keys.

```text
key 3  Giant Mudster  levels 4  position (32,259, 379, -112,131)  range 2,000
key 5  Khan           levels 4  position (-101,306, -7,274, 598,938)  range 500
```

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `boss_spawnlevel.bss` | Optional | The boss character of each key, from its level 0 entry ([boss_spawnlevel](boss_spawnlevel_bss.md)) |
| `languagedata_en.loc` | Optional | LOC type 6 boss names                                                |

All multi-byte values are little-endian.

## File Layout

| Offset             | Type    | Field       | Notes                                              |
| ------------------ | ------- | ----------- | -------------------------------------------------- |
| `+0x00`            | char[4] | magic       | `PABR`                                             |
| `+0x04`            | u32     | row_count   | `6` on client 3464                                 |
| `+0x08`            | row[]   | rows        | `row_count` 43-byte rows                           |
| rows end           | u32     | string_count | `0`; the string table is empty                    |
| end - 8            | u32     | table_start | Where the rows end                                 |
| end - 4            | u32     | zero        |                                                    |

### Row (43 bytes)

| Offset  | Type    | Field       | Notes                                                                  |
| ------- | ------- | ----------- | ---------------------------------------------------------------------- |
| `+0x00` | u32     | key         | `BossSpawnKey`; `8, 5, 4, 3, 2, 1` in file order on client 3464        |
| `+0x04` | u32     | max_level   | `4` on every row; `boss_spawnlevel.bss` has 4 levels for every key     |
| `+0x08` | u32     | unknown_08  | `1` on every row                                                       |
| `+0x0C` | f32 x 3 | position    | World position; the second value is the height                         |
| `+0x18` | u32     | range       | `ToClient_bossSpawnRange`; `500` (keys 5, 8) or `2000`                 |
| `+0x1C` | u32     | unknown_1c  | `11` on every row                                                      |
| `+0x20` | u8      | unknown_20  | `1` on every row                                                       |
| `+0x21` | u8      | unknown_21  | `0` on keys 5 and 8, `1` on the rest                                    |
| `+0x22` | u8[4]   | unknown_22  | Zero on every row                                                      |
| `+0x26` | u8      | unknown_26  | `1` on every row                                                       |
| `+0x27` | u8      | unknown_27  | Zero on every row                                                      |
| `+0x28` | u8      | unknown_28  | Same as `unknown_21` on every row                                      |
| `+0x29` | u8      | unknown_29  | `1` on every row                                                       |
| `+0x2A` | u8      | unknown_2a  | Zero on every row                                                      |

Keys, with the boss from `boss_spawnlevel.bss` (client 3464):

| Key | Boss              | Range |
| --- | ----------------- | ----- |
| 1   | Ferrid            | 2000  |
| 2   | Moghulis          | 2000  |
| 3   | Giant Mudster     | 2000  |
| 4   | Org               | 2000  |
| 5   | Khan              | 500   |
| 8   | Gumiho & Duoksini | 500   |

## Notes

- Key 3's position lies 621 units from the Field boss Giant Mudster's
  position in [`bossinfostaicstatusmanager.bss`](bossinfostaicstatusmanager_bss.md),
  and key 1's lies 14,870 units from the Dark Rift Ferrid. The file holds no
  character ID; the names come only through `boss_spawnlevel.bss`.
- Keys 5 (Khan) and 8 (Gumiho & Duoksini) differ from the rest in `range`,
  `unknown_21` and `unknown_28`; in `boss_spawnlevel.bss` they are also the
  two bosses whose two character IDs differ.
- The window also calls `ToClient_bossSpawnMaxCost(bossKey)` and
  `ToClient_bossSpawnMaxCount(bossKey)`; the matching fields are not known
  (see Open Questions).

## Open Questions

### Max Cost and Max Count

The window shows a cost and a count against `ToClient_bossSpawnMaxCost` and
`ToClient_bossSpawnMaxCount`. `unknown_08` (`1`) and `unknown_1c` (`11`) are
the two constant u32s left, but which is which, or whether either is, is not
known. The current values come from the server (`getCurrentCost()`,
`getCurrentCount()`).

### unknown_21 and unknown_28

`0` on Khan and Gumiho & Duoksini, `1` on the rest. The window also checks
`ToClient_IsEnterMirrorField()` and `ToClient_EnterOrLeaveGuildBossField()`,
so one of them may mark a boss fought in a separate field, but no Lua call
reads them by name.
