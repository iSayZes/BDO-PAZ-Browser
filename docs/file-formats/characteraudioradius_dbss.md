# `characteraudioradius.dbss` Format

## Purpose

The sound radius of a few characters whose sounds carry further than usual: world bosses (Khan, Vell, Erebjork, Moghulis, Org, the Wilderness Golem), weather actors (Sandstorm, Snowstorm), Lekrashan and a tutorial character. Each row is a character key and its radius. `characteraudioradiusoffset.dbss` indexes the rows by character key.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------------ | --------- |
| 1      | 1485 and later | 3474    | `characteraudioradius.dbss`       | 166   | 27 Row       | 6         |
| 1      | 1485 and later | 3474    | `characteraudioradiusoffset.dbss` | 290   | 27 Index Row | 10        |

| Layout | File                              | Known          | Unknown    |
| ------ | --------------------------------- | -------------- | ---------- |
| 1      | `characteraudioradius.dbss`       | 166 B (100.0%) | 0 B (0.0%) |
| 1      | `characteraudioradiusoffset.dbss` | 290 B (100.0%) | 0 B (0.0%) |

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

| File                              | Required | Role                                                                 |
| --------------------------------- | -------- | -------------------------------------------------------------------- |
| `characteraudioradiusoffset.dbss` | Optional | Maps `character_key` to its row; the main file can be walked without it |
| `characterstaticoffset.dbss`      | Optional | Tells which keys have a [`characterstatic.dbss`](characterstatic_dbss.md) row, for the key link |
| `languagedata_en.loc`             | Optional | Character names (LOC type 6)                                         |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (6 bytes)

| Offset  | Type | Field         | Notes                                                                 |
| ------- | ---- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | character_key | Character key; unique, and every key has a `characterstatic.dbss` row (client 3474) |
| `+0x02` | f32  | sound_radius  | Distance the character's sounds carry; whole numbers from `8,000` to `100,000` (client 3474) |

### `characteraudioradiusoffset.dbss`

| Offset              | Type               | Field          | Notes                                                |
| ------------------- | ------------------ | -------------- | ---------------------------------------------------- |
| `+0x00`             | char[4]            | magic          | `PABR` (ASCII)                                       |
| `+0x04`             | u32                | count          | Number of index rows; equals the main file's `count` |
| `+0x08`             | Index Row[count]   | records        | See Index Row                                        |
| `records+0x00`      | String Table       | string_table   | The 12-byte trailer starts here; see String Table    |
| `string_table+0x00` | u32                | end_of_records | Byte offset of the end of `records` in this file     |
| `string_table+0x04` | u32                | zero           | Always `0`                                           |

### Index Row (10 bytes)

| Offset  | Type | Field         | Notes                                                        |
| ------- | ---- | ------------- | ------------------------------------------------------------ |
| `+0x00` | u16  | character_key | Equals the row's own `character_key`                         |
| `+0x02` | u32  | offset        | Byte offset of the row in `characteraudioradius.dbss`, at its `character_key` |
| `+0x06` | u32  | size          | Row byte count; always `6`                                   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Field Names

The names come from the `Monster_SoundRadius` sheet of a private server's `DataSheets.bexcel` on client 1784, columns `CharacterKey` and `SoundRadius`. The sheet's third column, `ContentsGroupKey`, is not in the file. Of the sheet's 12 rows, 11 are in the client 3474 file and all 11 match `sound_radius`. The 12th, Lekrashan `29779` (`8,000`, contents group `705`), is missing from both the client 1784 and the client 3474 file.

## Notes

- The main file stores the rows in a different order than the index; neither is sorted by key.
- Client 1784 holds 11 rows, client 3474 holds 27. The 16 added keys are four each of Moghulis (`29697` to `29700`), Org (`29693` to `29696`) and Wilderness Golem (`28628` to `28630`, `29692`), then Baby Vell (`21060`), Snowstorm (`23469`), Tripped Safeguard (`24688`) and `Tutorial_Illezra_Move` (`411`). The 11 shared keys have the same `sound_radius` in both clients.
- On client 3474 three rows set less than `100,000`: Lekrashan `21477` (`8,000`), Snowstorm `23469` (`10,000`) and Tripped Safeguard `24688` (`15,000`). The other 24 set `100,000`.

## Open Questions

### Radius Unit and Default

`sound_radius` is probably in centimetres, the unit of world positions, which makes `100,000` one kilometre. Neither the unit nor the radius a character without a row gets is in the file; the client code that reads the table would answer both.
