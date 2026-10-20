# `pet.dbss` Format

## Purpose

Defines one record per pet: species, tier, level cap, EXP table, look, icon path, market price fields, the loot, race and base skills, the equip-skill roll pool and the ten action rates. Each record is a specific pet at a specific tier (e.g. "Dog variant #40 at Tier 4"); fairies are pet records too (`pet_type` 1). Companion `petoffset.dbss` enables O(1) lookup by pet ID.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes   | Records                     | Row bytes                  |
| ------ | -------------- | ------- | ---------------- | ------- | --------------------------- | -------------------------- |
| 1      | 1784 and later | 3474    | `pet.dbss`       | 376,078 | 2,009 Payload, 2,009 Record | 180 to 194, 185 on average |
| 1      | 1784 and later | 3474    | `petoffset.dbss` | 20,094  | 2,009 Offset Row            | 10                         |

| Layout | File             | Known             | Unknown         |
| ------ | ---------------- | ----------------- | --------------- |
| 1      | `pet.dbss`       | 357,997 B (95.2%) | 18,081 B (4.8%) |
| 1      | `petoffset.dbss` | 16,076 B (80.0%)  | 4,018 B (20.0%) |

<!-- versions:end -->

## Companion Files

| File             | Required | Role                                                     |
| ---------------- | -------- | -------------------------------------------------------- |
| `petoffset.dbss` | Required | `pet_id → (data_offset, data_size)` for variable records |
| `petgrade.dbss`  | Optional | `(species, variant) → grade` per pet type                |
| `petequipskill.bss` | Optional | `base_skill_id` → base skill name (Section 2, LOC type 10) |
| `petskill.dbss`, `petskilloffset.dbss` | Optional | `loot_skill_id` and `race_skill_id` → skill type |
| `stringtable.bss` | Optional | Key hashes of the skill type names, see [petskill.dbss](petskill_dbss.md#skill-types) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A record count, then the records back to back. Each record is a 2-byte key
prefix and the payload that `petoffset.dbss` addresses.

| Offset  | Type          | Field   | Notes                                                                  |
| ------- | ------------- | ------- | ---------------------------------------------------------------------- |
| `+0x00` | u32           | count   | Number of pet records (observed: 1,782 before 2026-09-27, 2,009 after) |
| `+0x04` | Record[count] | records | See Record                                                             |

`+0x04` is the key prefix of the first record (`first_record_key` in earlier
versions of this doc), not a standalone header field. Records begin
immediately at `+0x04`.

### Record (variable: 2 bytes + payload)

Typically 181 to 194 bytes. Each record is stored as
`[u16 key_prefix][data_bytes]`. The `key_prefix` (2 bytes) equals `pet_id`
and is also the first 2 bytes of `data_bytes`.

| Offset  | Type    | Field      | Notes                                                  |
| ------- | ------- | ---------- | ------------------------------------------------------ |
| `+0x00` | u16     | key_prefix | Equals `pet_id`                                        |
| `+0x02` | Payload | payload    | `data_size` bytes; the offset row points at this field |

### Payload (variable: 126 bytes + icon path text)

The 32-byte fixed header, the icon path, then the 94-byte fixed footer.
Counts are records on client 3473.

| Offset           | Type     | Field                         | Notes                                                                                   |
| ---------------- | -------- | ----------------------------- | --------------------------------------------------------------------------------------- |
| `+0x00`          | u16      | pet_id                        | Unique record key; equal to the preceding 2-byte file prefix                            |
| `+0x02`          | u8       | variant                       | Sub-variant within the species (1–57 observed)                                          |
| `+0x03`          | u8       | species                       | Pet family/model code                                                                   |
| `+0x04`          | u8       | unknown_04                    | `0` in every record                                                                     |
| `+0x05`          | u8       | tier                          | Tier (0 = lowest, 4 = highest for regular pets)                                         |
| `+0x06`          | u8       | unknown_06                    | `1` in every record                                                                     |
| `+0x07`          | i32      | max_level                     | 10 on 1,994 records; Laila has 10, 20, 30 or 50 by `exp_key`                            |
| `+0x0B`          | i32      | max_hunger                    | `400` in every record                                                                   |
| `+0x0F`          | u16      | exp_key                       | Key into [petexp.dbss](petexp_dbss.md): 1 to 4 for pets, 6 to 9 for the Laila grades    |
| `+0x11`          | u8       | is_indexed                    | `1` on 355 records                                                                      |
| `+0x12`          | u32      | default_action_index          | Default look within the `change_look_key` group                                         |
| `+0x16`          | u16      | change_look_key               | Key into `petchangelook.dbss`; `0` on 614 records                                       |
| `+0x18`          | str8     | icon_path                     | u64 byte length (`icon_path_len`), then the ASCII path with no null terminator          |
| `icon_path+0x00` | i64      | base_price_for_pet_market     | `30000` in every record                                                                 |
| `icon_path+0x08` | i64      | min_price_for_pet_market      | `base_price_for_pet_market × minest_percent_for_pet_market / 1,000,000`                  |
| `icon_path+0x10` | i64      | max_price_for_pet_market      | `base_price_for_pet_market × maxest_percent_for_pet_market / 1,000,000`                  |
| `icon_path+0x18` | i32      | minest_percent_for_pet_market | Millionths; `500000` in every record                                                    |
| `icon_path+0x1C` | i32      | maxest_percent_for_pet_market | Millionths; `1000000` in every record                                                   |
| `icon_path+0x20` | u32      | skill_max_count               | `2` in every record: `loot_skill_id` and `race_skill_id`                                 |
| `icon_path+0x24` | u16      | acquire_type_id               | Equip-skill roll pool; 0 = none. Pets key into [petequipskillaquire.dbss](petequipskillaquire_dbss.md), fairies (501 to 504) into [fairyequipskillaquire.dbss](fairyequipskillaquire_dbss.md) |
| `icon_path+0x26` | u16      | base_skill_id                 | The pet's base skill, a Section 2 `equip_skill_id` of [petequipskill.bss](petequipskill_bss.md) on all 2,009 records |
| `icon_path+0x28` | u16      | unknown_tail_28               | `0` in every record                                                                     |
| `icon_path+0x2A` | i32[10]  | action_rates                  | One millionths rate per pet action, see below                                           |
| `icon_path+0x52` | u8       | pet_type                      | `1` on the 21 fairy records, else `0`                                                   |
| `icon_path+0x53` | u16      | loot_skill_id                 | Key into [petskill.dbss](petskill_dbss.md): 11, 16 or 17 on 1,908 records; the pet window's "Basic" skill |
| `icon_path+0x55` | u16      | race_skill_id                 | Key into [petskill.dbss](petskill_dbss.md); the pet window's "Special" skill            |
| `icon_path+0x57` | u8       | unknown_57                    | `0` on 85 records, see Open Questions                                                   |
| `icon_path+0x58` | u8       | is_joker_pet_use              | `1` on 1,974 records                                                                    |
| `icon_path+0x59` | u8       | pc_room_type                  | `1` on 20 records, two each of ten species                                              |
| `icon_path+0x5A` | bytes[4] | unknown_tail_5a               | `0` in every record                                                                     |

The icon path is stored immediately after the fixed header, in ASCII.
**Not** null-terminated. Footer offsets are relative to the byte immediately
following the icon path. `unknown_57` keeps the name of its footer offset.

```text
New_UI_Common_forLua\Window\Stable\Pet\GoldStar_Pet_0004.dds
```

`exp_key` follows the tier on most pets (tier 0 has key 1, tier 1 key 2, tier 2 key 3, tiers 3 and 4 key 4). 138 records do not: key 4 on 55 tier-2 and 18 tier-1 records, key 2 on 54 tier-0 and 4 tier-2 records, key 3 on 7 tier-1 records.

Earlier versions of this doc read `exp_key` as `equip_skill_slots`, `is_indexed` as `unknown_10` (a u16 at `+0x10` that was `256` when set), `default_action_index` as `unknown_12` and `change_look_key` as `unknown_14` (a u32 at `+0x14`, `change_look_key << 16`). `max_level` was a u8, and the bytes of `max_hunger` read as `0x90000000` at `+0x08` and a constant `1` at `+0x0C`.

The ten `action_rates` follow the sheet's `Action_0` to `Action_9`, whose Korean comments name the actions: joy, feed, angry, sleepy, run, sit, play, crouch, cry and sulk. 1,642 of the 1,782 records before the 2026-09-27 update store ten times 1,000,000 and 96 store ten zeros; the rest mix 0 and 1,000,000 or carry smaller values such as 220,000, 100,000 and 40,000.

Earlier versions of this doc called the market fields and `skill_max_count` `unknown_00` (six `const_*` fields before that), `action_rates` `unknown_2a` (`upgrade_table` before that), `loot_skill_id` `unknown_53` (`tier_score`) and `base_skill_id` `equip_skill_id`. `pet_type`, `race_skill_id` and the two flags after `unknown_57` were listed as constant bytes.

### `petoffset.dbss`

Provides O(1) lookup of any pet record by `pet_id`. Records are **not** stored in file order; use the offset to locate any record.

| Offset  | Type              | Field | Notes                       |
| ------- | ----------------- | ----- | --------------------------- |
| `+0x00` | u32               | count | Must equal `pet.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row              |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                                           |
| ------- | ---- | ----------- | ------------------------------------------------------------------------------- |
| `+0x00` | u16  | pet_id      | Matches `pet_id` in the main record                                             |
| `+0x02` | u32  | data_offset | Absolute byte offset in `pet.dbss` to the **data** (past the 2-byte key prefix) |
| `+0x06` | u16  | data_size   | Size of data in bytes (excluding the 2-byte key prefix)                         |
| `+0x08` | u16  | unknown_08  | Always 0                                                                        |

`record_start = data_offset - 2` gives the position of the 2-byte key prefix in the file.  
`total_record_size = data_size + 2`.  
The parser reads `data_size` and `unknown_08` as one u32 (`parse_bare_offset_rows()`).

## Notes

- Total file size = 4 + Σ(2 + `data_size`) over all records: 332,420 bytes for the 1,782 records before the 2026-09-27 client update, 376,078 bytes for 2,009 records after it.
- Record size varies because `icon_path_len` differs per pet (observed: 55–68 bytes). The 32-byte header and 94-byte footer are fixed; only the path varies.
- `pet_id` appears three times per record: as the 2-byte key prefix in the file, as field `+0x00` in the data header, and as the `pet_id` field in the `petoffset.dbss` index.
- English pet display names resolve from `languagedata_en.loc` with `str_type = 6` and `str_id1 = pet_id`.
- The fairy records are species 25 (Laila, 20 records, `exp_key` 6 to 9 by grade) and one "Fairy's Energy" record of species 100. They are the 21 records with `pet_type` 1 and the 21 with `acquire_type_id` 501 to 504, which have no row in `petequipskillaquire.dbss`.
- `acquire_type_id` values 301–304 appear for regular pets and correspond to tiers 0–4 (tier 0 → 301, tier 4 → 304); lower values (1, 2, 3, 4) and mid-range values (101–104, 201–204, 401–404) appear for specific sub-groups.
- 21 records have no `petgrade.dbss` row for their `(species, variant)` and show no grade.

## Field Names

The names follow the `Pet_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 (keyed by `CharacterKey`), which shares 1,264 records with client 3473, and the 2016 `gc::PetStaticStatus` member order: `_maxLevel`, `_maxHungry`, `_petExpKey`, `_isIndexed`, `_defaultActionIndex`, `_changeLookKey`, `_iconPath`, `_basePriceForPetMarket`, `_minPriceForPetMarket`, `_maxPriceForPetMarket`, `_minestPricePercent`, `_maxestPricePercent`, `_skillMaxCount`, `_skillList[2]`, `_learnAttractList[10]`, `_petEquipSkillAquireKey`. In the 2016 struct the four bytes at `+0x02` are one u32 `_fusionKey`: `variant`, `species`, a zero byte and `tier`.

| Column | Field | Equal (non-zero rows) |
| ------ | ----- | --------------------- |
| `Kind` (Korean comment "body type") | `variant` | 1,264 of 1,264 |
| `Race` ("race") | `species` | 1,262 of 1,264 |
| `Tier` ("grade") | `tier` | 1,023 of 1,023 |
| `Level` | `max_level` | 1,259 of 1,264 |
| `Hunger` | `max_hunger` | `400` on every sheet row and record |
| `RequireEXPType` | `exp_key` | 1,264 of 1,264 |
| `IsIndexed` | `is_indexed` | 285 of 285 |
| `DefaultActionIndex` ("appearance") | `default_action_index` | 1,249 of 1,249 |
| `PetChangeLookKey` | `change_look_key` | 956 of 956 |
| `basePriceForPetMarket`, `minestPercentForPetMarket`, `maxestPercentForPetMarket` | the market fields | `30000`, `500000` and `1000000` on every sheet row and record |
| `EquipSkillAquireKey` ("skill group") | `acquire_type_id` | 986 of 986 |
| `BaseSkill` ("base skill") | `base_skill_id` | 1,264 of 1,264 |
| `Action_0` to `Action_9` | `action_rates` | 1,168 of 1,168 to 1,187 of 1,187 per column |
| `PetType` | `pet_type` | 21 of 21 |
| `Skill_0` ("looting") | `loot_skill_id` | 1,221 of 1,264 |
| `Skill_1` ("race skill") | `race_skill_id` | 1,264 of 1,264 |
| `IsJokerPetUse` | `is_joker_pet_use` | 1,236 of 1,236 |
| `PcRoomType` | `pc_room_type` | 10 of 10 |

`BaseSkill` keys the `Pet_BaseSkill_Table` sheet, whose 60 rows match Section 2 of `petequipskill.bss` by skill number (60 of 60); `Pet_EquipSkill_Table` matches Section 1 (43 of 43). The sheet's `EquipSkill_0` to `EquipSkill_14` and `BoneScale` columns have no field in the record. The derived min and max prices are not sheet columns; the 2016 member order places them.

## Open Questions

### `unknown_57` Meaning

The u8 at footer `+0x57` is `0` on every record of species 4 (Penguin), 21 (Kuku), 39 (Young Crimson Dragon), 40 (Young Fogan), 46 (Arctic Fox, Black Leopard, Prankkebi, Tarkhes) and 49 (Jojo, Putrakium), 85 records on client 3473, and `1` on the rest. It sits between `race_skill_id` and `is_joker_pet_use`, where the sheet has no column. The private server's own `pet.dbss` (client 1784) stores the same byte with the same split by species, so it is filled from a source outside `Pet_Table`.
