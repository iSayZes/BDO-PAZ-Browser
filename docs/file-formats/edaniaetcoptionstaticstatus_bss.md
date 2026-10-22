# `edaniaetcoptionstaticstatus.bss` Format

## Purpose

The Edania (Throne of Edana) options: one row per castle, in
`__eEdaniaRegion` order, with its contents group, the minimum AP, DP and
item grade to enter its battles, its entry scroll tax rate and base
amount, the weekly throne quest, a world position near the castle, the
boss clear item and a list of 16 Dawn crystals; then seven settings stored
once, three of them Edana's drop buff. The Lua reads it with `ToClient_GetEdaniaEtcOption()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------- | --------- |
| 2      | 3474 and later | 3482    | `edaniaetcoptionstaticstatus.bss` | 1,388 | 10 Row  | 135       |
| 1      | 3002 to 3251   | 3251    | `edaniaetcoptionstaticstatus.bss` | 373   | 5 Row   | 67        |

| Layout | File                              | Known         | Unknown       |
| ------ | --------------------------------- | ------------- | ------------- |
| 2      | `edaniaetcoptionstaticstatus.bss` | 448 B (32.3%) | 940 B (67.7%) |
| 1      | `edaniaetcoptionstaticstatus.bss` | 238 B (63.8%) | 135 B (36.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | No file  |
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

| File                  | Required | Role                                                                                  |
| --------------------- | -------- | ------------------------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Castle names (LOC type 37), quest titles (LOC type 18) and item names (LOC type 0)    |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset      | Type         | Field           | Notes                                                                  |
| ----------- | ------------ | --------------- | ---------------------------------------------------------------------- |
| `+0x00`     | char[4]      | magic           | ASCII `PABR`                                                           |
| `+0x04`     | Row[10]      | rows            | One per `__eEdaniaRegion` castle, Aetherion to Voidekaia; no row count |
| `rows+0x00` | u8           | unknown_rows_00 | `7`; see Open Questions                                                |
| `rows+0x01` | u8           | unknown_rows_01 | `3`                                                                    |
| `rows+0x02` | u32          | unknown_rows_02 | `5`                                                                    |
| `rows+0x06` | u32          | drop_buff_count | Edana's drop buff uses per term; `10`                                  |
| `rows+0x0A` | u32          | drop_buff_rate  | Its Item Drop Rate bonus, 1,000,000 = 100%; `1000000`                  |
| `rows+0x0E` | u32          | drop_buff_minutes | Its duration in minutes; `60`                                        |
| `rows+0x12` | u32          | unknown_rows_12 | `0`                                                                    |
| `rows+0x16` | String Table | string_table    | See String Table                                                       |
| `EOF-0x08`  | u32          | table_start     | Offset of the string table, where `unknown_rows_12` ends               |
| `EOF-0x04`  | u32          | zero            | Always `0`                                                             |

The parser reads rows up to 22 bytes before `table_start`, where the
settings start, and numbers them from `0` as their `__eEdaniaRegion`
value.

### Row (variable: 71 bytes + item IDs)

| Offset  | Type                     | Field               | Notes                                                                                     |
| ------- | ------------------------ | ------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u32                      | contents_group_hash | Contents group key as the client's string hash; `2177` Aetherion to `2245` Voidekaia      |
| `+0x04` | f32                      | min_ap_1            | Minimum AP to enter; `350` (Aetherion) to `428` (Voidekaia); see Open Questions           |
| `+0x08` | f32                      | min_dp_1            | Minimum DP to enter; `427` to `520`                                                       |
| `+0x0C` | f32                      | min_ap_2            | Equals `min_ap_1` on every row                                                            |
| `+0x10` | f32                      | min_dp_2            | Equals `min_dp_1` on every row                                                            |
| `+0x14` | u8                       | min_item_grade_1    | Minimum item grade of the worn gear; `4` (orange, "Red grade") on every row               |
| `+0x15` | u32                      | unknown_15          | `13` on every row                                                                         |
| `+0x19` | u8                       | min_item_grade_2    | Equals `min_item_grade_1` on every row                                                    |
| `+0x1A` | u32                      | unknown_1a          | `13` on every row                                                                         |
| `+0x1E` | u32                      | tax_rate            | Share of the entry scroll price that accrues as tax, 1,000,000 = 100%; `2000` to `5000`  |
| `+0x22` | u8                       | unknown_22          | The castle's `LUA_EDANIA_SYSTEM_CASTLE_NAME_<n>` number minus one; see Notes              |
| `+0x23` | bytes[3]                 | unknown_23          | `71 0B 00` on every row                                                                   |
| `+0x26` | u32                      | throne_quest        | Packed quest ID (`quest_id << 16 \| quest_chain_id`): `9108/1` to `9108/5`, `9308/1` to `9308/5` |
| `+0x2A` | f32                      | unknown_2a          | With the next two a world position near the castle; see Notes                             |
| `+0x2E` | f32                      | unknown_2e          |                                                                                           |
| `+0x32` | f32                      | unknown_32          |                                                                                           |
| `+0x36` | u64                      | tax_base_amount     | Silver the tax starts from; `3,000,000,000` to `25,000,000,000`, rising with the row      |
| `+0x3E` | u32                      | boss_clear_item_key | Item ID, an "Edania: ... Chest"; `890056` (Azureach Chest) on row `0`                     |
| `+0x42` | u8                       | unknown_42          | `0` on every row                                                                          |
| `+0x43` | u32                      | unknown_item_count  | Number of `unknown_item_ids`; `16` on every row                                           |
| `+0x47` | u32[unknown_item_count]  | unknown_item_ids    | Item IDs, the same 16 Dawn crystals on every row; see Open Questions                      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

### File Layout

| Offset     | Type         | Field           | Notes                                                    |
| ---------- | ------------ | --------------- | -------------------------------------------------------- |
| `+0x00`    | char[4]      | magic           | ASCII `PABR`                                             |
| `+0x04`    | Row[5]       | rows            | Aetherion to Zephyros, the first Edana group             |
| `+0x153`   | u8           | unknown_rows_00 |                                                          |
| `+0x154`   | u8           | unknown_rows_01 |                                                          |
| `+0x155`   | u32          | unknown_rows_02 |                                                          |
| `+0x159`   | u32          | drop_buff_count |                                                          |
| `+0x15D`   | u32          | drop_buff_rate  |                                                          |
| `+0x161`   | u32          | drop_buff_minutes |                                                          |
| `+0x165`   | u32          | unknown_rows_12 |                                                          |
| `+0x169`   | String Table | string_table    | See String Table                                         |
| `EOF-0x08` | u32          | table_start     | Offset of the string table, where `unknown_rows_12` ends |
| `EOF-0x04` | u32          | zero            | Always `0`                                               |

### Row (67 bytes)

| Offset  | Type     | Field               | Notes                                  |
| ------- | -------- | ------------------- | -------------------------------------- |
| `+0x00` | u32      | contents_group_hash |                                        |
| `+0x04` | f32      | min_ap_1            |                                        |
| `+0x08` | f32      | min_dp_1            |                                        |
| `+0x0C` | f32      | min_ap_2            |                                        |
| `+0x10` | f32      | min_dp_2            |                                        |
| `+0x14` | u8       | min_item_grade_1    |                                        |
| `+0x15` | u32      | unknown_15          |                                        |
| `+0x19` | u8       | min_item_grade_2    |                                        |
| `+0x1A` | u32      | unknown_1a          |                                        |
| `+0x1E` | u32      | tax_rate            |                                        |
| `+0x22` | u8       | unknown_22          |                                        |
| `+0x23` | bytes[3] | unknown_23          |                                        |
| `+0x26` | u32      | throne_quest        |                                        |
| `+0x2A` | f32      | unknown_2a          |                                        |
| `+0x2E` | f32      | unknown_2e          |                                        |
| `+0x32` | f32      | unknown_32          |                                        |
| `+0x36` | u64      | tax_base_amount     |                                        |
| `+0x3E` | u32      | boss_clear_item_key | A different item ID per row (`761697` on row `0`) |
| `+0x42` | u8       | unknown_42          |                                        |

## Castles

The rows on client 3482.

| Row | Contents group | `throne_quest` | Quest title                          | `boss_clear_item_key` | Item                        |
| --- | -------------- | -------------- | ------------------------------------ | --------------------- | --------------------------- |
| 0   | `2177`         | `9108/1`       | [Weekly] For the Throne: Aetherion   | `890056`              | Edania: Azureach Chest      |
| 1   | `2178`         | `9108/2`       | [Weekly] For the Throne: Nymphamaré  | `890057`              | Edania: Emeraltides Chest   |
| 2   | `2176`         | `9108/3`       | [Weekly] For the Throne: Orbita      | `890058`              | Edania: Amberwilds Chest    |
| 3   | `2179`         | `9108/4`       | [Weekly] For the Throne: Tenebraum   | `890059`              | Edania: Ebonshade Chest     |
| 4   | `2175`         | `9108/5`       | [Weekly] For the Throne: Zephyros    | `890060`              | Edania: Crimsonroot Chest   |
| 5   | `2216`         | `9308/1`       | [Weekly] For the Throne: Aphrodon    | `790866`              | Edania: Goldroot Chest      |
| 6   | `2218`         | `9308/2`       | [Weekly] For the Throne: Hermesia    | `890102`              | Edania: Ebonmere Chest      |
| 7   | `2219`         | `9308/3`       | [Weekly] For the Throne: Magaia      | `890103`              | Edania: Everlight Chest     |
| 8   | `2220`         | `9308/4`       | [Weekly] For the Throne: Aresion     | `890104`              | Edania: Crimsonflare Chest  |
| 9   | `2245`         | `9308/5`       | [Weekly] For the Throne: Voidekaia   | `890105`              | Edania: Voidreach Chest     |

## Field Names

Edania is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers this file. The Edania window
(`panel_window_edania_contents_all_1.luac` and `_2.luac`, client 3482)
loops `regionIndex` from `0` to `__eEdaniaRegion_Count - 1` and reads, per
castle, `getLimitStat(regionIndex, isBossRoom, isOffence)`,
`checkContentsOption(regionIndex)`, `getEdanaBossClearItemKey(regionIndex)`
and `getEdanaPersonalFieldTaxPercent(regionIndex)`, and once
`getEdanaDropBuffTime()`, `getEdanaDropBuffPercent()` and
`getEdanaDropBuffCount()`. The file has one row per castle and one block
of settings, which fits that split.

| Field                 | Source                                                                                                         |
| --------------------- | -------------------------------------------------------------------------------------------------------------- |
| `contents_group_hash` | Each value is the client's string hash of a contents group key (`_common/contents_group.py`), `2175` to `2245`; a per-castle switch is what `checkContentsOption` tests |
| `throne_quest`        | Each value is a packed quest ID whose LOC type 18 title names the castle of its row                            |
| `boss_clear_item_key` | The only per-row item ID besides the shared crystal list; each is an "Edania: ... Chest", one per castle, which `getEdanaBossClearItemKey` returns for the boss clear slot |

The official Throne of Edana page of the NA/EU game wiki (wikiNo 457)
lists the entry conditions and the tax of Aetherion, Nymphamaré and
Orbita Castle, and Edana's drop buff. Its values match the file:

| Field | Official wiki page | File (client 3482) |
| ----- | ------------------ | ------------------ |
| `min_ap_1`, `min_dp_1` | "AP 350+ / DP 427+", "AP 375+ / DP 440+", "AP 385+ / DP 445+" | `350, 427`, `375, 440` and `385, 445` on rows `0` to `2` |
| `min_item_grade_1` | At least "Red grade" gear equipped, at every castle | `4` on every row, the grade the client draws orange-red (`_common/item_grade.py`) |
| `tax_rate` | Tax Rate 0.4%, 0.3% and 0.25% | `4000`, `3000` and `2500` on the 1,000,000 = 100% scale |
| `tax_base_amount` | Base amount 3, 5 and 8 billion Silver | `3000000000`, `5000000000` and `8000000000` |
| `drop_buff_rate`, `drop_buff_minutes`, `drop_buff_count` | Edana's Blessing: Item Drop Rate +100% for up to 1 hour, up to 10 times per week | `1000000` (100%), `60` and `10` |

The page gives one AP, DP and grade condition per castle for both the
10-challenger battle and the final challenger vs. Edana battle; the file
stores two copies, which fits `getLimitStat(regionIndex, isBossRoom,
isOffence)` and the two `ToClient_Check...RoomItemGradeType` calls. The
window compares the offence value with `ToClient_getAttackDisplayOffenceMax()`
(AP) and the defence value with `ToClient_getAttackDisplayDefence()` (DP).

## Notes

- Clients 3002 and 3251 use Layout 1: five rows (the first Edana group)
  of 67 bytes, with no crystal list. Client 3474 adds the second group and
  the list and matches client 3482 byte for byte. The settings block is
  the same on all four clients. The file is not in the archives of client
  1784.
- `unknown_22` runs `0, 1, 3, 2, 4, 5, ...`: the castle number of the
  `LUA_EDANIA_SYSTEM_CASTLE_NAME_<n>` key of the row's castle minus one,
  where Orbita and Tenebraum swap numbers 3 and 4
  ([`edaniaregioninfo.bss`](edaniaregioninfo_bss.md#enum-values)). The row
  order follows `__eEdaniaRegion`: the quest titles and the positions put
  Orbita on row `2` and Tenebraum on row `3`.
- `unknown_2a`, `unknown_2e` and `unknown_32` read as a world position
  (`y` the height). On client 3482 its X and Z lie within 400 units of the
  castle's map mark in
  [`edanacastleinfostaicstatusmanager.bss`](edanacastleinfostaicstatusmanager_bss.md)
  on 7 of 10 rows (`559137, 573784` against `559141, 573692` for
  Aetherion), 4,253 and 6,995 units away for Tenebraum and Zephyros and
  16,152 for Orbita. The Lua names a castle teleport
  (`HandleEventLUp_Edania_Contents_TeleportToMyCastle`,
  `__ePreCoolTimeType_EdanaCastleTeleport`) but no getter for it.
- `unknown_item_ids` lists the HAN, JIN, BON and WON grades of four Dawn
  crystals (`15264` to `15275` and `15282` to `15285`): "Black Spirit's
  Rage", "Accuracy", "Damage Reduction" and "Evasion" (LOC type 0, "JIN
  Dawn Crystal - Accuracy").
- The handler shows one row per castle: the castle name, the contents
  group key, the AP, DP and grade minimums, the tax rate and base amount,
  the quest title and the boss clear item, with the drop buff in the count
  line; the other fields stay on the record.

## Open Questions

### Which Copy Is Which Room

`min_ap_1`, `min_dp_1` and `min_item_grade_1` equal `min_ap_2`,
`min_dp_2` and `min_item_grade_2` on every row, so which copy is the boss
(Edana) room and which the challenger room of `getLimitStat(regionIndex,
isBossRoom, isOffence)` cannot be told from the values.

### The Other Settings

`unknown_rows_00` (`7`), `unknown_rows_01` (`3`), `unknown_rows_02` (`5`)
and `unknown_rows_12` (`0`) are stored once next to the drop buff. No
number on the official wiki page matches them.

### The Other Row Fields

What `unknown_15` and `unknown_1a` (`13` after each grade), `unknown_23`
(`71 0B 00`) and the crystal list are for. The entry scroll prices on the
official wiki page (50, 70 and 80 million Silver) are not in the row.
