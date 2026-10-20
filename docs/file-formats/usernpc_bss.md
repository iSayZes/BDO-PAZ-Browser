# `usernpc.bss` Format

## Purpose

The Fishing God NPCs: NPCs that take the look of a player character. Each
row names the player character by its character number, places the NPC in
the world with a position and a facing angle, gives the action it plays
(`FISHING_GOD_WAIT`) and the class it is drawn as. The server dump of a
private server on client 1784 loads the table into `UserNpcStaticStatusManager`
(`loadUserNpcInformation`). The same dump has the database call
`SqlCharacter::getUserNpcCumtomize`; the file itself holds no appearance data.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File          | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------- | ----- | -------------- | --------- |
| 1      | 1784 and later | 3474    | `usernpc.bss` | 99    | 2 User NPC Row | 29        |

| Layout | File          | Known         | Unknown    |
| ------ | ------------- | ------------- | ---------- |
| 1      | `usernpc.bss` | 99 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                            |
| --------------------- | -------- | ------------------------------- |
| `languagedata_en.loc` | Optional | Class names, LOC type 21        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

The shared PABR string table layout of `mansionpartinfo.bss`
(`_common/pabr_strings.py`).

| Offset              | Type                 | Field        | Notes                                          |
| ------------------- | -------------------- | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]              | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32                  | count        | Number of rows; `2` on client 3474             |
| `+0x08`             | User NPC Row[count]  | rows         | See User NPC Row; byte-packed                  |
| `rows+0x00`         | String Table         | string_table | See String Table                               |
| `string_table+0x00` | u32                  | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32                  | zero         | Always `0`                                     |

The file is `8 + 29 x 2 + 25 + 8 = 99` bytes on client 3474. The parser
rejects a file whose rows do not end exactly at `table_start`.

### User NPC Row (29 bytes)

| Offset  | Type | Field               | Notes                                                                 |
| ------- | ---- | ------------------- | --------------------------------------------------------------------- |
| `+0x00` | u64  | player_character_no | Character number of the player whose look the NPC takes               |
| `+0x08` | f32  | pos_x               | World X                                                               |
| `+0x0C` | f32  | pos_y               | World Y (height)                                                      |
| `+0x10` | f32  | pos_z               | World Z                                                               |
| `+0x14` | f32  | direction           | Facing angle in radians                                               |
| `+0x18` | u32  | action_ref          | String table index of the action the NPC plays                        |
| `+0x1C` | u8   | class_type          | Class the NPC is drawn as; LOC type 21 names it                       |

The two rows of client 3474:

| player_character_no | pos_x, pos_y, pos_z          | direction | Action             | class_type    |
| ------------------- | ---------------------------- | --------- | ------------------ | ------------- |
| `1000000000001304`  | 1112.81, -8091.49, 87251.80  | 3.14159   | `FISHING_GOD_WAIT` | 16 Tamer      |
| `643`               | 1191.38, -8106.86, 87098.83  | 4.5       | `FISHING_GOD_WAIT` | 12 Berserker  |

### String Table (variable: 4 bytes + strings)

One string on client 3474, `FISHING_GOD_WAIT`, which both rows point at.

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Field Names

The names follow the `FishingGod_NPC` sheet of a private server's
`DataSheets.bexcel` on client 1784 and of the developer workbook
`datasheet_characterdatatable.xlsm`. Its columns are `PA_GAME_SERVICE_TYPE`,
`Player_CharacterNo`, `Position`, `Direction`, `ActionName`, `ItemNo` and
`ClassType`. The row stores five of them in sheet order, `Position` as three
f32 and `ActionName` as a string table index:

| Column               | In the row                                                    |
| -------------------- | ------------------------------------------------------------- |
| PA_GAME_SERVICE_TYPE | Not stored                                                    |
| Player_CharacterNo   | `player_character_no`                                         |
| Position             | `pos_x`, `pos_y`, `pos_z`                                      |
| Direction            | `direction`                                                   |
| ActionName           | `action_ref`                                                  |
| ItemNo               | Not stored                                                    |
| ClassType            | `class_type`                                                  |

The sheet's two rows hold `1112.81,-8091.49,87251.8`, `3.14159` and
`FISHING_GOD_WAIT`, the same position, angle and action as the first row of
client 3474. Their character numbers (`40000000000178712` and
`100000000000020879`) are not in the client file. The sheet's `#설명` note
column reads "3 (한국) - 레인저" and "1 (개발용) - 레인저" (service 3 Korea,
service 1 development, Ranger), and both rows have `ClassType` `4`, the
Ranger class type. Their `ItemNo` `22250,16152` is [Ranger] Da-Dum Da-Dum
Diving Suit and Golden Fishing Rod, the outfit of a Ranger.

The private server's own `usernpc.bss` and the one of client 1784 are 20
bytes with no rows, so no build of the sheet can be compared byte for byte.
The column-to-offset match rests on the values of the first row of client
3474 and on the column order.

Neither the 2016 client with debug symbols nor the tables of a private server on
client 519 have a user NPC type or table.

## Notes

- `PA_GAME_SERVICE_TYPE` is not stored: each sheet row belongs to one
  service, and the file of a client holds a subset of the rows. The sheet's
  character numbers are 4 x 10^16 + 178712 (service 3) and 10^17 + 20879
  (service 1); the first row of client 3474 is 10^15 + 1304.
- The client Lua (3,073 scripts on client 3473) has no `UserNpc` or
  `FISHING_GOD` text, so no UI window reads the table.
- LOC holds one Fishing God line, a dialog line of type 36: "Welcome,
  everyone! As Mena's first Fishing God, I wish you all the best of luck!"
- `ItemNo` (the equipment the NPC wears in the sheet) is not in the client
  file.

## Open Questions

### Who Is Character `643`

The second row of client 3474 has character number `643`, with none of the
per-service prefixes the sheet's numbers carry. The client data does not
show whether it is an older character number or a placeholder.
