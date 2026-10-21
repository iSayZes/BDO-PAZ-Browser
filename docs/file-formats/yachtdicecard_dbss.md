# `yachtdicecard.dbss` Format

## Purpose

A second Yar! card list: each row is one card with a symbol and an eye
value from `1` to `10`, and no picture. Unlike the
[`yachtbasecard.dbss`](yachtbasecard_dbss.md) cards, no other Yar! table
names these keys. `yachtdicecardoffset.dbss` is the index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ----- | ------------- | --------- |
| 1      | 1784 and later | 3474    | `yachtdicecard.dbss`       | 404   | 40 Row        | 10        |
| 1      | 1784 and later | 3474    | `yachtdicecardoffset.dbss` | 484   | 40 Offset Row | 12        |

| Layout | File                       | Known          | Unknown    |
| ------ | -------------------------- | -------------- | ---------- |
| 1      | `yachtdicecard.dbss`       | 404 B (100.0%) | 0 B (0.0%) |
| 1      | `yachtdicecardoffset.dbss` | 484 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                       | Required | Role                                                                                     |
| -------------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `yachtdicecardoffset.dbss` | Optional | `key -> (data_offset, data_size)` of every row; the rows have one fixed size and can be walked without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `40` on client 3474          |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (10 bytes)

| Offset  | Type | Field        | Notes                                                         |
| ------- | ---- | ------------ | ------------------------------------------------------------- |
| `+0x00` | u32  | card_key     | Card key; unique per row                                      |
| `+0x04` | u32  | card_key_dup | Equal to `card_key` in every row; the offset file points here |
| `+0x08` | u8   | symbol       | Card symbol, `1` to `4`, as in `yachtbasecard.dbss`           |
| `+0x09` | u8   | eye          | Eye value, `1` to `10`                                        |

On client 3474 the 40 rows hold keys 31 to 70: symbol 1 with eyes 1 to 10
on keys 31 to 40, symbol 2 on 41 to 50, 3 on 51 to 60 and 4 on 61 to 70.
The rows are not in key order: keys 70 down to 64, 47 down to 32, 63
down to 48, then 31 (clients 1784 and 3474).

### `yachtdicecardoffset.dbss`

| Offset  | Type              | Field | Notes                                 |
| ------- | ----------------- | ----- | ------------------------------------- |
| `+0x00` | u32               | count | Equals the `yachtdicecard.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row  |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                          |
| ------- | ---- | ----------- | ---------------------------------------------- |
| `+0x00` | u32  | key         | Key of the row it points at                    |
| `+0x04` | u32  | data_offset | Row start + 4, at `card_key_dup`               |
| `+0x08` | u32  | data_size   | The row without its leading key: `6`           |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in file order, and every index row points at the row with
its key (clients 1784 and 3474).

## Field Names

The `DiceCardList` sheet of a private server's `datasheet_minigame.xlsm` on
client 1784 has the columns `DicecardIndex` (`card_key`), `Symbol`
(`symbol`) and `Eye` (`eye`). Its 40 rows match the 40 rows of clients 1784
and 3474 in every column. The file writes the key twice: once as the index
key, once inside the row.

## Notes

- Clients 1784 and 3474 ship the same `yachtdicecard.dbss` and
  `yachtdicecardoffset.dbss`, byte for byte.
- `yachtdice.dbss` lists only cards 1 to 30, and the `#참조` sheet of the
  same workbook has no note for `DiceCardList`.

## Open Questions

### What Reads These Cards

No client table names keys 31 to 70: `yachtdice.dbss` lists the
`yachtbasecard.dbss` keys 1 to 30, and the client Lua reads cards only
through the dice (`ToClient_getYachtDiceCardWrapper(index, faceIndex,
isMyTurn)`). The eyes `7` to `10` fit no hand rank of `yachthandrank.bss`,
whose eye checks stop at `6`. Whether the server deals these cards in some
mode, or the list is unused, is open.
