# `solareoptionstaticstatusmanager.bss` Format

## Purpose

Arena of Solare options. Per game mode the rank tiers: eight rank groups,
each with up to four tiers, and per tier the lowest rating, a ranking
limit, the `GAME` sheet key of the tier name, the tier icon, the four frame
textures of the match slot and the HP widget, and nine item lists: the
match rewards of Ranked, Practice and Custom matches, each for a victory,
a defeat and a draw (see [Item Lists](#item-lists)). After the modes
come common values, a list of 20 item keys and the Solare equipment
presets: per class type the weapons a player can pick, and one shared
preset with the armor, accessories and crystals. On client 3482 game modes `0` and `1` hold 24 tiers each, and 32
class types have weapon presets.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                  | Bytes  | Records                                                                             | Row bytes              |
| ------ | -------------- | ------- | ------------------------------------- | ------ | ----------------------------------------------------------------------------------- | ---------------------- |
| 4      | 3474 and later | 3482    | `solareoptionstaticstatusmanager.bss` | 17,773 | 333 List Item, 432 Item List, 48 Tier, 32 Group, 4 Mode, 132 Preset Item, 48 Preset | 8 to 40, 20 on average |
| 3      | 3412 to 3454   | 3454    | `solareoptionstaticstatusmanager.bss` | 14,169 | 144 Item Block, 48 Tier, 32 Group, 4 Mode, 132 Preset Item, 48 Preset               | 36                     |
| 2      | 3381           | 3381    | `solareoptionstaticstatusmanager.bss` | 14,099 | 144 Item Block, 48 Tier, 32 Group, 4 Mode, 129 Preset Item, 48 Preset               | 36                     |
| 1      | 3314 to 3349   | 3349    | `solareoptionstaticstatusmanager.bss` | 13,846 | 144 Item Block, 48 Tier, 32 Group, 4 Mode, 129 Preset Item, 38 Preset               | 36                     |

| Layout | File                                  | Known            | Unknown         |
| ------ | ------------------------------------- | ---------------- | --------------- |
| 4      | `solareoptionstaticstatusmanager.bss` | 13,709 B (77.1%) | 4,064 B (22.9%) |
| 3      | `solareoptionstaticstatusmanager.bss` | 11,441 B (80.7%) | 2,728 B (19.3%) |
| 2      | `solareoptionstaticstatusmanager.bss` | 11,423 B (81.0%) | 2,676 B (19.0%) |
| 1      | `solareoptionstaticstatusmanager.bss` | 11,253 B (81.3%) | 2,593 B (18.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 4 |
| 3474   | Layout 4 |
| 3454   | Layout 3 |
| 3412   | Layout 3 |
| 3381   | Layout 2 |
| 3349   | Layout 1 |
| 3314   | Layout 1 |
| 3283   | No file  |
| 3251   | No file  |
| 3212   | No file  |
| 3177   | No file  |
| 3144   | No file  |
| 3103   | No file  |
| 3062   | No file  |
| 3037   | No file  |
| 3002   | No file  |
| 2959   | No file  |
| 2923   | No file  |
| 2900   | No file  |
| 2872   | No file  |
| 2834   | No file  |
| 2803   | No file  |
| 2765   | No file  |
| 2736   | No file  |
| 2703   | No file  |
| 2665   | No file  |
| 2637   | No file  |
| 2606   | No file  |
| 2583   | No file  |
| 2545   | No file  |
| 2519   | No file  |
| 2498   | No file  |
| 2468   | No file  |
| 2438   | No file  |
| 2414   | No file  |
| 2384   | No file  |
| 2358   | No file  |
| 2335   | No file  |
| 2313   | No file  |
| 2290   | No file  |
| 2250   | No file  |
| 2224   | No file  |
| 2203   | No file  |
| 2179   | No file  |
| 2151   | No file  |
| 2134   | No file  |
| 2107   | No file  |
| 2073   | No file  |
| 2052   | No file  |
| 2011   | No file  |
| 1996   | No file  |
| 1969   | No file  |
| 1937   | No file  |
| 1914   | No file  |
| 1886   | No file  |
| 1866   | No file  |
| 1838   | No file  |
| 1818   | No file  |
| 1794   | No file  |
| 1784   | No file  |
| 1749   | No file  |
| 1717   | No file  |
| 1698   | No file  |
| 1674   | No file  |
| 1636   | No file  |
| 1608   | No file  |
| 1587   | No file  |
| 1565   | No file  |
| 1537   | No file  |
| 1509   | No file  |
| 1485   | No file  |
| 1466   | No file  |
| 1445   | No file  |
| 1426   | No file  |
| 1409   | No file  |
| 1390   | No file  |
| 1372   | No file  |
| 1360   | No file  |
| 1348   | No file  |
| 1338   | No file  |
| 1324   | No file  |
| 1316   | No file  |
| 1309   | No file  |
| 1286   | No file  |
| 1256   | No file  |
| 1230   | No file  |
| 1211   | No file  |
| 1194   | No file  |
| 1177   | No file  |
| 1156   | No file  |
| 1127   | No file  |
| 1109   | No file  |
| 1076   | No file  |
| 1058   | No file  |
| 1016   | No file  |
| 990    | No file  |
| 955    | No file  |
| 911    | No file  |
| 885    | No file  |
| 855    | No file  |
| 822    | No file  |
| 794    | No file  |
| 748    | No file  |
| 711    | No file  |
| 683    | No file  |
| 656    | No file  |
| 630    | No file  |
| 606    | No file  |
| 577    | No file  |
| 542    | No file  |
| 526    | No file  |
| 508    | No file  |
| 485    | No file  |
| 457    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role |
| --------------------- | -------- | ---- |
| `stringtable.bss`     | Optional | Hash of the `description` key, for its LOC type 37 text |
| `ui_texture/texturestringkey/texturestring_combine.xml` | Optional | Sprite sheet and rectangle of the `icon_texture` key |
| `languagedata_en.loc` | Optional | Tier name in the user's language, item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 4

### File Layout

A PABR file with no record count. Every array has a fixed length: four
game modes, eight rank groups per mode and 48 presets.

| Offset                      | Type                       | Field                       | Notes |
| --------------------------- | -------------------------- | --------------------------- | ----- |
| `+0x00`                     | char[4]                    | magic                       | `PABR` |
| `+0x04`                     | Mode[4]                    | modes                       | See Mode; modes `0` and `1`, then two unused |
| `modes+0x00`                | f32                        | unknown_modes_00            | `10000` |
| `modes+0x04`                | u8                         | unknown_modes_04            | `100` |
| `modes+0x05`                | f32                        | unknown_modes_05            | `5000` |
| `modes+0x09`                | u64[9]                     | unknown_modes_09            | `120, 180, 60, 30, 180, 15, 180, 180, 60` |
| `modes+0x51`                | u32                        | unknown_win_str_ref         | Index into `strings`: `SOLARE_WIN` |
| `modes+0x55`                | u32                        | unknown_draw_str_ref        | Index into `strings`: `SOLARE_DRAW` |
| `modes+0x59`                | u32                        | unknown_lose_str_ref        | Index into `strings`: `SOLARE_LOSE` |
| `modes+0x5D`                | u32                        | unknown_modes_5d            | `14` |
| `modes+0x61`                | u32                        | unknown_modes_61            | `7` |
| `modes+0x65`                | u32                        | unknown_modes_65            | `2500` |
| `modes+0x69`                | u64                        | unknown_item_count          | Number of `unknown_item_keys`, `20` |
| `modes+0x71`                | u32[unknown_item_count]    | unknown_item_keys           | Item keys; see [unknown_item_keys](#unknown_item_keys) |
| `unknown_item_keys+0x00`    | bytes[3]                   | unknown_item_keys_00        | `0` |
| `unknown_item_keys+0x03`    | Preset[48]                 | equip_presets               | See Preset; index `0` to `46` is the class type, index `47` the shared preset |
| `equip_presets+0x00`        | f32[3]                     | unknown_equip_presets_00    | `3351, -8003, 83845`, a world position |
| `equip_presets+0x0C`        | f32[3]                     | unknown_equip_presets_0c    | `12889, -6781, 77556`, a world position |
| `equip_presets+0x18`        | f32                        | unknown_equip_presets_18    | `300` |
| `equip_presets+0x1C`        | f32                        | unknown_equip_presets_1c    | `13000` |
| `equip_presets+0x20`        | String Table               | string_table                | See String Table |
| `string_table+0x00`         | u32                        | string_table_start          | Absolute offset of `string_count` |
| `string_table+0x04`         | u32                        | zero                        | `0` |

### Mode (variable: 79 bytes + groups)

| Offset  | Type     | Field      | Notes |
| ------- | -------- | ---------- | ----- |
| `+0x00` | u8       | game_mode  | `0` and `1`; `4` on the two unused modes, which are `0` in every other byte |
| `+0x01` | u8       | unknown_01 | `0` |
| `+0x02` | u32      | unknown_02 | `60` |
| `+0x06` | u32      | unknown_06 | `401` |
| `+0x0A` | u8       | unknown_0a | `10` |
| `+0x0B` | f32      | unknown_0b | `1.5` |
| `+0x0F` | u32      | unknown_0f | `75` |
| `+0x13` | u32      | unknown_13 | `300` |
| `+0x17` | u32      | unknown_17 | `400` |
| `+0x1B` | u32      | unknown_1b | `150` |
| `+0x1F` | u32      | unknown_1f | `450` |
| `+0x23` | u32      | unknown_23 | `600` |
| `+0x27` | u32      | unknown_27 | `1` in mode `0`, `800` in mode `1`; the only value the two modes do not share |
| `+0x2B` | u32      | unknown_2b | `10` |
| `+0x2F` | f32      | unknown_2f | `400` |
| `+0x33` | u32      | unknown_33 | `10000` |
| `+0x37` | u32      | unknown_37 | `150` |
| `+0x3B` | i32      | unknown_3b | `-200` |
| `+0x3F` | u32      | unknown_3f | `100` |
| `+0x43` | u32      | unknown_43 | `300` |
| `+0x47` | u32      | unknown_47 | `300` |
| `+0x4B` | u32      | unknown_4b | `40` |
| `+0x4F` | Group[8] | groups     | See Group; rank groups `0` to `7` |

The values are those of client 3482, the same in modes `0` and `1` except
`unknown_27`.

### Group (variable: 49 bytes + tiers)

| Offset  | Type             | Field      | Notes |
| ------- | ---------------- | ---------- | ----- |
| `+0x00` | u8               | rank_group | `0` to `7` in file order; `8` in the unused modes |
| `+0x01` | f32              | unknown_01 | `40` in group `0` rising to `70` in groups `5` to `7` |
| `+0x05` | f32              | unknown_05 | `40` in group `0`, `46` in group `1`, `50` from group `2` on |
| `+0x09` | u16              | unknown_09 | `2` in groups `0` and `1`, `3` in group `2`, else `0` |
| `+0x0B` | u16              | unknown_0b | `1` in groups `0` and `1`, `2` in group `2`, else `0` |
| `+0x0D` | u16              | unknown_0d | `50`, `40`, `30` in groups `0` to `2`, else `0` |
| `+0x0F` | u8               | unknown_0f | `3`, or `0` in group `0` with three zero values after it |
| `+0x10` | f32[3]           | unknown_10 | `1.1, 1.2, 0.025` in groups `1` and `2`, up to `1.1, 1.5, 0.1` from group `4` on |
| `+0x1C` | u8               | unknown_1c | `3` in groups `0` to `2`, else `0` with three zero values after it |
| `+0x1D` | f32[3]           | unknown_1d | `1.05, 1.1, 0.05` in groups `0` and `1` |
| `+0x29` | u64              | tier_count | `3`, `4` in groups `5` and `6`, `1` in group `7`, `0` in the unused modes |
| `+0x31` | Tier[tier_count] | tiers      | See Tier |

### Tier (variable: 34 bytes + item lists)

| Offset  | Type          | Field                  | Notes |
| ------- | ------------- | ---------------------- | ----- |
| `+0x00` | u32           | min_rating             | Lowest rating of the tier: `2401` in group `0`, then `2301` down by 100 to `401`, and `0` for the last tier |
| `+0x04` | u32           | max_ranking            | `1` and `30` on the first two tiers of group `0`, else `0` (no ranking limit) |
| `+0x08` | u16           | rank_tier_key          | Rank group in the high byte, tier `1` up in the low byte (`0x0101` group 1, tier 1) |
| `+0x0A` | u32           | description            | Index into `strings`: a `GAME` sheet key (`LUA_SOLARE_RANK_TIER_00`) |
| `+0x0E` | u32           | icon_texture           | Index into `strings`: a texture key (`Solare_Tier01`) |
| `+0x12` | u32           | match_slot_right_frame | Index into `strings`: `Combine_Etc_Solare_War_MatchSlot_Right_Frame_NN` |
| `+0x16` | u32           | match_slot_left_frame  | Index into `strings`: `..._MatchSlot_Left_Frame_NN` |
| `+0x1A` | u32           | hp_widget_right_frame  | Index into `strings`: `..._HPWidget_Right_Frame_NN` |
| `+0x1E` | u32           | hp_widget_left_frame   | Index into `strings`: `..._HPWidget_Left_Frame_NN` |
| `+0x22` | Item List[9]  | item_lists             | See Item List and [Item Lists](#item-lists) |

### Item List (variable: 8 bytes + items)

| Offset  | Type             | Field      | Notes |
| ------- | ---------------- | ---------- | ----- |
| `+0x00` | u64              | item_count | Number of items, `0` to `2` |
| `+0x08` | List Item[item_count] | items | See List Item |

### List Item (16 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u32  | item_key   | Item key (`890008` Enthusiastic Solare Box, `65396` Seal of Solare) |
| `+0x04` | u32  | unknown_04 | `0x7FF6` on client 3482, `0x7FF7` on client 3474; the only bytes that differ between the two files |
| `+0x08` | u64  | count      | Item count |

### Preset (variable: 25 bytes + items)

| Offset             | Type                      | Field       | Notes |
| ------------------ | ------------------------- | ----------- | ----- |
| `+0x00`            | u8                        | class_type  | Class type (`0` Warrior), or `47` (`__eClassType_Count`) on the shared preset and on the unused entries |
| `+0x01`            | f32                       | unknown_01  | `1` on every filled preset, `0` on the unused ones |
| `+0x05`            | f32                       | unknown_05  | Equals `unknown_01` |
| `+0x09`            | u64                       | equip_count | Number of `equip_items`: `3` per class, `18` in the shared preset |
| `+0x11`            | Preset Item[equip_count]  | equip_items | See Preset Item |
| `equip_items+0x00` | u64                       | jewel_count | Number of `jewel_items`: `18` in the shared preset, else `0` |
| `equip_items+0x08` | Preset Item[jewel_count]  | jewel_items | See Preset Item; `index` is the socket |

### Preset Item (10 bytes)

| Offset  | Type | Field         | Notes |
| ------- | ---- | ------------- | ----- |
| `+0x00` | u32  | item_key      | Item key (`741301` Resolute Longsword, `15721` Secrua's Flaming Crystal) |
| `+0x04` | i32  | unknown_04    | `-1` on every item |
| `+0x08` | u8   | equip_slot_no | Equipment slot: `0` main weapon, `1` sub-weapon, `29` awakening weapon, `3` to `12` and `27` in the shared preset |
| `+0x09` | u8   | index         | `0` up per slot: the preset level of an equip item, the socket of a jewel item |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `80` on client 3482 |
| `+0x04` | pstr[string_count] | strings      | UTF-8 keys: tier names, tier icons, frame textures, then `SOLARE_WIN`, `SOLARE_DRAW`, `SOLARE_LOSE` |

## Layout 3

Clients 3412 and 3454 store one item per list: each tier holds three
blocks of three items with their counts, where Layout 4 has nine lists of
any length. The common values have no `unknown_modes_65`.

### File Layout

| Offset                   | Type                    | Field                    | Notes    |
| ------------------------ | ----------------------- | ------------------------ | -------- |
| `+0x00`                  | char[4]                 | magic                    | `PABR`   |
| `+0x04`                  | Mode[4]                 | modes                    | See Mode |
| `modes+0x00`             | f32                     | unknown_modes_00         |          |
| `modes+0x04`             | u8                      | unknown_modes_04         |          |
| `modes+0x05`             | f32                     | unknown_modes_05         |          |
| `modes+0x09`             | u64[9]                  | unknown_modes_09         |          |
| `modes+0x51`             | u32                     | unknown_win_str_ref      |          |
| `modes+0x55`             | u32                     | unknown_draw_str_ref     |          |
| `modes+0x59`             | u32                     | unknown_lose_str_ref     |          |
| `modes+0x5D`             | u32                     | unknown_modes_5d         |          |
| `modes+0x61`             | u32                     | unknown_modes_61         |          |
| `modes+0x65`             | u64                     | unknown_item_count       |          |
| `modes+0x6D`             | u32[unknown_item_count] | unknown_item_keys        |          |
| `unknown_item_keys+0x00` | bytes[3]                | unknown_item_keys_00     |          |
| `unknown_item_keys+0x03` | Preset[48]              | equip_presets            |          |
| `equip_presets+0x00`     | f32[3]                  | unknown_equip_presets_00 |          |
| `equip_presets+0x0C`     | f32[3]                  | unknown_equip_presets_0c |          |
| `equip_presets+0x18`     | f32                     | unknown_equip_presets_18 |          |
| `equip_presets+0x1C`     | f32                     | unknown_equip_presets_1c |          |
| `equip_presets+0x20`     | String Table            | string_table             |          |
| `string_table+0x00`      | u32                     | string_table_start       |          |
| `string_table+0x04`      | u32                     | zero                     | `0`      |

### Tier (142 bytes)

| Offset  | Type          | Field                  | Notes |
| ------- | ------------- | ---------------------- | ----- |
| `+0x00` | u32           | min_rating             | |
| `+0x04` | u32           | max_ranking            | |
| `+0x08` | u16           | rank_tier_key          | |
| `+0x0A` | u32           | description            | |
| `+0x0E` | u32           | icon_texture           | |
| `+0x12` | u32           | match_slot_right_frame | |
| `+0x16` | u32           | match_slot_left_frame  | |
| `+0x1A` | u32           | hp_widget_right_frame  | |
| `+0x1E` | u32           | hp_widget_left_frame   | |
| `+0x22` | Item Block[3] | item_lists             | See Item Block |

### Item Block (36 bytes)

| Offset  | Type   | Field     | Notes |
| ------- | ------ | --------- | ----- |
| `+0x00` | u32[3] | item_keys | One item key per list, `0` for none |
| `+0x0C` | u64[3] | counts    | The count of each item |

## Layout 2

Client 3381 has the item blocks of Layout 3, no `unknown_modes_5d` and
`unknown_modes_61`, and no values after the presets.

### File Layout

| Offset                   | Type                    | Field                | Notes                     |
| ------------------------ | ----------------------- | -------------------- | ------------------------- |
| `+0x00`                  | char[4]                 | magic                | `PABR`                    |
| `+0x04`                  | Mode[4]                 | modes                | See Mode                  |
| `modes+0x00`             | f32                     | unknown_modes_00     |                           |
| `modes+0x04`             | u8                      | unknown_modes_04     |                           |
| `modes+0x05`             | f32                     | unknown_modes_05     |                           |
| `modes+0x09`             | u64[9]                  | unknown_modes_09     |                           |
| `modes+0x51`             | u32                     | unknown_win_str_ref  |                           |
| `modes+0x55`             | u32                     | unknown_draw_str_ref |                           |
| `modes+0x59`             | u32                     | unknown_lose_str_ref |                           |
| `modes+0x5D`             | u64                     | unknown_item_count   |                           |
| `modes+0x65`             | u32[unknown_item_count] | unknown_item_keys    |                           |
| `unknown_item_keys+0x00` | bytes[3]                | unknown_item_keys_00 | `01 01 01` on client 3381 |
| `unknown_item_keys+0x03` | Preset[48]              | equip_presets        |                           |
| `equip_presets+0x00`     | String Table            | string_table         |                           |
| `string_table+0x00`      | u32                     | string_table_start   |                           |
| `string_table+0x04`      | u32                     | zero                 | `0`                       |

### Tier (142 bytes)

| Offset  | Type          | Field                  | Notes |
| ------- | ------------- | ---------------------- | ----- |
| `+0x00` | u32           | min_rating             | |
| `+0x04` | u32           | max_ranking            | |
| `+0x08` | u16           | rank_tier_key          | |
| `+0x0A` | u32           | description            | |
| `+0x0E` | u32           | icon_texture           | |
| `+0x12` | u32           | match_slot_right_frame | |
| `+0x16` | u32           | match_slot_left_frame  | |
| `+0x1A` | u32           | hp_widget_right_frame  | |
| `+0x1E` | u32           | hp_widget_left_frame   | |
| `+0x22` | Item Block[3] | item_lists             | See Item Block |

### Item Block (36 bytes)

| Offset  | Type   | Field     | Notes |
| ------- | ------ | --------- | ----- |
| `+0x00` | u32[3] | item_keys | One item key per list, `0` for none |
| `+0x0C` | u64[3] | counts    | The count of each item |

## Layout 1

Clients 3314 and 3349 have the item blocks of Layout 3 and 38 presets,
the shared one at index `37`; the three bytes after the item keys and
the values after the presets are not there.

### File Layout

| Offset                   | Type                    | Field                | Notes    |
| ------------------------ | ----------------------- | -------------------- | -------- |
| `+0x00`                  | char[4]                 | magic                | `PABR`   |
| `+0x04`                  | Mode[4]                 | modes                | See Mode |
| `modes+0x00`             | f32                     | unknown_modes_00     |          |
| `modes+0x04`             | u8                      | unknown_modes_04     |          |
| `modes+0x05`             | f32                     | unknown_modes_05     |          |
| `modes+0x09`             | u64[9]                  | unknown_modes_09     |          |
| `modes+0x51`             | u32                     | unknown_win_str_ref  |          |
| `modes+0x55`             | u32                     | unknown_draw_str_ref |          |
| `modes+0x59`             | u32                     | unknown_lose_str_ref |          |
| `modes+0x5D`             | u64                     | unknown_item_count   |          |
| `modes+0x65`             | u32[unknown_item_count] | unknown_item_keys    |          |
| `unknown_item_keys+0x00` | Preset[38]              | equip_presets        |          |
| `equip_presets+0x00`     | String Table            | string_table         |          |
| `string_table+0x00`      | u32                     | string_table_start   |          |
| `string_table+0x04`      | u32                     | zero                 | `0`      |

### Tier (142 bytes)

| Offset  | Type          | Field                  | Notes |
| ------- | ------------- | ---------------------- | ----- |
| `+0x00` | u32           | min_rating             | |
| `+0x04` | u32           | max_ranking            | |
| `+0x08` | u16           | rank_tier_key          | |
| `+0x0A` | u32           | description            | |
| `+0x0E` | u32           | icon_texture           | |
| `+0x12` | u32           | match_slot_right_frame | |
| `+0x16` | u32           | match_slot_left_frame  | |
| `+0x1A` | u32           | hp_widget_right_frame  | |
| `+0x1E` | u32           | hp_widget_left_frame   | |
| `+0x22` | Item Block[3] | item_lists             | See Item Block |

### Item Block (36 bytes)

| Offset  | Type   | Field     | Notes |
| ------- | ------ | --------- | ----- |
| `+0x00` | u32[3] | item_keys | One item key per list, `0` for none |
| `+0x0C` | u64[3] | counts    | The count of each item |

## Item Lists

Every tier holds nine item lists, three per match type in the order
Ranked, Practice, Custom, and within each three the rewards of a
victory, a defeat and a draw. This is not the `SOLARE_WIN`,
`SOLARE_DRAW`, `SOLARE_LOSE` order of the strings.

| List | Match    | Result  |
| ---- | -------- | ------- |
| 1    | Ranked   | Victory |
| 2    | Ranked   | Defeat  |
| 3    | Ranked   | Draw    |
| 4    | Practice | Victory |
| 5    | Practice | Defeat  |
| 6    | Practice | Draw    |
| 7    | Custom   | Victory |
| 8    | Custom   | Defeat  |
| 9    | Custom   | Draw    |

On client 3482 lists 4 to 6 hold Seal of Solare `65396` x30, x15 and x20
on every tier, and lists 7 to 9 are empty. The Arena of Solare GM note on
the official NA/EU site (2025-05-29) gives Seal of Solare 30 for a
victory, 20 for a draw and 15 for a defeat, names a Victory and a Defeat
box for ranked matches and says Custom matches give no reward and
Practice matches keep the seal rewards. The 2026-04-30 patch notes list
the ranked boxes per point bracket: Enthusiastic and Indomitable from
1801 points, Elated and Courageous from 1201, Exultant and Rallying from
601, and Seal of Solare x30 and x15 at 600 points or less. Lists 1 and 2
of mode `0` hold the same boxes for the same `min_rating` ranges. Item
`890117` is Combat Secret Book (S) in `languagedata_en.loc`.

| Mode | Tiers (`rank_tier_key`) | List 1 | List 2 | List 3 |
| ---- | ----------------------- | ------ | ------ | ------ |
| 0    | `0x0001` to `0x0203`    | Enthusiastic Solare Box `890008` x1, `890117` x1 | Indomitable Solare Box `890009` x1 | Seal of Solare x20 |
| 0    | `0x0301` to `0x0403`    | Elated Solare Box `890006` x1, `890117` x1 | Courageous Solare Box `890007` x1 | Seal of Solare x20 |
| 0    | `0x0501` to `0x0602`    | Exultant Solare Box `890004` x1, `890117` x1 | Rallying Solare Box `890005` x1 | Seal of Solare x20 |
| 0    | `0x0603` to `0x0701`    | Seal of Solare x30 | Seal of Solare x15 | Seal of Solare x20 |
| 1    | `0x0001` to `0x0303`    | Elated Solare Box `761882` x1, `890117` x1 | Courageous Solare Box `761883` x1 | Seal of Solare x20 |
| 1    | `0x0401` to `0x0504`    | Exultant Solare Box `761606` x1, `890117` x1 | Rallying Solare Box `761607` x1 | Seal of Solare x20 |
| 1    | `0x0601` to `0x0701`    | Rallying Solare Box `761607` x1, `890117` x1 | Seal of Solare x15 | Seal of Solare x20 |

## Field Names

The tier fields follow the getters of the object that
`ToClient_GetSolareRankTierOption(gameMode, rating, ranking)` returns in
`panel_solrare_match_score.luac`, `panel_solrare_matching_1.luac` and
`panel_solrare_ranking_2.luac` (client 3482): `getRankTierKey()` with
`getRankGroup()` and `getTier()`, `getDescription()` (shown with
`PAGetString(Defines.StringSheet_GAME, ...)`), `getIconTextureID()` and
`getFrameTextureID(isLeft, isHPWidget)`; the four frame strings name the
side and the widget. The getter takes the game mode, which is the key of
a Mode, and a rating and ranking: `min_rating` falls by 100 from tier to
tier, and `max_ranking` limits the two top tiers to rank 1 and the top 30.
The preset fields follow `ToClient_GetSolareEquipPresetItemKey(equipSlotNo,
classType, presetLevel)` and `ToClient_GetSolareJewelPresetItemKey(equipSlot,
socketIndex)` in `panel_solrare_equippresetlist.luac`; the window passes
`__eClassType_Count` as the class type for every tab but the weapon tab,
and only the shared preset holds jewel items. The file is not in client
1784, and no sheet of a private server's `DataSheets.bexcel` on client
1784 has `Solare` in its name.

## Notes

- The file is in client 3314 and later. Apart from the `unknown_04` of
  the list items, the files of clients 3474 and 3482 are equal.
- Group `7` has one tier, `0x0701` with `min_rating` `0` (`Solare_Tier21`).
  The icons of group `0` are `Solare_Tier22` (rank 1), `Solare_Tier00`
  (top 30) and `Solare_Tier01`; every later tier has its own icon.
- The `unknown_04` of a list item looks like the upper half of a 64-bit
  value the build tool left unset.
- The handler (`_bss/solareoptionstaticstatusmanager/`) shows one row per
  tier of modes `0` and `1` with its non-empty item lists; the presets and
  the common values stay in the parser's result.

## Open Questions

### Game Modes 0 and 1

Both modes hold the same tiers and seal counts. Mode `1` has its own box
items (`761882`, `761883`, `761606`, `761607`), named like the Elated,
Courageous, Exultant and Rallying boxes of mode `0`, on other rank groups
(see the table in Item Lists), and no Enthusiastic or Indomitable box.
Which arena season or setting each mode is stays open. `ToClient_GetSolareRewardSize(solareMatchMode,
gameResultType)` in `panel_solrare_match_score.luac` reads the rewards by
match type and result; Layouts 1 to 3 keep the same grouping as three
blocks of three single items per tier.

### unknown_item_keys

On client 3482 the 20 item keys are two Sharp Alchemy Stones (`45220`,
`45252`), two Resolute Alchemy Stones (`741627`, `741628`), Secret Books
of Old Moon of every length (`46889`, `46890`, `47003`, `47006`, `47120`,
`47121`, `320133`, `601200` to `601207`) and item `48033`, which has no
LOC name. They could be items that are allowed,
or blocked, in the arena; no Lua getter reads them.

### Mode and Group Values

The 21 values of a mode and the nine fields of a group have no name. The group's
two `u8` + three `f32` blocks and the falling `unknown_0d` (`50`, `40`,
`30`) look like rating gain and loss settings per rank group.
