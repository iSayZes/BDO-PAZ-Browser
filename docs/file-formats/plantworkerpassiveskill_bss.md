# `plantworkerpassiveskill.bss` Format

## Purpose

Worker passive skill table. The file stores passive skill IDs, inline Korean fallback strings, DDS icon paths, and effect parameter fields used by worker skill UI rows. User-facing names and descriptions should prefer LOC type `22` when available.

Example rows:

```text
1603 -> 날개C, /New_UI_Common_forLua/Skill/WorkerSkill/1303.dds, 기본 이동속도의 6% 증가
1923 -> 숙련 공성 무기 제작 기술, /New_UI_Common_forLua/Skill/WorkerSkill/1923.dds, 공성 무기 제작 시 3회 추가 작업
1012 -> 타고난 일꾼, /New_UI_Common_forLua/Skill/WorkerSkill/1012_N.dds, 작업속도 +2, 기본 이동속도의 7% 증가
```

## Graph

### Tags

- file format
- bss
- worker
- skill

### Connections

- [plantworker.bss](plantworker_bss.md) - worker definitions that can reference worker/passive skill behavior in UI
- [plantworkerselect.bss](plantworkerselect_bss.md) - same-prefix worker selection table; related, not required to parse this file
- [languagedata_en.loc](languagedata_loc.md) - optional localized worker skill names and descriptions through LOC type `22`

---

## Companion Files

No companion file is required to parse the file. Names and descriptions are stored inline as UTF-16LE Korean fallback strings. For user-facing display, `languagedata_en.loc` is optional and should be preferred when a matching LOC type `22` row exists.

| File                  | Required | Role                                                |
| --------------------- | -------- | --------------------------------------------------- |
| `languagedata_en.loc` | Optional | Provides localized skill names and descriptions via LOC type `22` |

All multi-byte values are little-endian unless noted otherwise.

---

## File Layout

| Offset  | Type  | Field              | Notes                                                   |
| ------- | ----- | ------------------ | ------------------------------------------------------- |
| `+0x00` | u8[4] | magic              | `PABR` (ASCII)                                          |
| `+0x04` | u32   | skill_record_count | Number of skill records; observed `72`                  |
| `+0x08` | ...   | skill_records      | Usually `0x38` bytes each; one observed extended record |
| varies  | u32   | string_count       | Number of string entries; observed `174`                |
| varies  | ...   | string_table       | Length-prefixed UTF-16LE strings                        |
| EOF-8   | u32   | string_table_start | Absolute file offset of `string_count`; observed `0xFD8` |
| EOF-4   | u32   | zero_trailer       | Observed `0`                                            |

The fixed/extended skill-record block begins at `0x08` and the string table starts at `0xFD8` in the observed file. Skill records reference string table entries by zero-based index.

---

## Record Structure

### Skill Record (`0x38` bytes, usually)

| Offset  | Type | Field              | Notes                                                   |
| ------- | ---- | ------------------ | ------------------------------------------------------- |
| `+0x00` | u16  | skill_id           | Passive worker skill ID                                 |
| `+0x02` | u16  | duplicate_skill_id | Always matches `skill_id` in observed records           |
| `+0x04` | u32  | name_index         | Index into `string_table`; Korean skill name            |
| `+0x08` | u32  | icon_index         | Index into `string_table`; DDS path                     |
| `+0x0C` | u32  | description_index  | Index into `string_table`; Korean effect description    |
| `+0x10` | u32  | acquisition_weight | Observed values: `1000`, `1050`, `1400`, `2100`, `2500`, `2800` |
| `+0x14` | u32  | zero_a             | Always observed as `0`                                  |
| `+0x18` | u32  | effect_type        | Effect family; see Effect Types                         |
| `+0x1C` | u32  | apply_mode         | Usually `7`; observed `0` for `skill_id=1012`           |
| `+0x20` | u32  | apply_scope        | Always observed as `7`                                  |
| `+0x24` | u32  | effect_type_copy   | Mirrors `effect_type` in many rows                      |
| `+0x28` | u32  | effect_target      | Stat/category/chance target, depending on `effect_type` |
| `+0x2C` | u32  | effect_value_a     | Primary scaled effect value                             |
| `+0x30` | u32  | effect_value_b     | Secondary scaled effect value for some rows             |
| `+0x34` | u32  | zero_b             | Always observed as `0`                                  |

One observed record, `skill_id=1012` (`타고난 일꾼`), is followed by an extra 16-byte parameter block before the next record:

| Offset  | Type | Field                | Notes                             |
| ------- | ---- | -------------------- | --------------------------------- |
| `+0x38` | u32  | extra_zero_a         | Observed `0`                      |
| `+0x3C` | u32  | extra_effect_value_a | Observed `2000000`                |
| `+0x40` | u32  | extra_effect_value_b | Observed `1`                      |
| `+0x44` | u32  | extra_zero_b         | Observed `0`                      |

Derived fields:

```text
inline_name = string_table[name_index]
icon_path = string_table[icon_index]
inline_description = string_table[description_index]
display_name = LOC type 22, str_id1=skill_id, str_id4=0; fallback inline_name
display_description = LOC type 22, str_id1=skill_id, str_id4=1; fallback inline_description
```

---

## Effect Types

### `effect_type = 0` - Direct Stat Or Work-Speed Modifier

Direct stat and work-speed effects. `effect_target` is `0` for generic stat modifiers such as movement speed, work speed, and luck. For named work-speed knowledge skills, `effect_target` identifies the work category.

| Effect Target | Meaning | Example Skill |
| ------------- | ------- | ------------- |
| `0` | Generic stat modifier | `1603` Wings C, `1103` Simple C, `1503` Lucky Guy C |
| `1` | Jeweler work speed | `1001` Polishing Knowledge |
| `2` | Mass production work speed | `1002` Mass Production Knowledge |
| `3` | Weapon/armor workshop speed | `1003` Workshop Knowledge |
| `4` | Tool workshop speed | `1004` Tool Knowledge |
| `5` | Furniture workshop speed | `1005` Furniture Knowledge |
| `7` | Costume workshop speed | `1007` Costume Knowledge |
| `8` | Refinery/specialty work speed | `1008` General Knowledge |
| `9` | Cannon/siege weapon work speed | `1009` Siege Knowledge |
| `10` | Ship/wagon/horse gear work speed | `1010` Mount Knowledge |
| `11` | Node/farm work speed | `1011` Farm Knowledge |
| `13` | Specialty node work speed | `1013` Specialty Node Knowledge |

Observed scaling:

| Description Pattern | Value Field | Scaling |
| ------------------- | ----------- | ------- |
| Movement Speed +N% | `effect_value_a` | `N * 10000` |
| Work Speed +N | `effect_value_a` | `N * 1000000` |
| Luck +N | `effect_value_a` | `N * 10000` |

`skill_id=1012` combines two generic direct effects: the base record stores Movement Speed +7%, and the extra parameter block stores Work Speed +2.

### `effect_type = 1` - Material Return Chance

Material return effects. `effect_target` is the chance scaled by `1,000,000`. `effect_value_a` and `effect_value_b` describe returned material amount/type parameters.

| Example Skill | Effect Target | Meaning | Effect Values |
| ------------- | ------------- | ------- | ------------- |
| `1203` Thrifty C | `50000` | 5% chance | `100000`, `100000` |
| `1202` Thrifty B | `70000` | 7% chance | `100000`, `100000` |
| `1201` Thrifty A | `100000` | 10% chance | `100000`, `100000` |
| `2003` Unexpected Luck C | `1000` | Extremely low chance | `1000000`, `1000000` |
| `2002` Unexpected Luck B | `3000` | Very low chance | `1000000`, `1000000` |
| `2001` Unexpected Luck A | `5000` | Low chance | `1000000`, `1000000` |

### `effect_type = 2` - Per-Level Stat Growth

Per-level stat growth effects. `effect_target` identifies the stat that grows on worker level-up.

| Effect Target | Meaning | Example Skill | Effect Value |
| ------------- | ------- | ------------- | ------------ |
| `0` | Movement speed | `1901` Leg Work | `5000` = Movement Speed +0.5% per level |
| `1` | Work speed | `1902` Craftsmanship | `200000` = Work Speed +0.2 per level |
| `2` | Luck | `1903` Blessed Hand | `2000` = Luck +0.2 per level |

### `effect_type = 6` - Extra/Repeat Work

Extra-work effects. `effect_target` identifies the production category and `effect_value_a` is the extra work count.

| Effect Target | Meaning | Example Skill |
| ------------- | ------- | ------------- |
| `5001` | Weapon production | `1916` Weapon Production |
| `5002` | Armor production | `1917` Armor Production |
| `5003` | Life clothes production | `1918` Life Clothes Production |
| `5004` | Siege weapon production | `1922` Siege Weapon Production |
| `9001` | Produce packing | `1904` Produce Packing |
| `9002` | Herb packing | `1905` Herb Packing |
| `9003` | Mushroom packing | `1906` Mushroom Packing |
| `9004` | Fish packing | `1907` Fish Packing |
| `9005` | Timber packing | `1908` Timber Packing |
| `9006` | Ore packing | `1909` Ore Packing |

### String Table

| Offset  | Type              | Field   | Notes                                           |
| ------- | ----------------- | ------- | ----------------------------------------------- |
| `+0x00` | u32               | count   | Number of string entries; observed `174`        |
| `+0x04` | string_entry[...] | entries | Repeated `count` times                          |

### String Entry

| Offset  | Type       | Field       | Notes                              |
| ------- | ---------- | ----------- | ---------------------------------- |
| `+0x00` | u8         | present     | Always observed as `1`             |
| `+0x01` | u32        | byte_length | UTF-16LE byte length, no alignment |
| `+0x05` | u8[length] | text        | UTF-16LE text                      |

The string table is a flat pool, not grouped records. Skill records choose any string indices; several records reuse icon/name/description entries.

---

## Reference Rows

| Skill ID | Name | Icon | Description | Weight | Effect Values |
| -------- | ---- | ---- | ----------- | ------ | ------------- |
| `1603` | Wings C | `1303.dds` | Movement Speed +6% | `1000` | `60000`, `0` |
| `1602` | Wings B | `1302.dds` | Movement Speed +8% | `1050` | `80000`, `0` |
| `1601` | Wings A | `1301.dds` | Movement Speed +11% | `1400` | `110000`, `0` |
| `1923` | Adv. Siege Weapon Production | `1923.dds` | Extra Work (+3) Done for Siege Weapons | `2500` | `3`, `0` |
| `1203` | Thrifty C | `1203.dds` | 5% Chance to Return 10% of 1 Crafting Material | `1000` | `100000`, `100000` |
| `1012` | Adept Worker | `1012_N.dds` | Work Speed +2, Movement Speed +7% | `1050` | `70000`, `0`; extra `2000000`, `1` |

---

## Suggested UI Layout

| Column      | Type | Notes                                      |
| ----------- | ---- | ------------------------------------------ |
| Skill ID    | num  | `skill_id`, right-aligned                  |
| Icon        | text | Render `icon_path` with icon-cell preview  |
| Name        | text | Prefer LOC type `22`; fall back to `inline_name` |
| Description | text | Prefer LOC type `22`; fall back to `inline_description` |
| Weight      | num  | `acquisition_weight`, right-aligned        |
| Effect Type | num  | `effect_type`, right-aligned               |
| Target      | num  | `effect_target`, right-aligned             |
| Effect A    | num  | `effect_value_a`, right-aligned            |
| Effect B    | num  | `effect_value_b`, right-aligned when nonzero |

---

## Notes

- Observed file size is `13,090` bytes.
- The string table starts at `0xFD8`; the EOF trailer repeats this offset as `string_table_start`.
- The string table contains `174` entries: names, icon paths, and descriptions in one shared pool.
- Icon paths are UTF-16LE strings under `/New_UI_Common_forLua/Skill/WorkerSkill/`.
- Several records reuse string entries. For example, `1302` reuses the `1302.dds` icon entry from `1602`.
- LOC type `22` appears to carry worker skill localization. Use `str_id1=skill_id`, with `str_id4=0` for name and `str_id4=1` for description, when localized rows are available.

## Open Questions

### Extended `1012` Record

`skill_id=1012` has an extra 16-byte parameter block before the next record. The extra values encode its Work Speed +2 effect, but the general rule that determines when this extension appears is not confirmed.
