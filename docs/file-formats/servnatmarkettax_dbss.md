# `servnatmarkettax.dbss` Format

## Purpose

The Horse Market silver bonus per Training level: one row per level from
`1` with the extra share of silver a player collects from the Horse and
Breeding Markets. The character window shows it in the Training tooltip
("+{rate3}% Silver collection when using the Horse or Breeding Markets"),
the stable market in its discount tooltip. The file name is a misspelling
of "servant market tax". Companion `servnatmarkettaxoffset.dbss` lists
where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ----------------------------- | ----- | -------------- | --------- |
| 1      | 1485 and later | 3474    | `servnatmarkettax.dbss`       | 1,444 | 180 Row        | 8         |
| 1      | 1485 and later | 3474    | `servnatmarkettaxoffset.dbss` | 2,164 | 180 Offset Row | 12        |

| Layout | File                          | Known            | Unknown    |
| ------ | ----------------------------- | ---------------- | ---------- |
| 1      | `servnatmarkettax.dbss`       | 1,444 B (100.0%) | 0 B (0.0%) |
| 1      | `servnatmarkettaxoffset.dbss` | 2,164 B (100.0%) | 0 B (0.0%) |

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

| File                          | Required | Role                                                                  |
| ----------------------------- | -------- | --------------------------------------------------------------------- |
| `servnatmarkettaxoffset.dbss` | Optional | `life_level -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`         | Optional | The rank names (Beginner to Guru) for the Rank column, LOC type `37`   |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 180 x 8 = 1,444 bytes.

### Row (8 bytes)

| Offset  | Type | Field                    | Notes                                                                  |
| ------- | ---- | ------------------------ | ---------------------------------------------------------------------- |
| `+0x00` | u32  | life_level               | Training level, the row key; `1` to `count` in order                    |
| `+0x04` | u32  | horse_market_tax_percent | Silver bonus in units of 0.0001%: `10000` is 1%; see Notes              |

### `servnatmarkettaxoffset.dbss`

Bare offset table into `servnatmarkettax.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                    |
| ------- | ----------------- | ----- | ---------------------------------------- |
| `+0x00` | u32               | count | Equals the `servnatmarkettax.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                           |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u32  | life_level  | Key of the row it points at                              |
| `+0x04` | u32  | data_offset | Absolute offset of the row in `servnatmarkettax.dbss`, at `life_level` |
| `+0x08` | u32  | data_size   | `8` on every row: the whole row                          |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in level order, as the file; on clients 1784 and 3474 every
index row points at the row with its key.

## Field Names

The `ServantMarketTax_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `LifeLevel` and `HorseMarketTaxPercent`. Its
note column `#조련 레벨` (Training level) labels each row with the rank
(`초급 Lv.1`, Beginner 1). The 2016 client's debug symbols have no struct
for the table.

| Field                    | Column                  | Same value (client 1784) | Same value (client 3474) |
| ------------------------ | ----------------------- | ------------------------ | ------------------------ |
| life_level               | `LifeLevel`             | 130 of 130               | 130 of 180               |
| horse_market_tax_percent | `HorseMarketTaxPercent` | 130 of 130               | 130 of 130               |

Client 3474 adds levels 131 to 180 and keeps the values of levels 1 to 130.

## Notes

- Two Lua files read the value for the player's own Training level through
  `ToClient_GetServantMarketTaxPercent()` and divide it by `10000`:
  `panel_characterinfo_basic_all_2.luac` fills `{rate3}` of
  `LUA_CHARACTERINFO_LIFE_TRAINING_DESC_2` with one decimal, and
  `panel_dialog_servantmarket_all_2.luac` fills `{rate}` of
  `LUA_STABLEMARKET_DISCOUNT_BTN_TOOLTIP_DESC` ("Current: +{rate}%") under
  `PANEL_STABLEMARKET_DISCOUNT_TOOLTIP_NAME` ("Rates per Training Grade").
- On client 3474 the bonus is `0` for levels 1 to 10 (Beginner), `10000`
  (1%) at level 11 and `300000` (30%) from level 81 (Guru 1) to 180.
- The levels are Training levels: the sheet's note column and the
  character window's Training tooltip both name them so. The ranks follow
  `PaGlobalFunc_Util_CraftLevelReplace` (see
  [`barterlifelevelinfo.bss`](barterlifelevelinfo_bss.md), same row shape).
