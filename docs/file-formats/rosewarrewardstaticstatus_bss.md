# `rosewarrewardstaticstatus.bss` Format

## Purpose

The Rose War rewards: one row without and one with a guild, each with the
items for a victory, a defeat and a liberation and a fourth item list. On
client 3474 the row with `is_guild` `0` hands out the Blossoming reward
boxes ("Third Legion" in their LOC text) and the row with `is_guild` `1`
the Flourishing ones ("Leading Guild"), each with Combat Secret Books, and
the guild row's fourth list holds 25 [Guild] Trace of Doom.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records          | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ----- | ---------------- | --------- |
| 2      | 3474 and later | 3474    | `rosewarrewardstaticstatus.bss` | 294   | 13 Reward, 2 Row | 16        |
| 1      | 3002 to 3251   | 3251    | `rosewarrewardstaticstatus.bss` | 118   | 2 Row            | 49        |

| Layout | File                            | Known         | Unknown      |
| ------ | ------------------------------- | ------------- | ------------ |
| 2      | `rosewarrewardstaticstatus.bss` | 226 B (76.9%) | 68 B (23.1%) |
| 1      | `rosewarrewardstaticstatus.bss` | 94 B (79.7%)  | 24 B (20.3%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                      |
| --------------------- | -------- | ------------------------- |
| `languagedata_en.loc` | Optional | Item names, LOC type 0    |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows; `2` on every client checked   |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 33 bytes + rewards)

| Offset                 | Type                         | Field                | Notes                                                     |
| ---------------------- | ---------------------------- | -------------------- | --------------------------------------------------------- |
| `+0x00`                | u64                          | win_reward_count     | Number of `win_rewards`                                   |
| `+0x08`                | Reward[win_reward_count]     | win_rewards          | Victory rewards; see Reward                               |
| `win_rewards+0x00`     | u64                          | lose_reward_count    | Number of `lose_rewards`                                  |
| `win_rewards+0x08`     | Reward[lose_reward_count]    | lose_rewards         | Defeat rewards                                            |
| `lose_rewards+0x00`    | u64                          | draw_reward_count    | Number of `draw_rewards`                                  |
| `lose_rewards+0x08`    | Reward[draw_reward_count]    | draw_rewards         | Liberation rewards                                        |
| `draw_rewards+0x00`    | u64                          | unknown_reward_count | Number of `unknown_rewards`                               |
| `draw_rewards+0x08`    | Reward[unknown_reward_count] | unknown_rewards      | Empty on the `is_guild` `0` row; see Open Questions       |
| `unknown_rewards+0x00` | u8                           | is_guild             | `0` or `1`                                                |

### Reward (16 bytes)

| Offset  | Type     | Field      | Notes                                                                 |
| ------- | -------- | ---------- | --------------------------------------------------------------------- |
| `+0x00` | u32      | item_id    | `itemenchant.dbss` item ID; the handler shows its LOC type 0 name     |
| `+0x04` | bytes[4] | unknown_04 | `FC 7F 00 00` on every reward; see Notes                              |
| `+0x08` | u64      | count      | How many of the item                                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

### Row (49 bytes)

| Offset  | Type | Field              | Notes                                                    |
| ------- | ---- | ------------------ | -------------------------------------------------------- |
| `+0x00` | u32  | win_item_id        | Victory reward box                                       |
| `+0x04` | u32  | lose_item_id       | Defeat reward box                                        |
| `+0x08` | u32  | draw_item_id       | Liberation reward box                                    |
| `+0x0C` | u32  | unknown_item_id    | `0` on the `is_guild` `0` row, `761680` on the other     |
| `+0x10` | u64  | win_item_count     | `1`                                                      |
| `+0x18` | u64  | lose_item_count    | `1`                                                      |
| `+0x20` | u64  | draw_item_count    | `1`                                                      |
| `+0x28` | u64  | unknown_item_count | `0`, or `25` with item `761680`                          |
| `+0x30` | u8   | is_guild           | `0` or `1`                                               |

## Rewards

Client 3474; the names are LOC type 0, the result in each box's "How to
Obtain" line.

| `is_guild` | List              | Items                                                             |
| ---------- | ----------------- | ----------------------------------------------------------------- |
| `0`        | `win_rewards`     | Blossoming Victory Reward x1, Combat Secret Book (XL) x1          |
| `0`        | `lose_rewards`    | Blossoming Resolve Reward x1, Combat Secret Book (M) x4           |
| `0`        | `draw_rewards`    | Blossoming Battle Reward x1, Combat Secret Book (M) x4            |
| `1`        | `win_rewards`     | Flourishing Victory Reward x1, Combat Secret Book (XL) x1         |
| `1`        | `lose_rewards`    | Flourishing Resolve Reward x1, Combat Secret Book (M) x4          |
| `1`        | `draw_rewards`    | Flourishing Battle Reward x1, Combat Secret Book (M) x4           |
| `1`        | `unknown_rewards` | [Guild] Trace of Doom x25                                         |

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. The menu Lua
(`panel_rosewar_menu_1.luac`, client 3474) reads the rewards with
`ToClient_GetRoseWarWinReward(isGuild, index)`,
`ToClient_GetRoseWarDrawReward` and `ToClient_GetRoseWarLoseReward`, each
with a `...RewardSize(isGuild)`, and shows them as Win, Liberation and
Lose. Each box's LOC text names its result: Victory boxes say "victory",
Resolve boxes "defeat" and Battle boxes "liberation", which fixes the list
order win, lose, draw. The Flourishing boxes say "Leading Guild" and the
Blossoming ones "Third Legion", so the row whose last byte is `1` is the
guild row.

## Notes

- Clients 3002 and 3251 use Layout 1, one item per result: the same boxes
  (3251) or items `761587` to `761589` and `761584` to `761586` (3002), one
  each, and 25 of `761680` on the guild row (118 bytes). Client 3474 turns
  each result into a list and adds the Combat Secret Books (294 bytes). The
  file is not in the archives of client 1784.
- `unknown_04` is `FC 7F 00 00` on all 13 rewards of client 3474, the upper
  half of a 64-bit pointer, as in the `0x00007FFC` groups of
  [`instancefieldmapinfo.bss`](instancefieldmapinfo_bss.md): the item ID
  sits in an 8-byte slot whose upper half the tool that wrote the file did
  not clear.
- The handler (`_bss/rosewarrewardstaticstatus/`) reads Layout 2 and shows
  one row per reward item, with the item name, the count, the result of its
  list and the guild flag.

## Open Questions

### The Fourth List

The menu Lua reads three reward lists, and the fourth list holds [Guild]
Trace of Doom on the guild row only. A reward for the guild leading the
war or for the castle owner fits, but nothing names the list.
