# `rosewarstaticstatus.bss` Format

## Purpose

The Rose War settings: one set of values after the PABR magic, with two
u64, 25 u32 and one f32 settings, the boss and the home region of each
team, the Rose War regions, an item and two weekly schedules. On client 3474 the
bosses are Narchillan and Sephir, the home regions Grána and O'draxxia,
and the item is Medal of Sylvia (`761066`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records             | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------------------- | --------- |
| 1      | 3002 and later | 3474    | `rosewarstaticstatus.bss` | 372   | 16 Time, 2 Schedule | 12        |

| Layout | File                      | Known         | Unknown       |
| ------ | ------------------------- | ------------- | ------------- |
| 1      | `rosewarstaticstatus.bss` | 250 B (67.2%) | 122 B (32.8%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                           |
| --------------------- | -------- | -------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Character (type 6), region (type 17) and item (type 0) names   |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                     | Field                         | Notes                                                       |
| ------------------- | ------------------------ | ----------------------------- | ----------------------------------------------------------- |
| `+0x00`             | char[4]                  | magic                         | ASCII `PABR`                                                |
| `+0x04`             | u64                      | unknown_04                    | `5,000,000,000` (client 3474); `10,000,000,000` on 3002     |
| `+0x0C`             | u64                      | unknown_0c                    | `500,000,000`                                               |
| `+0x14`             | u32                      | unknown_14                    | `400`                                                       |
| `+0x18`             | u32                      | unknown_18                    | `5`                                                         |
| `+0x1C`             | u32                      | unknown_1c                    | `6000`                                                      |
| `+0x20`             | u32                      | unknown_20                    | `20000`                                                     |
| `+0x24`             | u32                      | unknown_24                    | `60000`                                                     |
| `+0x28`             | u32                      | unknown_28                    | `3500`                                                      |
| `+0x2C`             | u32                      | unknown_2c                    | `100000`                                                    |
| `+0x30`             | u32                      | unknown_30                    | `10`                                                        |
| `+0x34`             | u32                      | unknown_34                    | `600`                                                       |
| `+0x38`             | u32                      | unknown_38                    | `40`                                                        |
| `+0x3C`             | u32                      | unknown_3c                    | `100`                                                       |
| `+0x40`             | u32                      | unknown_40                    | `1800`                                                      |
| `+0x44`             | f32                      | unknown_44                    | `700.0`                                                     |
| `+0x48`             | u32                      | unknown_48                    | `20` (client 3474); `30` on 3002                            |
| `+0x4C`             | u32                      | unknown_4c                    | `40`; `20` on 3002                                          |
| `+0x50`             | u32                      | unknown_50                    | `30`; `45` on 3002                                          |
| `+0x54`             | u32                      | unknown_54                    | `100`                                                       |
| `+0x58`             | u16                      | kamasylvia_boss_character_key | `21871` Narchillan (LOC type 6)                             |
| `+0x5A`             | u16                      | odyllita_boss_character_key   | `21872` Sephir                                              |
| `+0x5C`             | u32                      | unknown_5c                    | `10`                                                        |
| `+0x60`             | u32                      | unknown_60                    | `600`                                                       |
| `+0x64`             | u32                      | unknown_64                    | `600`                                                       |
| `+0x68`             | u32                      | unknown_68                    | `60`                                                        |
| `+0x6C`             | u32                      | unknown_6c                    | `10`                                                        |
| `+0x70`             | u32                      | unknown_70                    | `5`                                                         |
| `+0x74`             | u32                      | unknown_74                    | `15`                                                        |
| `+0x78`             | u16                      | kamasylvia_region_key         | `735` Grána (LOC type 17)                                   |
| `+0x7A`             | u16                      | odyllita_region_key           | `955` O'draxxia                                             |
| `+0x7C`             | u32                      | unknown_7c                    | `2700` (client 3474); `900` on 3002                         |
| `+0x80`             | u32                      | unknown_80                    | `300`                                                       |
| `+0x84`             | u32                      | region_count                  | Number of `region_keys`                                     |
| `+0x88`             | u16[region_count]        | region_keys                   | `regioninfo.bss` keys; see Regions                          |
| `region_keys+0x00`  | u32                      | item_id                       | `761066` Medal of Sylvia (LOC type 0)                       |
| `region_keys+0x04`  | u32                      | schedule_count                | Number of `schedules`; `2` on every client checked          |
| `region_keys+0x08`  | Schedule[schedule_count] | schedules                     | See Schedule                                                |
| `schedules+0x00`    | String Table             | string_table                  | See String Table                                            |
| `string_table+0x00` | u32                      | table_start                   | Offset of the string table, where `schedules` ends          |
| `string_table+0x04` | u32                      | zero                          | Always `0`                                                  |

### Schedule (97 bytes)

| Offset  | Type    | Field      | Notes                                         |
| ------- | ------- | ---------- | --------------------------------------------- |
| `+0x00` | u8      | unknown_00 | `0` and `1`, one per schedule                 |
| `+0x01` | Time[8] | times      | See Time and Schedules                        |

### Time (12 bytes)

| Offset  | Type | Field       | Notes                       |
| ------- | ---- | ----------- | --------------------------- |
| `+0x00` | u32  | day_of_week | `0` to `6`                  |
| `+0x04` | u32  | hour        | `0` to `23`                 |
| `+0x08` | u32  | minute      | `0` to `59`                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Regions

`region_keys` holds 11 keys on clients 3002 to 3474, each a LOC type 17
region name: `703` Lemoria Guard Post, `706` Old Wisdom Tree, `724`
Kamasylvia Castle, `727` Acher Guard Post, `735` Grána, `955` O'draxxia,
`956` O'dyllita Castle, `961` Bahit Sanctum, `966` Starry Midnight Port,
`1024` Mountain of Division and `1028` Dead Moon Post. Both team home
regions are in the list.

## Schedules

The eight times of each schedule as day, hour and minute (client 3474):

| Time | Schedule `0` | Schedule `1` |
| ---- | ------------ | ------------ |
| 1    | `0` 22:00    | `0` 15:00    |
| 2    | `1` 00:00    | `0` 17:00    |
| 3    | `6` 06:00    | `5` 23:00    |
| 4    | `0` 06:10    | `6` 23:10    |
| 5    | `0` 06:10    | `6` 23:10    |
| 6    | `0` 20:05    | `0` 13:05    |
| 7    | `0` 20:05    | `0` 13:05    |
| 8    | `0` 22:00    | `0` 15:00    |

Each time of schedule `1` is the same time of schedule `0` moved back 7
hours, across the day line where it falls before midnight; on client 3251
the shift is 6 hours (`0` 16:00 for time 1). The two schedules read as one
war calendar in two time zones. The client Lua names the war states
`__eRoseWar_GuildApplying`, `_GuildStopApplying`, `_MercenaryApplying`,
`_MercenaryStopApplying`, `_PreStart`, `_Start` and `_Stop` (plus
`_Count`), but not which time opens which.

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. The named fields resolve by
value:

- The two boss keys are LOC type 6 Narchillan and Sephir; the Lua reads a
  team's boss with `ToClient_GetRoseWarBossInfoXXX(roseWarTeamNo)`, and
  [`rosewarteamnostaticstatus.bss`](rosewarteamnostaticstatus_bss.md) puts
  Narchillan's Blessing on team `0` (Kamasylvia) and Sephir's Blessing on
  team `1`.
- The two region keys are the capitals Grána (Kamasylvia) and O'draxxia
  (O'dyllita).
- `item_id` is LOC type 0 Medal of Sylvia.
- `day_of_week`, `hour` and `minute` stay in `0` to `6`, `0` to `23` and
  `0` to `59`, and both schedules shift by whole hours.

## Notes

- The file is 372 bytes on clients 3002, 3251 and 3474; the values that
  differ are in the layout table. The file is not in the archives of
  client 1784.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`
  as one row: the bosses, the home regions, the region list, the item and
  each schedule as `<unknown_00>: <day> <hh:mm>, ...`.

## Open Questions

### The Settings

The 25 unnamed u32 settings, the f32 and the two u64 have no name in any
source. The u64 values (`5,000,000,000` and `500,000,000`) read as silver
amounts, and `600`, `1800` and `2700` as seconds, but the menu Lua's
`ToClient_GetRoseWarGuildApplyPoint()`, `ToClient_GetRoseWarReviveTime()`
and `ToClient_GetRoseWarMiniMapDetectDistanceLimitForFierceBattle()`
return them without saying which offset they read.

### The Day Numbers

`day_of_week` runs `0` to `6`, but no source says whether `0` is Sunday or
Monday, or which time zone each schedule follows.
