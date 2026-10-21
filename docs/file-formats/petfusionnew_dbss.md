# `petfusionnew.dbss` Format

## Purpose

The result tiers of a pet exchange, one row per tier of the main pet (the
first pet registered in the exchange window): the tier the new pet gets on
a success with its base chance, and the tier it gets otherwise. The other
pets in the exchange raise the first chance by the add rates of
[`petfusionnewaddrateinfo.dbss`](petfusionnewaddrateinfo_dbss.md).
Companion `petfusionnewoffset.dbss` lists where every row sits. Tiers are
stored from 0, as `tier` of [`pet.dbss`](pet_dbss.md) stores them: `0` is
Tier 1. Rates are on the 1,000,000 = 100% scale.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------------ | --------- |
| 1      | 1485 and later | 3474    | `petfusionnew.dbss`       | 68    | 4 Row        | 17        |
| 1      | 1485 and later | 3474    | `petfusionnewoffset.dbss` | 40    | 4 Offset Row | 9         |

| Layout | File                      | Known         | Unknown    |
| ------ | ------------------------- | ------------- | ---------- |
| 1      | `petfusionnew.dbss`       | 68 B (100.0%) | 0 B (0.0%) |
| 1      | `petfusionnewoffset.dbss` | 40 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                                     |
| ------------------------- | -------- | ------------------------------------------------------------------------ |
| `petfusionnewoffset.dbss` | Optional | `tier -> (offset, size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type      | Field | Notes                                 |
| ------- | --------- | ----- | ------------------------------------- |
| `+0x00` | Row[..end] | rows | See Row; no count, the rows fill the file |

On client 3474 the file is 4 x 17 = 68 bytes.

### Row (17 bytes)

| Offset  | Type     | Field         | Notes                                                                            |
| ------- | -------- | ------------- | -------------------------------------------------------------------------------- |
| `+0x00` | u8       | tier          | Row key: the main pet's tier, from 0                                             |
| `+0x01` | u8       | select_tier_0 | Tier of the new pet on a success, from 0                                         |
| `+0x02` | bytes[3] | padding_02    | Alignment bytes of the `select_tier_0` entry, see Notes                          |
| `+0x05` | u32      | select_rate_0 | Base chance of `select_tier_0`: `100` (0.01%) for main tiers 0 to 2, `1000000` for tier 3 (client 3474) |
| `+0x09` | u8       | select_tier_1 | Tier of the new pet otherwise, from 0; `0` with `select_rate_1` `0` on tier 3     |
| `+0x0A` | bytes[3] | padding_0a    | Alignment bytes of the `select_tier_1` entry, see Notes                          |
| `+0x0D` | u32      | select_rate_1 | `1000000` on main tiers 0 to 2, `0` on tier 3 (client 3474)                       |

### `petfusionnewoffset.dbss`

Bare offset table into `petfusionnew.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                   |
| ------- | ----------------- | ----- | --------------------------------------- |
| `+0x00` | u32               | count | Number of rows in `petfusionnew.dbss`   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                          |

### Offset Row (9 bytes)

| Offset  | Type | Field  | Notes                                                                    |
| ------- | ---- | ------ | ------------------------------------------------------------------------ |
| `+0x00` | u8   | tier   | Key of the row it points at                                              |
| `+0x01` | u32  | offset | Absolute byte offset of the row in `petfusionnew.dbss`, at its `tier`    |
| `+0x05` | u32  | size   | The whole row: always `17`                                               |

## Exchange Results

On client 3474, with tiers as the game numbers them:

| Main pet | Success     | Base chance | Otherwise |
| -------- | ----------- | ----------- | --------- |
| Tier 1   | Tier 3      | 0.01%       | Tier 2    |
| Tier 2   | Tier 3      | 0.01%       | Tier 2    |
| Tier 3   | Tier 4      | 0.01%       | Tier 3    |
| Tier 4   | Tier 4      | 100%        | none      |

The base chance plus the add rates of the other pets is the success chance
the exchange window shows. Garmoth's
[pets guide](https://garmoth.com/guides/post/bdo-basics-pets) lists six
chances that match this sum for one other pet, rounded to a whole percent:
55% for Tier 1 + Tier 1, 65% for Tier 2 + Tier 1, 80% for Tier 2 + Tier 2,
15% for Tier 3 + Tier 1, 25% for Tier 3 + Tier 2 and 35% for Tier 3 +
Tier 3. See [`petfusionnewaddrateinfo.dbss`](petfusionnewaddrateinfo_dbss.md)
for the add rates.

## Field Names

The `Pet_Fusion_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Tier`, `SelectRate_0`, `SelectTier_0`,
`SelectRate_1` and `SelectTier_1`, and its 4 rows match the file on all 4
keys and all four value columns (clients 1784 and 3474). The file stores
each tier before its rate; the sheet lists the rate first. The empty
`SelectRate_1` and `SelectTier_1` cells of tier `3` (`<null>`) are the
zeros of the file. The developer workbook (`datasheet_petdatatable.xlsm`)
adds the note columns `#SelectCharacterName_0` and
`#SelectCharacterName_1`, which name each select tier as a generation
(`세대`): `3세대` for `2`, `4세대` for `3`, `2세대` for `1`, so the stored
tier plus 1 is the game's tier. A third note column reads `#참조 : 합성 세대
정보` ("reference: fusion generation info").

The client Lua of the exchange window (`panel_window_petfusion_all_1.luac`,
`setRate`) reads `ToClient_getMainFusionRate(mainPetTier) / 10000` as the
base chance in percent, which is `select_rate_0` on the 1,000,000 = 100%
scale. It shows the target tier as Tier 3 for a Tier 1 or Tier 2 main pet
and as Tier 4 for a Tier 3 or Tier 4 one (`setTargetTier`), the
`select_tier_0` column plus 1, and the second bar as the tier below it, the
`select_tier_1` column plus 1. For a Tier 4 main pet it hides the second
bar, the row whose `select_rate_1` is `0`.

## Notes

- The success chance in the window is `select_rate_0` plus, for each of
  up to four other pets (`_subPetMaxTableCount = 4`), its add rate by the
  main pet's tier and its own tier, capped at 100% and rounded to a whole
  percent (`math.floor(totalRate + 0.5)`). The other result gets the rest.
  At 100% the window takes no more pets (`LUA_PETFUSION_100PERCENT_TEXT`,
  "You can no longer increase the probability of pet tier increase.").
- The window takes no other pet of a higher tier than the main pet
  (`PANEL_RENEWAL_PETLIST_TEMP_3`) and no Tier 5 pet
  (`LUA_PETFUSION_LEADERPET`), so tier `4` has no row.
- `padding_02` and `padding_0a` are the 3 bytes between a u8 tier and its
  4-byte aligned rate: each select is an 8-byte entry (u8, 3 alignment
  bytes, u32) copied whole. The bytes differ between builds while every
  sheet value stays the same: `00 00 00` and `00 00 00` on client 1485,
  `7F 00 00` and `00 00 00` on clients 1784 and 2519, `00 00 00` and
  `02 00 00` on client 3002, `00 00 00` and `01 00 00` on clients 3251 and
  3474, in every row of the file.
- Clients 1485 to 3474 ship `petfusionnew.dbss`, `petfusionnewoffset.dbss`
  and `petfusionnewaddrateinfo.dbss` with the same values. Client 1230 has
  none of the three and ships `petfusionnew.bss` instead: PABR, then these
  68 bytes, the 80 bytes of `petfusionnewaddrateinfo.dbss`, an empty
  string table and the trailer. Client 794 has `en/petfusion.bss`.
- Both files list the tiers in the same order, `0` to `3`. The offset
  points at the row's own `tier`.
- The older pet exchange table [`petoldfusion.dbss`](petoldfusion_dbss.md)
  (sheet `Pet_OldFusion_Table`) keys its result tiers by fusion key
  (variant, species and tier) in place of the tier alone.
