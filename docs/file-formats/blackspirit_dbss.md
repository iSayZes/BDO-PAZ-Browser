# `blackspirit.dbss` Format

## Purpose

The Black Spirit forms (looks) a character can pick at the Black Spirit's
skin select window, and the condition script that unlocks each: one row per
form, a u8 index and a UTF-16 condition. Form `0` has no condition; the
others ask for cleared quests (`clearQuest(122,5);`) or a level
(`getLevel()>92;`), with `<or>` between alternatives. On client 3482 the
file holds 15 forms, `0` to `7` and `10` to `16` (10 on client 1784).
Companion `blackspiritoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records       | Row bytes                |
| ------ | -------------- | ------- | ------------------------ | ----- | ------------- | ------------------------ |
| 1      | 1348 and later | 3482    | `blackspirit.dbss`       | 2,971 | 15 Row        | 9 to 693, 198 on average |
| 1      | 1348 and later | 3482    | `blackspiritoffset.dbss` | 139   | 15 Offset Row | 9                        |

| Layout | File                     | Known            | Unknown    |
| ------ | ------------------------ | ---------------- | ---------- |
| 1      | `blackspirit.dbss`       | 2,971 B (100.0%) | 0 B (0.0%) |
| 1      | `blackspiritoffset.dbss` | 139 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                                                                 |
| ------------------------ | -------- | ------------------------------------------------------------------------------------ |
| `blackspiritoffset.dbss` | Optional | `index -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 9 bytes + condition text)

| Offset  | Type  | Field     | Notes                                                                    |
| ------- | ----- | --------- | ------------------------------------------------------------------------ |
| `+0x00` | u8    | index     | Row key: the form, as `ToClient_getBlackSpiritFromInfoByIndex()` returns it |
| `+0x01` | str16 | condition | Unlock condition script; empty for form `0`                               |

The rows are in no key order; client 3482 opens with 15, 14, 13 and ends
with 0 and 16.

### `blackspiritoffset.dbss`

Bare offset table into `blackspirit.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                               |
| ------- | ----------------- | ----- | ----------------------------------- |
| `+0x00` | u32               | count | Equals the `blackspirit.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                      |

### Offset Row (9 bytes)

| Offset  | Type | Field       | Notes                                              |
| ------- | ---- | ----------- | -------------------------------------------------- |
| `+0x00` | u8   | index       | Key of the row it points at                        |
| `+0x01` | u32  | data_offset | Absolute offset of the row in `blackspirit.dbss`, at `index` |
| `+0x05` | u32  | data_size   | The whole row: 9 + 2 x the condition length        |

Read by `parse_bare_u8_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in file order; on clients 1784 and 3482 every index row points at
the row whose `index` is its key.

## Field Names

The `BlackSpirit_InfoTable` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `Index` and `Condition`, 10 rows.

| Field     | Column      | Same value (client 1784) |
| --------- | ----------- | ------------------------ |
| index     | `Index`     | 10 of 10                 |
| condition | `Condition` | 6 of 10                  |

The four conditions that differ (forms `2`, `3`, `4` and `7`) end with one
more `<or>clearquest(40022,N);` alternative in the client file, which the
private server's sheet leaves out. The 2016 client's debug symbols have no
struct for the table; the server dump of client 1784 names its loader
`BlackSpiritStaticStatusManager`.

## Notes

- `panel_widget_blackspirit_skillselect.luac` (client 3482) walks the forms
  with `ToClient_getBlackSpiritFromInfoList()` (the count of unlocked forms)
  and `ToClient_getBlackSpiritFromInfoByIndex(i)` (the form index), marks
  the one equal to `ToClient_getCurrentFormIndex()` as applied, and sets a
  new one with `ToClient_setCurrentFormIndex(index)`. Its `_texUV` table
  cuts a portrait out of `renewal/pcremaster/remaster_blackspirit_00.dds`
  for forms `0` to `4`, `10` and `11` only; the window hides any other form.
- [`blackspiritchangeformcondition.bss`](blackspiritchangeformcondition_bss.md)
  holds the condition to open the form change at all.
- On client 3482 forms `13` to `15` count three quests: chain `9102` quest
  35 or 37, chain `9104` quest 29 and chain `9105` quest 29. Form `13` needs exactly one of them
  cleared, form `14` exactly two (`!clearQuest(...)` rules out the third)
  and form `15` all three.
