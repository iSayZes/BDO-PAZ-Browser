# `redbattlefieldstaticstatusmanager.bss` Format

## Purpose

The Red Battlefield settings: 28 unnamed times and limits, the banner text
and the banner and map textures of the Red Battlefield window (client 3474
on), and the reward items for a win and a loss. On client 3474 the banner
text is "Red Battlefield: Castle Ruins", the win reward Battlefield Token
x50, Skill EXP (Red Battlefield Win) and Combat Secret Book (S), the loss
reward Battlefield Token x10 and Skill EXP (Red Battlefield Lose).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                    | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | --------------------------------------- | ----- | ------------- | --------- |
| 3      | 3474 and later | 3474    | `redbattlefieldstaticstatusmanager.bss` | 488   | 5 Reward Item | 12        |
| 2      | 3251           | 3251    | `redbattlefieldstaticstatusmanager.bss` | 198   | 4 Reward Item | 12        |
| 1      | 3002           | 3002    | `redbattlefieldstaticstatusmanager.bss` | 178   | 4 Reward Item | 12        |

| Layout | File                                    | Known         | Unknown       |
| ------ | --------------------------------------- | ------------- | ------------- |
| 3      | `redbattlefieldstaticstatusmanager.bss` | 358 B (73.4%) | 130 B (26.6%) |
| 2      | `redbattlefieldstaticstatusmanager.bss` | 72 B (36.4%)  | 126 B (63.6%) |
| 1      | `redbattlefieldstaticstatusmanager.bss` | 72 B (40.4%)  | 106 B (59.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 3 |
| 3251   | Layout 2 |
| 3002   | Layout 1 |
| 2519   | No file  |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                      |
| --------------------- | -------- | --------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Item names, LOC type 0; the banner text, LOC type 37      |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset                   | Type                          | Field                 | Notes                                                                    |
| ------------------------ | ----------------------------- | --------------------- | ------------------------------------------------------------------------ |
| `+0x00`                  | char[4]                       | magic                 | ASCII `PABR`                                                             |
| `+0x04`                  | u32                           | unknown_04            | `300000` on clients 3002 to 3474                                         |
| `+0x08`                  | u64                           | unknown_08            | `120`                                                                    |
| `+0x10`                  | u16                           | unknown_10            | `1`                                                                      |
| `+0x12`                  | u16                           | unknown_12            | `426`                                                                    |
| `+0x14`                  | f32                           | unknown_14            | `200`                                                                    |
| `+0x18`                  | f32                           | unknown_18            | `180`                                                                    |
| `+0x1C`                  | f32                           | unknown_1c            | `580`                                                                    |
| `+0x20`                  | u16                           | unknown_20            | `20` on client 3474, `16` on 3002 and 3251                               |
| `+0x22`                  | u32                           | unknown_22            | `100`                                                                    |
| `+0x26`                  | f32                           | unknown_26            | `999`                                                                    |
| `+0x2A`                  | f32                           | unknown_2a            | `999`                                                                    |
| `+0x2E`                  | f32                           | unknown_2e            | `999`                                                                    |
| `+0x32`                  | u32                           | unknown_32            | `20`                                                                     |
| `+0x36`                  | u64                           | unknown_36            | `120`                                                                    |
| `+0x3E`                  | u64                           | unknown_3e            | `30`                                                                     |
| `+0x46`                  | u64                           | unknown_46            | `300`                                                                    |
| `+0x4E`                  | u32                           | unknown_4e            | `1`                                                                      |
| `+0x52`                  | u32                           | unknown_52            | `3`; not on client 3002                                                  |
| `+0x56`                  | u32                           | unknown_56            | `2`                                                                      |
| `+0x5A`                  | u32                           | unknown_5a            | `40` on client 3474, `20` on 3002 and 3251                               |
| `+0x5E`                  | u32                           | unknown_5e            | `30` on client 3474, `16` on 3002 and 3251                               |
| `+0x62`                  | u64                           | unknown_62            | `180`                                                                    |
| `+0x6A`                  | u64                           | unknown_6a            | `900`                                                                    |
| `+0x72`                  | u32                           | unknown_72            | `3`; not on client 3002                                                  |
| `+0x76`                  | u32                           | unknown_76            | `15` on client 3474, `3` on 3251                                         |
| `+0x7A`                  | u32                           | unknown_7a            | `200000` on client 3474, `1000` on 3251                                  |
| `+0x7E`                  | u32                           | unknown_7e            | `100000` on client 3474, `1200` on 3251                                  |
| `+0x82`                  | u32                           | unknown_82            | `3`; client 3474 only                                                    |
| `+0x86`                  | u32                           | banner_text_sheet_ref | String table index of the sheet of the banner text, `GAME`               |
| `+0x8A`                  | u32                           | banner_text_key_ref   | String table index of the banner text key, `LUA_WINDOW_VOICECHAT_SETTING_CHANNEL_2` ("Red Battlefield: Castle Ruins") |
| `+0x8E`                  | u32                           | banner_texture_ref    | String table index of the banner texture, `Combine_Etc_RedBattleField_War_Renewal_Img_02` |
| `+0x92`                  | u32                           | map_texture_ref       | String table index of the map texture, `Ingame_RedBattleField_War_Map_01` |
| `+0x96`                  | u32                           | win_reward_count      | Number of win rewards, up to 3 (the Lua asserts it)                      |
| `+0x9A`                  | Reward Item[win_reward_count] | win_reward_items      | See Reward Item                                                          |
| `win_reward_items+0x00`  | u32                           | lose_reward_count     | Number of loss rewards, up to 3                                          |
| `win_reward_items+0x04`  | Reward Item[lose_reward_count] | lose_reward_items    | See Reward Item                                                          |
| `lose_reward_items+0x00` | String Table                  | string_table          | See String Table                                                         |
| `string_table+0x00`      | u32                           | table_start           | Offset of the string table, where `lose_reward_items` ends               |
| `string_table+0x04`      | u32                           | zero                  | Always `0`                                                               |

Values without a client are the same on clients 3002, 3251 and 3474.

### Reward Item (12 bytes)

| Offset  | Type | Field      | Notes                                                                                     |
| ------- | ---- | ---------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key   | `enchant_level << 24 \| item_id`, the key of [itemenchant](itemenchant_dbss.md); every level is `0` |
| `+0x04` | u64  | item_count | Number of items                                                                           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                  |
| ------- | ------------------ | ------------ | ---------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `4` on client 3474, `0` on 3002 and 3251            |
| `+0x04` | pstr[string_count] | strings      | Wide ASCII: the sheet, the text key and the two texture names, in field order |

## Layout 2

### File Layout

| Offset                   | Type                          | Field             | Notes                                                       |
| ------------------------ | ----------------------------- | ----------------- | ----------------------------------------------------------- |
| `+0x00`                  | char[4]                       | magic             | ASCII `PABR`                                                |
| `+0x04`                  | u32                           | unknown_04        |                                                             |
| `+0x08`                  | u64                           | unknown_08        |                                                             |
| `+0x10`                  | u16                           | unknown_10        |                                                             |
| `+0x12`                  | u16                           | unknown_12        |                                                             |
| `+0x14`                  | f32                           | unknown_14        |                                                             |
| `+0x18`                  | f32                           | unknown_18        |                                                             |
| `+0x1C`                  | f32                           | unknown_1c        |                                                             |
| `+0x20`                  | u16                           | unknown_20        |                                                             |
| `+0x22`                  | u32                           | unknown_22        |                                                             |
| `+0x26`                  | f32                           | unknown_26        |                                                             |
| `+0x2A`                  | f32                           | unknown_2a        |                                                             |
| `+0x2E`                  | f32                           | unknown_2e        |                                                             |
| `+0x32`                  | u32                           | unknown_32        |                                                             |
| `+0x36`                  | u64                           | unknown_36        |                                                             |
| `+0x3E`                  | u64                           | unknown_3e        |                                                             |
| `+0x46`                  | u64                           | unknown_46        |                                                             |
| `+0x4E`                  | u32                           | unknown_4e        |                                                             |
| `+0x52`                  | u32                           | unknown_52        |                                                             |
| `+0x56`                  | u32                           | unknown_56        |                                                             |
| `+0x5A`                  | u32                           | unknown_5a        |                                                             |
| `+0x5E`                  | u32                           | unknown_5e        |                                                             |
| `+0x62`                  | u64                           | unknown_62        |                                                             |
| `+0x6A`                  | u64                           | unknown_6a        |                                                             |
| `+0x72`                  | u32                           | unknown_72        |                                                             |
| `+0x76`                  | u32                           | unknown_76        |                                                             |
| `+0x7A`                  | u32                           | unknown_7a        |                                                             |
| `+0x7E`                  | u32                           | unknown_7e        |                                                             |
| `+0x82`                  | u32                           | win_reward_count  | No `unknown_82` and no text or texture indexes before it    |
| `+0x86`                  | Reward Item[win_reward_count] | win_reward_items  | See Reward Item                                             |
| `win_reward_items+0x00`  | u32                           | lose_reward_count |                                                             |
| `win_reward_items+0x04`  | Reward Item[lose_reward_count] | lose_reward_items |                                                            |
| `lose_reward_items+0x00` | String Table                  | string_table      | No strings                                                  |
| `string_table+0x00`      | u32                           | table_start       |                                                             |
| `string_table+0x04`      | u32                           | zero              |                                                             |

## Layout 1

### File Layout

| Offset                   | Type                          | Field             | Notes                                                       |
| ------------------------ | ----------------------------- | ----------------- | ----------------------------------------------------------- |
| `+0x00`                  | char[4]                       | magic             | ASCII `PABR`                                                |
| `+0x04`                  | u32                           | unknown_04        |                                                             |
| `+0x08`                  | u64                           | unknown_08        |                                                             |
| `+0x10`                  | u16                           | unknown_10        |                                                             |
| `+0x12`                  | u16                           | unknown_12        |                                                             |
| `+0x14`                  | f32                           | unknown_14        |                                                             |
| `+0x18`                  | f32                           | unknown_18        |                                                             |
| `+0x1C`                  | f32                           | unknown_1c        |                                                             |
| `+0x20`                  | u16                           | unknown_20        |                                                             |
| `+0x22`                  | u32                           | unknown_22        |                                                             |
| `+0x26`                  | f32                           | unknown_26        |                                                             |
| `+0x2A`                  | f32                           | unknown_2a        |                                                             |
| `+0x2E`                  | f32                           | unknown_2e        |                                                             |
| `+0x32`                  | u32                           | unknown_32        |                                                             |
| `+0x36`                  | u64                           | unknown_36        |                                                             |
| `+0x3E`                  | u64                           | unknown_3e        |                                                             |
| `+0x46`                  | u64                           | unknown_46        |                                                             |
| `+0x4E`                  | u32                           | unknown_4e        |                                                             |
| `+0x52`                  | u32                           | unknown_56        | No `unknown_52` before it                                   |
| `+0x56`                  | u32                           | unknown_5a        |                                                             |
| `+0x5A`                  | u32                           | unknown_5e        |                                                             |
| `+0x5E`                  | u64                           | unknown_62        |                                                             |
| `+0x66`                  | u64                           | unknown_6a        |                                                             |
| `+0x6E`                  | u32                           | win_reward_count  | No `unknown_72` to `unknown_7e` before it                   |
| `+0x72`                  | Reward Item[win_reward_count] | win_reward_items  | See Reward Item                                             |
| `win_reward_items+0x00`  | u32                           | lose_reward_count |                                                             |
| `win_reward_items+0x04`  | Reward Item[lose_reward_count] | lose_reward_items |                                                            |
| `lose_reward_items+0x00` | String Table                  | string_table      | No strings                                                  |
| `string_table+0x00`      | u32                           | table_start       |                                                             |
| `string_table+0x04`      | u32                           | zero              |                                                             |

## Reward Items

| Client      | Win                                                                                      | Loss                                                              |
| ----------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| 3002, 3251  | Weathered Battlefield Token (767689) x25, Skill EXP (Red Battlefield Win) (61) x1          | Weathered Battlefield Token x10, Skill EXP (Red Battlefield Lose) (62) x1 |
| 3474        | Battlefield Token (890002) x50, Skill EXP (Red Battlefield Win) x1, Combat Secret Book (S) (890117) x1 | Battlefield Token x10, Skill EXP (Red Battlefield Lose) x1 |

## Field Names

The Red Battlefield file is newer than client 1784 and 2107, which do not
ship it, so no sheet of a private server's `DataSheets.bexcel` covers it.
The named fields follow the client Lua of client 3474:

- `panel_redbattlefieldinfo_all` reads `ToClient_GetRedBattleFieldRewardSize(isWin)`,
  then per index `...RewardItemKey(isWin, index)` and `...RewardItemCount`,
  and asserts at most 3 rewards per side. The first list is the win side:
  its Skill EXP item is the Win one.
- `banner_Init` sets the banner title from
  `ToClient_GetRedBattleFieldBannerMapString()`, the banner from
  `...BannerTextureID()` and the minimap from `...MapTextureID()`. The four
  string-table entries are a GAME sheet key whose text names a battlefield
  map and two texture names, a banner image and a map image.

The Lua also reads `ToClient_GetPlayingTimeRedBattleField()`,
`...IntrusionTime...` (both divided by 60 for minutes),
`...MatchingPlayerCount()`, `...MaxPlayerCount()`,
`ToClient_GetAttackForLimitedRedBattleField()`, `...Defense...` and
`...ADSummary...`; which unnamed values they come from is not known.

## Notes

- The file is 178 bytes on client 3002, 198 on 3251 and 488 on 3474;
  clients 1784 to 2519 do not ship it.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in `_bss/pabr_values/pvp_tables.py`:
  the banner text key with its text, the two textures and the reward items.

## Open Questions

### Unnamed Settings

Which of `unknown_04` to `unknown_82` are the play time, the join
(intrusion) time, the matching and maximum player counts and the AP, DP and
AP + DP limits of the limited Red Battlefield. Leads: `unknown_14` to
`unknown_1c` (200, 180, 580) and `unknown_26` to `unknown_2e` (999 each)
are float triples that fit the three limits; `unknown_6a` is 900 (15
minutes in seconds). The u64 and u16 widths follow zero high bytes and are
not confirmed.
