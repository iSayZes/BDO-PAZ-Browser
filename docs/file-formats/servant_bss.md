# `servant.bss` Format

## Purpose

Base data of the servants (horses, donkeys, camels, elephants, wagons,
boats, ships, the camping tent): one record per servant character with its
Korean dev name, servant kind, tier, grade, coat colors, breeding count,
lifespan, price, the vehicle skills it starts with or can keep, and the
mix and breeding flags. On client 3474 the file has 419 records. The level
stats live in [servantexperience.dbss](servantexperience_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes  | Records        | Row bytes                 |
| ------ | -------------- | ------- | -------------------- | ------ | -------------- | ------------------------- |
| 2      | 3474 and later | 3474    | `servant.bss`        | 45,128 | 419 Row        | 84 to 165, 108 on average |
| 1      | 1784           | 1784    | `servant.dbss`       | 33,748 | 333 Row        | 84 to 145, 101 on average |
| 1      | 1784           | 1784    | `servantoffset.dbss` | 3,334  | 333 Offset Row | 10                        |

| Layout | File                 | Known            | Unknown        |
| ------ | -------------------- | ---------------- | -------------- |
| 2      | `servant.bss`        | 42,195 B (93.5%) | 2,933 B (6.5%) |
| 1      | `servant.dbss`       | 31,417 B (93.1%) | 2,331 B (6.9%) |
| 1      | `servantoffset.dbss` | 3,334 B (100.0%) | 0 B (0.0%)     |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                 |
| ---------------------------- | -------- | -------------------------------------------------------------------- |
| `vehicleskill.dbss`          | Optional | Korean skill names for `basic_learn_skill_keys` and `stallion_skill_keys` when LOC has none |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key, so a `character_id` without a row shows as plain text instead of a link |
| `languagedata_en.loc`        | Optional | Servant names (LOC type 6, `str_id1` = `character_id`) and skill names (LOC type 8, `str_id1` = skill key) |

Client 1784 ships the same records as `servant.dbss` with the index
`servantoffset.dbss` (Layout 1).

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field   | Notes                                  |
| ------- | ---------- | ------- | -------------------------------------- |
| `+0x00` | u32        | count   | 419 on client 3474                     |
| `+0x04` | Row[count] | records | Back to back, variable size, up to EOF |

### Row (variable: 80 bytes + name text and skill lists)

| Offset                        | Type                           | Field                             | Notes |
| ----------------------------- | ------------------------------ | --------------------------------- | ----- |
| `+0x00`                       | u16                            | character_id                      | Servant character, as in `characterstatic.dbss`; records sort by it, highest first |
| `+0x02`                       | u16                            | character_id_dup                  | Equals `character_id` on every record |
| `+0x04`                       | str16                          | name_kr                           | Korean dev name (`탑승용 수말29`); the game name is LOC type 6 |
| `name_kr+0x00`                | u8                             | servant_kind                      | `ServantKind`: 0 horse on 332 records (client 3474); the groups are in [itemenchant.dbss](itemenchant_dbss.md#equip_slot) |
| `name_kr+0x01`                | u8                             | servant_kind_sub                  | 0 to 10; non-zero on the dream horses and other kinds' variants |
| `name_kr+0x02`                | u16                            | tier                              | 0 to 9 |
| `name_kr+0x04`                | u16                            | grade                             | |
| `name_kr+0x06`                | u16                            | color1                            | |
| `name_kr+0x08`                | u16                            | color2                            | |
| `name_kr+0x0A`                | u16                            | color3                            | |
| `name_kr+0x0C`                | u8                             | mating_count                      | Breeding count; 0 on everything that cannot breed |
| `name_kr+0x0D`                | u32                            | lifespan                          | Seconds; 0 except 9057, an event Horse (259,200, 3 days) and 31125 Doomcaller (1,209,600, 14 days) on client 3474 |
| `name_kr+0x11`                | i64                            | base_price                        | Silver |
| `name_kr+0x19`                | i64                            | price_per_level                   | Silver |
| `name_kr+0x21`                | u8                             | is_male                           | |
| `name_kr+0x22`                | u8                             | is_display_gender                 | 0 on 22 records (client 3474), among them the dream horses, the dragons and the Twins |
| `name_kr+0x23`                | u8                             | servant_main_model                | 1 on one servant per kind (Notes) |
| `name_kr+0x24`                | u8                             | is_mating_result                  | |
| `name_kr+0x25`                | u8                             | is_trade                          | |
| `name_kr+0x26`                | u8                             | link_count                        | 0, 1, 2 or 4 |
| `name_kr+0x27`                | i32                            | experience_per_one                | 0, or 250,000 to 1,050,000 on 11 records (client 3474) |
| `name_kr+0x2B`                | u16                            | form_index                        | |
| `name_kr+0x2D`                | u8                             | basic_learn_skill_max_count       | |
| `name_kr+0x2E`                | u32                            | basic_learn_skill_count           | |
| `name_kr+0x32`                | u8[basic_learn_skill_count]    | basic_learn_skill_keys            | `vehicleskill.dbss` keys |
| `basic_learn_skill_keys+0x00` | bytes[5]                       | unknown_basic_learn_skill_keys_00 | `0` on every record (clients 1784 and 3474) |
| `basic_learn_skill_keys+0x05` | u32                            | reward_money_percent              | 500,000 on every record (clients 1784 and 3474) |
| `basic_learn_skill_keys+0x09` | u8                             | is_only_pcroom                    | 1 on 8 records (client 3474) |
| `basic_learn_skill_keys+0x0A` | u32                            | stallion_skill_count              | |
| `basic_learn_skill_keys+0x0E` | u8[stallion_skill_count]       | stallion_skill_keys               | `vehicleskill.dbss` keys: 3, 4, 8, 9, 10, 18 and 19 on client 3474 |
| `stallion_skill_keys+0x00`    | u8                             | can_mix                           | |
| `stallion_skill_keys+0x01`    | u8                             | can_mating                        | 1 exactly where `mating_count` is above 0 (Field Names) |
| `stallion_skill_keys+0x02`    | bytes[2]                       | unknown_stallion_skill_keys_02    | `0` on every record (clients 1784 and 3474) |

## Layout 1

Client 1784 names the file `servant.dbss`, with the same records, and adds
the index `servantoffset.dbss`.

### `servant.dbss`

| Offset  | Type       | Field   | Notes                                  |
| ------- | ---------- | ------- | -------------------------------------- |
| `+0x00` | u32        | count   | 333 on client 1784                     |
| `+0x04` | Row[count] | records | Back to back, variable size, up to EOF |

### `servantoffset.dbss`

| Offset  | Type              | Field   | Notes                       |
| ------- | ----------------- | ------- | --------------------------- |
| `+0x00` | u32               | count   | Equals the `servant.dbss` count |
| `+0x04` | Offset Row[count] | entries | `count` entries of 10 bytes |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                    |
| ------- | ---- | ------------ | -------------------------------------------------------- |
| `+0x00` | u16  | character_id | The record's `character_id`                              |
| `+0x02` | u32  | offset       | Where the record's `character_id_dup` starts, 2 bytes into the record |
| `+0x06` | u32  | size         | Record size minus 2, from `character_id_dup` to the record end |

## Field Names

The names follow the `ServantSet_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, matched value by value against the
official client 1784 `servant.dbss` (333 records, every one in the sheet)
and client 3474 (329 of 419 records in the sheet):

| Column | Field | Equal (client 1784) | Equal (client 3474) |
| ------ | ----- | ------------------- | ------------------- |
| `RaceType` | `servant_kind` | 333 | 329 |
| `RaceSubType` | `servant_kind_sub` | 333 | 314 |
| `Tier`, `Grade` | `tier`, `grade` | 333 | 328, 329 |
| `Color1` to `Color3` | `color1` to `color3` | 333 | 329 |
| `MatingCount` | `mating_count` | 333 | 329 |
| `Lifespan` (minutes) | `lifespan` (seconds, x 60) | 333 | 329 |
| `basePrice`, `PricePerLevel` | `base_price`, `price_per_level` | 178 | 99, 101 |
| `IsMale`, `isDisplayGender` | `is_male`, `is_display_gender` | 333 | 329 |
| `ServantMainModel` | `servant_main_model` | 333 | 328 |
| `IsMatingResult`, `IsTrade` | `is_mating_result`, `is_trade` | 333 | 329 |
| `LinkCount`, `ExperiencePerOn` | `link_count`, `experience_per_one` | 333 | 329 |
| `FormIndex` | `form_index` | 333 | 329 |
| `basicLearnSkillMaxCount` | `basic_learn_skill_max_count` | 333 | 295 |
| `basicLearnSkillKey` (comma list) | `basic_learn_skill_keys` | 333 | 127 |
| `rewardMoneyPercent`, `isOnlyPcroom` | `reward_money_percent`, `is_only_pcroom` | 333 | 329 |
| `stallionSkillKey` (comma list) | `stallion_skill_keys` | 333 | 329 |
| `CanMix` | `can_mix` | 333 | 329 |

The prices are the private server's own; every other column matches all of
client 1784. The client 3474 misses are later changes: 15 dream horses
(Arduanatt, Diné, Doom and their dream and GT versions) have a
`servant_kind_sub` of 1 to 7 where the sheet has 0, Epheria Carrack:
Advance (31054) is a main model and Panokseon (31025) tier 3, and 183 of
the 202 `basic_learn_skill_keys` misses are the sheet's list plus vehicle
skill 4 (Sprint).

The sheet has no column for `can_mating`. The 2016 `gc::ServantStaticStatus`
ends with `_canMix` and `_canMating`, and the byte after `can_mix` is 1
exactly where `mating_count` is above 0 (419 of 419 records, client 3474).
The same struct holds `_servantKind`, `_servantExpirationPeriod` (the
`lifespan` slot) and `_experiencePerOne`, in the file's order. The client Lua
calls `getServantKind`, `getServantKindSub`, `getTier`, `getGrade`,
`isMale`, `isDisplayGender`, `getMatingCount`, `getLinkCount` and
`isPcroomOnly`.

## Notes

- `servant_main_model` is 1 on 8 records (client 3474), one per kind: 9909
  (Horse), 9010 (Brown Camel), 9113 (Donkey), 9052 (Merchant Wagon), 9032
  (Rowboat), 9065 (Fishing Boat), 31001 (Epheria Sailboat) and 31054
  (Epheria Carrack: Advance).
- The skill lists index [vehicleskill.dbss](vehicleskill_dbss.md) by its
  u8 key (1 to 106 on client 3474): stallion skill 3 is `드리프트` (Drift), 4
  `전력질주` (Sprint), 8 `순간가속` (Instant Acceleration), 9 `돌진` (Charge).
- In game on client 3474, a Mythical horse with Base Coat "Breed 13" (only
  31619 fits, see [bdoservanttitless.bss](bdoservanttitless_bss.md)) shows
  Skill List (27), all locked at 100%: its 27 `basic_learn_skill_keys`.
- No field holds HP, stamina, weight or a movement stat, so the 500 HP and 1
  stamina that two horses start above their `servantexperience.dbss` level 1
  row (its Open Questions) do not come from this file.

## Open Questions

### The Zero Fields

`unknown_basic_learn_skill_keys_00` (5 bytes) and
`unknown_stallion_skill_keys_02` (2 bytes) are `0` on every record of
clients 1784 and 3474. In column order the first sits where the sheet has
`specialLearnSkillMaxCount` and `specialLearnSkillKey`, but the sheet holds
`1` in `specialLearnSkillMaxCount` on every row, so the bytes do not follow
it. A u8 plus a u32 count of an empty list would fit the 5 bytes as well.
