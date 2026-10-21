# `yachtbasecard.dbss` Format

## Purpose

The cards on the faces of the Yar! dice: each row is one card, its symbol,
its eye value (`1` to `6`) and the `UI_Artwork` picture the card shows.
[`yachtdice.dbss`](yachtdice_dbss.md) lists six cards per die.
`yachtbasecardoffset.dbss` is the index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ----- | ------------- | --------- |
| 1      | 1784 and later | 3474    | `yachtbasecard.dbss`       | 1,924 | 30 Row        | 64        |
| 1      | 1784 and later | 3474    | `yachtbasecardoffset.dbss` | 364   | 30 Offset Row | 12        |

| Layout | File                       | Known            | Unknown    |
| ------ | -------------------------- | ---------------- | ---------- |
| 1      | `yachtbasecard.dbss`       | 1,924 B (100.0%) | 0 B (0.0%) |
| 1      | `yachtbasecardoffset.dbss` | 364 B (100.0%)   | 0 B (0.0%) |

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

| File                       | Required | Role                                                                     |
| -------------------------- | -------- | ------------------------------------------------------------------------ |
| `yachtbasecardoffset.dbss` | Optional | `key -> (data_offset, data_size)` of every row; the rows can be walked without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `30` on client 3474          |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 18 bytes + image path)

| Offset  | Type  | Field        | Notes                                                        |
| ------- | ----- | ------------ | ------------------------------------------------------------ |
| `+0x00` | u32   | card_key     | Card key; unique per row                                     |
| `+0x04` | u32   | card_key_dup | Equal to `card_key` in every row; the offset file points here |
| `+0x08` | u8    | symbol       | Card symbol, `1` to `4`; see Symbols                         |
| `+0x09` | u8    | eye          | Eye value, `1` to `6`                                        |
| `+0x0A` | str16 | image_path   | Picture path under `ui_texture/` (`UI_Artwork/IC_00015.dds`) |

The rows run from key 15 down to 1, then from 30 down to 16 (clients 1784
and 3474).

### `yachtbasecardoffset.dbss`

| Offset  | Type              | Field | Notes                                 |
| ------- | ----------------- | ----- | ------------------------------------- |
| `+0x00` | u32               | count | Equals the `yachtbasecard.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row  |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u32  | key         | Key of the row it points at                              |
| `+0x04` | u32  | data_offset | Row start + 4, at `card_key_dup`                         |
| `+0x08` | u32  | data_size   | The row without its leading key: `60` on client 3474     |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in file order, and every index row points at the row with
its key (clients 1784 and 3474).

## Symbols

The `#참조` sheet of a private server's `datasheet_minigame.xlsm` on client
1784 names the symbols in its note on the `Symbol` column: `1` sun (`해`),
`2` moon (`달`), `3` star (`별`), `4` flower (`꽃`). The live match window
draws the eye on a card texture named after a suit instead,
`UI_Artwork/Card/Card_<suit>_<eye>.dds` with `Space`, `Diamonds`, `Heart`
and `Clover` (`_symbolString` in `panel_window_minigame_yachtdice.luac`,
keyed by the `__eYachtSymbol_*` enum, whose values the Lua does not show).

On client 3474 cards 1 to 24 hold every symbol with every eye (symbol 1
on cards 1 to 6, 2 on 7 to 12, 3 on 13 to 18, 4 on 19 to 24). Cards 25 to
30 repeat six of those pairs with other pictures: `1`/`1`, `2`/`2`,
`3`/`3`, `4`/`4`, `1`/`5` and `2`/`6`.

## Field Names

The `BaseCardList` sheet of a private server's `datasheet_minigame.xlsm` on
client 1784 has the columns `DicecardIndex` (`card_key`), `Symbol`
(`symbol`), `Eye` (`eye`) and `Image` (`image_path`). Its 30 rows match the
30 rows of clients 1784 and 3474 in every column. The file writes the key
twice: once as the index key, once inside the row.

## Notes

- Clients 1784 and 3474 ship the same `yachtbasecard.dbss` and
  `yachtbasecardoffset.dbss`, byte for byte.
- Every `image_path` on client 3474 is a knowledge picture
  (`UI_Artwork/IC_000NN.dds`); the match window draws it on the card as
  `stc_knowledgeImage` through `getCardTextureName()` of
  `ToClient_getYachtDiceCardWrapper()`. Cards 13 and 19 use `IC_00032` and
  `IC_00034` where the key would give `IC_00013` and `IC_00019`.
