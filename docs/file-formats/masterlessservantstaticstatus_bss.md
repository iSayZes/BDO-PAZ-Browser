# `masterlessservantstaticstatus.bss` Format

## Purpose

The Traveler's Horse, the horse a stable keeper lends to a player without a
horse of their own: five rows of three numbers, each ending with the horse's
character ID 31560. The client Lua (`panel_dialog_horsewithoutowner_all`)
holds the same ID as `_rentCharacterKeyRaw = 31560` and summons it with
`ToClient_SummonMasterLessHorse`. What the three numbers set is open.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------------------- | ----- | ------- | --------- |
| 1      | 2107 and later | 3474    | `masterlessservantstaticstatus.bss` | 90    | 5 Row   | 14        |

| Layout | File                                | Known        | Unknown      |
| ------ | ----------------------------------- | ------------ | ------------ |
| 1      | `masterlessservantstaticstatus.bss` | 30 B (33.3%) | 60 B (66.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role |
| ---------------------------- | -------- | ---- |
| `languagedata_en.loc`        | Optional | The horse's name (LOC type 6, `str_id1` = `character_id`) |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key, so a `character_id` without a row shows as plain text instead of a link |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type              | Field              | Notes                              |
| ------------------- | ----------------- | ------------------ | ---------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                             |
| `+0x04`             | u32               | record_count       | 5 on client 3474                   |
| `+0x08`             | Row[record_count] | records            | See Row                            |
| `records+0x00`      | String Table      | string_table       | Present but empty                  |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; `78` |
| `string_table+0x04` | u32               | zero               | `0`                                |

### Row (14 bytes)

| Offset  | Type | Field        | Notes |
| ------- | ---- | ------------ | ----- |
| `+0x00` | u32  | unknown_00   | 50,000, 150,000, 300,000, 500,000, 1,000,000 (client 3474) |
| `+0x04` | u32  | unknown_04   | 45 on every row (client 3474) |
| `+0x08` | u32  | unknown_08   | 50,000, 100,000, 150,000, 200,000, 500,000 (client 3474) |
| `+0x0C` | u16  | character_id | 31560 (Traveler's Horse) on every row |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | `0`        |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Notes

- Client 1784 has no such file, and the `DataSheets.bexcel` of a private
  server on that client has no sheet for it.

## Open Questions

### The Three Numbers

The rows pair a rising `unknown_00` (50,000 to 1,000,000) with a rising
`unknown_08` (50,000 to 500,000) and a constant 45 in `unknown_04`, in file
order. No client Lua reads them: the Traveler's Horse dialog only summons
and returns character 31560, and its LOC texts (`PANEL_TRAVELHORSE_*`,
`PANEL_HORSEWITHOUTOWNER_*`) name no number.
