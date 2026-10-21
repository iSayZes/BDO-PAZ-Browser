# `hardcorechanneltitlestaticstatusmanager.bss` Format

## Purpose

The titles of the Hardcore channel, one 47-byte row each: a title key, the
number of kills it needs, the Korean name, description and condition text
in the string table, and the colour the title shows in. On client 3474 the
75 titles come in tiers of 100 to 10,000 kills of one monster group each
(Ancient Weapons, Desert Naga, Desert Fogan, Crescent Shrine, Gahaz Bandits,
Pila Ku Jail, Aakman Temple, Hystria Ancient Weapons), and the colour
rises with the tier: white, green, blue, yellow, orange. The keys are the
Hardcore window's own: [`title.dbss`](title_dbss.md) title 1 is Battle
Ready and title 65 Destroyer of Blind Faith, where this file has an Ancient
Weapon and an Aakman title.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                          | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------------------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `hardcorechanneltitlestaticstatusmanager.bss` | 9,461 | 75 Row  | 47        |

| Layout | File                                          | Known           | Unknown         |
| ------ | --------------------------------------------- | --------------- | --------------- |
| 1      | `hardcorechanneltitlestaticstatusmanager.bss` | 7,586 B (80.2%) | 1,875 B (19.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
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

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (47 bytes)

| Offset  | Type | Field           | Notes                                                                                     |
| ------- | ---- | --------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16  | title_key       | Hardcore title key, unique; `1` to `80` with gaps on client 3474                          |
| `+0x02` | u8   | unknown_02      | Always `0`                                                                                |
| `+0x03` | u32  | unknown_03      | One value per monster group and kind (`241` to `259`); see Open Questions                 |
| `+0x07` | u32  | kill_count      | Kills the title needs; the number in the condition text on all 75 rows (client 3474)      |
| `+0x0B` | u32  | unknown_0b      | Always `0`                                                                                |
| `+0x0F` | u32  | unknown_0f      | `0` to `39`; shared by the same step of several groups; see Open Questions                      |
| `+0x13` | u32  | unknown_13      | Equals `unknown_03` on every row                                                          |
| `+0x17` | u32  | unknown_17      | Equals `kill_count` on every row                                                          |
| `+0x1B` | u32  | name_ref        | String-table index of the Korean title name; `ToClient_getHardCoreTitleNameByKey`         |
| `+0x1F` | u32  | description_ref | String-table index of the Korean description; `ToClient_getHardCoreTitleDescByKey`        |
| `+0x23` | u32  | condition_ref   | String-table index of the Korean condition; `ToClient_getHardCoreTitleConditionByKey`     |
| `+0x27` | u32  | unknown_27      | `3` on every row                                                                          |
| `+0x2B` | u32  | grade_color     | ARGB colour of the title name; `ToClient_GetHardCoreTitleGradeColor`                      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                                 |
| ------- | ------------------ | ------------ | ------------------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `166` on client 3474                                               |
| `+0x04` | pstr[string_count] | strings      | UTF-16LE Korean text; rows of one monster group share their description string         |

## Grade Colours

`grade_color` by `kill_count` (client 3474). The Ancient Weapon titles
(`unknown_03` `247`) step 100, 500, 1,000, 2,000 and 5,000; every other
group 100, 1,000, 3,000, 5,000 and 10,000.

| `grade_color` | Colour | Ancient Weapons | Other groups |
| ------------- | ------ | --------------- | ------------ |
| `0xFFFFFFFF`  | White  | 100             | 100          |
| `0xFF2DC200`  | Green  | 500             | 1,000        |
| `0xFF0F47FF`  | Blue   | 1,000           | 3,000        |
| `0xFFF3D900`  | Yellow | 2,000           | 5,000        |
| `0xFFF32200`  | Orange | 5,000           | 10,000       |

## Field Names

The Hardcore channel is newer than client 1784: no sheet of a private
server's `DataSheets.bexcel` on that client and no string of its server
dump has `HardCore` in the name. The names follow the Hardcore character
window of client 3474 (`panel_characterinfo_hardcore_basic_all_1.luac` and
`_2.luac`): it lists the titles with `ToClient_getHardCoreTitleCount()` and
`ToClient_getHardCoreTitleKeyByIndex(index)`, then shows each key's
`ToClient_getHardCoreTitleNameByKey`, `...DescByKey` and
`...ConditionByKey` text and colours the name with
`ToClient_GetHardCoreTitleGradeColor`. The three strings of every row are
a name, a description ("<난폭한> 사막 나가 처치", defeat the Desert Naga) and
a condition with a count ("... 100마리 처치", defeat 100), in that order.

## Notes

- The file is byte-identical on clients 3002, 3251 and 3474; clients 1784
  and 2519 do not ship it.
- `unknown_03` pairs per monster group: the "<난폭한>" (violent) titles of a
  group hold one value and the "<격노한>" (enraged) titles another, ten
  apart (Desert Naga `251` and `241`, Hystria `256` and `246`); the
  Ancient Weapon titles hold `247` only and the Gahaz Bandits `259` and
  `258`.
- No field points into LOC, so the handler shows the Korean name,
  description and condition.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/hardcore_tables.py`.

## Open Questions

### Monster Group Value

What `unknown_03` names. One value per monster group and kind fits a kill
group key, but no Lua call reads it, no LOC type 116 hunting ground has the
key, and the second copy at `unknown_13` shows no difference on any row.

### Title Rank Value

What `unknown_0f` is. It runs `0` to `4` for the Ancient Weapon titles,
`10` to `19` for the Naga, Fogan, Crescent and Gahaz titles, `20` to `29`
for Pila Ku and Aakman and `30` to `39` for Hystria, one step per title
of a group, so the Naga, Fogan, Crescent and Gahaz "Tracker" titles all hold
`10`. It may pick the title's look in `ToClient_insertNewTitleUI(key32,
content)`, which the title list calls with the key.
