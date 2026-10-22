# `palacemanagementstaticstatus.bss` Format

## Purpose

The palace management (royal workshop) boards: eight board groups, each
with its Korean name, texture, type (production or processing), NPC and
boards, then the production boards with their items and chances, the
processing boards with their items, six u16 settings and a u16 per service
nation code. Every item is an `itemexchangesource.bss` key. The Lua reads
it through the `ToClient_PalaceManage*` and `ToClient_GetPalaceManage*`
calls of `panel_window_palacemanagement_*.luac`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes | Records                                                                                                                     | Row bytes |
| ------ | -------------- | ------- | ---------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------- | --------- |
| 1      | 2765 and later | 3482    | `palacemanagementstaticstatus.bss` | 4,325 | 32 Board Ref, 8 Board Group, 182 Production Item, 20 Production Board, 84 Manufacture Item, 12 Manufacture Board, 12 Nation | 10        |

| Layout | File                               | Known           | Unknown     |
| ------ | ---------------------------------- | --------------- | ----------- |
| 1      | `palacemanagementstaticstatus.bss` | 4,257 B (98.4%) | 68 B (1.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | No file  |
| 2313   | No file  |
| 2107   | No file  |
| 1937   | No file  |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                           |
| --------------------- | -------- | -------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | NPC names (LOC type 6) and exchange names (LOC type 24)        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                    | Type                                       | Field                         | Notes                                                    |
| ------------------------- | ------------------------------------------ | ----------------------------- | -------------------------------------------------------- |
| `+0x00`                   | char[4]                                    | magic                         | ASCII `PABR`                                             |
| `+0x04`                   | u32                                        | board_group_count             | Number of `board_groups`; `8` on client 3482             |
| `+0x08`                   | Board Group[board_group_count]             | board_groups                  | See Board Group                                          |
| `board_groups+0x00`       | u32                                        | production_board_count        | Number of `production_boards`; `20` on client 3482       |
| `board_groups+0x04`       | Production Board[production_board_count]   | production_boards             | See Production Board                                     |
| `production_boards+0x00`  | u32                                        | manufacture_board_count       | Number of `manufacture_boards`; `12` on client 3482      |
| `production_boards+0x04`  | Manufacture Board[manufacture_board_count] | manufacture_boards            | See Manufacture Board                                    |
| `manufacture_boards+0x00` | u16                                        | unknown_manufacture_boards_00 | `0`                                                      |
| `manufacture_boards+0x02` | u16                                        | unknown_manufacture_boards_02 | `1`                                                      |
| `manufacture_boards+0x04` | u16                                        | unknown_manufacture_boards_04 | `1`                                                      |
| `manufacture_boards+0x06` | u16                                        | unknown_manufacture_boards_06 | `10`                                                     |
| `manufacture_boards+0x08` | u16                                        | unknown_manufacture_boards_08 | `1420`, a node key (Magoria); see Open Questions         |
| `manufacture_boards+0x0A` | u16                                        | unknown_manufacture_boards_0a | `1419`, a node key (Magoria)                             |
| `manufacture_boards+0x0C` | u32                                        | nation_count                  | Number of `nations`; `12` on client 3482                 |
| `manufacture_boards+0x10` | Nation[nation_count]                       | nations                       | See Nation                                               |
| `nations+0x00`            | String Table                               | string_table                  | See String Table                                         |
| `EOF-0x08`                | u32                                        | table_start                   | Offset of the string table, where `nations` ends         |
| `EOF-0x04`                | u32                                        | zero                          | Always `0`                                               |

### Board Group (variable: 23 bytes + boards)

| Offset  | Type                   | Field                | Notes                                                                        |
| ------- | ---------------------- | -------------------- | ---------------------------------------------------------------------------- |
| `+0x00` | u16                    | board_group_key      | `1` to `8`                                                                   |
| `+0x02` | u32                    | board_group_name_ref | String-table index of the Korean group name (`경회루` for group `1`)         |
| `+0x06` | u32                    | texture_ref          | String-table index of the texture ID, `Combine_Etc_PalaceManagement_NodePopUpImg_<n>` |
| `+0x0A` | u32                    | desc_ref             | String-table index of the description; `2`, the empty string, on every group |
| `+0x0E` | u8                     | board_group_type     | `0` production (groups `1` to `4`), `1` processing (`5` to `8`)              |
| `+0x0F` | u16                    | npc_character_key    | The group's NPC; LOC type 6 title `<Royal Workshop Manager>` on every group |
| `+0x11` | u16                    | npc_dialog_index     | `1` on every group                                                           |
| `+0x13` | u32                    | board_count          | Number of `boards`; `5` per production group, `3` per processing group       |
| `+0x17` | Board Ref[board_count] | boards               | See Board Ref                                                                |

### Board Ref (3 bytes)

| Offset  | Type | Field      | Notes                                                                                    |
| ------- | ---- | ---------- | ---------------------------------------------------------------------------------------- |
| `+0x00` | u16  | board_key  | A `production_boards` key in a production group, a `manufacture_boards` key in a processing group |
| `+0x02` | u8   | unknown_02 | `1` on the first board of each group, else `0`                                           |

### Production Board (variable: 10 bytes + items)

| Offset  | Type                         | Field          | Notes                                                    |
| ------- | ---------------------------- | -------------- | -------------------------------------------------------- |
| `+0x00` | u16                          | board_key      | `1` to `20`                                              |
| `+0x02` | u32                          | board_name_ref | String-table index of the Korean board name              |
| `+0x06` | u32                          | item_count     | Number of `items`; `7` to `10` on client 3482            |
| `+0x0A` | Production Item[item_count]  | items          | See Production Item                                      |

### Production Item (10 bytes)

| Offset  | Type | Field        | Notes                                                                    |
| ------- | ---- | ------------ | ------------------------------------------------------------------------ |
| `+0x00` | u16  | item_index   | `0` up, the item's place on its board                                    |
| `+0x02` | u32  | probability  | Chance on the 1,000,000 = 100% scale; a board's items sum to `1000000`   |
| `+0x06` | u32  | exchange_key | `itemexchangesource.bss` key                                             |

### Manufacture Board (variable: 10 bytes + items)

| Offset  | Type                          | Field          | Notes                                       |
| ------- | ----------------------------- | -------------- | ------------------------------------------- |
| `+0x00` | u16                           | board_key      | `1` to `12`                                 |
| `+0x02` | u32                           | board_name_ref | String-table index of the Korean board name |
| `+0x06` | u32                           | item_count     | Number of `items`; `7` on every board       |
| `+0x0A` | Manufacture Item[item_count]  | items          | See Manufacture Item                        |

### Manufacture Item (6 bytes)

| Offset  | Type | Field        | Notes                                  |
| ------- | ---- | ------------ | -------------------------------------- |
| `+0x00` | u16  | item_index   | `0` to `6`                             |
| `+0x02` | u32  | exchange_key | `itemexchangesource.bss` key           |

### Nation (6 bytes)

| Offset  | Type | Field           | Notes                                                       |
| ------- | ---- | --------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | nation_code_ref | String-table index of a service nation code (`KR`, `NA`)    |
| `+0x04` | u16  | unknown_04      | `10` to `50`; see Open Questions                            |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                       |
| ------- | ------------------ | ------------ | --------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `61` on client 3482                                      |
| `+0x04` | pstr[string_count] | strings      | UTF-16 Korean names, texture IDs, one empty string and the nation codes     |

## Board Groups

The groups on client 3482, with the NPC's LOC type 6 name.

| `board_group_key` | Name       | Type       | `npc_character_key` | NPC           | Boards     |
| ----------------- | ---------- | ---------- | ------------------- | ------------- | ---------- |
| 1                 | 경회루     | Production | `62114`             | Yeongman      | `1` to `5`   |
| 2                 | 제생원     | Production | `62115`             | Choi Doyun    | `6` to `10`  |
| 3                 | 좌조       | Production | `62116`             | Kim Munki     | `11` to `15` |
| 4                 | 우조       | Production | `62117`             | Park Gyusik   | `16` to `20` |
| 5                 | 도서관사   | Processing | `62123`             | Seokdo        | `1` to `3`   |
| 6                 | 소주방     | Processing | `62120`             | Park Sugyeong | `4` to `6`   |
| 7                 | 선원전     | Processing | `62121`             | Sangdeok      | `7` to `9`   |
| 8                 | 군부       | Processing | `62125`             | Hyeokcheol    | `10` to `12` |

The nations on client 3482, as `nation_code` and `unknown_04`: KR `10`,
JP `10`, RU `25`, CH `10`, NA `50`, TW `10`, SA `10`, TH `10`, ID `10`,
TR `12`, ASIA `10`, CS `50`.

## Field Names

The palace management content is newer than client 1784's sheets (the
file first ships in client 2765), so no sheet of a private server's
`DataSheets.bexcel` on that client covers it. The names come from the
Lua of client 3482 and from the values:

| Field                                   | Lua (client 3482) and values                                                                    |
| --------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `board_group_key`                       | `ToClient_GetPalaceManageBoardGroupKey(index)` over `ToClient_GetPalaceManageBoardGroupCount()` |
| `board_group_name_ref`, `texture_ref`, `desc_ref` | `ToClient_GetPalaceManageBoardGroupName`, `...GetBoardGroupTextureID` and `...GetBoardGroupDesc(boardGroupKey)`: the three strings of each group are a Korean name, a texture ID and the one empty string |
| `board_group_type`                      | `ToClient_PalaceManagegetBoadGroupTypeRaw(boardGroupKey)`, compared with `__ePalaceManageType_Production` and `_Manufacture`; only type `0` groups list boards with chances, and the window asks `ToClient_PalaceManageGetProbability` only for production |
| `npc_character_key`, `npc_dialog_index` | `ToClient_PalaceManageGetNpcCharacterKey` and `...GetNpcDialogIndex(boardGroupKey)`; all eight keys are NPCs titled `<Royal Workshop Manager>` (LOC type 6) |
| `board_key`, `board_name_ref`           | `ToClient_PalaceManagegetBoadKeyRaw(boardGroupKey, index)` and `ToClient_PalaceManageGetBoardName` |
| `probability`                           | `ToClient_PalaceManageGetProbability(boardGroupKey, boardIndex, itemIndex)`; each production board sums to `1000000` |
| `exchange_key`                          | `ToClient_PalaceManageSelectItemExchangeSource(boardGroupKey, boardKey, itemIndex)`; every value is an `itemexchangesource.bss` key, `생산 거점` (production node) or `가공 거점` (processing node) by name |
| `nation_code_ref`                       | The strings it points to are the service nation codes                                           |

## Notes

- Clients 2765 and 3002 hold 11 nations (no `CS`) and are otherwise laid
  out the same; client 3251 matches client 3482 byte for byte. The file is
  not in the archives of client 1784.
- The handler shows one row per board item: the board group, its type and
  NPC, the board, the item index, the chance and the exchange. The group
  texture, the settings and the nation list stay on every record.

## Open Questions

### The Settings and Nation Values

The window reads `ToClient_GetPalaceManageFreeRerollCount()`,
`ToClient_PalaceManageGetNeedPearlCountForReroll()`,
`Toclient_getPalaceManageRegionKeyRaw()`,
`Toclient_getPalaceManageRegionWaypointKey()` and
`Toclient_getPalaceManageWorkerRegionWaypointKey()` with no argument,
which may read the six u16 after the boards: `1420` and `1419` are both
node keys of Magoria. The nation values (`50` for NA and CS, `25` for RU,
`12` for TR, `10` elsewhere) fit a Pearl price per service region for the
reroll, but no source ties them to it.

### The Board Flag

`unknown_02` is `1` on the first board each group lists. The window asks
`ToClient_PalaceManageGetBoardIsOpen(boardGroupKey, index)`, which may
start from it.
