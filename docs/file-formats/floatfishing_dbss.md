# `floatfishing.dbss` Format

## Purpose

The fish drop groups of the fishing points that float on open water (the
`Fishing Point` and `Clearwater Fishing Point` characters that
[`floatfishingpoint.dbss`](floatfishingpoint_dbss.md) spawns). Each row is
one fishing group: five drop slots (treasure, rare, large, general, junk),
each an item drop group and its chance. Companion `floatfishingoffset.dbss`
lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ------ | -------------- | --------- |
| 2      | 3002 and later | 3474    | `floatfishing.dbss`       | 29,264 | 418 Row        | 70        |
| 2      | 3002 and later | 3474    | `floatfishingoffset.dbss` | 4,184  | 418 Offset Row | 10        |
| 1      | 1485 to 2519   | 2519    | `floatfishing.dbss`       | 25,084 | 418 Row        | 60        |
| 1      | 1485 to 2519   | 2519    | `floatfishingoffset.dbss` | 4,184  | 418 Offset Row | 10        |

| Layout | File                      | Known            | Unknown          |
| ------ | ------------------------- | ---------------- | ---------------- |
| 2      | `floatfishing.dbss`       | 17,560 B (60.0%) | 11,704 B (40.0%) |
| 2      | `floatfishingoffset.dbss` | 4,184 B (100.0%) | 0 B (0.0%)       |
| 1      | `floatfishing.dbss`       | 13,380 B (53.3%) | 11,704 B (46.7%) |
| 1      | `floatfishingoffset.dbss` | 4,184 B (100.0%) | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                                                   |
| ------------------------- | -------- | -------------------------------------------------------------------------------------- |
| `floatfishingoffset.dbss` | Optional | `fishing_group_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `floatfishingpoint.dbss`  | Optional | The fishing points that use each group, for the Points column                          |

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A row count, then 70-byte rows; the
file ends after the last row.

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 418 x 70 = 29,264 bytes.

### Row (70 bytes)

| Offset  | Type      | Field             | Notes                                                                                     |
| ------- | --------- | ----------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16       | fishing_group_key | Unique; the `fishing_group_key` of a [`floatfishingpoint.dbss`](floatfishingpoint_dbss.md) row points here |
| `+0x02` | bytes[28] | unknown_02        | `0` on every row of clients 1784 and 3474; see Open Questions                             |
| `+0x1E` | u32[5]    | drop_ids          | Item drop group per slot, see Drop Slots; `0` for an empty slot                           |
| `+0x32` | u32[5]    | drop_rates        | Chance of each slot on the 1,000,000 = 100% scale; `0` for an empty slot                  |

The rows are not sorted by key; the file starts with `239`, `238`, `237`.

### `floatfishingoffset.dbss`

Bare offset table into `floatfishing.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                  |
| ------- | ----------------- | ----- | -------------------------------------- |
| `+0x00` | u32               | count | Equals the `floatfishing.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                         |

### Offset Row (10 bytes)

| Offset  | Type | Field             | Notes                                                            |
| ------- | ---- | ----------------- | ---------------------------------------------------------------- |
| `+0x00` | u16  | fishing_group_key | Key of the row it points at                                      |
| `+0x02` | u32  | data_offset       | Absolute offset of the row in `floatfishing.dbss`, at its key    |
| `+0x06` | u32  | data_size         | `70` on every row: the whole row                                 |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in file order, and on clients 1784 and 3474 every one points at
the row with its key.

## Layout 1

### Row (60 bytes)

The drop groups are u16; every other field is as in Layout 2.

| Offset  | Type      | Field             | Notes                                       |
| ------- | --------- | ----------------- | ------------------------------------------- |
| `+0x00` | u16       | fishing_group_key |                                             |
| `+0x02` | bytes[28] | unknown_02        |                                             |
| `+0x1E` | u16[5]    | drop_ids          |                                             |
| `+0x28` | u32[5]    | drop_rates        |                                             |

On client 1784 the file is 4 + 410 x 60 = 24,604 bytes, and the offset rows
give `60` as the size.

## Drop Slots

The slot names are the developer comments (`<주석>` row) of the
`FloatFishing_Table` sheet in a private server's `datasheet_regiondatatable.xlsm`
on client 1784.

| Slot | `drop_ids` / `drop_rates` index | Sheet columns          | Comment          |
| ---- | ------------------------------- | ---------------------- | ---------------- |
| 1    | 0                               | `DropID1`, `DropRate1` | Treasure (`보물`) |
| 2    | 1                               | `DropID2`, `DropRate2` | Rare (`희귀`)     |
| 3    | 2                               | `DropID3`, `DropRate3` | Large (`대형`)    |
| 4    | 3                               | `DropID4`, `DropRate4` | General (`일반`)  |
| 5    | 4                               | `DropID5`, `DropRate5` | Junk (`잡템`)     |

On clients 1784 and 3474 every row fills slot 2 only, with rate
`1000000`. Client 3474 uses 20 drop groups there, `10916` to `10950`;
`10936` sits on 74 rows, `10935` on 44 and `10940` on 36. None of them is a
`group_id` of [`itemmaingroup.bss`](itemmaingroup_bss.md) or a subgroup of
`itemsubgroup.dbss`, so the client files do not say which fish they hold.

## Field Names

The `FloatFishing_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `FishingGroupKey`, `DropRate1`, `DropID1` to
`DropRate5`, `DropID5`, `MinWaitTime`, `MaxWaitTime`, `PointRemainTime`,
`MinFishCount`, `MaxFishCount`, `AvailableFishingLevel`,
`ObserveFishingLevel` and `ContentsGroupKey`. Its 410 rows match the 410
rows of client 1784 on the key, all five `DropID` values and `DropRate2`
(410 of 410). The sheet holds `100` in the empty slots' `DropRate`
columns; the client file holds `0` there.

## Notes

- Client 3474 holds the 410 groups of client 1784 unchanged and adds groups
  `440` to `447`.
- 16 groups have no fishing point in `floatfishingpoint.dbss` on client
  3474: `432` to `439`, the eight sheet rows with `ContentsGroupKey` `1633`
  whose points the client file leaves out, and the new `440` to `447`.
- The sheet's `ContentsGroupKey` column is not in the client file.

## Open Questions

### unknown_02

28 bytes that are `0` on every row of clients 1784 and 3474. The sheet
columns `MinWaitTime`, `MaxWaitTime`, `PointRemainTime`, `MinFishCount`,
`MaxFishCount`, `AvailableFishingLevel` and `ObserveFishingLevel` carry the
`%` (server-only) prefix in `datasheet_regiondatatable.xlsm` and are not
`0` there (`80830`, `110830`, `1282211`, `1`, `1`, `11`, `21` on group 1),
so a client build writes them as `0`. Seven u32 fill 28 bytes, but with
only zeros the order and widths cannot be read from the file.
