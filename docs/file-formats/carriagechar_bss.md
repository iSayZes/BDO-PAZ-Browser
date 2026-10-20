# `carriagechar.bss` Format

## Purpose

Pairs each carrier character of the warehouse transport system with a
model from the world map model folder `object/worldmap/`. On client 3474
the file has 3 rows:
`59012` Velia Freight Wagon (`WorldMap/WorldMap_Cart.pam`), `59013`
Calpheon Cargo Ship (`WorldMap/WorldMap_WoodenBoat_small.pam`) and `59014`
Altinova Freight Ship (`WorldMap/WorldMap_SailingShip.pam`). These are the
three [`characterstatic.dbss`](characterstatic_dbss.md) rows whose AI script
is `NPC_Delivery_Carriage_NewDelivery`. The transport carriage types
themselves are in [`carriagespec.dbss`](carriagespec_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------ | ----- | ------- | --------- |
| 1      | 1230 and later | 3474    | `carriagechar.bss` | 150   | 3 Row   | 6         |

| Layout | File               | Known         | Unknown    |
| ------ | ------------------ | ------------- | ---------- |
| 1      | `carriagechar.bss` | 146 B (97.3%) | 4 B (2.7%) |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                          |
| ---------------------------- | -------- | ------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key; a key without a row shows as plain text instead of a link |
| `languagedata_en.loc`        | Optional | Character name (type `6`, `str_id1` = `character_key`)        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset      | Type               | Field        | Notes                                                        |
| ----------- | ------------------ | ------------ | ------------------------------------------------------------ |
| `+0x00`     | char[4]            | magic        | ASCII `PABR`                                                 |
| `+0x04`     | u32                | unknown_04   | `2` on every client, one less than the rows; see Open Questions |
| `+0x08`     | Row[..table_start] | rows         | Rows back to back until `table_start`; see Row               |
| `rows+0x00` | String Table       | string_table | See String Table                                             |
| `EOF-0x08`  | u32                | table_start  | Offset of the string table, where `rows` ends                |
| `EOF-0x04`  | u32                | zero         | Always `0`                                                   |

The parser takes the row count from the trailer, `(table_start - 8) / 6`,
and rejects a file whose rows do not fill that space.

### Row (6 bytes)

| Offset  | Type | Field             | Notes                                                                 |
| ------- | ---- | ----------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | character_key     | `characterstatic.dbss` key; unique                                    |
| `+0x02` | u32  | object_name_index | String table index of the world map model path (`object_name`); `0`, `1`, `2` in row order |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                       |
| ------- | ------------------ | ------------ | ----------------------------------------------------------- |
| `+0x00` | u32                | string_count | Equals the number of rows                                   |
| `+0x04` | pstr[string_count] | strings      | UTF-8 model paths relative to `object/`, one per row        |

## Field Names

The names follow the `New_Carriage_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 (also in its
`datasheet_plantdatatable.xlsm`, next to `New_Carriage2_Table`, the source of
`carriagespec.dbss`). Its columns are `CharacterKey` and `ObjectName`; the
note column `#^E_Merge Index` and a `<주석>` row hold no developer comments.
All 3 sheet rows match the file in both columns, in order, on clients 1784
and 3474 (3 of 3 keys). The server dump of client 1784
(`Instance_dumpFull.exe`) names the class `CarriageCharacterStaticStatus`
in the errors `CarriageCharacterStaticStatus::set()` writes for a bad
`Characterkey` and `_objectName`, and names the loader step
`GameCommonParameterLoaderFromExcel::loadMain(loadCarriageCharacterInfomation)`.

The 2016 client's debug symbols have no `CarriageCharacterStaticStatus`.

## Notes

- Clients 1230, 1485, 1784, 2107, 2519, 3002, 3251 and 3474 ship the same
  150-byte file; client 794 has none.
- The model paths are relative to `object/`: the PAZ holds
  `object/worldmap/worldmap_cart.pam`, `worldmap_woodenboat_small.pam` and
  `worldmap_sailingship.pam`. The characters' own models in
  `characterstatic.dbss` are `riding/carriage/npc/carriagenpc_type1` (the
  wagon) and `npc/npc_ship2_moving` (both ships).
- The file has no carriage key column, so it does not join
  `carriagespec.dbss`.
- No extracted client Lua file names the file, the sheet, the three
  character keys or the model paths.

## Open Questions

### What unknown_04 Counts

`unknown_04` sits where other PABR tables keep their row count, but it is
`2` while the file holds 3 rows and 3 strings, on every client from 1230
to 3474. The scan of every PABR `.bss` on client 3474 whose rows are a key
and a string table index in row order finds two more files,
`photomodestaticstatus.bss` and `autousebuffitemcategoryinfo.bss`, and both
store the row count there. Whether the client reads only 2 rows (and so
never loads the Altinova Freight Ship model), or reads the rows up to
`table_start` and ignores the value, is open. The sibling
`carriagespec.bss` of client 1230, built from the same workbook, also
stores `2`, its own row count.
