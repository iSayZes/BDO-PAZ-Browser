# `abyssonewarehouse.bss` Format

## Purpose

The town storages of the Magnus (`AbyssOne` in the client's names): one
row per town region with the knowledge entry of its area, an Abyssal Vein
(`Abyssal Veins - Serendia` for Heidel and Glish) or `The Magnus` itself
(Velia, Olvia, Iliya Island and Oquilla's Eye on client 3482). The file
has no PABR magic. The client opens a Magnus storage with the
`FromClient_AbyssOneWarehouseOpenNak(warehouseName)` message
`LUA_ABYSSONE_WAREHOUSE_OPEN_TITLE` (`nakmessage_warehouse_clear_all.luac`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | ------- | --------- |
| 2      | 2224 and later | 3482    | `abyssonewarehouse.bss` | 202   | 33 Row  | 6         |
| 1      | 2011 to 2203   | 2203    | `abyssonewarehouse.bss` | 260   | 22 Row  | 6         |

| Layout | File                    | Known          | Unknown    |
| ------ | ----------------------- | -------------- | ---------- |
| 2      | `abyssonewarehouse.bss` | 202 B (100.0%) | 0 B (0.0%) |
| 1      | `abyssonewarehouse.bss` | 260 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3454   | Layout 2 |
| 3412   | Layout 2 |
| 3381   | Layout 2 |
| 3349   | Layout 2 |
| 3314   | Layout 2 |
| 3283   | Layout 2 |
| 3251   | Layout 2 |
| 3212   | Layout 2 |
| 3177   | Layout 2 |
| 3144   | Layout 2 |
| 3103   | Layout 2 |
| 3062   | Layout 2 |
| 3037   | Layout 2 |
| 3002   | Layout 2 |
| 2959   | Layout 2 |
| 2923   | Layout 2 |
| 2900   | Layout 2 |
| 2872   | Layout 2 |
| 2834   | Layout 2 |
| 2803   | Layout 2 |
| 2765   | Layout 2 |
| 2736   | Layout 2 |
| 2703   | Layout 2 |
| 2665   | Layout 2 |
| 2637   | Layout 2 |
| 2606   | Layout 2 |
| 2583   | Layout 2 |
| 2545   | Layout 2 |
| 2519   | Layout 2 |
| 2498   | Layout 2 |
| 2468   | Layout 2 |
| 2438   | Layout 2 |
| 2414   | Layout 2 |
| 2384   | Layout 2 |
| 2358   | Layout 2 |
| 2335   | Layout 2 |
| 2313   | Layout 2 |
| 2290   | Layout 2 |
| 2250   | Layout 2 |
| 2224   | Layout 2 |
| 2203   | Layout 1 |
| 2179   | Layout 1 |
| 2151   | Layout 1 |
| 2134   | Layout 1 |
| 2107   | Layout 1 |
| 2073   | Layout 1 |
| 2052   | Layout 1 |
| 2011   | Layout 1 |
| 1996   | No file  |
| 1969   | No file  |
| 1937   | No file  |
| 1914   | No file  |
| 1886   | No file  |
| 1866   | No file  |
| 1838   | No file  |
| 1818   | No file  |
| 1794   | No file  |
| 1784   | No file  |
| 1749   | No file  |
| 1717   | No file  |
| 1698   | No file  |
| 1674   | No file  |
| 1636   | No file  |
| 1608   | No file  |
| 1587   | No file  |
| 1565   | No file  |
| 1537   | No file  |
| 1509   | No file  |
| 1485   | No file  |
| 1466   | No file  |
| 1445   | No file  |
| 1426   | No file  |
| 1409   | No file  |
| 1390   | No file  |
| 1372   | No file  |
| 1360   | No file  |
| 1348   | No file  |
| 1338   | No file  |
| 1324   | No file  |
| 1316   | No file  |
| 1309   | No file  |
| 1286   | No file  |
| 1256   | No file  |
| 1230   | No file  |
| 1211   | No file  |
| 1194   | No file  |
| 1177   | No file  |
| 1156   | No file  |
| 1127   | No file  |
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

None. The handler names the region (LOC type 17) and the knowledge entry
(LOC type 34) from `languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type           | Field     | Notes          |
| ------- | -------------- | --------- | -------------- |
| `+0x00` | u32            | row_count | Number of rows |
| `+0x04` | Row[row_count] | rows      | See Row        |

### Row (6 bytes)

| Offset  | Type | Field         | Notes                                                                          |
| ------- | ---- | ------------- | ------------------------------------------------------------------------------ |
| `+0x00` | u16  | region_key    | `regioninfo.bss` region key of a storage town (LOC type 17); unique per row    |
| `+0x02` | u32  | knowledge_key | Knowledge entry (LOC type 34) of the town's area; shared by the towns of one area |

## Layout 1

A list of item IDs after the rows.

### File Layout

| Offset         | Type              | Field      | Notes                                                       |
| -------------- | ----------------- | ---------- | ----------------------------------------------------------- |
| `+0x00`        | u32               | row_count  | Number of rows                                              |
| `+0x04`        | Row[row_count]    | rows       | See Row                                                     |
| `rows+0x00`    | u32               | item_count | Number of `item_ids`; `30` on client 2107                   |
| `rows+0x04`    | u32[item_count]   | item_ids   | Item IDs (LOC type 0), from `40780` Greater Blessed Spirit Essence; see Notes |

## Field Names

The Magnus is newer than client 1784: the file is not in its archives and
no sheet of a private server's `DataSheets.bexcel` on that client has
`Abyss` in its name. Both fields are named by what they resolve to. Every
`region_key` has a LOC type 17 name and is a town with a storage
(Heidel, Calpheon City, Altinova, Grána, Duvencrune, O'draxxia, Eilton,
Nampo's Moodle Village and more on client 3482). Every `knowledge_key` has
a LOC type 34 name: eleven Abyssal Vein entries, one per area, and
`11358` The Magnus.

## Notes

- On client 3482, 33 towns share 12 knowledge keys: `11355` Abyssal Vein -
  Land of the Morning Light covers six towns, `11358` The Magnus four.
  The row count grows with the clients: 21 on client 2107, 28 on 2519, 31
  on 2637, 32 on 3002 and 33 on 3474.
- Layout 1 (client 2107) ends with 30 item IDs. Its last four (`59321`
  Ebenruth's Nol, `16019` Archaeologist's Map, `16016` Lafi Bedmountain's
  Upgraded Compass and `12034` Rich Merchant's Ring) are four of the five
  entries of [`othertownnotmovableitem.bss`](othertownnotmovableitem_bss.md)
  on client 2519, where this file no longer has the list. Client 2107
  does not ship `othertownnotmovableitem.bss`.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/abyssone_tables.py`: the
  region and the knowledge entry with their names. It reads Layout 2 only.

## Open Questions

### What the Knowledge Entry Unlocks

Each town carries the Abyssal Vein knowledge of its area. Whether the
storage opens in the Magnus once the character has that knowledge, or the
entry only groups the towns by area, is not in the client Lua checked
(`nakmessage_warehouse_clear_all.luac` gets the storage name only).
