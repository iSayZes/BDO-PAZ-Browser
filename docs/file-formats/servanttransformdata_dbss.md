# `servanttransformdata.dbss` Format

## Purpose

The ship appearance changes a wharf offers: one row per change, from one
ship character to another. On client 3474 the file has 2 rows: form `1`
turns Epheria Sailboat (`31001`) into Epheria Galleon (`31020`), form `2`
turns Epheria Frigate (`31003`) into Panokseon (`31025`). The look change
window of `panel_dialog_servantlookchange_all_1.luac` and `_2.luac` reads
the table through `getServantTransformManager()` when it is opened at a
wharf (its confirm box uses `LUA_WHARFLIST_CHANGECONFIRM_TITLE`), and sends
the chosen form with `stable_servantTransform(slot, formIndex)`. Companion
`servanttransformdataoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records      | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------------ | --------- |
| 1      | 1485 and later | 3474    | `servanttransformdata.dbss`       | 20    | 2 Row        | 8         |
| 1      | 1485 and later | 3474    | `servanttransformdataoffset.dbss` | 24    | 2 Offset Row | 10        |

| Layout | File                              | Known         | Unknown    |
| ------ | --------------------------------- | ------------- | ---------- |
| 1      | `servanttransformdata.dbss`       | 20 B (100.0%) | 0 B (0.0%) |
| 1      | `servanttransformdataoffset.dbss` | 24 B (100.0%) | 0 B (0.0%) |

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
| `servanttransformdataoffset.dbss` | Optional | `form_key -> (offset, size)` of every row; the main file can be walked without it |
| `characterstaticoffset.dbss`      | Optional | Tells which keys have a [`characterstatic.dbss`](characterstatic_dbss.md) row, for the key links |
| `languagedata_en.loc`             | Optional | Character names (LOC type 6)                                         |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (8 bytes)

| Offset  | Type | Field              | Notes                                                              |
| ------- | ---- | ------------------ | ------------------------------------------------------------------ |
| `+0x00` | u16  | form_key           | Unique; the `formIndex` the Lua sends to `stable_servantTransform` |
| `+0x02` | u16  | form_key_dup       | Equal to `form_key` in every row; the offset file points here      |
| `+0x04` | u16  | from_character_key | Ship that changes; a [`servant.bss`](servant_bss.md) row (client 3474) |
| `+0x06` | u16  | to_character_key   | Ship it changes into; a `servant.bss` row (client 3474)            |

### `servanttransformdataoffset.dbss`

| Offset  | Type              | Field | Notes                                        |
| ------- | ----------------- | ----- | -------------------------------------------- |
| `+0x00` | u32               | count | Equals the `servanttransformdata.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row         |

### Offset Row (10 bytes)

| Offset  | Type | Field    | Notes                                                   |
| ------- | ---- | -------- | ------------------------------------------------------- |
| `+0x00` | u16  | form_key | Key of the row it points at                             |
| `+0x02` | u32  | offset   | Row start + 2, at `form_key_dup`                        |
| `+0x06` | u32  | size     | The row without its leading `form_key`: always `6`      |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in main file order.

## Field Names

The names follow the `ServantTransform_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 and the same sheet in its
`datasheet_formdatatable.xlsm` (next to `Form_Table`), columns `FormKey`,
`FromCharacterKey` and `ToCharacterKey`. Its 2 rows match the file by all
three values on clients 1784 and 3474 (2 of 2). The `ServantTransform_Table`
of a private server on client 519 holds the same 2 rows.

The client 1784 server dump names the static status
`gc::ServantTransformStaticStatus`, keyed by a `KeyType<unsigned short>`,
and its loader `LoadServantTransformStaticInformation`. Its check messages
call the key member `_transformIndex` and the table "Servant 외형변경 정보"
(servant appearance change info). The client Lua reads the same row with
`getTransformIndex()` and `getTransformCharacterKey()`.

## Notes

- Client 1784 has the same 20-byte file and the same 24-byte offset file,
  byte for byte.
- The file is not sorted by key: form `2` comes first.
- Neither change is a ship upgrade: [`servantupgrade.dbss`](servantupgrade_dbss.md)
  on client 3474 upgrades Epheria Sailboat into Improved Epheria Sailboat
  (`31058`) or Epheria Caravel (`31048`), and Epheria Frigate into Improved
  Epheria Frigate (`31059`) or Epheria Galleass (`31049`). No upgrade row
  leads to Epheria Galleon or Panokseon.
- The 1784 server dump rejects a row whose two character keys are equal,
  whose keys have no servant, or whose servants differ in `servantKind` or
  `servantKindSub`.
- `CppEnums.ContentsType_ServantTransform` is `67` in
  `global_define_cpp_enum.luac` (client 3474).

## Open Questions

### Servant Kinds of the Two Ships

The 1784 server check wants the same `servantKind` on both sides of a row,
but [`servant.bss`](servant_bss.md) on client 3474 gives Epheria Sailboat
kind `15` (`PersonalTradeShip`) and Epheria Galleon kind `21`
(`CashPersonalTradeShip`), Epheria Frigate `17` and Panokseon `22`. The
`RaceType` column of the client 1784 `ServantSet_Table` sheet, which matches
`servant_kind` on all 333 client 1784 records, has the same four kinds, so
they did not change after client 1784. Which kind the check compares is
open.

### Whether a Change Can Be Undone

The Lua lists the forms for the ship's current character key
(`getFormListSize(fromCharacterKey)`) and greys out the change button when
the picked form's `getTransformCharacterKey()` equals that key. The file
holds only one direction per form, so whether an Epheria Galleon is offered
form `1` back to Epheria Sailboat is open.
