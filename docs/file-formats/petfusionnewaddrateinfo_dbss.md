# `petfusionnewaddrateinfo.dbss` Format

## Purpose

The add rates of a pet exchange: how much each other pet raises the success
chance of the main pet (the first pet registered in the exchange window), by
the main pet's tier and the other pet's tier. The base chance and the result
tiers are in [`petfusionnew.dbss`](petfusionnew_dbss.md). Tiers are stored
from 0, as `tier` of [`pet.dbss`](pet_dbss.md) stores them: `0` is Tier 1.
Rates are on the 1,000,000 = 100% scale. The file has no PABR magic, no
count and no trailer: four rows of add rates, then one more array of four
values.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | ------- | --------- |
| 1      | 1485 and later | 3474    | `petfusionnewaddrateinfo.dbss` | 80    | 4 Row   | 16        |

| Layout | File                           | Known         | Unknown    |
| ------ | ------------------------------ | ------------- | ---------- |
| 1      | `petfusionnewaddrateinfo.dbss` | 80 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type   | Field      | Notes                                                           |
| ------- | ------ | ---------- | --------------------------------------------------------------- |
| `+0x00` | Row[4] | rows       | See Row; the row index is the main pet's tier, from 0           |
| `+0x40` | u32[4] | gosphy_add_rate | Added by a Wizard Gosphy as the other pet, one rate per main pet tier, from 0 |

### Row (16 bytes)

| Offset  | Type | Field           | Notes                                                  |
| ------- | ---- | --------------- | ------------------------------------------------------ |
| `+0x00` | u32  | add_rate_tier_0 | Added by an other pet of tier `0` (Tier 1)             |
| `+0x04` | u32  | add_rate_tier_1 | Added by an other pet of tier `1` (Tier 2)             |
| `+0x08` | u32  | add_rate_tier_2 | Added by an other pet of tier `2` (Tier 3)             |
| `+0x0C` | u32  | add_rate_tier_3 | Added by an other pet of tier `3` (Tier 4)             |

## Add Rates

On client 3474, with tiers as the game numbers them:

| Main pet | + Tier 1 | + Tier 2 | + Tier 3 | + Tier 4 | + Wizard Gosphy |
| -------- | -------- | -------- | -------- | -------- | --------------- |
| Tier 1   | 55%      | 0%       | 0%       | 0%       | 65%             |
| Tier 2   | 65%      | 80%      | 0%       | 0%       | 75%             |
| Tier 3   | 15%      | 25%      | 35%      | 0%       | 20%             |
| Tier 4   | 0%       | 0%       | 0%       | 0%       | 0%              |

The zeros above the diagonal are pairs the window refuses: it takes no
other pet of a higher tier than the main pet (`PANEL_RENEWAL_PETLIST_TEMP_3`,
"The pet cannot have a higher tier than main pet."). A Tier 4 main pet
keeps its tier at 100% (see `petfusionnew.dbss`), so its row adds nothing.

With the base chance of 0.01% from `petfusionnew.dbss`, one other pet gives
the success chances Garmoth's
[pets guide](https://garmoth.com/guides/post/bdo-basics-pets) lists for the
six tier pairs of the first three rows: 55%, 65%, 80%, 15%, 25% and 35%.

## Field Names

The `Pet_Fusion_AddRate_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `Tier`, `Tier0`,
`Tier1`, `Tier2` and `Tier3`, and 8 rows. Rows `Tier` `0` to `3` match
`rows` on all 16 values, `Tier0` to `Tier3` in column order (clients 1784
and 3474); their empty cells (`<null>`) are the zeros of the file. Rows
`Tier` `10` to `13` fill only `Tier0`, with `650000`, `750000`, `200000`
and `0`: the four values of `gosphy_add_rate`, in row order. The developer
workbook (`datasheet_petdatatable.xlsm`) has no note column on this sheet.

The client Lua of the exchange window (`panel_window_petfusion_all_1.luac`,
`setRate`) adds `ToClient_getAddFusionRate(mainPetTier, subTier, subRace)
/ 10000` percent for each other pet, which names the row as the main pet's
tier and the column as the other pet's tier. Both tiers are the stored
`getPetTier()` values, the same ones the window shows plus 1 (`LUA_SERVANT_TIER`).

## Notes

- Clients 1485, 1784, 2107, 2519, 3002, 3251 and 3474 ship the same 80
  bytes. Client 1230 stores them inside `petfusionnew.bss` after the
  `petfusionnew.dbss` rows (see [`petfusionnew.dbss`](petfusionnew_dbss.md)),
  so `gosphy_add_rate` is a separate array there too, not a fifth row.
- The window sums the add rates of up to four other pets, adds the base
  chance and caps the total at 100%.
- `gosphy_add_rate` is the add rate of [Wizard
  Gosphy](https://bdocodex.com/us/item/18423/), the pet
  `ToClient_getAddFusionRate` gets race `99` for. The Lua passes the other
  pet's race (`getPetRace()`, `species` in `pet.dbss`) to the add rate
  lookup, and race `99` is the one race the window treats apart: it cannot
  be the main pet (`PANEL_RENEWAL_PETLIST_TEMP_9`, "Wizard Gosphy cannot be
  the main pet.") and goes in only when the main pet has `is_joker_pet_use`
  set. The only race `99` record in `pet.dbss` is Wizard Gosphy (`55175`,
  tier `0`). In game on client 3474 my Tier 3 main pet with one Tier 1
  Wizard Gosphy shows "Tier 4 20%" and "Tier 3 80%", and with four Wizard
  Gosphys "Tier 4 80%": 0.01% base plus one or four times `200000`, where a
  normal Tier 1 pet adds `150000` (15%). Garmoth's pets guide says Wizard
  Gosphy "has increased chances of success for enhancing other pets".
