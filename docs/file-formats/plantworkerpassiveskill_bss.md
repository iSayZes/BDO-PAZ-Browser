# `plantworkerpassiveskill.bss` Format

## Purpose

Worker passive skill table. The file stores passive skill IDs, inline Korean fallback strings, DDS icon paths, and effect parameter fields used by worker skill UI rows. User-facing names and descriptions should prefer LOC type `22` when available.

Example rows:

```text
1603 -> 날개C, /New_UI_Common_forLua/Skill/WorkerSkill/1303.dds, 기본 이동속도의 6% 증가
1923 -> 숙련 공성 무기 제작 기술, /New_UI_Common_forLua/Skill/WorkerSkill/1923.dds, 공성 무기 제작 시 3회 추가 작업
1012 -> 타고난 일꾼, /New_UI_Common_forLua/Skill/WorkerSkill/1012_N.dds, 작업속도 +2, 기본 이동속도의 7% 증가
```

## Companion Files

No companion file is required to parse the file. Names and descriptions are stored inline as UTF-16LE Korean fallback strings. For user-facing display, `languagedata_en.loc` is optional and should be preferred when a matching LOC type `22` row exists.

| File                  | Required | Role                                                |
| --------------------- | -------- | --------------------------------------------------- |
| `languagedata_en.loc` | Optional | Provides localized skill names and descriptions via LOC type `22` |

All multi-byte values are little-endian unless noted otherwise.

## File Layout

| Offset  | Type  | Field              | Notes                                                   |
| ------- | ----- | ------------------ | ------------------------------------------------------- |
| `+0x00` | u8[4] | magic              | `PABR` (ASCII)                                          |
| `+0x04` | u32   | skill_record_count | Number of skill records; observed `72` (also in the 2026-09-27 client) |
| `+0x08` | ...   | skill_records      | Usually `0x38` bytes each; one observed extended record |
| varies  | u32   | string_count       | Number of string entries; observed `174`                |
| varies  | ...   | string_table       | Length-prefixed UTF-16LE strings                        |
| EOF-8   | u32   | string_table_start | Absolute file offset of `string_count`; observed `0xFD8` |
| EOF-4   | u32   | zero_trailer       | Observed `0`                                            |

The fixed/extended skill-record block begins at `0x08` and the string table starts at `0xFD8` in the observed file. Skill records reference string table entries by zero-based index.

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
| `+0x18` | u32  | effect_type        | `0` flat stats, `1` full refund, `2` stats per level up, `6` extra work; see Effect Types |
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

## Effect Types

### `effect_type = 0` - Flat Stats

Direct stat and work-speed effects. `effect_target` is `0` for generic stat modifiers such as movement speed, work speed, and luck. For named work-speed knowledge skills, `effect_target` identifies the work category.

| Effect Target | Meaning | Example Skill |
| ------------- | ------- | ------------- |
| `0` | Generic stat modifier | `1603` [Wings C](https://bdocodex.com/us/sskill/1603/), `1103` [Simple C](https://bdocodex.com/us/sskill/1103/), `1503` [Lucky Guy C](https://bdocodex.com/us/sskill/1503/) |
| `1` | Jeweler work speed | `1001` [Polishing Knowledge](https://bdocodex.com/us/sskill/1001/) |
| `2` | Mass production work speed | `1002` [Mass Production Knowledge](https://bdocodex.com/us/sskill/1002/) |
| `3` | Weapon/armor workshop speed | `1003` [Workshop Knowledge](https://bdocodex.com/us/sskill/1003/) |
| `4` | Tool workshop speed | `1004` [Tool Knowledge](https://bdocodex.com/us/sskill/1004/) |
| `5` | Furniture workshop speed | `1005` [Furniture Knowledge](https://bdocodex.com/us/sskill/1005/) |
| `7` | Costume workshop speed | `1007` [Costume Knowledge](https://bdocodex.com/us/sskill/1007/) |
| `8` | Refinery/specialty work speed | `1008` [General Knowledge](https://bdocodex.com/us/sskill/1008/) |
| `9` | Cannon/siege weapon work speed | `1009` [Siege Knowledge](https://bdocodex.com/us/sskill/1009/) |
| `10` | Ship/wagon/horse gear work speed | `1010` [Mount Knowledge](https://bdocodex.com/us/sskill/1010/) |
| `11` | Node/farm work speed | `1011` [Farm Knowledge](https://bdocodex.com/us/sskill/1011/) |
| `13` | Specialty node work speed | `1013` [Specialty Node Knowledge](https://bdocodex.com/us/sskill/1013/) |

Observed scaling:

| Description Pattern | Value Field | Scaling |
| ------------------- | ----------- | ------- |
| Movement Speed +N% | `effect_value_a` | `N * 10000` |
| Work Speed +N | `effect_value_a` | `N * 1000000` |
| Luck +N | `effect_value_a` | `N * 10000` |

`effect_value_b` selects the stat for every `effect_type = 0` record: `0` movement speed, `1` work speed, `2` luck (the same codes `effect_type = 2` uses in `effect_target`). The named work-speed skills (targets `1` to `13`) all store `1`. This holds for every record and matches every English description in the 2026-09-27 client.

`skill_id=1012` combines two generic direct effects: the base record stores Movement Speed +7%, and the extra parameter block stores Work Speed +2.

### `effect_type = 1` - Full Refund

Material refund effects. `effect_target` is the chance scaled by `1,000,000`. `effect_value_a` is the share of the material refunded, on the same scale (`1000000` is a full refund). `effect_value_b` equals `effect_value_a` on every refund record in both clients (`100000` before the 2026-09-27 update, when the text read "10% of 1 Crafting Material", `1000000` after), so it is shown on the same scale; which of the two the game reads is not known.

| Example Skill | Effect Target | Meaning | Effect Values |
| ------------- | ------------- | ------- | ------------- |
| `1203` [Thrifty C](https://bdocodex.com/us/sskill/1203/) | `50000` | 5% chance | `100000`, `100000` |
| `1202` [Thrifty B](https://bdocodex.com/us/sskill/1202/) | `70000` | 7% chance | `100000`, `100000` |
| `1201` [Thrifty A](https://bdocodex.com/us/sskill/1201/) | `100000` | 10% chance | `100000`, `100000` |
| `2003` [Unexpected Luck C](https://bdocodex.com/us/sskill/2003/) | `1000` | Extremely low chance | `1000000`, `1000000` |
| `2002` [Unexpected Luck B](https://bdocodex.com/us/sskill/2002/) | `3000` | Very low chance | `1000000`, `1000000` |
| `2001` [Unexpected Luck A](https://bdocodex.com/us/sskill/2001/) | `5000` | Low chance | `1000000`, `1000000` |

### `effect_type = 2` - Stats per Level Up

Per-level stat growth effects. `effect_target` identifies the stat that grows on worker level-up.

| Effect Target | Meaning | Example Skill | Effect Value |
| ------------- | ------- | ------------- | ------------ |
| `0` | Movement speed | `1901` [Leg Work](https://bdocodex.com/us/sskill/1901/) | `5000` = Movement Speed +0.5% per level |
| `1` | Work speed | `1902` [Craftsmanship](https://bdocodex.com/us/sskill/1902/) | `200000` = Work Speed +0.2 per level |
| `2` | Luck | `1903` [Blessed Hand](https://bdocodex.com/us/sskill/1903/) | `2000` = Luck +0.2 per level |

### `effect_type = 6` - Extra Work

Extra-work effects. `effect_target` identifies the production category and `effect_value_a` is the extra work count.

| Effect Target | Meaning | Example Skill |
| ------------- | ------- | ------------- |
| `5001` | Weapon production | `1916` [Weapon Production](https://bdocodex.com/us/sskill/1916/) |
| `5002` | Armor production | `1917` [Armor Production](https://bdocodex.com/us/sskill/1917/) |
| `5003` | Life clothes production | `1918` [Life Clothes Production](https://bdocodex.com/us/sskill/1918/) |
| `5004` | Siege weapon production | `1922` [Siege Weapon Production](https://bdocodex.com/us/sskill/1922/) |
| `9001` | Produce packing | `1904` [Produce Packing](https://bdocodex.com/us/sskill/1904/) |
| `9002` | Herb packing | `1905` [Herb Packing](https://bdocodex.com/us/sskill/1905/) |
| `9003` | Mushroom packing | `1906` [Mushroom Packing](https://bdocodex.com/us/sskill/1906/) |
| `9004` | Fish packing | `1907` [Fish Packing](https://bdocodex.com/us/sskill/1907/) |
| `9005` | Timber packing | `1908` [Timber Packing](https://bdocodex.com/us/sskill/1908/) |
| `9006` | Ore packing | `1909` [Ore Packing](https://bdocodex.com/us/sskill/1909/) |

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

## Reference Rows

| Skill ID | Name | Icon | Description | Weight | Effect Values |
| -------- | ---- | ---- | ----------- | ------ | ------------- |
| `1603` | [Wings C](https://bdocodex.com/us/sskill/1603/) | `1303.dds` | Movement Speed +6% | `1000` | `60000`, `0` |
| `1602` | [Wings B](https://bdocodex.com/us/sskill/1602/) | `1302.dds` | Movement Speed +8% | `1050` | `80000`, `0` |
| `1601` | [Wings A](https://bdocodex.com/us/sskill/1601/) | `1301.dds` | Movement Speed +11% | `1400` | `110000`, `0` |
| `1923` | [Adv. Siege Weapon Production](https://bdocodex.com/us/sskill/1923/) | `1923.dds` | Extra Work (+3) Done for Siege Weapons | `2500` | `3`, `0` |
| `1203` | [Thrifty C](https://bdocodex.com/us/sskill/1203/) | `1203.dds` | 5% Chance to Return 10% of 1 Crafting Material | `1000` | `100000`, `100000` |
| `1012` | [Adept Worker](https://bdocodex.com/us/sskill/1012/) | `1012_N.dds` | Work Speed +2, Movement Speed +7% | `1050` | `70000`, `0`; extra `2000000`, `1` |

## Suggested UI Layout

| Column      | Type | Notes                                      |
| ----------- | ---- | ------------------------------------------ |
| Skill ID    | num  | `skill_id`, right-aligned                  |
| Icon        | text | Render `icon_path` with icon-cell preview  |
| Name        | text | Prefer LOC type `22`; fall back to `inline_name` |
| Description | text | Prefer LOC type `22`; fall back to `inline_description` |
| Weight      | num  | `acquisition_weight`, right-aligned        |
| Effect Type | text | `effect_type` by name: Flat Stats, Full Refund, Stats per Level Up, Extra Work; sorts by the number |
| Target      | text | What the skill affects: the stat (`Work Speed`, `Move Speed`, `Luck`), with the work category for targets `1` to `13` (`Cannon/Siege Weapon Work Speed`); the production category for extra work (`Siege Weapons`); a dash for refunds, whose `effect_target` is the chance. Sorts by `target_sort_value`: `effect_target`, or `None` for refunds |
| Effect A    | num  | How much: `+2` work speed, `+7%` movement speed, `+0.7` luck, `+0.2` per level, `+3` extra work; for refunds the chance (`effect_target`, `7000` is `0.7%`). Sorts by `effect_a_sort_value`, the raw number shown |
| Effect B    | num  | For refunds the share refunded (`effect_value_a`, `1000000` is `100%`); a dash for every other type. Sorts by `effect_b_sort_value`: `effect_value_a` for refunds, `None` for the dashes |

The shown values are scaled from the raw fields, which stay on the record unchanged for export. Each column sorts by the raw number its cell shows, so a dash sorts last (see "Store none as None" in `docs/handler.md`). The stat names follow the `0`/`1`/`2` codes, which match every description. The category names are not stored anywhere found so far: they are the wording the skills' own English descriptions use for each target value (each value has exactly one wording), so a value not seen yet shows as its number. The targets are not keys of another table found so far: the workshop types in `houseinforeceipe.dbss` number the same work differently (jewelry `8`, tool `9`, refinery `10`, costume `18`), and its processing sub-types `30` to `34` come in a different order than the packing targets `9001` to `9006`.

## Notes

- Observed file size is `13,090` bytes (2026-09-27 client: `13,294`).
- The 2026-09-27 client retunes the Thrifty skills: `effect_target` `50000`/`70000`/`100000` became `7000`/`10000`/`15000` for C/B/A, both effect values `100000` became `1000000`, and Thrifty C now reads "0.7% Chance to Fully Refund One Material, Selected with Equal Probability". The tables above show the pre-2026-09-27 values.
- BDO Codex lists every worker skill with Level `Naive` and Class `Warrior`. These look like the defaults for zero values (class `0` is Warrior), not data: no field in this record varies that way, and `zero_a` / `zero_b` are `0` on every skill.
- `acquisition_weight` is most likely the weight for rolling the skill when a worker learns one; the game does not show it, so it cannot be checked in game.
- The string table starts at `0xFD8`; the EOF trailer repeats this offset as `string_table_start`.
- The string table contains `174` entries: names, icon paths, and descriptions in one shared pool.
- Icon paths are UTF-16LE strings under `/New_UI_Common_forLua/Skill/WorkerSkill/`.
- Several records reuse string entries. For example, `1302` reuses the `1302.dds` icon entry from `1602`.
- LOC type `22` appears to carry worker skill localization. Use `str_id1=skill_id`, with `str_id4=0` for name and `str_id4=1` for description, when localized rows are available.

## Open Questions

### Extended `1012` Record

`skill_id=1012` has an extra 16-byte parameter block before the next record. The extra values encode its Work Speed +2 effect, but the general rule that determines when this extension appears is not confirmed.

### `effect_target` Is Not Fully Confirmed

`effect_target` means something different per `effect_type`, and not every reading is equally backed (2026-09-27 client):

| Reading | Evidence | Status |
| ------- | -------- | ------ |
| Refund chance (`effect_type = 1`) | All 6 refund skills match their text (`7000` is "0.7% Chance"), and the 2026-09-27 update changed value and text together (`50000`/`70000`/`100000` read 5/7/10% before, `7000`/`10000`/`15000` read 0.7/1/1.5% after) | Confirmed |
| Stat code (`effect_type = 2`) | `0`/`1`/`2` match the stat named in all 4 descriptions, with the same codes `effect_value_b` uses for `effect_type = 0` | Confirmed |
| Category key (`effect_type = 0` targets `1` to `13`, `effect_type = 6`) | Each value goes with exactly one category wording across 32 skills, including the paired `10xx`/`20xx` skills (`1009` and `2015` are both target `9`, both "Cannon/Siege Weapon"), and workermanjs applies the skills by the same categories (see In-Game Checks) | Very likely |
| Category names | Taken from those descriptions; no table in the client files found that names the keys (`houseinforeceipe.dbss` numbers workshops differently) | Not confirmed |

## In-Game Checks

### Farm Knowledge Counts on Nodes Only

Needs worker: one with [Farm Knowledge](https://bdocodex.com/us/sskill/1011/) (`1011`, "Node Work Speed +5")

Whether the client reads `effect_target` to decide which work gets the bonus is not proven from the client files. [workermanjs](https://github.com/shrddr/workermanjs), a worker planner whose model is checked against observed yields, applies the skills with the same split (`src/stores/game.js`, `wspdBonus`, 2026-09-26): general work speed (target `0`) counts everywhere; target `11` (its `wspd_farm`, the skill now worded "Node Work Speed") counts on every node and in no workshop; a workshop adds only the skill of its own industry (`wspd_jewelry`, `wspd_weap` and so on, one per target `1` to `5`, `7` to `10` and `13`); and target `8` (`wspd_refine`, "Refinery/Specialty") also counts in the six packing workshops, which match the `effect_type = 6` targets `9001` to `9006` by name. Its hand-written skill list puts every skill ID in the same category as its `effect_target` here.

Put the worker on a node, then in a workshop of any industry, and compare the work time per cycle with the worker's base work speed. If the time matches work speed + 5 on the node and the base work speed in the workshop, the client applies the bonus by `effect_target` (`11`, node work) as read here. A +5 in the workshop too means the target does not limit it.
