# `sha_dueltournamentoption.bss` Format

## Purpose

The Shadow Arena duel tournament settings: the hashes of three action
names, the player count and the times of the tournament states. Clients
1784 and 2107 fill the values; from client 2519 every value is `0`, the
file size unchanged.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | -------------- | --------- |
| 1      | 1485 and later | 3474    | `sha_dueltournamentoption.bss` | 60    | 1 String Table | 4         |

| Layout | File                           | Known        | Unknown      |
| ------ | ------------------------------ | ------------ | ------------ |
| 1      | `sha_dueltournamentoption.bss` | 36 B (60.0%) | 24 B (40.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler reads this file alone.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field                   | Notes                                                                           |
| ------------------- | ------------ | ----------------------- | ------------------------------------------------------------------------------- |
| `+0x00`             | char[4]      | magic                   | ASCII `PABR`                                                                    |
| `+0x04`             | u32          | game_start_action_hash  | `ascii_key_hash` of the action name: `BS_START` (`0x0E907704`) on client 1784    |
| `+0x08`             | u32          | fight_start_action_hash | `START_CHARACTER` (`0x8640C8B7`) on client 1784                                  |
| `+0x0C`             | u32          | winner_action_hash      | `SHADOW_ENDING_STUN` (`0x4CF4BE41`) on client 1784                               |
| `+0x10`             | u32          | max_player_count        | `6` on client 1784                                                              |
| `+0x14`             | u32          | unknown_14              | `180` on client 1784; see Open Questions                                        |
| `+0x18`             | u32          | unknown_18              | `60` on client 1784                                                             |
| `+0x1C`             | u32          | unknown_1c              | `60` on client 1784                                                             |
| `+0x20`             | u32          | unknown_20              | `10` on client 1784                                                             |
| `+0x24`             | u32          | unknown_24              | `10` on client 1784                                                             |
| `+0x28`             | u32          | after_time_end_state    | `120` on client 1784                                                            |
| `+0x2C`             | u32          | unknown_2c              | `180` on client 1784                                                            |
| `+0x30`             | String Table | string_table            | See String Table                                                                |
| `string_table+0x00` | u32          | table_start             | Offset of the string table, `0x30`                                              |
| `string_table+0x04` | u32          | zero                    | Always `0`                                                                      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `SHA_DuelTournamentOption_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has one row with `GameStartAction`
`BS_START`, `FightStartAction` `START_CHARACTER` and `WinnerAction`
`SHADOW_ENDING_STUN`. The three hashes of the client 1784 file are
`ascii_key_hash` (lookup3 over the ASCII bytes, seed `0xC5EDE`) of exactly
these names, in that order.

The private server's server executable names eleven members of
`DuelTournamentOptionStaticStatus`: `_startAction`, `_duelStartAction`,
`_winnerStartAction`, `_maxPlayerCount`, `_waitMaxSec`, `_duelLimitSec`
and `_afterTimePlayState`, `_afterTimeDuelState`, `_afterTimeWaitState`,
`_afterTimeReayState`, `_afterTimeEndState`, which are the 11 fields of the
file. The sheet's numbers for these columns are `PlayerMaxCount` 6,
`AfterTimePlayState` 60, `AfterTimeDuelState` 10, `AfterTimeWaitState` 10,
`AfterTimeReadyState` 60, `AfterTimeEndState` 120, `DuelTimeLimit` 180 and
`GameForceStartTime` 180, the same 8 values as the file in another order.
`max_player_count` (6) and `after_time_end_state` (120) match one column
each; the other six values come in pairs and stay `unknown_*`.

## Notes

- The file is 60 bytes on every client checked (1784, 2107, 2519, 3002,
  3251, 3474). The sheet also has `MaxRound`, `MaxKillCount`,
  `StartGiveItem`, `ItemKey` and `ItemCount`, which the file does not
  store.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in `_bss/pabr_values/pvp_tables.py`,
  the action hashes as hex.

## Open Questions

### Paired Times

Which field of each equal pair is which column: `unknown_14` and
`unknown_2c` (180) are `DuelTimeLimit` and `GameForceStartTime` (the
server's `_duelLimitSec` and `_waitMaxSec`), `unknown_18` and `unknown_1c`
(60) are `AfterTimePlayState` and `AfterTimeReadyState`, `unknown_20` and
`unknown_24` (10) are `AfterTimeDuelState` and `AfterTimeWaitState`, each
pair in an unknown order. Every client from 2519 stores `0`, so only an
older client with other values could tell.
