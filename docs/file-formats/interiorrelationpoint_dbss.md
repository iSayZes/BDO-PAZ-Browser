# `interiorrelationpoint.dbss` Format

## Purpose

Placement points of the house furniture: one 66-byte row per furniture
character with the chair that matches it and a point value for each piece
of furniture it can stand on (dresser, bedside cabinet, table, shelf and
more) and for each free side (front, back, left, right). The matching
character pairs a table with its chair: Melissande Table (`6252`) and
Melissande Dining Table (`6251`) both match Melissande Chair (`6751`).
On client 3482 the file holds 1,140 rows, 966 on client 1784. Companion
`interiorrelationpointoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes  | Records          | Row bytes |
| ------ | -------------- | ------- | ---------------------------------- | ------ | ---------------- | --------- |
| 1      | 1348 and later | 3482    | `interiorrelationpoint.dbss`       | 75,260 | 1,140 Row        | 66        |
| 1      | 1348 and later | 3482    | `interiorrelationpointoffset.dbss` | 11,420 | 1,140 Offset Row | 10        |

| Layout | File                               | Known             | Unknown    |
| ------ | ---------------------------------- | ----------------- | ---------- |
| 1      | `interiorrelationpoint.dbss`       | 75,260 B (100.0%) | 0 B (0.0%) |
| 1      | `interiorrelationpointoffset.dbss` | 11,420 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
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

| File                               | Required | Role                                                                                    |
| ---------------------------------- | -------- | --------------------------------------------------------------------------------------- |
| `interiorrelationpointoffset.dbss` | Optional | `character_key -> data_offset` of every row; the parser walks the main file without it   |
| `characterstaticoffset.dbss`       | Optional | The `characterstatic.dbss` keys, so a key without a row shows as plain text              |
| `languagedata_en.loc`              | Optional | Furniture names, LOC type 6                                                              |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of fixed rows with an empty string table, read by
`fixed_row_offsets()` in `_common/pabr_strings.py`.

| Offset      | Type       | Field        | Notes                                    |
| ----------- | ---------- | ------------ | ---------------------------------------- |
| `+0x00`     | char[4]    | magic        | `PABR`                                   |
| `+0x04`     | u32        | count        | Number of rows; 1,140 on client 3482     |
| `+0x08`     | Row[count] | rows         | See Row                                  |
| `rows+0x00` | u32        | string_count | `0`: the empty PABR string table         |
| `rows+0x04` | u32        | table_start  | End of the rows (`8 + 66 * count`)       |
| `rows+0x08` | u32        | zero         | Always `0`                               |

### Row (66 bytes)

Values on client 3482; a point is `0`, `1`, `2`, `3` or `5`.

| Offset  | Type | Field                    | Notes                                                                    |
| ------- | ---- | ------------------------ | ------------------------------------------------------------------------ |
| `+0x00` | u16  | character_key            | Row key: the furniture installation, a `characterstatic.dbss` character  |
| `+0x02` | u16  | character_key_dup        | Equal to `character_key` on every row; the offset index points here      |
| `+0x04` | u16  | matching_character_key   | The matching chair, a `characterstatic.dbss` key; `0` on 1,016 rows      |
| `+0x06` | i32  | matching_character_point | `0` on every row (clients 1784 and 3482)                                 |
| `+0x0A` | i32  | on_dresser               | Non-zero on 262 rows                                                      |
| `+0x0E` | i32  | on_bed_side_cabinet      | Equal to `on_dresser` on every row                                       |
| `+0x12` | i32  | on_wardrobe              | `0` on every row                                                          |
| `+0x16` | i32  | on_dining_table          | Non-zero on 261 rows                                                      |
| `+0x1A` | i32  | on_table                 | Non-zero on 262 rows                                                      |
| `+0x1E` | i32  | on_chair                 | `0` on every row                                                          |
| `+0x22` | i32  | on_sofa                  | `0` on every row                                                          |
| `+0x26` | i32  | on_bed                   | `0` on every row                                                          |
| `+0x2A` | i32  | on_book_case             | `3` on 17 rows, else `0`                                                 |
| `+0x2E` | i32  | on_shelf                 | Non-zero on 261 rows                                                      |
| `+0x32` | i32  | is_empty_in_front        | Non-zero on 531 rows                                                      |
| `+0x36` | i32  | is_empty_in_back         | `2` on 61 rows, else `0`                                                 |
| `+0x3A` | i32  | is_empty_in_left         | Equal to `is_empty_in_back` on every row                                 |
| `+0x3E` | i32  | is_empty_in_right        | Equal to `is_empty_in_back` on every row                                 |

The rows are in no key order; client 3482 opens with 16111, 16110, 16109.

### `interiorrelationpointoffset.dbss`

The `PABR` index layout of `characterstaticoffset.dbss`, read by
`parse_pabr_offset_rows()` in `_common/pabr_offset.py`.

| Offset      | Type              | Field        | Notes                                         |
| ----------- | ----------------- | ------------ | --------------------------------------------- |
| `+0x00`     | char[4]           | magic        | `PABR`                                        |
| `+0x04`     | u32               | count        | Equals the `interiorrelationpoint.dbss` count |
| `+0x08`     | Offset Row[count] | rows         | See Offset Row                                |
| `rows+0x00` | u32               | string_count | `0`: the empty PABR string table              |
| `rows+0x04` | u32               | table_start  | End of the rows (`8 + 10 * count`)            |
| `rows+0x08` | u32               | zero         | Always `0`                                    |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                     |
| ------- | ---- | ------------- | ----------------------------------------- |
| `+0x00` | u16  | character_key | Key of the row it points at               |
| `+0x02` | u32  | data_offset   | Row start + 2, at `character_key_dup`     |
| `+0x06` | u32  | data_size     | `0` on every row                          |

The index rows are in another order than the file; on clients 1784 and
3482 every index row points at the row with its key.

## Field Names

The `InteriorRelationPoint_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has 17 columns: `CharacterKey`, the ten
`On*` columns (`OnDresser` to `OnShelf`), the four `IsEmptyIn*` columns,
`MatchingCharacterKey` and `MatchingCharacterPoint`. The 2016
`gc::InteriorRelationPointStaticStatus` holds `_installationCharacterKey`,
`_relationPoint` (13 i32 then, 14 now) and `_matchingCharacterKey` and
`_matchingCharacterPoint` as a pair.

All 966 keys of the sheet have a row on client 1784. The ten relation
columns with non-zero values match a field on 966 of 966 keys each, in
sheet order: `OnDresser` and `OnBedSideCabinet` (equal columns, `+0x0A`
and `+0x0E`), `OnDiningTable`, `OnTable`, `OnBookCase`, `OnShelf`,
`IsEmptyInFront`, and the equal `IsEmptyInBack`, `IsEmptyInLeft` and
`IsEmptyInRight` (`+0x36` to `+0x3E`). The four columns that are `0` on
every sheet row (`OnWardrobe`, `OnChair`, `OnSofa`, `OnBed`) take the four
all-zero fields between them in the same order. `MatchingCharacterKey`
matches `matching_character_key` on 966 of 966 keys (`<null>` as `0`), and
`MatchingCharacterPoint` (`0` on every sheet row) is the one field left,
next to the key as in the 2016 struct.

## Notes

- 124 of the 1,140 rows name a matching character on client 3482: tables
  and dining tables name the chair of their set. All 45 chairs named that
  way have a row of their own.
- No Lua file of client 3482 reads this table. The house window shows the
  interior points of the visited house through
  `toClient_GetVisitingTotalInteriorPoint()`, `...BaseInteriorPoint()`,
  `...SetOptionInteriorPoint()` and `...BonusInteriorPoint()`
  (`panel_window_installationmode_housepoint_renew.luac`).

## Open Questions

### How the Relation Points Count

The points read as a bonus for placing the furniture on another piece or
with a free side, but what the game adds them to (the interior points of
the house window, or a placement check) and what the values `1` to `5`
weigh is open.
