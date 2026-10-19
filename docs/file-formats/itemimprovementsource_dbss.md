# `itemimprovementsource.dbss` Format

## Purpose

The reform stones of Gear Reform, see
[`itemimprovement.dbss`](itemimprovement_dbss.md). A record is a stone item
with a stone category and a reform group; the gear records of the same group
are what the stone reforms.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ---------------------------------- | ----- | ------------- | --------- |
| 2      | 3473 and later | 3474    | `itemimprovementsource.dbss`       | 4,246 | 101 Record    | 42        |
| 2      | 3473 and later | 3474    | `itemimprovementsourceoffset.dbss` | 1,216 | 101 Index Row | 12        |
| 1      | 1784           | 1784    | `itemimprovementsource.dbss`       | 3,899 | 95 Record     | 41        |
| 1      | 1784           | 1784    | `itemimprovementsourceoffset.dbss` | 1,144 | 95 Index Row  | 12        |

| Layout | File                               | Known            | Unknown         |
| ------ | ---------------------------------- | ---------------- | --------------- |
| 2      | `itemimprovementsource.dbss`       | 4,246 B (100.0%) | 0 B (0.0%)      |
| 2      | `itemimprovementsourceoffset.dbss` | 1,216 B (100.0%) | 0 B (0.0%)      |
| 1      | `itemimprovementsource.dbss`       | 1,999 B (51.3%)  | 1,900 B (48.7%) |
| 1      | `itemimprovementsourceoffset.dbss` | 1,144 B (100.0%) | 0 B (0.0%)      |

<!-- versions:end -->

## Companion Files

| File                             | Required | Role                                                     |
| -------------------------------- | -------- | -------------------------------------------------------- |
| `itemimprovementsourceoffset.dbss` | Optional | `item_id -> (data_offset, data_size)` index, see below; the handler walks the records without it |

Item names come from LOC type 0 and icons from the `ITEM_ICON` lookup index.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                                |
| ------- | ------------- | ------- | ---------------------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `101` on client 3464              |
| `+0x04` | Record[count] | records | Back to back to the end of the file; see Record      |

### Record (variable: 22 bytes + values)

| Offset            | Type             | Field              | Notes                                                    |
| ----------------- | ---------------- | ------------------ | -------------------------------------------------------- |
| `+0x00`           | u32              | item_id            | The stone; the index's `data_offset` points past it      |
| `+0x04`           | u64              | value_count        | `5` in every record                                      |
| `+0x0C`           | u32[value_count] | results            | `1,000,000` in every slot of every record (client 3474); see Field Names |
| `results+0x00`    | u32              | category           | Gear the stone takes, see below                          |
| `results+0x04`    | u32              | group              | Reform group, `1` to `48`; matches `group` of the gear records |
| `results+0x08`    | u16              | is_default_display | `1` for the 24 stones of [`itemimprovementdefaultdisplaylist.bss`](itemimprovementdefaultdisplaylist_bss.md), else `0` |

Each `(category, group)` pair belongs to one stone (101 pairs, client 3464).

| category | Stones (client 3464)                                                             |
| -------- | -------------------------------------------------------------------------------- |
| `1`      | Weapon stones: Heart of Kutum, Resplendent Boss Weapon Reform Stone I to V, `[Season] Tuvala Main Weapon Conversion Stone` |
| `2`      | Armor stones: Resplendent Boss Armor Reform Stone I to V, `Combatant's Stone (Armor)`, `[Season] Tuvala Helmet Conversion Stone` |
| `3`      | Accessory stones: Cup of Destined Dawn and the other Cups, `[Season] Tuvala Necklace Conversion Stone` |
| `4`      | Blessed Soul Fragment, Exalted Soul Fragment, Crimson Behelit Alchemy Stone Appearance |
| `5`      | Flawless Herald's Crystal                                                        |

### `itemimprovementsourceoffset.dbss`

| Offset  | Type             | Field | Notes                                            |
| ------- | ---------------- | ----- | ------------------------------------------------ |
| `+0x00` | u32              | count | Equals the `itemimprovementsource.dbss` count    |
| `+0x04` | Index Row[count] | rows  | No magic, no trailer; see Index Row              |

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                   |
| ------- | ---- | ----------- | --------------------------------------- |
| `+0x00` | u32  | item_id     | Record key                              |
| `+0x04` | u32  | data_offset | Record start + 4, past `item_id`        |
| `+0x08` | u32  | data_size   | Record size - 4: `38`                   |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`; on client
3464 every row matches the record walked from the start of the file.

## Layout 1

Client 1784 stores `is_default_display` as a u8, so each record is one
byte shorter. Only the Record differs from Layout 2.

### Record (variable: 21 bytes + values)

| Offset            | Type             | Field              | Notes                                       |
| ----------------- | ---------------- | ------------------ | ------------------------------------------- |
| `+0x00`           | u32              | item_id            |                                             |
| `+0x04`           | u64              | value_count        |                                             |
| `+0x0C`           | u32[value_count] | results            |                                             |
| `results+0x00`    | u32              | category           | `1` to `3` on client 1784                   |
| `results+0x04`    | u32              | group              |                                             |
| `results+0x08`    | u8               | is_default_display | `1` on 19 of the 95 records (client 1784)   |

## Field Names

The record is the `Item_ImprovementSource_Table` sheet of a private server
on client 1784. That server's dump (`Instance_dumpFull.exe`) reads the
client file with the row reader at VA `0x140b365e0`: a u64 count and that
many u32 values into a list, then `category`, `group` and
`is_default_display`. Its sheet loader fills the same members:

| Field                | Sheet column                    |
| -------------------- | ------------------------------- |
| `item_id`            | `SourceItemKey`                 |
| `results`            | `result0` to `result4`          |
| `category`           | `equipType`                     |
| `group`              | `Grade`                         |
| `is_default_display` | `SourceItemDisplay`             |

The loader formats the column name `result%d` for `0` to `4` (VA
`0x1408c02f3`), reads each as a u32, skips a value above 1,000,000 (VA
`0x1408c034d`) and appends the rest, so `value_count` is the number of
`result` columns at or under 1,000,000. It accepts `equipType` `1` to `3`
only and a `Grade` above 0.

The private server's own file holds 95 of the sheet's 98 stones; on all 95
the five `results`, `category`, `group` and `is_default_display` equal the
sheet. On that build six stones (`4906` to `4911`) have a `result0` of
10,000, 20,000 or 50,000; client 3474 has `1,000,000` in all 505 slots.

## Notes

- `category` follows from the stone names; the gear side of the match is an
  open question in [`itemimprovement.dbss`](itemimprovement_dbss.md#which-stone-a-record-takes).
- 28 groups (`17` to `32`, `36`, `38` to `48`) have stones but no gear record
  on client 3464.
- `is_default_display` and the default display list hold the same 24 stones;
  the Reform window loads the list through
  `ToClient_GetImprovementSourceItemCount()` and
  `ToClient_GetDefaultDisplayImprovementSourceItemByIndex(index)`
  (`panel_improvement_all_1`).

## Open Questions

### What the Five `results` Do

The server caps each value at 1,000,000, the scale of rates elsewhere
(`buff.dbss` `apply_rate`), and the window text says a higher-grade stone
gives a higher chance of higher-grade gear, but no code in the client 1784
server dump reads the list after loading it. Whether slot `i` pairs with
the `i`-th result item of [`itemimprovement.dbss`](itemimprovement_dbss.md)
is open.
