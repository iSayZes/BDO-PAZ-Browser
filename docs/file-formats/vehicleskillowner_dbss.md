# `vehicleskillowner.dbss` Format

## Purpose

Which [vehicleskill.dbss](vehicleskill_dbss.md) skills each servant can
learn: one record per servant character with a list of skill keys, each
with a learn value, an EXP value and a learn flag. On client 3474 the file
has 366 records, every one a `servant.bss` character, with 0 to 37 skills
each (5,620 in all).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes  | Records                 | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ------ | ----------------------- | --------- |
| 2      | 2519 and later | 3474    | `vehicleskillowner.dbss`       | 94,316 | 5,620 Skill, 366 Record | 16        |
| 2      | 2519 and later | 3474    | `vehicleskillowneroffset.dbss` | 3,680  | 366 Offset Row          | 10        |
| 1      | 1485 to 2107   | 2107    | `vehicleskillowner.dbss`       | 57,016 | 4,204 Skill, 295 Record | 13        |
| 1      | 1485 to 2107   | 2107    | `vehicleskillowneroffset.dbss` | 2,970  | 295 Offset Row          | 10        |

| Layout | File                           | Known            | Unknown          |
| ------ | ------------------------------ | ---------------- | ---------------- |
| 2      | `vehicleskillowner.dbss`       | 77,456 B (82.1%) | 16,860 B (17.9%) |
| 2      | `vehicleskillowneroffset.dbss` | 3,680 B (100.0%) | 0 B (0.0%)       |
| 1      | `vehicleskillowner.dbss`       | 44,404 B (77.9%) | 12,612 B (22.1%) |
| 1      | `vehicleskillowneroffset.dbss` | 2,970 B (100.0%) | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2519   | Layout 2 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                           | Required | Role                                                    |
| ------------------------------ | -------- | ------------------------------------------------------- |
| `vehicleskillowneroffset.dbss` | Optional | PABR index: character ID to the record's offset and size |
| `vehicleskill.dbss`            | Optional | The skills `skill_key` points at; their Korean names when LOC has none |
| `characterstaticoffset.dbss`   | Optional | Every `characterstatic.dbss` key, so a `character_id` without a row shows as plain text instead of a link |
| `languagedata_en.loc`          | Optional | Servant names (LOC type 6) and skill names (LOC type 8) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                  |
| ------- | ------------- | ------- | -------------------------------------- |
| `+0x00` | u32           | count   | 366 on client 3474                     |
| `+0x04` | Record[count] | records | Back to back, variable size, up to EOF |

### Record (variable: 12 bytes + skills)

| Offset  | Type                | Field            | Notes |
| ------- | ------------------- | ---------------- | ----- |
| `+0x00` | u16                 | character_id     | Servant character, as in `servant.bss` |
| `+0x02` | u16                 | character_id_dup | Equals `character_id` on every record |
| `+0x04` | u32                 | cant_learnable_rate | Weight of "Does not learn" ([Learn Chance](#learn-chance)); 0 on 218 records, up to 1,000,000 on 148 (client 3474) |
| `+0x08` | u32                 | skill_count      | 0 to 37 on client 3474 |
| `+0x0C` | Skill[skill_count]  | skills           | In `skill_key` order |

### Skill (16 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u32  | skill_key  | `vehicleskill.dbss` key, 1 to 106 on client 3474 |
| `+0x04` | u32  | able       | 1,000,000 on 996 of 5,620 entries (client 3474) |
| `+0x08` | u32  | add_exp    | |
| `+0x0C` | u8   | is_learn   | 0 on 153 entries (client 3474) |
| `+0x0D` | u8   | unknown_0d | 2 on every entry (client 3474) |
| `+0x0E` | u16  | unknown_0e | `0` on every entry (clients 1784 and 3474) |

### `vehicleskillowneroffset.dbss`

| Offset              | Type              | Field              | Notes                              |
| ------------------- | ----------------- | ------------------ | ---------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                             |
| `+0x04`             | u32               | count              | Equals the main file's `count`     |
| `+0x08`             | Offset Row[count] | entries            | Not in file order                  |
| `entries+0x00`      | String Table      | string_table       | Present but empty                  |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`  |
| `string_table+0x04` | u32               | zero               | `0`                                |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                       |
| ------- | ---- | ------------ | ----------------------------------------------------------- |
| `+0x00` | u16  | character_id | The record's `character_id`                                 |
| `+0x02` | u32  | offset       | Where the record's `character_id_dup` starts, 2 bytes into the record |
| `+0x06` | u32  | size         | Record size minus 2                                         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Layout 1

Client 1784 has no `cant_learnable_rate` and stores `skill_key` as a u8; it has 288
records and 4,134 skills, keys 1 to 76.

### Record (variable: 8 bytes + skills)

| Offset  | Type                | Field            | Notes |
| ------- | ------------------- | ---------------- | ----- |
| `+0x00` | u16                 | character_id     | |
| `+0x02` | u16                 | character_id_dup | |
| `+0x04` | u32                 | skill_count      | 0 to 27 |
| `+0x08` | Skill[skill_count]  | skills           | In `skill_key` order on 286 of 288 records |

### Skill (13 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u8   | skill_key  | |
| `+0x01` | u32  | able       | |
| `+0x05` | u32  | add_exp    | |
| `+0x09` | u8   | is_learn   | |
| `+0x0A` | u8   | unknown_0d | `0` on every entry |
| `+0x0B` | u16  | unknown_0e | `0` on every entry |

## Learn Chance

The horse growth window (Horse Growth Info, My Horse Info tab) lists a
chance per skill and a "Does not learn" row. The client Lua
(`panel_dialog_servantsimulator_5`) fills that row from
`ToClient_GetHorseSimulateDetailInformationCantLearnableRate()`. With the
window's Total Gain Chance `g`:

```text
chance(skill)   = able × (1 + g) / (cant_learnable_rate + sum of able of the skills not learned yet)
chance(nothing) = 100% - sum of chance(skill)
```

Learned and inherent skills drop out of the sum. On 103 of the 148 records
with a non-zero `cant_learnable_rate` (client 3474), it plus the `able` of
every entry below 1,000,000 is exactly 1,000,000; the formula does not need
that, and holds on a record where the total is 1,061,581 too (9890 below).

Checked on 2026-10-20 (client 3474) with Training Artisan 7, on two tier 6
stallions of the 9915 group (9915, 9952, 9953, 9973, 9978:
`cant_learnable_rate` 536,040, Hind Kick 75,000) at Total Gain Chance
21.7%, and on the tier 8 mare 9890 (`cant_learnable_rate` 379,906, Caution
37,000, Two-seater 9,000) at 31.7%:

| Horse | Learned | Sum | Chance | Does not learn |
| ----- | ------- | --- | ------ | -------------- |
| 9953 (Breed 11), level 8 | Fore Chop, Sprint (inherent) | 924,405 | Hind Kick 9.8739% (shown 9.8739%) | 48.8715% (shown 48.8715%) |
| 9915 (Breed 2), level 4 | Sprint (inherent), Start Accel, Streak Leap | 906,912 | Hind Kick 10.0644% (shown 10.0644%) | 50.2327% (shown 50.2327%) |
| 9890 (Breed 13), level 30 | 18 of 20, S: Instant Accel and Sprint inherent | 425,906 | Caution 11.4413%, Two-seater 2.7830% (shown 11.4413%, 2.783%) | 85.7757% (shown 85.7757%) |

The window's Base Coat line (`bdoservanttitless.bss`) names the breed,
which picks one character of the group. The level 4 horse's window lists
three learned skills; only Streak Leap
(38,064) as the third one gives its shown chances, and Drift, Fore Chop,
High Jump, Quick Stop and Instant Accel then match to the last digit too.

## Field Names

The names follow the `VehicleSkillOwner_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784: one row per `CharacterKey` with
`Able_N`, `AddExp_N` and `IsLearn_N` for skill keys 1 to 76. On client 1784
(288 records, every one in the sheet) the entries match by value:

| Column | Field | Equal (client 1784, 4,134 entries) | Equal (client 3474, 3,899 entries of 279 shared records) |
| ------ | ----- | ---------------------------------- | -------------------------------------------------------- |
| `Able_N` | `able` of the entry with `skill_key` N | 4,112 | 2,529 |
| `AddExp_N` | `add_exp` | 4,134 | 3,197 |
| `IsLearn_N` | `is_learn` | 4,134 | 3,899 |

The 22 client 1784 `able` misses are sheet values with a fraction stored
truncated (`4666.666667` as 4,666). Every record lists each skill whose
`Able_N` is not 0; 23 records also list skills whose `Able_N` is 0. The
client 3474 misses come from changed values: `able` 1,000,000 and `add_exp`
0 where client 1784 has 200,000 and 2,500 (camel 9081, Fore Chop 20 and
Hind Kick 21), and the client Lua gates the
skill-rate display of the breeding simulator behind
`_ContentsGroup_VehicleLearnSkill_Renewal`.

## Open Questions

### Records With No Does-Not-Learn Weight

`cant_learnable_rate` is new on client 3474: 0 on all tier 1 to 5 horses
and on 218 records in all, non-zero on 148, mostly tier 6 to 9 horses. 51
of the 218 start with every skill they list (31619, checked in game, shows
Skill List (27) with all 27 at 100%), but the other 167, among them every
tier 1 to 5 horse, still have skills to learn. With a weight of 0 the
formula gives "Does not learn" 0% and the skills more than 100% in sum, so
the window either shows those horses another way or uses another formula
for them.

### The Constant Byte

`unknown_0d` is 2 on every client 3474 entry and 0 on client 1784.
