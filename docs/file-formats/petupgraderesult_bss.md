# `petupgraderesult.bss` Format

## Purpose

The outcome of Tier 5 Pet Training per pet: which Tier 5 pet a Tier 4 pet
trains into, and the talent (base skill) the pet shows while it is the
alpha. The file holds two maps with no PABR magic and no trailer: Tier 4
pet to result, then Tier 5 pet to alpha talent. Pet keys are `pet_id`s of
[`pet.dbss`](pet_dbss.md); talents are Section 2 `equip_skill_id`s of
[`petequipskill.bss`](petequipskill_bss.md), the keys `pet.dbss` stores as
`base_skill_id`. The training cost is in [`petupgrade.bss`](petupgrade_bss.md)
and the alpha's loot cooldown bonus in
[`petleaderbuff.bss`](petleaderbuff_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records                      | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ---------------------------- | --------- |
| 1      | 2107 and later | 3474    | `petupgraderesult.bss` | 7,112 | 444 Result, 444 Leader Skill | 10        |

| Layout | File                   | Known            | Unknown    |
| ------ | ---------------------- | ---------------- | ---------- |
| 1      | `petupgraderesult.bss` | 7,112 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None. The handler names the pets and the talents from
[`pet.dbss`](pet_dbss.md) (with `petoffset.dbss`) and
[`petequipskill.bss`](petequipskill_bss.md) when they are present.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset          | Type                          | Field              | Notes                                         |
| --------------- | ----------------------------- | ------------------ | --------------------------------------------- |
| `+0x00`         | u32                           | result_count       | Number of Result rows                         |
| `+0x04`         | Result[result_count]          | results            | See Result                                    |
| `results+0x00`  | u32                           | leader_skill_count | Number of Leader Skill rows; equals `result_count` on client 3474 |
| `results+0x04`  | Leader Skill[leader_skill_count] | leader_skills   | See Leader Skill                              |

On client 3474 the file is 4 + 444 x 10 + 4 + 444 x 6 = 7,112 bytes.

### Result (10 bytes)

| Offset  | Type | Field                | Notes                                                                                     |
| ------- | ---- | -------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16  | pet_id               | Map key: the Tier 4 pet (`tier` `3` in [`pet.dbss`](pet_dbss.md))                         |
| `+0x02` | u16  | pet_id_dup           | Equals `pet_id` on every row                                                              |
| `+0x04` | u16  | result_pet_id        | The Tier 5 pet the training gives (`tier` `4` in `pet.dbss`)                              |
| `+0x06` | u32  | leader_base_skill_id | Talent of the trained pet as the alpha: a Section 2 `equip_skill_id` of [`petequipskill.bss`](petequipskill_bss.md) |

### Leader Skill (6 bytes)

| Offset  | Type | Field                | Notes                                                           |
| ------- | ---- | -------------------- | --------------------------------------------------------------- |
| `+0x00` | u16  | pet_id               | Map key: a Tier 5 pet, the `result_pet_id` of one Result row     |
| `+0x02` | u32  | leader_base_skill_id | Equals `leader_base_skill_id` of that Result row                 |

## Training Results

On client 3474 every Tier 4 pet of `pet.dbss` has a Result row except the
five fairy records (`pet_type` 1), and every Tier 5 pet is the
`result_pet_id` of exactly one row. 431 of the 444 rows give a pet with the
same LOC name; the other 13 give the Tier 5 record of the same pet where
the Tier 4 record has no LOC name (`아토락시온 타르케스_T4` to Tarkhes,
`반려동물 쪼쪼_교역_T4` to Jojo).

`leader_base_skill_id` is the talent one level above the Tier 4 pet's own
`base_skill_id`, keyed by that base skill on all 444 rows:

| Tier 4 `base_skill_id` | `leader_base_skill_id` | Talent as the alpha (LOC type 10) | Rows (client 3474) |
| ---------------------- | ---------------------- | --------------------------------- | ------------------ |
| 18                     | 99                     | Skill EXP +5%                     | 118                |
| 38                     | 101                    | Durability Reduction Resistance +5% | 100              |
| 23                     | 100                    | Life EXP +5%                      | 99                 |
| 58                     | 103                    | Weight Limit +60 LT               | 31                 |
| 43                     | 102                    | Normal and Higher Grade Gain Chance Lv. 5 | 30         |
| 78                     | 106                    | Death Penalty Resistance +5%      | 28                 |
| 73                     | 105                    | Combat EXP +5%                    | 24                 |
| 82                     | 107                    | Item Drop Rate +5%                | 5                  |
| 68                     | 104                    | Max HP +125                       | 5                  |
| 86                     | 108                    | Mount EXP +5%                     | 2                  |
| 98                     | 111                    | Big Ship Inventory Weight +250 LT | 1                  |
| 94                     | 110                    | Barter EXP +5%                    | 1                  |

The Tier 5 pet's own record in `pet.dbss` keeps the Tier 4 `base_skill_id`
on every row.

## Field Names

No reference source has the table: the file is not in the client 1784
archive, a private server's `DataSheets.bexcel` on client 1784 has no sheet
with `Upgrade` and `Pet` in its name, and the 2016 client's debug symbols
have no pet upgrade type. The names come from the client Lua of client
3474 and the official Black Desert wiki:

- `pet_id` and `result_pet_id`: the Tier 5 Pet Training window
  (`panel_dialog_petleader_all_1.luac`) calls
  `ToClient_getPetUpgradeSimulationResult(characterKey)` with the character
  key of the Tier 4 pet in the slot and reads the tier of the pet it
  returns (`newPetStaticStatus:getPetTier()`) for the alpha bonus. Every
  key of Result is a Tier 4 pet and every `result_pet_id` a Tier 5 one.
- `leader_base_skill_id`: the same window, the pet list
  (`panel_window_petlist_all_2.luac`) and the pet info window
  (`panel_window_petinfo_all_1.luac`) show the talent of an alpha pet with
  `ToClient_getPetBaseSkillStaticStatus(ToClient_getLeaderBaseSkill(petNo))`,
  and of any other pet with `getPetBaseSkillIndex()`. The official Black
  Desert wiki page "Tier 5 Pet Training/Alpha Appointment" says "The Alpha
  Pet's Talent gains one additional level", with the examples "Combat EXP
  +4% -> +5%" and "HP +100 -> +125", and that other Tier 5 pets "share the
  same stats as a Tier 4 pet". That is the step from `base_skill_id` to
  `leader_base_skill_id` in Training Results (`73` Combat EXP +5% and `104`
  Max HP +125).
- `pet_id_dup`: equal to the key on all 444 rows, as `plantupgradeparam.bss`
  stores its map key again as the first member of the value.

## Notes

- Clients 2107, 2519, 3002 and 3251 ship the file too; client 1784 does
  not.
- The rows of neither map are sorted by key, and the two maps
  list the pets in different orders.
- `ToClient_getLeaderBaseSkill` takes a pet number, not a key, so the Lua
  does not show which of the two maps it reads. The training window calls
  it for a Tier 4 pet (a Result key), the pet list for an alpha, which is a
  Tier 5 pet (a Leader Skill key).

## Open Questions

### Why the Second Map

Leader Skill repeats the talent of every Result row under the Tier 5 pet's
key. The client could look the talent up through either key; which call
reads which map is not in the client Lua, and the client 3474 executable
does not name the table's loader.
