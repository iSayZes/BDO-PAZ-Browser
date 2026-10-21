# `yachtdicepreset.dbss` Format

## Purpose

The dice presets of Yar!: each row is one preset, the five
[`yachtdice.dbss`](yachtdice_dbss.md) dice a player rolls.
[`yachtnpcdiceinfo.bss`](yachtnpcdiceinfo_bss.md) gives each NPC game one
preset by key. `yachtdicepresetoffset.dbss` is the index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | ------------- | --------- |
| 1      | 1784 and later | 3474    | `yachtdicepreset.dbss`       | 872   | 31 Row        | 28        |
| 1      | 1784 and later | 3474    | `yachtdicepresetoffset.dbss` | 376   | 31 Offset Row | 12        |

| Layout | File                         | Known          | Unknown    |
| ------ | ---------------------------- | -------------- | ---------- |
| 1      | `yachtdicepreset.dbss`       | 872 B (100.0%) | 0 B (0.0%) |
| 1      | `yachtdicepresetoffset.dbss` | 376 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                                     |
| ---------------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `yachtdicepresetoffset.dbss` | Optional | `key -> (data_offset, data_size)` of every row; the rows have one fixed size and can be walked without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `31` on client 3474          |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (28 bytes)

| Offset  | Type   | Field               | Notes                                                      |
| ------- | ------ | ------------------- | ---------------------------------------------------------- |
| `+0x00` | u32    | dice_preset_key     | Preset key; unique per row                                 |
| `+0x04` | u32    | dice_preset_key_dup | Equal to `dice_preset_key` in every row; the offset file points here |
| `+0x08` | u32[5] | dice_keys           | Keys of `yachtdice.dbss`, one per die, in sheet order      |

The rows run from key 15 down to 1, then from 31 down to 16 (clients 1784
and 3474).

### `yachtdicepresetoffset.dbss`

| Offset  | Type              | Field | Notes                                   |
| ------- | ----------------- | ----- | --------------------------------------- |
| `+0x00` | u32               | count | Equals the `yachtdicepreset.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row    |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u32  | key         | Key of the row it points at                              |
| `+0x04` | u32  | data_offset | Row start + 4, at `dice_preset_key_dup`                  |
| `+0x08` | u32  | data_size   | The row without its leading key: `24`                    |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in file order, and every index row points at the row with
its key (clients 1784 and 3474).

## Presets

On client 3474 presets 1 to 24 each hold one die of a single symbol (dice
1 to 4), one die of mixed symbols (dice 6 to 11) and three odd or even dice
(12 to 15). Preset 25 holds the mixed dice 6 to 10, 26 the dice 1 to 5,
and 27 to 31 mixes of the others. The NPC games of `yachtnpcdiceinfo.bss`
use presets 1, 25, 26 and 31.

## Field Names

The `DicePreset` sheet of a private server's `datasheet_minigame.xlsm` on
client 1784 has the columns `PresetIndex` (`dice_preset_key`) and
`DiceList` (`dice_keys`, one comma-separated list). Its 31 rows match the
31 rows of clients 1784 and 3474, dice order included. The note column
`#참고` names each preset by its symbol, eye and odd or even dice
(`해,1,홀수`: sun, 1, odd). The file writes the key twice: once as the
index key, once inside the row.

## Notes

- Clients 1784 and 3474 ship the same `yachtdicepreset.dbss` and
  `yachtdicepresetoffset.dbss`, byte for byte.
