# `servantmating.bss` Format

## Purpose

Horse breeding grade table: one row per band of the parents' average grade,
with the lowest and highest grade a foal of that band can get. Client 3474
adds the Imperial Steed and the band's chance to breed it (Breeding
Results). On client 3474 the file has 34 rows, keys 1 to 36 without 29 and
30.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ----- | ------------- | --------- |
| 2      | 3474 and later | 3474    | `servantmating.bss`        | 684   | 34 Row        | 20        |
| 1      | 1784           | 1784    | `servantmating.dbss`       | 340   | 24 Row        | 14        |
| 1      | 1784           | 1784    | `servantmatingoffset.dbss` | 292   | 24 Offset Row | 12        |

| Layout | File                       | Known          | Unknown    |
| ------ | -------------------------- | -------------- | ---------- |
| 2      | `servantmating.bss`        | 684 B (100.0%) | 0 B (0.0%) |
| 1      | `servantmating.dbss`       | 340 B (100.0%) | 0 B (0.0%) |
| 1      | `servantmatingoffset.dbss` | 292 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role |
| ---------------------------- | -------- | ---- |
| `languagedata_en.loc`        | Optional | The Imperial Steed's name (LOC type 6, `str_id1` = `imperial_steed_character_id`) |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key, so an `imperial_steed_character_id` without a row shows as plain text instead of a link |

Client 1784 ships the table as `servantmating.dbss` with the index
`servantmatingoffset.dbss` (Layout 1).

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                   |
| ------- | ---------- | ----- | --------------------------------------- |
| `+0x00` | u32        | count | 34 on client 3474                       |
| `+0x04` | Row[count] | rows  | `count` rows of 20 bytes, ending at EOF |

### Row (20 bytes)

| Offset  | Type | Field            | Notes |
| ------- | ---- | ---------------- | ----- |
| `+0x00` | u32  | key              | Band index; not in key order (36 to 32, 15 to 1, 31 to 16 on client 3474) |
| `+0x04` | u32  | key_dup          | Equals `key` on every row |
| `+0x08` | u16  | average_grade    | Lower end of the band: 0 to 1,150 in steps of 50 for keys 1 to 24, then 1,160 to 1,250 in steps of 10 (client 3474) |
| `+0x0A` | u16  | result_max_grade | 520 to 660 on client 3474 |
| `+0x0C` | u16  | result_min_grade | 460 to 615 on client 3474 |
| `+0x0E` | u16  | imperial_steed_character_id | 31594 on every row (client 3474), the Imperial Steed in `servant.bss` |
| `+0x10` | u32  | imperial_steed_rate | Millionths: 1,600 (0.16%) to 70,000 (7%), rising with `average_grade` (client 3474) |

## Layout 1

### `servantmating.dbss`

| Offset  | Type       | Field | Notes                                   |
| ------- | ---------- | ----- | --------------------------------------- |
| `+0x00` | u32        | count | 24 on client 1784                       |
| `+0x04` | Row[count] | rows  | `count` rows of 14 bytes, ending at EOF |

### Row (14 bytes)

| Offset  | Type | Field            | Notes |
| ------- | ---- | ---------------- | ----- |
| `+0x00` | u32  | key              | 15 down to 1, then 24 down to 16 |
| `+0x04` | u32  | key_dup          | Equals `key` on every row |
| `+0x08` | u16  | average_grade    | |
| `+0x0A` | u16  | result_max_grade | |
| `+0x0C` | u16  | result_min_grade | |

### `servantmatingoffset.dbss`

| Offset  | Type              | Field   | Notes                           |
| ------- | ----------------- | ------- | ------------------------------- |
| `+0x00` | u32               | count   | Equals the `servantmating.dbss` count |
| `+0x04` | Offset Row[count] | entries | `count` entries of 12 bytes     |

### Offset Row (12 bytes)

| Offset  | Type | Field  | Notes                                               |
| ------- | ---- | ------ | --------------------------------------------------- |
| `+0x00` | u32  | key    | The row's `key`                                     |
| `+0x04` | u32  | offset | Where the row's `key_dup` starts, 4 bytes into the row |
| `+0x08` | u32  | size   | 10 on every entry: the row from `key_dup` on        |

## Breeding Results

Checked in game on client 3474 (2026-10-20) in the Horse Growth Info
Breed/Exchange Calculator with a tier 8 mare of grade 650 (9890) and a
stallion that puts the pair in band key 12 (`average_grade` 550,
`result_min_grade` 462, `result_max_grade` 535, `imperial_steed_rate`
3,200, the only band with that rate):

- The result grid holds 40 horses in pairs of 2.037% (mare) and 2.963%
  (stallion). `servant.bss` has exactly 40 breeding-result horses
  (`is_mating_result` 1) with a `grade` from 462 to 535: 20 tier 6 mares
  and 20 tier 6 stallions, at grades 490 and 520.
- Under the heading Imperial Steed it shows one mare at 0.32%: 3,200
  millionths, `imperial_steed_rate` of the band. 31594 is a mare
  (`is_male` 0); the calculators' horse list shows it with 31565 under the
  same heading.

The 40 pair chances add up to 100% without the Imperial Steed's 0.32%. How
the client splits mare and stallion chances (40.74% to 59.26% of each
pair here) is not in this file.

## Field Names

The names follow the `ServantMating_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 (24 rows, `Index`, `AverageGrade`,
`ResultMinGrade`, `ResultMaxGrade`), matched value by value:

| Column | Field | Equal (client 1784) | Equal (client 3474) |
| ------ | ----- | ------------------- | ------------------- |
| `Index` | `key` | 24 of 24 | 24 of 24 |
| `AverageGrade` | `average_grade` | 24 | 24 |
| `ResultMaxGrade` | `result_max_grade` | 24 | 10 |
| `ResultMinGrade` | `result_min_grade` | 24 | 8 |

The client 3474 misses are rebalances: band 15 (average 700) gives 468 to
600 against 435 to 600 on client 1784, and keys 1 to 11 all give 460 to 520
where client 1784 starts at 155 to 166. The 2016 `gc::ServantMatingStaticStatus`
holds `_key`, `_grade`, `_gradeByMin` and `_gradeByMax`; the file stores the
maximum before the minimum. The sheet has no column for
`imperial_steed_character_id` and `imperial_steed_rate`; their names come
from the in-game check in Breeding Results.
