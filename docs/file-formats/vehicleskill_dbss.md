# `vehicleskill.dbss` Format

## Purpose

Mount and ship skills: one record per skill with its Korean name, skill EXP
cap, price, icon, key-command and description texts, contents groups,
condition, lock flag, the ship skills' display order and the Training level
that unlocks auto-sprint. On client 3474 the file has 106 records, keys 1 to
106, from Hind Kick (1) and Drift (3) to the ship skills such as
`충각 (항해 초급Lv.1이상)` (Ram, 36).
[servant.bss](servant_bss.md) lists the skills each servant starts with by
these keys.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes  | Records        | Row bytes                    |
| ------ | -------------- | ------- | ------------------------- | ------ | -------------- | ---------------------------- |
| 1      | 1784 and later | 3474    | `vehicleskill.dbss`       | 70,285 | 106 Record     | 268 to 1,646, 663 on average |
| 1      | 1784 and later | 3474    | `vehicleskilloffset.dbss` | 974    | 106 Offset Row | 9                            |

| Layout | File                      | Known            | Unknown        |
| ------ | ------------------------- | ---------------- | -------------- |
| 1      | `vehicleskill.dbss`       | 69,012 B (98.2%) | 1,273 B (1.8%) |
| 1      | `vehicleskilloffset.dbss` | 974 B (100.0%)   | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3474   | Layout 1             |
| 3251   | Layout 1             |
| 3002   | Layout 1             |
| 2519   | Layout 1             |
| 2107   | Layout 1             |
| 1784   | Layout 1             |
| 1485   | No documented layout |
| 1230   | No file              |
| 794    | No file              |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                               |
| ------------------------- | -------- | ------------------------------------------------------------------ |
| `vehicleskilloffset.dbss` | Optional | PABR index: key to the record's offset and size                    |
| `languagedata_en.loc`     | Optional | LOC type 8, `str_id1` = `key`: `str_id4` 0 name, 1 key command, 3 description, 4 console key command |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field      | Notes                                         |
| ------- | ------------- | ---------- | --------------------------------------------- |
| `+0x00` | u8            | unknown_00 | `count` + 1 on clients 1784 (77) and 3474 (107) |
| `+0x01` | u32           | count      | 106 on client 3474                            |
| `+0x05` | Record[count] | records    | Back to back in key order, up to EOF          |

### Record (variable: 104 bytes + texts and contents groups)

| Offset                                | Type                         | Field                                | Notes |
| ------------------------------------- | ---------------------------- | ------------------------------------ | ----- |
| `+0x00`                               | u8                           | key                                  | 1 to 106 on client 3474 |
| `+0x01`                               | str16                        | name_kr                              | `뒷발차기` (Hind Kick) |
| `name_kr+0x00`                        | u32                          | max_exp                              | 30,000 on every record (client 3474) |
| `name_kr+0x04`                        | u32                          | add_exp_for_check                    | |
| `name_kr+0x08`                        | u64                          | base_price                           | |
| `name_kr+0x10`                        | u32                          | add_mating_rate                      | 0, or 20,000 to 40,000 on 5 records (client 3474) |
| `name_kr+0x14`                        | u8                           | is_learn_from_item                   | 1 on 16 records (client 3474) |
| `name_kr+0x15`                        | str16                        | icon_path                            | `New_Icon\04_PC_Skill/06_Riding_Skill/Riding_Skill_0004.dds` |
| `icon_path+0x00`                      | str16                        | desc_kr                              | Key command, `뒷발 공격 ↓+ F`; LOC `str_id4` 1 |
| `desc_kr+0x00`                        | str16                        | desc2_kr                             | Description with `<PAColor>` tags and `\n`; LOC `str_id4` 3 |
| `desc2_kr+0x00`                       | str16                        | console_desc_kr                      | Key command with `{KeyBind:...}`; LOC `str_id4` 4 |
| `console_desc_kr+0x00`                | str16                        | training_skill_characters            | Empty, or servant character IDs as text (`9989, 9889`) on keys 49 to 51 |
| `training_skill_characters+0x00`      | u8                           | is_market_filter                     | |
| `training_skill_characters+0x01`      | u32                          | contents_group_count                 | 1, or 2 on 4 records (client 3474) |
| `training_skill_characters+0x05`      | u32[contents_group_count]    | contents_group_key_hashes            | `key_hash` of each contents group key; `"0"` hashes to `1612107767` |
| `contents_group_key_hashes+0x00`      | bytes[8]                     | unknown_contents_group_key_hashes_00 | `0` on every record (clients 1784 and 3474) |
| `contents_group_key_hashes+0x08`      | str16                        | condition_desc                       | Empty, or a script call such as `VEHICLESKILL_CONDITION_4();` on 19 records (client 3474) |
| `condition_desc+0x00`                 | u8                           | vehicle_skill_lock                   | 0 on 9 records (client 3474) |
| `condition_desc+0x01`                 | u32                          | unknown_condition_desc_01            | `0` on every record (clients 1784 and 3474) |
| `condition_desc+0x05`                 | u32                          | skill_order                          | 0, or 101 to 115 on the 15 ship skills (client 3474) |
| `condition_desc+0x09`                 | u32                          | need_life_level_for_auto_skill       | 0, or 31 on the 5 sprint skills (client 3474) |

### `vehicleskilloffset.dbss`

| Offset              | Type              | Field              | Notes                                        |
| ------------------- | ----------------- | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                                       |
| `+0x04`             | u32               | count              | Equals the main file's `count`               |
| `+0x08`             | Offset Row[count] | entries            | Key order                                    |
| `entries+0x00`      | String Table      | string_table       | Present but empty                            |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`            |
| `string_table+0x04` | u32               | zero               | `0`                                          |

### Offset Row (9 bytes)

| Offset  | Type | Field  | Notes                                         |
| ------- | ---- | ------ | --------------------------------------------- |
| `+0x00` | u8   | key    | The record's `key`                            |
| `+0x01` | u32  | offset | Start of the record; the first is `5`         |
| `+0x05` | u32  | size   | Record size; each record ends where the next starts |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Field Names

The names follow the `VehicleSkill_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, matched value by value against client
1784 (76 records, every one in the sheet) and the 76 client 3474 records in
the sheet:

| Column | Field | Equal (client 1784) | Equal (client 3474) |
| ------ | ----- | ------------------- | ------------------- |
| `Index`, `Name`, `Icon` | `key`, `name_kr`, `icon_path` | 76 | 76 |
| `MaxExp`, `AddMatingRate`, `IsLearnFromItem` | `max_exp`, `add_mating_rate`, `is_learn_from_item` | 76 | 76 |
| `AddExpForCheck` | `add_exp_for_check` | 76 | 72 |
| `basePrice` | `base_price` | 76 | 12 |
| `Desc`, `Desc2`, `ConsoleDesc` | `desc_kr`, `desc2_kr`, `console_desc_kr` | 76 | 65, 61, 63 |
| `IsTrainingSkill` | `training_skill_characters` | 76 | 76 |
| `isMarketFilter` | `is_market_filter` | 76 | 76 |
| `ContentsGroupKey` (comma list) | `contents_group_key_hashes`, by `key_hash` | 76 | 76 |
| `ConditionDesc`, `VehicleSkillLock` | `condition_desc`, `vehicle_skill_lock` | 76 | 76 |
| `isSkillOrder` | `skill_order` | 76 | 68 |
| `LifeExperienceLevForAutoSkill` | `need_life_level_for_auto_skill` | 71 | 71 |

`key_hash` is the client's contents group key hash
([contentsgroupoptionstaticstatusmanager.bss](contentsgroupoptionstaticstatusmanager_bss.md#key-hash)):
`ContentsGroupKey` `284,80` is stored as the two hashes of `"284"` and
`"80"`, and an empty cell as the hash of `"0"`.

`need_life_level_for_auto_skill` is 41 on client 1784 and 31 on client 3474
for Sprint (4), `빠른발걸음` (22), `빠른 뛰기` (28), `숲의 질주` (55) and
`달려달려` (62); the sheet and the private server's own compiled file hold 0
there. The client Lua confirms the field: the horse stamina widget
(`horsemp`, `panel_widget_horsemp_renew`) blocks auto-sprint while the
player's life level is below `vehicleProxy:getNeedLifeLevelForAutoSkill(skillKey)`
(`LUA_AUTOSPRINT_CANNOTUSE`).

`skill_order` holds the column `isSkillOrder`, which is a number, not a flag:
the 15 ship skills on client 3474 run 101 to 115, the 10 on client 1784
101 to 110, and the new skills moved the old ones (Ram 101 on both,
`급발진` 105 on client 1784 and 108 on client 3474). `training_skill_characters` holds the column
`IsTrainingSkill`, a text list of servant character IDs (9989 and 9889 are
the male and female Arduanatt); the servant windows hide skills whose
wrapper says `isTrainingSkill()`. The client 3474 text misses are rewrites
of the descriptions and key hints; the price and EXP misses are rebalances.

The sheet's `PriceRate_0` to `PriceRate_2` (1,000,000 on every row) have no
field.

## Notes

- Client 1784 has the same layout with 76 records; 30 skills were added by
  client 3474.
- The highest key plus one is in its own one-byte file,
  [vehicleskillcount.dbss](vehicleskillcount_dbss.md). The skills each
  servant can learn are in
  [vehicleskillowner.dbss](vehicleskillowner_dbss.md).

## Open Questions

### The Header Byte and Zero Fields

`unknown_00` holds the same value as
[vehicleskillcount.dbss](vehicleskillcount_dbss.md) on clients 1485 to
3474: the highest key plus one, the 2016
`gc::VehicleSkillStaticStatusManager::_count`. The keys have no gap on any
of these clients, so the byte cannot be told apart from the record count
plus one, and nothing shows which of the two files the client takes
`_count` from. `unknown_contents_group_key_hashes_00`
(8 bytes) and `unknown_condition_desc_01` (u32) are `0` on every record of
both clients and match no sheet column.
