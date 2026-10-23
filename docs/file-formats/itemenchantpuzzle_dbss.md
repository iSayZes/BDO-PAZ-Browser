# `itemenchantpuzzle.dbss` Format

## Purpose

The inventory puzzles of [`itempuzzle.dbss`](itempuzzle_dbss.md) listed by
their first piece: per item the puzzle keys whose
`start_puzzle_item_key` it is. Puzzle `1` lays items `40001` to `40003` in
a row and starts with `40001` (Ancient Pottery Fragment), so that item's
record lists puzzle `1`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records    | Row bytes               |
| ------ | -------------- | ------- | ------------------------ | ----- | ---------- | ----------------------- |
| 1      | 2203 and later | 3482    | `itemenchantpuzzle.dbss` | 4,184 | 284 Record | 14 to 40, 15 on average |

| Layout | File                     | Known            | Unknown    |
| ------ | ------------------------ | ---------------- | ---------- |
| 1      | `itemenchantpuzzle.dbss` | 4,184 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3454   | Layout 1 |
| 3412   | Layout 1 |
| 3381   | Layout 1 |
| 3349   | Layout 1 |
| 3314   | Layout 1 |
| 3283   | Layout 1 |
| 3251   | Layout 1 |
| 3212   | Layout 1 |
| 3177   | Layout 1 |
| 3144   | Layout 1 |
| 3103   | Layout 1 |
| 3062   | Layout 1 |
| 3037   | Layout 1 |
| 3002   | Layout 1 |
| 2959   | Layout 1 |
| 2923   | Layout 1 |
| 2900   | Layout 1 |
| 2872   | Layout 1 |
| 2834   | Layout 1 |
| 2803   | Layout 1 |
| 2765   | Layout 1 |
| 2736   | Layout 1 |
| 2703   | Layout 1 |
| 2665   | Layout 1 |
| 2637   | Layout 1 |
| 2606   | Layout 1 |
| 2583   | Layout 1 |
| 2545   | Layout 1 |
| 2519   | Layout 1 |
| 2498   | Layout 1 |
| 2468   | Layout 1 |
| 2438   | Layout 1 |
| 2414   | Layout 1 |
| 2384   | Layout 1 |
| 2358   | Layout 1 |
| 2335   | Layout 1 |
| 2313   | Layout 1 |
| 2290   | Layout 1 |
| 2250   | Layout 1 |
| 2224   | Layout 1 |
| 2203   | Layout 1 |
| 2179   | No file  |
| 2151   | No file  |
| 2134   | No file  |
| 2107   | No file  |
| 2073   | No file  |
| 2052   | No file  |
| 2011   | No file  |
| 1996   | No file  |
| 1969   | No file  |
| 1937   | No file  |
| 1914   | No file  |
| 1886   | No file  |
| 1866   | No file  |
| 1838   | No file  |
| 1818   | No file  |
| 1794   | No file  |
| 1784   | No file  |
| 1749   | No file  |
| 1717   | No file  |
| 1698   | No file  |
| 1674   | No file  |
| 1636   | No file  |
| 1608   | No file  |
| 1587   | No file  |
| 1565   | No file  |
| 1537   | No file  |
| 1509   | No file  |
| 1485   | No file  |
| 1466   | No file  |
| 1445   | No file  |
| 1426   | No file  |
| 1409   | No file  |
| 1390   | No file  |
| 1372   | No file  |
| 1360   | No file  |
| 1348   | No file  |
| 1338   | No file  |
| 1324   | No file  |
| 1316   | No file  |
| 1309   | No file  |
| 1286   | No file  |
| 1256   | No file  |
| 1230   | No file  |
| 1211   | No file  |
| 1194   | No file  |
| 1177   | No file  |
| 1156   | No file  |
| 1127   | No file  |
| 1109   | No file  |
| 1076   | No file  |
| 1058   | No file  |
| 1016   | No file  |
| 990    | No file  |
| 955    | No file  |
| 911    | No file  |
| 885    | No file  |
| 855    | No file  |
| 822    | No file  |
| 794    | No file  |
| 748    | No file  |
| 711    | No file  |
| 683    | No file  |
| 656    | No file  |
| 630    | No file  |
| 606    | No file  |
| 577    | No file  |
| 542    | No file  |
| 526    | No file  |
| 508    | No file  |
| 485    | No file  |
| 457    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0) |

The puzzle keys link to their `itempuzzle.dbss` rows; the handler reads no
other file. All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                 | Field        | Notes                                                  |
| ------- | -------------------- | ------------ | ------------------------------------------------------ |
| `+0x00` | u32                  | record_count | Number of records; no offset index, no PABR magic      |
| `+0x04` | Record[record_count] | records      | See Record; in no item order                           |

### Record (variable: 12 bytes + puzzle keys)

| Offset  | Type                   | Field                 | Notes                                                                          |
| ------- | ---------------------- | --------------------- | ------------------------------------------------------------------------------ |
| `+0x00` | u32                    | start_puzzle_item_key | The first piece, a packed item key; level `0` and unique on client 3482          |
| `+0x04` | u64                    | puzzle_key_count      | Number of `puzzle_keys`; `1` to `14` on client 3482                              |
| `+0x0C` | u16[puzzle_key_count]  | puzzle_keys           | `itempuzzle.dbss` `puzzle_key`s; not sorted within a record                      |

## Field Names

On client 3482 every one of the 386 `itempuzzle.dbss` puzzles is in exactly
one record, and in all 386 the puzzle's `start_puzzle_item_key` is the
record's item. The field names follow that file. The 2016 client's PDB has
no `ItemEnchantPuzzle` type, and the `ItemPuzzle_Table` sheet of a private
server's `DataSheets.bexcel` on client 1784 has no column for the list.

## Notes

- Client 3482 has 284 records: 252 with one puzzle, the rest with 2 to 14.
- Items that are a piece but never the first piece have no record: 684
  items lie in a puzzle grid on client 3482, 284 of them first.
- The file is not in the client 1784 PAZ.
- The handler (`_dbss/itemenchantpuzzle/`) shows one row per item with its
  puzzle keys, each a link to its `itempuzzle.dbss` row.
