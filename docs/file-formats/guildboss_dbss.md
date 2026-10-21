# `guildboss.dbss` Format

## Purpose

One row per guild boss character with the skill EXP and guild funds amounts
of the `GuildBoss_Table` sheet. On client 3474 the file has 1 row, character
`23014` Black Shadow `<Boss>` (Korean label `Cal_사우닐 주둔지 보스_미완성`, a
Calpheon Saunil camp boss marked unfinished, model
`monster/m0180_wyvern_f_boss`). Companion `guildbossoffset.dbss` lists where
every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ------------ | --------- |
| 1      | 1485 and later | 3474    | `guildboss.dbss`       | 21    | 1 Row        | 17        |
| 1      | 1485 and later | 3474    | `guildbossoffset.dbss` | 14    | 1 Offset Row | 10        |

| Layout | File                   | Known         | Unknown    |
| ------ | ---------------------- | ------------- | ---------- |
| 1      | `guildboss.dbss`       | 20 B (95.2%)  | 1 B (4.8%) |
| 1      | `guildbossoffset.dbss` | 14 B (100.0%) | 0 B (0.0%) |

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
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                 |
| ---------------------------- | -------- | -------------------------------------------------------------------- |
| `guildbossoffset.dbss`       | Optional | `character_key -> (offset, size)` of every row; the main file can be walked without it |
| `characterstaticoffset.dbss` | Optional | Tells which keys have a [`characterstatic.dbss`](characterstatic_dbss.md) row, for the key link |
| `languagedata_en.loc`        | Optional | Character names (LOC type 6)                                         |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (17 bytes)

| Offset  | Type | Field             | Notes                                                       |
| ------- | ---- | ----------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | character_key     | Boss character; has a `characterstatic.dbss` row (client 3474) |
| `+0x02` | u8   | unknown_02        | `1`; the offset file points here                            |
| `+0x03` | u16  | character_key_dup | Equal to `character_key`                                    |
| `+0x05` | i32  | skill_point_exp   | `100000` (client 3474)                                      |
| `+0x09` | i64  | guild_money       | `100000000` (client 3474)                                   |

### `guildbossoffset.dbss`

| Offset  | Type              | Field | Notes                                   |
| ------- | ----------------- | ----- | --------------------------------------- |
| `+0x00` | u32               | count | Equals the `guildboss.dbss` count       |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row    |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                                   |
| ------- | ---- | ------------- | ------------------------------------------------------- |
| `+0x00` | u16  | character_key | Key of the row it points at                             |
| `+0x02` | u32  | offset        | Row start + 2, at `unknown_02`                          |
| `+0x06` | u32  | size          | The row without its leading `character_key`: always `15` |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`.

## Field Names

The names follow the `GuildBoss_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, columns `CharacterKey`, `SkillPointExp`
and `GuildMoney`. Its one row, `23014`, `100000`, `100000000`, matches the
file on clients 1784 and 3474 (1 of 1 keys, both values). The
`GuildBoss_Table` of a private server on client 519 holds the same row.

The client 1784 server dump (`Instance_dumpFull.exe`) reads the sheet in the
function at VA `0x140959be0`. It builds a 24-byte row: a byte at `+0x00` that
it sets to `0` and never fills from the sheet, the `CharacterKey` cell
truncated to a u16 at `+0x02`, `SkillPointExp` with `ReadColumnInt` at
`+0x04` and `GuildMoney` with `ReadColumnInt64` at `+0x08`, then 8 zero
bytes. The file holds the same order after its leading key (u8, u16, 4-byte
and 8-byte values), so `skill_point_exp` is an `i32` and `guild_money` an
`i64`. The 2016 client's debug symbols have no guild boss static status.

## Notes

- Client 1784 has the same 21-byte file, byte for byte.
- The same `u16 key | u8 1 | u16 character key` head starts the rows of
  [`fieldboss.dbss`](fieldboss_dbss.md) and
  [`weatheractor.dbss`](weatheractor_dbss.md), where the byte is `1` on every
  row as well.
- The Guild Boss Summon window (`panel_guild_bosssummon_all`) lists its
  bosses through `ToClient_bossSpawnList()` and `BossSpawnKey`, the
  [`boss_spawn.bss`](boss_spawn_bss.md) records, and never names this file.
  Of the 3,073 `.luac` files of client 3474, only the season character and
  EXP exchange windows hold the text `skillPointExp`, for the player's own
  skill EXP.

## Open Questions

### What the Row Rewards

`23014` Black Shadow is marked unfinished in its Korean label, and the
current guild boss summons come from `boss_spawn.bss`. Whether the server
still pays `skill_point_exp` and `guild_money` for a guild boss kill, and to
whom (each member's skill EXP, the guild's funds), is open; no client Lua or
UI text reads the table.

### unknown_02

The byte is `1` in the one row, and the client 1784 server loader leaves its
copy of it at `0`, so the data cannot tell a flag from a constant. The same
byte is `1` on every row of `fieldboss.dbss` and `weatheractor.dbss`.
