# `producttool.dbss` Format

## Purpose

One value per fishing rod or float and enhancement level, named
`AutofishingTimePercents` in the source sheet. On client 3474 the file holds
22 records: Cedar Float at each level from 0 to 10, and eleven fishing rods
at level 0. The value is `1,000,000` for Cedar Float, the Triple-Float
Fishing Rod and four rods that catch several fish at once, and `500,000`
for the Splendid and Lucky Silver and Golden Fishing Rods. What the client
does with it is open (see Open Questions). "Product" is the client's word
for life skills; the item descriptions call a fishing rod "a gathering
tool". Companion `producttooloffset.dbss` lists where every record sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | ------------ | --------- |
| 1      | 1485 and later | 3474    | `producttool.dbss`       | 620   | 22 Record    | 28        |
| 1      | 1485 and later | 3474    | `producttooloffset.dbss` | 268   | 22 Index Row | 12        |

| Layout | File                     | Known          | Unknown       |
| ------ | ------------------------ | -------------- | ------------- |
| 1      | `producttool.dbss`       | 268 B (43.2%)  | 352 B (56.8%) |
| 1      | `producttooloffset.dbss` | 268 B (100.0%) | 0 B (0.0%)    |

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

None. `producttooloffset.dbss` is the offset file of this table; the
records fill the main file, so the handler reads them in file order without
it. Item names come from LOC type 0 and icons from the `ITEM_ICON` lookup
index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                    |
| ------- | ------------- | ------- | ---------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `22` on client 3474   |
| `+0x04` | Record[count] | records | See Record; not in item or level order   |

There is no `PABR` magic and no trailer: the file is `4 + count x 28` bytes
(620 on client 3474).

### Record (28 bytes)

| Offset  | Type | Field                     | Notes                                                                                   |
| ------- | ---- | ------------------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key                  | `enchant_level << 24 \| item_id`, as in `itemenchant.dbss`; equals the index row key    |
| `+0x04` | u32  | item_key_dup              | Repeats `item_key` on every record; the index row's `data_offset` points here           |
| `+0x08` | u32  | unknown_08                | `0` on every record (client 3474)                                                       |
| `+0x0C` | u32  | unknown_0c                | `0` on every record (client 3474)                                                       |
| `+0x10` | u32  | unknown_10                | `0` on every record (client 3474)                                                       |
| `+0x14` | u32  | unknown_14                | `0` on every record (client 3474)                                                       |
| `+0x18` | u32  | autofishing_time_percents | Sheet column `AutofishingTimePercents`; `500,000` or `1,000,000` (client 3474)          |

`item_key` is unique. The parser splits it into `item_id` (low 24 bits) and
`enchant_level` (high 8 bits) with `split_item_key()` in
`_common/item_key.py`, and raises an error when `item_key_dup` differs.

### `producttooloffset.dbss`

| Offset  | Type             | Field | Notes                               |
| ------- | ---------------- | ----- | ----------------------------------- |
| `+0x00` | u32              | count | Equals the `producttool.dbss` count |
| `+0x04` | Index Row[count] | rows  | See Index Row                       |

The rows are the `[u32 key][u32 offset][u32 size]` rows of a PABR offset
table with no `PABR` magic and no trailer (268 bytes = 4 + 22 x 12 on
client 3474), read by `parse_bare_u32_offset_rows` in
`_common/pabr_offset.py`. They are not in the order of the main file.

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                                                  |
| ------- | ---- | ----------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | item_key    | The record's `item_key`                                                |
| `+0x04` | u32  | data_offset | Start of the record in the main file plus 4: points at `item_key_dup`  |
| `+0x08` | u32  | data_size   | Record length minus the 4-byte `item_key`: `24`                        |

## Records

The records on client 3474, by item.

| Item ID | Item                                   | Levels | `autofishing_time_percents` |
| ------: | -------------------------------------- | ------ | --------------------------: |
| 16153   | Triple-Float Fishing Rod               | 0      | 1,000,000                   |
| 16169   | Cedar Float                            | 0-10   | 1,000,000                   |
| 17591   | Splendid Silver Fishing Rod            | 0      | 500,000                     |
| 17592   | Splendid Golden Fishing Rod            | 0      | 500,000                     |
| 17596   | [Event] Splendid Golden Fishing Rod    | 0      | 500,000                     |
| 17612   | Lucky Silver Fishing Rod               | 0      | 500,000                     |
| 17613   | Lucky Golden Fishing Rod               | 0      | 500,000                     |
| 17669   | [Event] Splendid Golden Fishing Rod    | 0      | 500,000                     |
| 767158  | Grandpa Cron's Fishing Rod             | 0      | 1,000,000                   |
| 767187  | Cool Wind Fishing Rod                  | 0      | 1,000,000                   |
| 767277  | Dreamy Starlight Fishing Rod (30 Days) | 0      | 1,000,000                   |
| 767671  | Crio's Miraculous Fishing Rod          | 0      | 1,000,000                   |

The item descriptions of 767158, 767187 and 767671 say the rod catches
several fish at once "like with the Triple-Float Fishing Rod". Client 1784
has the same 18 records without the four 767xxx rods.

## Field Names

The record is the `ProductTool_Property` sheet of a private server's
`DataSheets.bexcel` on client 1784 (columns `ItemKey`, `EnchantLevel`,
`ItemName`, `Param_0` to `Param_3`, `AutofishingTimePercents`). Its 18 rows
match the live file on all 18 shared keys (client 3474): `ItemKey` and
`EnchantLevel` are `item_id` and `enchant_level`, `AutofishingTimePercents`
is `autofishing_time_percents`, and `Param_0` to `Param_3` are `0` as
`unknown_08` to `unknown_14` are. The client 1784 file holds exactly these
18 records. The four 767xxx rods are newer than the sheet. The server dump
(`Instance_dumpFull.exe`) of the same private server names the loader
`LoadProductToolStaticInformation` and stores each record as a
`gc::ProductToolStaticStatus` in a `ProductToolStaticStatusManager` keyed by
`gc::ItemEnchantKey`. The 2016 PDB has no `ProductTool` type.

## Notes

- `1,000,000` is the client's 100% value, `CppDefine.e100Percent` (see
  [guaranteeenchantss](guaranteeenchantss_dbss.md) Notes), and the column
  name ends in `Percents`.
- The value is not the tooltip's auto-fishing line. In my game, the Grandpa
  Cron's Fishing Rod tooltip lists "Auto-fishing Time -80%" under Item
  Effect while its record holds `1,000,000`, the Balenos Fishing Rod
  (16162) lists 25% less auto-fishing time when enhanced and has no record
  here at any level, and the
  Splendid and Lucky Silver and Golden Fishing Rods, which hold `500,000`,
  list no auto-fishing line at all.
- The client calls the stat "Auto-fishing Time": pet items carry
  "(Auto-fishing Time Reduction)" and buff scrolls list "Auto-fishing Time
  -10%" (LOC type 0). `CppEnums.ShowParamBuffType.AutoFishingRate` (`8`) in
  `global_define_cpp_enum.luac` is the buff detail window's auto-fishing
  line; its description list in `panel_characterinfo_buffdetail_all.luac`
  includes `LUA_BUFFDETAIL_DESC_FISHINGROD`.
- Cedar Float is a float, not a rod. Its eleven records store
  `1,000,000` at every level.

## Open Questions

### What `autofishing_time_percents` Does

The sheet names the column `AutofishingTimePercents`, but the tooltips do
not show it (see Notes): a rod with `1,000,000` lists "Auto-fishing Time
-80%", the enhanced Balenos Fishing Rod lists 25% less with no record in this file,
and the rods with `500,000` list no auto-fishing line. It may be a
hidden multiplier on the auto-fishing time that the tooltip leaves out, or
a value the current client no longer uses. No client 3474 `.luac` file
contains the string `ProductTool`. The server dump's `LoadProductToolStaticInformation`
and its callers would show where the value is applied.

### The Four Zero Fields

`unknown_08` to `unknown_14` are `0` on every record of clients 1784 and
3474. The sheet has four columns in that place, `Param_0` to `Param_3`,
also `0` on every row, so the column names carry no meaning to match. A
record with a non-zero value, or the server dump's row reader for
`gc::ProductToolStaticStatus`, would show what they hold.
