# `minigamefind.bss` Format

## Purpose

The Lakiaro digging minigame (`Panel_MiniGame_Find_All`): one row per game
type with its grid size, the hoes it takes, its rates, its six reward items
and the [`minigamefindpattern.dbss`](minigamefindpattern_dbss.md) slot groups
it draws from, then a second table with one row per Lakiaro character and
dig depth. On client 3482 the file holds 18 game types in four chains (1 to
5, 6 to 10, 11 to 15, 16 to 18) and 19 Lakiaro rows.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes | Records                          | Row bytes |
| ------ | -------------- | ------- | ------------------ | ----- | -------------------------------- | --------- |
| 1      | 1230 and later | 3482    | `minigamefind.bss` | 2,296 | 18 Type Row, 19 Collect Rate Row | 26        |

| Layout | File               | Known           | Unknown     |
| ------ | ------------------ | --------------- | ----------- |
| 1      | `minigamefind.bss` | 2,220 B (96.7%) | 76 B (3.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3482   | Layout 1             |
| 3474   | Layout 1             |
| 3251   | Layout 1             |
| 3002   | Layout 1             |
| 2765   | Layout 1             |
| 2519   | Layout 1             |
| 2107   | Layout 1             |
| 1937   | Layout 1             |
| 1784   | Layout 1             |
| 1636   | Layout 1             |
| 1485   | Layout 1             |
| 1348   | Layout 1             |
| 1230   | Layout 1             |
| 1058   | No file              |
| 794    | No documented layout |

<!-- versions:end -->

## Companion Files

None. Item names come from LOC type 0 and character names from LOC type 6.

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR with two counted tables back to back, then the counted string table and
8-byte trailer of [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`). The string table holds the two image paths the
Lakiaro rows name.

| Offset                   | Type                                 | Field              | Notes                                         |
| ------------------------ | ------------------------------------ | ------------------ | --------------------------------------------- |
| `+0x00`                  | char[4]                              | magic              | ASCII `PABR`                                  |
| `+0x04`                  | u32                                  | type_count         | Number of game types; 18 on client 3482       |
| `+0x08`                  | Type Row[type_count]                 | type_rows          | See Type Row                                  |
| `type_rows+0x00`         | u32                                  | collect_rate_count | Number of Lakiaro rows; 19 on client 3482     |
| `type_rows+0x04`         | Collect Rate Row[collect_rate_count] | collect_rate_rows  | See Collect Rate Row                          |
| `collect_rate_rows+0x00` | String Table                         | string_table       | See String Table                              |
| `string_table+0x00`      | u32                                  | string_table_start | Offset of the string table, where the rows end |
| `string_table+0x04`      | u32                                  | zero               | Always `0`                                    |

On client 3482 the file is 8 + 18 x 92 + 4 + 19 x 26 + 130 + 8 = 2,296
bytes.

### Type Row (92 bytes)

| Offset  | Type   | Field               | Notes                                                                    |
| ------- | ------ | ------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u8     | game_type           | Row key, `1` to `18`                                                     |
| `+0x01` | u8     | game_type_dup       | Equal to `game_type` on every row                                        |
| `+0x02` | u8     | next_game           | `game_type` of the next game in the chain; `255` on the last one         |
| `+0x03` | u32    | min_damage_rate     | `1000000` on every row with a next game, `0` on the last ones            |
| `+0x07` | u32    | next_rate           | `1000000` on every row with a next game, `0` on the last ones            |
| `+0x0B` | u8     | life_type           | `0` on every row (clients 1784 and 3482)                                 |
| `+0x0C` | u32    | life_rate           | `5000` on every row (clients 1784 and 3482)                              |
| `+0x10` | u32[5] | tool_item_keys      | Hoes the game takes; `0` in a free slot                                  |
| `+0x24` | u32    | tool_rate           | `10000` on every row (clients 1784 and 3482)                             |
| `+0x28` | u32    | stone_rate          | `50000` to `300000` on client 3482, rising along each chain              |
| `+0x2C` | u32    | stone_drop_item_key | `4006` Rough Stone on every row (clients 1784 and 3482)                  |
| `+0x30` | u8     | col                 | Grid width: `12` or `14`; equal to `row` on every row                    |
| `+0x31` | u8     | row                 | Grid height: `12` or `14`                                                |
| `+0x32` | u8[4]  | start_pos           | `0, 0, 4, 4` on every row (clients 1784 and 3482)                        |
| `+0x36` | u8[6]  | min_root_count      | `7, 7, 4, 3, 3, 0` on the 12 x 12 games, `9, 9, 6, 5, 5, 0` on the 14 x 14 ones |
| `+0x3C` | u8[4]  | begin_root_count    | One count per side in Left, Right, Top, Bottom order (see Directions)    |
| `+0x40` | u8[4]  | use_slot_indexes    | `slot_index` groups of `minigamefindpattern.dbss`; `0` in a free slot    |
| `+0x44` | u32[6] | reward_item_keys    | Reward items, slot 0 first (see Rewards)                                 |

The rows are stored in key order 15 down to 1, then 18, 17, 16 (clients
1784 and 3482).

### Collect Rate Row (26 bytes)

| Offset  | Type   | Field           | Notes                                                                    |
| ------- | ------ | --------------- | ------------------------------------------------------------------------ |
| `+0x00` | u16    | character_key   | Row key: a Lakiaro character (LOC type 6), unique                        |
| `+0x02` | u32    | unknown_02      | `1` on every row (clients 1784 and 3482); see Open Questions             |
| `+0x06` | u16[4] | slot_coordinate | Pixel rectangle (x1, y1, x2, y2) in `image_ref`'s image                  |
| `+0x0E` | u32    | image_ref       | String table index of the image path                                     |
| `+0x12` | u8     | main_game_type  | `game_type` that opens the chain: `1`, `6` or `11` on client 3482        |
| `+0x13` | u32    | collect_rate    | `1000000` on every row (clients 1784 and 3482)                           |
| `+0x17` | u8     | depth           | `1` to `5`                                                               |
| `+0x18` | u16    | vary_wp         | `0`, `20`, `30`, `40` or `50` on client 3482                             |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                          |
| ------- | ------------------ | ------------ | ------------------------------ |
| `+0x00` | u32                | string_count | `2` on clients 1784 and 3482   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries            |

The two strings are `New_UI_Common_forLua\Window\MiniGame\MiniGameFind_03.dds`
(index 0) and `MiniGameFind_01.dds` (index 1) in the same folder, which is
`ui_texture/new_ui_common_forlua/window/minigame/` in the PAZ index.

## Directions

`begin_root_count` holds one count per side in the order of the
`minigamefindpattern.dbss` direction values: Left, Right, Top, Bottom. The
order comes from the sheet (see Field Names): its `BeginRootCount_Left`,
`_Top`, `_Right` and `_Bottom` columns match bytes 0, 2, 1 and 3 on 18 of 18
rows (client 1784).

## Rewards

The minigame window Lua (`panel_minigame_find_all_1`, `getRewardIndex`)
highlights one of the six reward slots by the share it shows: slot 0 at
100%, otherwise slot 5 up to 20%, slot 4 up to 40%, slot 3 up to 60%, slot 2
up to 80% and slot 1 above. `FromClient_MiniGameFindSetReward` fills the
slots from a list of item keys.

On client 3482 chains 1 to 5 and 16 to 18 give Lakiaro sacks (`761251`
Young Lakiaro Sack to `761260` Primitive Lakiaro Sack) and chain 6 to 10 the
Lush ones (`761261` to `761270`); game type 16 also gives `720112` Wild
Grass Sack and `5439` Wild Grass. Chain 11 to 15 gives `720111` Wild Grass
Sack, `5439` Wild Grass and `5600` Weeds, as on client 1784.

## Field Names

The type rows are the `MiniGameFindType` sheet and the Lakiaro rows the
`MiniGameFindCollectRate` sheet of a private server's `DataSheets.bexcel` on
client 1784. Matched by key on the client 1784 file:

| Field                                 | Column                         | Same value (client 1784) |
| ------------------------------------- | ------------------------------ | ------------------------ |
| `game_type`                           | `GameType`                     | 18 of 18                 |
| `next_game` (`<null>` as `255`)       | `NextGame`                     | 18 of 18                 |
| `min_damage_rate`, `next_rate`        | `MinDamageRate`, `NextRate`    | 18 of 18                 |
| `life_type`, `life_rate`              | `LifeType`, `LifeRate`         | 18 of 18                 |
| `tool_item_keys`                      | `ToolIndex`                    | 18 of 18                 |
| `tool_rate`                           | `ToolRate`                     | 18 of 18                 |
| `stone_rate`, `stone_drop_item_key`   | `StoneRate`, `StoneDropKey`    | 18 of 18                 |
| `col`, `row`                          | `Col`, `Row`                   | 18 of 18                 |
| `start_pos`                           | `StartPos`                     | 18 of 18                 |
| `min_root_count`                      | `MinRootCount`                 | 18 of 18                 |
| `begin_root_count`                    | `BeginRootCount_*`             | 18 of 18                 |
| `use_slot_indexes`                    | `UseSlotIndexList`             | 18 of 18                 |
| `reward_item_keys`                    | `Reward_0` to `Reward_5`       | 18 of 18                 |
| `character_key`                       | `CharacterKey`                 | 12 of 14                 |
| `slot_coordinate`, `image_ref`        | `SlotCoordinate`, `ImageFile`  | 12 of 12                 |
| `main_game_type`, `collect_rate`      | `MainGameType`, `CollectRate`  | 12 of 12                 |
| `depth`, `vary_wp` (`<null>` as `0`)  | `Depth`, `VaryWp`              | 12 of 12                 |

The two sheet rows the client 1784 file lacks are `27635` and `27636`, the
only ones with `MainGameType` `16`. On client 3482 the same columns match 18
of 18 type keys except `begin_root_count` (17, game type 8 now ends in `1`)
and `reward_item_keys` (5, the new sack items), and 12 of 12 Lakiaro keys.
The sheet has no column for `unknown_02`. `col` and `row` are equal on every
row, so their order follows the sheet, not the data.

## Notes

- The tools on client 3482 are `16479` Manos Hoe, `16480` Dostter Hoe,
  `16540` Dostter Steel Hoe and `65496` QA Lakiaro Hoe on game types 1 to
  15, and `16652` [Event] Ahr Hoe and `65496` on 16 to 18.
- The Lakiaro characters are `27621` to `27630` and `27637`, `27638` (as on
  client 1784), and `24885` to `24889`, `25197` and `25198` (client 3482
  only); LOC type 6 names them all Lakiaro, `27626` to `27630` "... Lakiaro
  for Research".
- `slot_coordinate` and the image are the Lakiaro's picture: the Lua
  receives a texture path and a UV rectangle for the grid
  (`FromClient_Minigame_Find_All_DefaultImage`). The rectangles are 221 x
  221 pixels on every row of client 3482.
- The window Lua reads the damage share as `damageRate / 10000`, so rates
  in this minigame count `1000000` as 100%.

## Open Questions

### What `unknown_02` Holds

The u32 after `character_key` is `1` on every Lakiaro row of clients 1784
and 3482, and the `MiniGameFindCollectRate` sheet has no column left for
it.
