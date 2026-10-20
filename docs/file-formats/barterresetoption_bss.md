# `barterresetoption.bss` Format

## Purpose

The point cost of the barter list refreshes, for the trade item barters
and the ship material barters. Two counted u32 lists follow the PABR
magic, one per barter type. On client 3474 the
trade item list is `20, 40, 50` and the ship material list `10, 30`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | -------------- | --------- |
| 1      | 1485 and later | 3474    | `barterresetoption.bss` | 44    | 1 String Table | 4         |

| Layout | File                    | Known         | Unknown    |
| ------ | ----------------------- | ------------- | ---------- |
| 1      | `barterresetoption.bss` | 44 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset                       | Type                         | Field                 | Notes                                                      |
| ---------------------------- | ---------------------------- | --------------------- | ---------------------------------------------------------- |
| `+0x00`                      | char[4]                      | magic                 | ASCII `PABR`                                               |
| `+0x04`                      | u32                          | general_barter_count  | Trade item barter refreshes per day with a Value Pack (one fewer without) |
| `+0x08`                      | u32[general_barter_count]    | general_barter        | Barter Refresh Points of the 1st, 2nd, ... refresh of the day |
| `general_barter+0x00`        | u32                          | material_barter_count | Ship material barter refreshes per day                     |
| `general_barter+0x04`        | u32[material_barter_count]   | material_barter       | Barter Refresh Points of the 1st, 2nd, ... refresh of the day |
| `material_barter+0x00`       | String Table                 | string_table          | See String Table                                           |
| `string_table+0x00`          | u32                          | table_start           | Offset of the string table, where `material_barter` ends   |
| `string_table+0x04`          | u32                          | zero                  | Always `0`                                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The names follow the `BarterReset_Option` sheet of a private server's
`DataSheets.bexcel` on client 1784: columns `Index`, `GeneralBarter` and
`MaterialBarter`, rows `Index` 1 to 5. `GeneralBarter` holds `20, 40, 50`
and `MaterialBarter` `40, 50`, the other cells `<null>`; the file keeps
each column's filled cells in `Index` order as one list. All 3 of 3 and 2
of 2 values match the client 1784 file, and that file is byte for byte the
private server's compiled `binary/barterresetoption.bss`. The loader is
`GameCommonParameterLoaderFromExcel::loadMain(loadBarterResetOption)`.

## Barter Types

The barter refresh window (`panel_window_barterinforefresh_1.luac`,
client 3474) has five buttons. For buttons 0, 1, 3 and 4 it shows the cost
with `ToClient_getBarterResetNeedPoint(button)` as "[Points Used:
{value}]" (`PANEL_BARTERINFO_RESETBUTTON_COUNT`) and the refreshes left
with `ToClient_getMaxSeedChangeCountByBarterType(type)` minus
`ToClient_getSeedChangeCountByBarterType(type)`; buttons 0 and 1 count
against barter type `0`, buttons 3 and 4 against type `1`. Button 2,
"Reduce Refresh Cooldown", uses parley and no points. A refresh also
needs the cost within the day's points left
(`ToClient_getMaxChangeSeedCountForDay()` minus
`ToClient_getChangeSeedCountForDay()`); otherwise the window shows
"You have exceeded either the daily given number of refresh counts or
points." (`eErrNoBarterSeedChangeCountIsNull`).

| Barter type | List              | Buttons (English text, client 3474)                          |
| ----------- | ----------------- | ------------------------------------------------------------ |
| `0`         | `general_barter`  | Trade Item Barter Refresh, Trade Item Barter Instant Refresh |
| `1`         | `material_barter` | Ship Material Refresh, Instant Ship Material Refresh         |

The ship material buttons show only with `_ContentsGroup_BarterMaterialReset`.

## Notes

- Raw bytes on client 3474:
  `50 41 42 52 03 00 00 00 14 00 00 00 28 00 00 00 32 00 00 00 02 00 00 00 0A 00 00 00 1E 00 00 00 00 00 00 00 20 00 00 00 00 00 00 00`
  (44 bytes).
- Clients 1485 to 2107 hold `material_barter` `40, 50`; clients 2519 to
  3474 hold `10, 30`. `general_barter` is `20, 40, 50` on every client
  checked. The file is not in the archives of clients 794 and 1230.
- GrumpyG's barter guide
  ([grumpygreen.cricket/bdo-barter-sailing](https://grumpygreen.cricket/bdo-barter-sailing/),
  "Barter Refresh Options") lists the refresh costs as 20, 40 and 50
  Barter Refresh Points for Trade Material and 10 and 30 for Ship
  Material, the latter usable "only twice a day", out of 100 points a day
  (150 with a Value Pack). That is entry N as the cost of the N-th refresh
  of the day, and the list length as the daily refresh count of the type.
  The same guide limits the trade item refresh to "2 per day or 3 with
  VP", so the third `general_barter` entry (`50`) is the refresh a Value
  Pack adds. The instant refreshes cost "an additional 30 extra Barter
  Refresh Points", and the points refill every day at 06:00 UTC.
- In game on client 3474 my Refresh Barter Information window, before any
  refresh that day, showed "[Points Used: 20]" on Trade Item Barter
  Refresh, 50 on Trade Item Barter Instant Refresh, 10 on Ship Material
  Refresh and 40 on Instant Ship Material Refresh. Both instant buttons
  say they refresh "immediately by consuming 30 points": the first entry
  of each list plus 30 (see Open Questions).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py` as one
  record: `general_barter` and `material_barter` are `is_counted_list`
  fields, each the list of point costs in file order.

## Open Questions

### Instant Refresh Surcharge

The instant buttons cost the current refresh plus a flat 30 points (50 and
40 on the first refresh of the day), but no value of this file is `30` for
the trade item list, and the ship material `30` is its second refresh.
Where the client keeps the 30 for `ToClient_getBarterResetNeedPoint` of
buttons `1` and `4`, and where the Value Pack's third trade item refresh is
gated, is not in the client data read so far.
