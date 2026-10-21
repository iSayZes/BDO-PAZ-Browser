# `actionverification.bss` Format

## Purpose

A list of actions per character: each character key holds action name
hashes, each with an `AbleCallTime` value. On client 3474 the file holds 14
characters and 150 actions. Five are the player classes Warrior (`1`),
Ranger (`2`), Sorcerer (`3`), Tamer (`5`) and Musa (`21`), with one action
each (`BT_WAIT`, `BT_skill_SkyFall`, `BT_skill_ThrustAndSmash_AttQ1`). The
other nine are the hero characters `65002` to `65037` (Jordine, Peony,
Ahon Kirus, Povios, Syaki, Nelydormin, Orwen, Striker, Tamer in LOC type 6),
with 12 to 23 `SHADOW_*` and `BT_ROLL_*` actions each. Each hero key is
`64950` plus one of the class types in
[`actionverificationindex.dbss`](actionverificationindex_dbss.md) (see
Notes).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records                  | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | ------------------------ | --------- |
| 2      | 1485 and later | 3474    | `actionverification.bss` | 1,304 | 150 Action, 14 Character | 8         |
| 1      | 1230           | 1230    | `actionverification.bss` | 100   | 5 Row                    | 16        |

| Layout | File                     | Known            | Unknown      |
| ------ | ------------------------ | ---------------- | ------------ |
| 2      | `actionverification.bss` | 1,304 B (100.0%) | 0 B (0.0%)   |
| 1      | `actionverification.bss` | 60 B (60.0%)     | 40 B (40.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2519   | Layout 2 |
| 2107   | Layout 2 |
| 1784   | Layout 2 |
| 1485   | Layout 2 |
| 1230   | Layout 1 |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                          |
| ---------------------------- | -------- | ------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | Character keys with a `characterstatic.dbss` row, for the link |
| `languagedata_en.loc`        | Optional | Character names (LOC type 6, `str_id1` = character key)       |

All multi-byte values are little-endian.

## Layout 2

### File Layout

A `PABR` table of variable-size character entries with an empty string
table.

| Offset                | Type             | Field              | Notes                                         |
| --------------------- | ---------------- | ------------------ | --------------------------------------------- |
| `+0x00`               | char[4]          | magic              | ASCII `PABR`                                  |
| `+0x04`               | u32              | count              | Number of characters; `14` on client 3474     |
| `+0x08`               | Character[count] | characters         | See Character                                 |
| `characters+0x00`     | String Table     | string_table       | Empty string table                            |
| `string_table+0x00`   | u32              | string_table_start | End of the characters, `1292` on client 3474  |
| `string_table+0x04`   | u32              | zero               | `0`                                           |

The characters are in neither key order nor sheet order (`1`, `65002`,
`2`, `65003`, `3`, `65005`, `21`, `5`, `65008` and up on client 3474).

### Character (variable: 6 bytes + actions)

| Offset  | Type                 | Field        | Notes                                              |
| ------- | -------------------- | ------------ | -------------------------------------------------- |
| `+0x00` | u16                  | character_key | Character key (LOC type 6 name); unique in the file; see Notes |
| `+0x02` | u32                  | action_count | Number of actions                                  |
| `+0x06` | Action[action_count] | actions      | See Action                                         |

### Action (8 bytes)

| Offset  | Type | Field          | Notes                                                                 |
| ------- | ---- | -------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | action_hash    | `ascii_key_hash` of the action name (`_common/string_hash.py`); unique within a character |
| `+0x04` | u32  | able_call_time | `AbleCallTime`, the sheet value cut to a whole number (`598.290598` is stored as `598`) |

The actions of a character are not in sheet order either.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Layout 1

Client 1230 has one action per character and no action hash: 5 rows for
the five player classes of Layout 2, in the same order, each with the same
`able_call_time` as its one Layout 2 action.

### File Layout

| Offset              | Type         | Field              | Notes                                   |
| ------------------- | ------------ | ------------------ | --------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                            |
| `+0x04`             | u32          | count              | Number of rows; `5` on client 1230      |
| `+0x08`             | Row[count]   | rows               | See Row                                 |
| `rows+0x00`         | String Table | string_table       | Empty string table                      |
| `string_table+0x00` | u32          | string_table_start | End of the rows, `88` on client 1230    |
| `string_table+0x04` | u32          | zero               | `0`                                     |

### Row (16 bytes)

| Offset  | Type | Field          | Notes                                    |
| ------- | ---- | -------------- | ---------------------------------------- |
| `+0x00` | u32  | unknown_00     | `8` in every row; see Open Questions     |
| `+0x04` | u32  | unknown_04     | `0` in every row                         |
| `+0x08` | u32  | character_key  | Player class character key               |
| `+0x0C` | u32  | able_call_time | As in Layout 2                           |

## Action Names

The client stores the names only as `action_hash`. The handler names an
action from the 29 action names of the client 1784 sheet (see Field
Names), each hashed with `ascii_key_hash`; an action whose hash is not one
of them shows as hex. On client 3474 all 150 action hashes are one of the
29.

| Character keys  | Action names                                                                 |
| --------------- | ---------------------------------------------------------------------------- |
| `1`, `2`, `5`   | `BT_WAIT`                                                                    |
| `3`             | `BT_skill_SkyFall`                                                           |
| `21`            | `BT_skill_ThrustAndSmash_AttQ1`                                              |
| `65002` to `65037` | `SHADOW_ATTACK_1` to `SHADOW_ATTACK_6`, `SHADOW_ATTACK_1_2`, `SHADOW_ATTACK_F_1` to `SHADOW_ATTACK_F_5`, `SHADOW_ATTACK_L_1` to `SHADOW_ATTACK_L_3`, `SHADOW_ATTACK_L_1_C`, `SHADOW_ATTACK_R_1` to `SHADOW_ATTACK_R_3`, `SHADOW_ATTACK_R_1_C`, `SHADOW_DASHATTACK_1`, `SHADOW_JUMP_ATTACK`, `SHADOW_DASHJUMP_ATTACK`, `BT_ROLL_L`, `BT_ROLL_R`, `BT_ROLL_B` |

## Field Names

The names follow the `ActionVerification_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784, columns `CharacterKey`,
`ActionName` and `AbleCallTime`. All 150 sheet rows are in the client 1784
and 3474 files: the `ascii_key_hash` of each `ActionName` is an
`action_hash` of the row's `CharacterKey`, and its `AbleCallTime`, cut to a
whole number, is the stored `able_call_time` (150 of 150 rows, client
3474). The server dump of the same private server reads the sheet in the
function at `0x1408f0b10`.

The 2016 PDB has no action verification type and the client 519 tables
have no such table.

## Notes

- The client 1784, 1485, 2107, 2519, 3002, 3251 and 3474 files are byte for
  byte the same. Client 794 has no `actionverification.bss`.
- Each hero character key is `64950` plus a class type of
  [`actionverificationindex.dbss`](actionverificationindex_dbss.md):
  `65002` Jordine is class type `52` Jordine, and the LOC names of the two
  agree for Peony, Ahon Kirus, Povios, Syaki, Nelydormin and Orwen as well.
  `65031` (Striker) and `65037` (Tamer) give `81` and `87`, which LOC type
  21 names `[PH] 22` and `[PH] 28`. Class types `61`, `65` and `71` have no
  character in this file.
- On client 3474 the five player class keys have a `characterstatic.dbss`
  row and the nine hero keys have none; every key has a LOC type 6 name.
- `BT_ROLL_L`, `BT_ROLL_R` and `BT_ROLL_B` hold `230` for every hero on
  client 3474 (`230.769231` in the sheet).

## Open Questions

### Unit of `able_call_time`

The sheet values are fractions such as `230.769231` (`3000 / 13`) and
`598.290598`; the stored values are whole numbers from `230` to `6300` on
client 3474. No client Lua file names `ActionVerification` or
`AbleCallTime`, so the unit (milliseconds or another time base) is not
confirmed.

### What the Layout 1 `unknown_00` Holds

Each client 1230 row starts with a u32 `8` and a u32 `0`. The `8` could
be the size of the `character_key` and `able_call_time` pair that follows,
or an action count of another meaning; with five identical rows the
reading cannot be told apart.
