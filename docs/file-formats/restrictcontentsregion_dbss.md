# `restrictcontentsregion.dbss` Format

## Purpose

The functions a region turns off: per region key one flag each for the
maid, the world map, character change, muster, camp, compass, item map and
minimap. The client Lua asks for them by region with
`ToClient_RestrictContentsByRegion(__eRestrictContentsType_WorldMap)` (the
world map, minimap and family character list) and
`__eRestrictContentsType_Maid` (the maid list). On client 3474 the 48 rows
are regions such as Orze's Garden (`1550`), Syca's Garden (`1102`) and
Vaha's Cradle (`1078`). Companion `restrictcontentsregionoffset.dbss` lists
where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ----------------------------------- | ----- | ------------- | --------- |
| 2      | 2107 and later | 3474    | `restrictcontentsregion.dbss`       | 628   | 48 Row        | 13        |
| 2      | 2107 and later | 3474    | `restrictcontentsregionoffset.dbss` | 484   | 48 Offset Row | 10        |
| 1      | 1784           | 1784    | `restrictcontentsregion.dbss`       | 292   | 24 Row        | 12        |
| 1      | 1784           | 1784    | `restrictcontentsregionoffset.dbss` | 244   | 24 Offset Row | 10        |

| Layout | File                                | Known          | Unknown     |
| ------ | ----------------------------------- | -------------- | ----------- |
| 2      | `restrictcontentsregion.dbss`       | 580 B (92.4%)  | 48 B (7.6%) |
| 2      | `restrictcontentsregionoffset.dbss` | 484 B (100.0%) | 0 B (0.0%)  |
| 1      | `restrictcontentsregion.dbss`       | 292 B (100.0%) | 0 B (0.0%)  |
| 1      | `restrictcontentsregionoffset.dbss` | 244 B (100.0%) | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2519   | Layout 2 |
| 2107   | Layout 2 |
| 1784   | Layout 1 |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                                | Required | Role                                                                     |
| ----------------------------------- | -------- | ------------------------------------------------------------------------ |
| `restrictcontentsregionoffset.dbss` | Optional | `region_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`               | Optional | Region names (LOC type 17)                                               |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (13 bytes)

| Offset  | Type | Field                | Notes                                                        |
| ------- | ---- | -------------------- | ------------------------------------------------------------ |
| `+0x00` | u16  | region_key           | A `regioninfo.bss` region; LOC type 17 names every key of client 3474 |
| `+0x02` | u16  | region_key_dup       | Equal to `region_key`; the offset file points here           |
| `+0x04` | u8   | ban_maid             | `1`: no maid here; `0` on every row of client 3474            |
| `+0x05` | u8   | ban_world_map        | `1`: no world map                                            |
| `+0x06` | u8   | ban_character_change | `1`: no character change                                     |
| `+0x07` | u8   | ban_muster           | `1`: no muster                                               |
| `+0x08` | u8   | ban_camp             | `1`: no camp; `0` on every row of clients 1784 and 3474       |
| `+0x09` | u8   | ban_compass          | `1`: no compass                                              |
| `+0x0A` | u8   | ban_item_map         | `1`: no item map                                             |
| `+0x0B` | u8   | ban_mini_map         | `1`: no minimap                                              |
| `+0x0C` | u8   | unknown_0c           | `0` on every row of client 3474; not in client 1784           |

The rows are not sorted by key.

### `restrictcontentsregionoffset.dbss`

Bare offset table into `restrictcontentsregion.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                         |
| ------- | ----------------- | ----- | --------------------------------------------- |
| `+0x00` | u32               | count | Equals the `restrictcontentsregion.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                        |
| ------- | ---- | ----------- | ------------------------------------------------------------ |
| `+0x00` | u16  | region_key  | Key of the row it points at                                  |
| `+0x02` | u32  | data_offset | Row start + 2, at `region_key_dup`                           |
| `+0x06` | u32  | data_size   | The row without its leading `region_key`: `11` on client 3474 |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in another order than the file; on clients 1784 and 3474 every
index row points at the row with its key.

## Layout 1

Client 1784 rows have no `unknown_0c`. The offset rows have the same
layout, with `data_size` `10`.

### Row (12 bytes)

| Offset  | Type | Field                | Notes                                  |
| ------- | ---- | -------------------- | -------------------------------------- |
| `+0x00` | u16  | region_key           |                                        |
| `+0x02` | u16  | region_key_dup       |                                        |
| `+0x04` | u8   | ban_maid             | `1` on every row of client 1784        |
| `+0x05` | u8   | ban_world_map        |                                        |
| `+0x06` | u8   | ban_character_change |                                        |
| `+0x07` | u8   | ban_muster           |                                        |
| `+0x08` | u8   | ban_camp             |                                        |
| `+0x09` | u8   | ban_compass          |                                        |
| `+0x0A` | u8   | ban_item_map         |                                        |
| `+0x0B` | u8   | ban_mini_map         | `1` on `1078` and `1081` only           |

## Field Names

The flags are the `Ban_Function` sheet of a private server's
`DataSheets.bexcel` on client 1784: `RegionGroupKey`, then `Ban_Maid`,
`Ban_WorldMap`, `Ban_CharacterChange`, `Ban_Muster`, `Ban_Camp`,
`Ban_Compass`, `Ban_ItemMap` and `Ban_MiniMap`. Its 24 rows match the
client 1784 file on all 24 keys and all eight flags (an empty `Ban_Camp`
cell is `0`). The client 1784 server dump (`Instance_dumpFull.exe`) reads
the eight columns with its bool reader into consecutive bytes of the row in
this order (loader at VA `0x1408fad80`). Its check messages name the key
`_regionKey` and log "존재하지 않는 지역입니다" ("a region that does not exist")
for an unknown key, so the key is a region key, not a region group key.

Client 3474 keeps the 24 keys of client 1784 and adds 24, and its flags
differ: `ban_maid` is `0` on every row, `ban_world_map` `1` on every row,
and character change, muster, compass and item map are banned together on
7 rows (`1084`, `1542`, `1546` to `1550`). Rows `1078` and `1081`, the two
with `Ban_MiniMap` on client 1784, still ban the minimap (11 rows do),
which places the flags at the same offsets and the new byte at the end.

## Notes

- The Lua names three of the flags: `__eRestrictContentsType_Maid`,
  `__eRestrictContentsType_WorldMap` and `__eRestrictContentsType_MiniMap`
  (`panel_window_maidlist_all_1.luac`, `new_worldmap.luac`,
  `worldminimap.luac`, `radar.luac`). The enum values are set by the
  client, not the Lua.
- `ToClient_RestrictContentsByRegionWithKey` takes a region key as well, and
  the symbol `eErrNoRestrictContentsByRegion` is the message the Lua shows
  when a function is blocked.

## Open Questions

### unknown_0c

Client 3474 added a ninth byte, `0` on all 48 rows. No sheet of client 1784
has a ninth `Ban_*` column, and the Lua names only three
`__eRestrictContentsType_*` values.
