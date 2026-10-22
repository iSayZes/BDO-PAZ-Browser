# `oceansiegereviveposition.bss` Format

## Purpose

Where Blue Battlefield (ocean siege) players revive, per territory: each
row holds a territory key and groups of world positions, each position
with an f32 and a u8. On client 3482 Balenos and Calpheon each have a
group `0` of harbour positions and a group `1` of one position far out
at sea.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records                     | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | --------------------------- | --------- |
| 1      | 3251 and later | 3482    | `oceansiegereviveposition.bss` | 222   | 10 Position, 4 Group, 2 Row | 17        |

| Layout | File                           | Known         | Unknown      |
| ------ | ------------------------------ | ------------- | ------------ |
| 1      | `oceansiegereviveposition.bss` | 168 B (75.7%) | 54 B (24.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | No file  |
| 2765   | No file  |
| 2519   | No file  |
| 2107   | No file  |
| 1937   | No file  |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                         |
| --------------------- | -------- | ---------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows, one per territory             |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 6 bytes + groups)

| Offset  | Type               | Field         | Notes                                                                |
| ------- | ------------------ | ------------- | -------------------------------------------------------------------- |
| `+0x00` | u16                | territory_key | `territoryinfo.bss` key, LOC type 12 name; `0` Balenos, `2` Calpheon |
| `+0x02` | u32                | group_count   | Number of groups; `2` on client 3482                                 |
| `+0x06` | Group[group_count] | groups        | See Group                                                            |

### Group (variable: 5 bytes + positions)

| Offset  | Type                     | Field          | Notes                                              |
| ------- | ------------------------ | -------------- | -------------------------------------------------- |
| `+0x00` | u8                       | unknown_00     | `0` or `1`, in that order; see Open Questions      |
| `+0x01` | u32                      | position_count | Number of positions                                |
| `+0x05` | Position[position_count] | positions      | See Position                                       |

### Position (17 bytes)

| Offset  | Type | Field      | Notes                                                      |
| ------- | ---- | ---------- | ---------------------------------------------------------- |
| `+0x00` | f32  | x          | World x                                                    |
| `+0x04` | f32  | y          | Height, `-7777` to `-7315` on client 3482                  |
| `+0x08` | f32  | z          | World z                                                    |
| `+0x0C` | f32  | unknown_0c | `150` to `400`; see Open Questions                         |
| `+0x10` | u8   | unknown_10 | Equals its group's `unknown_00` on every position          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Positions

Client 3482, in file order, with the `regioninfo.bss` region whose return
point lies nearest.

| `territory_key` | Group | x, y, z                    | `unknown_0c` | Nearest return point                 |
| --------------- | ----- | -------------------------- | ------------ | ------------------------------------ |
| `0`             | `0`   | 6186, -7676, 93658         | 200          | Velia (14,114 units)                 |
| `0`             | `0`   | 152080, -7653, 291935      | 150          | Iliya Island (7,122)                 |
| `0`             | `0`   | -53614, -7658, 392395      | 400          | Crow Merchants' Vessel (5,740)       |
| `0`             | `0`   | -138892, -7500, 177043     | 250          | Olvia Academy Fountain (33,182)      |
| `0`             | `0`   | -74427, -7500, 127677      | 250          | Epheria Ridge (52,394)               |
| `0`             | `1`   | -339970, -7315, 374486     | 300          | none within 280,000                  |
| `2`             | `0`   | -358820, -7777, 38104      | 200          | Port Epheria (10,179)                |
| `2`             | `0`   | -451604, -7662, 30992      | 300          | Outpost Supply Port (4,703)          |
| `2`             | `0`   | -339970, -7315, 374486     | 300          | none within 280,000                  |
| `2`             | `1`   | -339970, -7315, 374486     | 300          | none within 280,000                  |

## Field Names

The Blue Battlefield is newer than client 1784: the file is not in its
archives and no sheet of a private server's `DataSheets.bexcel` on that
client covers it, and no Lua function of client 3482 names it. `territory_key` holds `0`
and `2`, the two keys of `CppEnums.OceanSiegeTerritoryName`
(`global_define_cpp_enum.luac`, client 3482: Balenos and Calpheon), and
each row's harbour positions lie in that territory: Velia for `0`, Port
Epheria for `2`. The positions read as BDO world coordinates on the
scale of the `regioninfo.bss` return points, y the height near sea
level.

## Notes

- Client 3251 has the Balenos row only (104 bytes): the first three
  group `0` positions of client 3482 and a group `1` position at
  `(-339772, -7531, 373439)` with `unknown_0c` `400`. The file is not in
  the archives of client 1784.
- The handler (`_bss/oceansiegereviveposition/`) shows one row per
  position: the territory key and name and the position rounded to whole
  units, in file order. It previews
  [`siege2024revivepositionstaticstatus.bss`](siege2024revivepositionstaticstatus_bss.md)
  too, with that file's reader.

## Open Questions

### The Two Groups

Each territory has a group `0` of harbour positions and a group `1` of
one position, the same `(-339970, -7315, 374486)` for both territories,
which Calpheon's group `0` lists too. Attacker and defender sides, or
the positions before and after the battle, both fit; no Lua names a
`__eRespawnType` for the ocean siege.

### The f32 of Each Position

`unknown_0c` is `150` to `400`. A spread radius around the position fits,
as the f32 after the positions of
[`rosewarrevivepositionstaticstatus.bss`](rosewarrevivepositionstaticstatus_bss.md)
does, but nothing reads it.
