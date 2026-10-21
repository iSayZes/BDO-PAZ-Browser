# `yachtdice.dbss` Format

## Purpose

The dice of Yar!: each row is one die, the six
[`yachtbasecard.dbss`](yachtbasecard_dbss.md) cards on its faces. A roll
shows one face, so a die decides which cards a player can draw.
[`yachtdicepreset.dbss`](yachtdicepreset_dbss.md) groups five dice into a
preset. `yachtdiceoffset.dbss` is the index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ------------- | --------- |
| 1      | 1784 and later | 3474    | `yachtdice.dbss`       | 484   | 15 Row        | 32        |
| 1      | 1784 and later | 3474    | `yachtdiceoffset.dbss` | 184   | 15 Offset Row | 12        |

| Layout | File                   | Known          | Unknown    |
| ------ | ---------------------- | -------------- | ---------- |
| 1      | `yachtdice.dbss`       | 484 B (100.0%) | 0 B (0.0%) |
| 1      | `yachtdiceoffset.dbss` | 184 B (100.0%) | 0 B (0.0%) |

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

| File                  | Required | Role                                                                                     |
| --------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `yachtdiceoffset.dbss` | Optional | `key -> (data_offset, data_size)` of every row; the rows have one fixed size and can be walked without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `15` on client 3474          |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (32 bytes)

| Offset  | Type   | Field        | Notes                                                       |
| ------- | ------ | ------------ | ----------------------------------------------------------- |
| `+0x00` | u32    | dice_key     | Dice key; unique per row                                    |
| `+0x04` | u32    | dice_key_dup | Equal to `dice_key` in every row; the offset file points here |
| `+0x08` | u32[6] | card_keys    | Keys of `yachtbasecard.dbss`, one per face, in sheet order  |

The rows run from key 15 down to 1 (clients 1784 and 3474).

### `yachtdiceoffset.dbss`

| Offset  | Type              | Field | Notes                                 |
| ------- | ----------------- | ----- | ------------------------------------- |
| `+0x00` | u32               | count | Equals the `yachtdice.dbss` count     |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row  |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                          |
| ------- | ---- | ----------- | ---------------------------------------------- |
| `+0x00` | u32  | key         | Key of the row it points at                    |
| `+0x04` | u32  | data_offset | Row start + 4, at `dice_key_dup`               |
| `+0x08` | u32  | data_size   | The row without its leading key: `28`          |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in file order, and every index row points at the row with
its key (clients 1784 and 3474).

## Dice

On client 3474 dice 1 to 4 each carry the six cards of one symbol (eyes 1
to 6), die 5 the six cards `25` to `30`, dice 6 to 11 one card of each
symbol and dice 12 to 15 the odd or even eyes of two symbols.

| Dice    | Cards                                   |
| ------- | --------------------------------------- |
| 1 to 4  | Symbol 1 to 4, eyes 1 to 6              |
| 5       | `25` to `30`                            |
| 6 to 11 | Mixed: `1, 7, 13, 19, 25, 26` for die 6 |
| 12, 14  | Odd (12) or even (14) eyes of symbols 1 and 2 |
| 13, 15  | Odd (13) or even (15) eyes of symbols 3 and 4 |

## Field Names

The `DiceList` sheet of a private server's `datasheet_minigame.xlsm` on
client 1784 has the columns `DiceIndex` (`dice_key`) and `DiceCardIndex`
(`card_keys`, one comma-separated list). Its 15 rows match the 15 rows of
clients 1784 and 3474, card order included. The note column `#주사위 참고`
names dice 1 to 4 after their symbol (`해 특화`: sun only) and die 5
`ETC..`. The file writes the key twice: once as the index key, once inside
the row.

## Notes

- Clients 1784 and 3474 ship the same `yachtdice.dbss` and
  `yachtdiceoffset.dbss`, byte for byte.
- The match window reads a die through `ToClient_getYachtDiceWrapper()`
  (`getCurrentFaceIndex()`, `isKeep()`) and the card on its face through
  `ToClient_getYachtDiceCardWrapper(index, faceIndex, isMyTurn)`
  (`panel_window_minigame_yachtdice_1.luac`).
