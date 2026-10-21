# `petoldfusion.dbss` Format

## Purpose

The result tiers of the old pet exchange, one row per fusion key (variant,
species and tier of the main pet, the four bytes `pet.dbss` stores at
payload `+0x02`): up to four result tiers, each with a chance. It is the
per-species table that [`petfusionnew.dbss`](petfusionnew_dbss.md) (one
row per tier) stands next to. Companion `petoldfusionoffset.dbss` lists
where every row sits. Tiers are stored from 0, as `tier` of
[`pet.dbss`](pet_dbss.md) stores them: `0` is Tier 1. Rates are on the
1,000,000 = 100% scale.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ------ | -------------- | --------- |
| 1      | 1485 and later | 3474    | `petoldfusion.dbss`       | 15,364 | 384 Row        | 40        |
| 1      | 1485 and later | 3474    | `petoldfusionoffset.dbss` | 4,612  | 384 Offset Row | 12        |

| Layout | File                      | Known            | Unknown      |
| ------ | ------------------------- | ---------------- | ------------ |
| 1      | `petoldfusion.dbss`       | 14,980 B (97.5%) | 384 B (2.5%) |
| 1      | `petoldfusionoffset.dbss` | 4,612 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                                       |
| ------------------------- | -------- | -------------------------------------------------------------------------- |
| `petoldfusionoffset.dbss` | Optional | `fusion key -> (offset, size)` of every row; the parser walks the main file without it |
| `pet.dbss` + `petoffset.dbss` | Optional | The LOC names of the pets with the row's fusion key                    |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 384 x 40 = 15,364 bytes.

### Row (40 bytes)

A 4-byte copy of the fusion key, then the 36 bytes the offset row
addresses.

| Offset  | Type     | Field         | Notes                                                                     |
| ------- | -------- | ------------- | ------------------------------------------------------------------------- |
| `+0x00` | u32      | key_prefix    | The fusion key `variant`, `species`, `unknown_06`, `tier` read as one u32 |
| `+0x04` | u8       | variant       | Fusion key byte 0: `variant` of the main pet in `pet.dbss` (sheet `Kind`) |
| `+0x05` | u8       | species       | Fusion key byte 1: `species` (sheet `Race`)                               |
| `+0x06` | u8       | unknown_06    | Fusion key byte 2: `0` on every row, as `unknown_04` of `pet.dbss`         |
| `+0x07` | u8       | tier          | Fusion key byte 3: the main pet's tier, from 0                            |
| `+0x08` | u8       | select_tier_0 | First result tier, from 0                                                 |
| `+0x09` | bytes[3] | padding_09    | Alignment bytes of the `select_tier_0` entry, see Notes                   |
| `+0x0C` | u32      | select_rate_0 | Chance of `select_tier_0`                                                 |
| `+0x10` | u8       | select_tier_1 | Second result tier, from 0; `0` with `select_rate_1` `0` when unused       |
| `+0x11` | bytes[3] | padding_11    | Alignment bytes of the `select_tier_1` entry                              |
| `+0x14` | u32      | select_rate_1 | `1000000` when used, else `0`                                             |
| `+0x18` | u8       | select_tier_2 | `0` on every row (client 3474)                                            |
| `+0x19` | bytes[3] | padding_19    | Alignment bytes of the `select_tier_2` entry                              |
| `+0x1C` | u32      | select_rate_2 | `0` on every row (client 3474)                                            |
| `+0x20` | u8       | select_tier_3 | `0` on every row (client 3474)                                            |
| `+0x21` | bytes[3] | padding_21    | Alignment bytes of the `select_tier_3` entry                              |
| `+0x24` | u32      | select_rate_3 | `0` on every row (client 3474)                                            |

### `petoldfusionoffset.dbss`

Bare offset table into `petoldfusion.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                  |
| ------- | ----------------- | ----- | -------------------------------------- |
| `+0x00` | u32               | count | Equals the `petoldfusion.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                         |

### Offset Row (12 bytes)

| Offset  | Type | Field      | Notes                                                                       |
| ------- | ---- | ---------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | fusion_key | Key of the row it points at, equal to its `key_prefix`                      |
| `+0x04` | u32  | offset     | Absolute byte offset in `petoldfusion.dbss` of the row's `variant`, past the key prefix |
| `+0x08` | u32  | size       | `36` on every row: the row without its key prefix                          |

Both files list the keys in the same order, which is not sorted.

## Exchange Results

On client 3474 the 384 rows cover 96 variant and species pairs of 42
species, four tiers each. With tiers as the game numbers them:

| Main pet | First result | Chance | Second result | Rows (client 3474) |
| -------- | ------------ | ------ | ------------- | ------------------ |
| Tier 1   | Tier 3       | 50%    | Tier 2        | 95                 |
| Tier 2   | Tier 3       | 70%    | Tier 2        | 94                 |
| Tier 3   | Tier 4       | 30%    | Tier 3        | 94                 |
| Tier 4   | Tier 4       | 100%   | none          | 96                 |

Five rows differ: one Tier 1 row with Tier 2 at 100%, one Tier 2 row with
Tier 3 at 100%, one Tier 2 row with Tier 3 at 40%, one Tier 3 row with
Tier 4 at 100% and one Tier 3 row with Tier 4 at 10%.

## Field Names

The `Pet_OldFusion_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Race`, `Kind`, `Tier`, `SelectRate_0` to
`SelectRate_3` and `SelectTier_0` to `SelectTier_3`, and its 380 rows match
the file on all 380 keys (`Race` = `species`, `Kind` = `variant`) and all
eight value columns, on client 1784 (380 rows) and on client 3474 (384
rows; the four more are species `84`, variant `1`). The file stores each
tier before its rate; the sheet lists the rate first, and its empty cells
(`<null>`) are the zeros of the file. The developer workbook
(`datasheet_petdatatable.xlsm`) adds the note columns
`#SelectCharacterName_0` to `#SelectCharacterName_3`, which name each select
tier as a generation (`3세대` for `2`), and `#참조 : 합성 세대 정보`
("reference: fusion generation info") with the tier pairs a row stands for
(`1+1` on tier `0`, `1+2, 2+2` on tier `1`).

The client 1784 server dump names the type `gc::PetOldFusionStaticStatus`,
held in a `BinaryUnorderedMap` keyed by `gc::PetFusionKey`, with the manager
`PetOldFusionStaticStatusManager`. The 2016 client's debug symbols have
`gc::PetFusionKey` as one u32 `_value`, and `gc::PetStaticStatus` stores the
same four bytes as `_fusionKey`; `pet.dbss` names them `variant`, `species`,
a zero byte and `tier`, and this doc takes those names.

## Notes

- `padding_09`, `padding_11`, `padding_19` and `padding_21` are the 3 bytes
  between a u8 tier and its 4-byte aligned rate, as in `petfusionnew.dbss`:
  each select is an 8-byte entry copied whole. On client 3474 they read
  `7F 00 00` in the first three entries and `00 00 00` in the fourth, in
  every row; on client 1784 `00 00 00`, `01 00 00`, `00 00 00` and
  `00 00 00`, while the sheet values are the same.
- Clients 1485, 1784, 2107, 2519, 3002 and 3251 ship both files.
- 20 rows on client 3474, all four tiers of five species and variant pairs
  (species `36` variant `1`, `39` and `6`, `84` and `1`, `99` and `99`,
  `100` and `100`), have no pet with their fusion key in `pet.dbss`; the
  handler's Pets column is empty for them.
- No client Lua reads the file: the exchange window
  (`panel_window_petfusion_all_1.luac`) shows the chances of
  [`petfusionnew.dbss`](petfusionnew_dbss.md) and
  [`petfusionnewaddrateinfo.dbss`](petfusionnewaddrateinfo_dbss.md)
  (`ToClient_getMainFusionRate`, `ToClient_getAddFusionRate`).

## Open Questions

### Whether the Server Still Reads the Table

The live exchange window shows the per-tier chances of `petfusionnew.dbss`,
and Garmoth's pets guide gives chances that match those. Whether the
server still uses the per-species rows here (the name says "old"), and
whether `select_rate_1` `1000000` is a cumulative bound or a chance of its
own, is not in the client data.
