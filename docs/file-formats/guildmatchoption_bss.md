# `guildmatchoption.bss` Format

## Purpose

The Guild League settings: 30 bytes of unnamed values, the reward items of
a victory and of a defeat, and a list of 93 item IDs (client 3474). The
victory reward is [Season] Guild League Victory Reward (890096) and item
890117, the defeat reward [Season] Guild League Resolve Reward (890097).
The item list holds cannon assembly kits, transformation scrolls, fences
and medical kits. The ranks are in [guildmatchrank](guildmatchrank_bss.md),
the EXP by level in [guildmatchexp](guildmatchexp_bss.md), and the guild
right to sign up for the league (right 29) in
[guildrightnewstaticstatus](guildrightnewstaticstatus_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ------------- | --------- |
| 1      | 2519 and later | 3474    | `guildmatchoption.bss` | 466   | 3 Reward Item | 12        |

| Layout | File                   | Known        | Unknown       |
| ------ | ---------------------- | ------------ | ------------- |
| 1      | `guildmatchoption.bss` | 60 B (12.9%) | 406 B (87.1%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                       |
| --------------------- | -------- | -------------------------- |
| `languagedata_en.loc` | Optional | Item names, LOC type 0     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                     | Type                          | Field                | Notes                                                                 |
| -------------------------- | ----------------------------- | -------------------- | --------------------------------------------------------------------- |
| `+0x00`                    | char[4]                       | magic                | ASCII `PABR`                                                          |
| `+0x04`                    | u16                           | unknown_04           | `1200` on client 3474, `1800` on 2519 to 3251                          |
| `+0x06`                    | u16                           | unknown_06           | `240` on client 3474, `120` on 2519 to 3251                            |
| `+0x08`                    | u16                           | unknown_08           | `10` on every client checked                                           |
| `+0x0A`                    | u16                           | unknown_0a           | `600` on client 3474, `1000` on 2519 to 3251                           |
| `+0x0C`                    | u16                           | unknown_0c           | `720` on client 3474, `1200` on 2519 to 3251                           |
| `+0x0E`                    | u8                            | unknown_0e           | `30` on client 3474, `50` on 2519 to 3251                              |
| `+0x0F`                    | u8                            | unknown_0f           | `3` on every client checked                                            |
| `+0x10`                    | bytes[8]                      | unknown_10           | `3c eb f4 bc e5 07 0a 03` on every client checked; see Notes           |
| `+0x18`                    | u32                           | unknown_18           | `604800` (7 days in seconds) on every client checked                   |
| `+0x1C`                    | u8                            | unknown_1c           | `4` on every client checked                                            |
| `+0x1D`                    | u8                            | unknown_1d           | `15` on every client checked                                           |
| `+0x1E`                    | u16                           | unknown_1e           | `400` on every client checked                                          |
| `+0x20`                    | u8                            | unknown_20           | `30` on every client checked                                           |
| `+0x21`                    | u8                            | unknown_21           | `15` on every client checked                                           |
| `+0x22`                    | u32                           | victory_reward_count | Number of victory reward items                                        |
| `+0x26`                    | Reward Item[victory_reward_count] | victory_reward_items | See Reward Item                                                  |
| `victory_reward_items+0x00` | u32                          | defeat_reward_count  | Number of defeat reward items                                         |
| `victory_reward_items+0x04` | Reward Item[defeat_reward_count] | defeat_reward_items | See Reward Item                                                   |
| `defeat_reward_items+0x00` | u32                           | unknown_item_count   | Number of `unknown_item_ids`                                          |
| `defeat_reward_items+0x04` | u32[unknown_item_count]       | unknown_item_ids     | Item IDs; 93 of 93 have a LOC type 0 name (client 3474); see Notes    |
| `unknown_item_ids+0x00`    | String Table                  | string_table         | See String Table                                                      |
| `string_table+0x00`        | u32                           | table_start          | Offset of the string table, where `unknown_item_ids` ends             |
| `string_table+0x04`        | u32                           | zero                 | Always `0`                                                            |

### Reward Item (12 bytes)

| Offset  | Type | Field      | Notes                                                                       |
| ------- | ---- | ---------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key   | `enchant_level << 24 \| item_id`, the key of [itemenchant](itemenchant_dbss.md); every level is `0` |
| `+0x04` | u64  | item_count | Number of items; `1` on every entry checked                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Reward Items

| Client | Victory                                                                  | Defeat                                                                   |
| ------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| 2519   | [Event] Guild League Victory Reward (56267), Victory Combat EXP (56276)  | [Event] Guild League Resolve Reward (56268), Defeat Combat EXP (56277)   |
| 3002   | [Season] Guild League Victory Reward (767690), Victory Combat EXP (56276) | [Season] Guild League Resolve Reward (767691), Defeat Combat EXP (56277) |
| 3251   | [Season] Guild League Victory Reward (761953), Victory Combat EXP (56276) | [Season] Guild League Resolve Reward (761954), Defeat Combat EXP (56277) |
| 3474   | [Season] Guild League Victory Reward (890096), item 890117 (no LOC name)  | [Season] Guild League Resolve Reward (890097)                            |

## Field Names

The Guild League is newer than client 1784 and 2107, which do not ship the
file, so no sheet of a private server's `DataSheets.bexcel` covers it. The
reward lists follow the client Lua of client 3474
(`panel_guildmatch_all_1.luac`): the reward tooltip reads
`ToClient_GetGuildMatchVictoryRewardCount()`, then per entry
`ToClient_GetGuildMatchVictoryRewardItemKey(index)` and
`ToClient_GetGuildMatchVictoryRewardItemCount(index)` (a 64-bit count), and
the same three `...DepeatReward...` calls for the defeat side. Every first
entry is a Guild League Victory Reward or Resolve Reward item, in that
order. The Lua also reads `ToClient_GetGuildMatchParticipatedMaxCount()`,
`...WaitRemainTime()`, `...PlayingRemainTime()` and `...ExitRemainTime()`;
which of the unnamed values they come from is not known.

## Notes

- The file is 482 bytes on clients 2519 to 3251 (94 item IDs) and 466 on
  3474, where item 757111 left the list. Clients 1784 and 2107 do not ship
  it.
- `unknown_item_ids` holds Cannon Assembly Kits (Lynch, Trina, Vype Stoner,
  Monsterbane), transformation scrolls (MOD Oog, Crasher, the 1-day and
  7-day ones), fences ([CP] Strong Fence, Old Moon Fence) and Medical Kits.
- `unknown_10` reads `e5 07 0a 03` at `+0x14`, which as u16 `2021`, u8
  `10`, u8 `3` would be a date; the first 4 bytes fit no plain number.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/guild_tables.py`: the two reward lists with item names
  and counts.

## Open Questions

### Unnamed Settings

Which of `unknown_04` to `unknown_21` is the match time, the waiting time,
the exit countdown and the weekly participation cap. `unknown_04` (1800 to
1200), `unknown_0a` (1000 to 600) and `unknown_0c` (1200 to 720) all fell
on client 3474, and `unknown_18` is 7 days in seconds.

### Item ID List

What the client does with `unknown_item_ids`. The entries are cannons,
transformation scrolls, fences and medical kits, which fits
items that cannot be used in a Guild League match, but no Lua reads the
list by a name.
