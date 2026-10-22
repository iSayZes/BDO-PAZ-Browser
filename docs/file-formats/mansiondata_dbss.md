# `mansiondata.dbss` Format

## Purpose

The furniture characters that belong to the manor: one 6-byte row per
installation character. On client 3482 the file lists 498 characters (304
on client 1784): 234 named `[Manor] ...` ("[Manor] Starspun Chandelier",
`4398`) or `[Event] [Manor] ...` in LOC type 6, 216 development objects
named `Dev ...` ("Dev Plant13- AfricanIron", `4454`), 4 more with a name and
44 keys (`6956` to `15993`) with no `characterstatic.dbss` row. Companion
`mansiondataoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | -------------- | --------- |
| 1      | 1636 and later | 3482    | `mansiondata.dbss`       | 2,992 | 498 Row        | 6         |
| 1      | 1636 and later | 3482    | `mansiondataoffset.dbss` | 4,984 | 498 Offset Row | 10        |

| Layout | File                     | Known            | Unknown       |
| ------ | ------------------------ | ---------------- | ------------- |
| 1      | `mansiondata.dbss`       | 1,996 B (66.7%)  | 996 B (33.3%) |
| 1      | `mansiondataoffset.dbss` | 4,984 B (100.0%) | 0 B (0.0%)    |

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
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                                    |
| ---------------------------- | -------- | --------------------------------------------------------------------------------------- |
| `mansiondataoffset.dbss`     | Optional | `character_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a key without a row shows as plain text              |
| `languagedata_en.loc`        | Optional | Furniture names, LOC type 6                                                              |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3482 the file is 4 + 498 x 6 = 2,992 bytes.

### Row (6 bytes)

| Offset  | Type | Field             | Notes                                                               |
| ------- | ---- | ----------------- | ------------------------------------------------------------------- |
| `+0x00` | u16  | character_key     | Row key: the furniture installation, a `characterstatic.dbss` character |
| `+0x02` | u16  | character_key_dup | Equal to `character_key` on every row; the offset index points here |
| `+0x04` | u8   | unknown_04        | `1` on every row (clients 1784 and 3482); see Open Questions        |
| `+0x05` | u8   | unknown_05        | `0` on every row (clients 1784 and 3482); see Open Questions        |

The rows are in no key order; client 3482 opens with 4398, 4454, 4390.

### `mansiondataoffset.dbss`

Bare offset table into `mansiondata.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                               |
| ------- | ----------------- | ----- | ----------------------------------- |
| `+0x00` | u32               | count | Equals the `mansiondata.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                      |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                                 |
| ------- | ---- | ------------- | ----------------------------------------------------- |
| `+0x00` | u16  | character_key | Key of the row it points at                           |
| `+0x02` | u32  | data_offset   | Row start + 2, at `character_key_dup`                 |
| `+0x06` | u32  | data_size     | `4` on every row: the row less its key                |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in another order than the file; on clients 1784 and 3482 every
index row points at the row with its key.

## Field Names

The `MansionData_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `CharacterKey`, `Type`, `Kind` and
`ContentsGroupKey`, 304 rows: `character_key` matches `CharacterKey` on 304
of 304. Every row of the sheet holds `Type` `1`, `Kind` `2` and
`ContentsGroupKey` `1622`. The 2016 client's debug symbols have no struct
for the table.

## Notes

- The client Lua asks whether an item is manor furniture through
  `ToClient_isMansionInstallationItem()`; no Lua call reads a field of this
  table.

## Open Questions

### What the Two u8 Fields Hold

`unknown_04` is `1` and `unknown_05` is `0` on every row of clients 1784
and 3482. The sheet's `Type` (`1` on every row) is a lead for
`unknown_04`, but a match on one constant value does not fix the column,
and `Kind` (`2` on every row) matches neither field.
