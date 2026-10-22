# `siegeobjectkindlistcache.bss` Format

## Purpose

The siege object kinds and one building character for each: rows of a u8
object kind and a `characterstatic.dbss` character key. On client 3482 the
14 rows are the Node War and Conquest War buildings a guild can install,
from the Barricade (kind `3`) to the Ballista Workshop (kind `29`). The
installation mode's war information window lists one line per row.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | ------- | --------- |
| 1      | 1127 and later | 3482    | `siegeobjectkindlistcache.bss` | 62    | 14 Row  | 3         |

| Layout | File                           | Known         | Unknown    |
| ------ | ------------------------------ | ------------- | ---------- |
| 1      | `siegeobjectkindlistcache.bss` | 62 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2637   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1324   | Layout 1 |
| 1316   | Layout 1 |
| 1309   | Layout 1 |
| 1286   | Layout 1 |
| 1256   | Layout 1 |
| 1230   | No file  |
| 1211   | No file  |
| 1194   | No file  |
| 1177   | No file  |
| 1156   | No file  |
| 1127   | Layout 1 |
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

| File                  | Required | Role                        |
| --------------------- | -------- | --------------------------- |
| `languagedata_en.loc` | Optional | Character names, LOC type 6 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (3 bytes)

| Offset  | Type | Field         | Notes                                                              |
| ------- | ---- | ------------- | ------------------------------------------------------------------ |
| `+0x00` | u8   | object_kind   | Siege object kind; unique per row, see Object Kinds                |
| `+0x01` | u16  | character_key | `characterstatic.dbss` key of a building of that kind              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Object Kinds

The rows of client 3482 in file order, with the LOC type 6 name of the
character, and the character key the same kind has on client 1784.

| `object_kind` | `character_key` (client 3482) | Name                       | `character_key` (client 1784) |
| ------------- | ----------------------------- | -------------------------- | ----------------------------- |
| 19            | 12837                         | Supply Depot               | 12650                         |
| 3             | 12605                         | Barricade                  | 12605                         |
| 21            | 2046                          | Wooden Fence               | 2046                          |
| 18            | 12835                         | Enhanced Flame Tower       | 12642                         |
| 26            | 12839                         | Indomitable Flag Factory   | 12660                         |
| 12            | 12832                         | Elephant Nursery           | 12629                         |
| 20            | 12838                         | Wooden Fence Gate          | 12655                         |
| 17            | 12836                         | Big Hwacha                 | 12645                         |
| 11            | 12808                         | Cannon Observatory         | 12623                         |
| 10            | 12807                         | Recovery Center            | 12619                         |
| 24            | 12804                         | Large Siege Tower Factory  | 2050                          |
| 23            | 12803                         | Medium Siege Tower Factory | 2049                          |
| 22            | 12802                         | Defense Tower              | 2047                          |
| 29            | 12800                         | Ballista Workshop          | 2070                          |

## Field Names

The `SiegeObjectType_Name` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `ObjectKind` and `RepCharacterIndex` (the
representative character) and two rows, `3, 12605` and `21, 2046`; both
are rows of the client 1784 file (2 of 2). The other 12 rows are not in
any sheet: that server's dump (client 1784) has the error text
`CharacterStaticStatusManager::readFromBinary() siegeObjectKindListCache
Open Failed.`, so the file is read with the character table, as a cache
of one character per object kind.

The client Lua of client 3482 reads the rows with
`ToClient_getSiegeObjectKindCount()` and
`ToClient_getObjectStaticStatusByObjectKindbyIndex(index)`
(`panel_house_installationmode_warinfomation_all_1.luac`), which returns
the row's character; the window skips characters with
`isRoseWarSpawnCharacter()`.

## Notes

- Clients 1784 and 3482 hold the same 14 kinds in another order. The
  character of 12 kinds changed between them; the Barricade and the
  Wooden Fence kept theirs.
- The kinds overlap the `Type` column of the `SiegeObjectTotalLimit` sheet
  on client 1784 (`3`, `10`, `11`, `12`, `17`, `18`, `19`, `20`, `26`).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/siegeobject_tables.py`:
  the object kind, then the character key with its name.

## Open Questions

### Object Kind Names

The server dump of client 1784 holds 24 `SiegeObjectType_*` names
(`SiegeObjectType_Baricade`, `SiegeObjectType_BaricadeDoor`, ...,
`SiegeObjectType_PlayerUpgradeBuilding`) but not their values, the 2016
PDB has no `SiegeObjectType` enum, and the client Lua of client 3482 has
no `__eSiegeObjectType` constant. Which name belongs to which kind number
is open, so the preview shows the number and the character name.
