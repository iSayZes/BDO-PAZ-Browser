# `regioninfo_linkandcheckvalid2.bss` Format

## Purpose

Lists, per world region, the town regions a character can be sent to from it by PC delivery (Field Names). It has one record for every [`regioninfo.bss`](regioninfo_bss.md) region, and each list is the same list that `regioninfo.bss` stores as `pc_delivery_region_keys`, so this file is a stand-alone copy of those link lists. 58 regions (all of them `MainTown` or `MinorTown`) have a list; the other 1536 have none.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                | Bytes  | Records                  | Row bytes               |
| ------ | -------------- | ------- | ----------------------------------- | ------ | ------------------------ | ----------------------- |
| 1      | 1784 and later | 3474    | `regioninfo_linkandcheckvalid2.bss` | 19,574 | 1,595 Region Link Record | 10 to 98, 12 on average |

| Layout | File                                | Known            | Unknown         |
| ------ | ----------------------------------- | ---------------- | --------------- |
| 1      | `regioninfo_linkandcheckvalid2.bss` | 13,194 B (67.4%) | 6,380 B (32.6%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Region names (LOC type 17, `str_id1 = region_key`)    |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

| Offset              | Type                             | Field              | Notes |
| ------------------- | -------------------------------- | ------------------ | ----- |
| `+0x00`             | char[4]                          | magic              | `PABR` (ASCII) |
| `+0x04`             | u32                              | record_count       | Observed `1594`, the same as `regioninfo.bss` |
| `+0x08`             | Region Link Record[record_count] | records            | Variable records packed back-to-back with no alignment |
| `records+0x00`      | String Table                     | string_table       | Shared `pabr_strings` layout; always empty here (`u32 count = 0`) |
| `string_table+0x00` | u32                              | string_table_start | Absolute file offset of `string_table.count`; the record walk ends exactly there |
| `string_table+0x04` | u32                              | zero               | Observed `0` |

### Region Link Record (variable: 10 bytes + links)

A record is `10 + 2 * link_count` bytes.

| Offset  | Type                | Field              | Notes |
| ------- | ------------------- | ------------------ | ----- |
| `+0x00` | u16                 | region_key         | `regioninfo.bss` region key; unique, and the key set equals that file's |
| `+0x02` | u32                 | link_count         | Number of keys that follow; `0` on 1536 records |
| `+0x06` | u32                 | unknown_06         | `0` in every record |
| `+0x0A` | u16[link_count]     | pc_delivery_region_keys | Region keys, in the same order as `regioninfo.bss` `pc_delivery_region_keys` for this region |

The records are not sorted by key. The file starts with regions 513, 1025, 1 (all `1 mod 512`), then 514, 1026, 2 and so on, which looks like a hash map written out in iteration order. The handler keeps file order.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                       |
| ------- | ------------------ | ------------ | --------------------------- |
| `+0x00` | u32                | string_count | `0`; the table is always empty |
| `+0x04` | pstr[string_count] | strings      | None                        |

## Field Names

The 2016 client with debug symbols holds the list in `gc::RegionInfo` at
`+0x278` as `pa_vector<KeyType<u16>> _pcDeliveryRegionKeyList`. A private
server on client 1784 builds the same member in its `RegionInfo`
link-and-check step (VA `0x140c3a530`), which opens
`regionInfo_linkAndCheckValid2`: for every pair of regions with a flag set
(region byte `+0x2d`, not yet tied to a sheet column) it searches a path
over the waypoints, rejects a path through flagged waypoints, and pushes the
other region's key into this region's list, the region itself included. The
only reader of the list in that dump is the PC delivery request
(`gm::TrReservePcDeliveryReqTroc`, VA `0x141a27af9`), which looks up the
destination region in the current region's list and refuses a request whose
destination is missing; on success it calls the function that holds
`gm::PlayerActor::reservePcDelivery`. So the list is the set of regions a
character can be sent to from this region. No sheet column feeds it.

On client 1784 the 42 lists all hold their own region but are not all
mutual, since the path search runs once per ordered pair; on client 3474
the 58 lists are mutual. 5 of the 42 regions with a list on 1784 have the
same list on 3474; most grew (35 to 41 keys).

## Notes

- **The lists form groups.** Every list holds its own region, and the links are mutual: when A lists B, B lists A. There are 12 distinct lists in client 3458. 27 regions share Velia's 41-key list (the mainland towns from Velia to Muzgar and Velandir, plus town sub-regions such as Ossuary, Velia Beach and the three Calpheon trade zones); the seven Land of the Morning Light towns share one list; Valencia City and Ancado Inner Harbor list each other; Lema Island, Iliya Island, Arehaza and Oquilla's Eye list only themselves.
- **The groups overlap rather than partition.** Shakatu lists 18 towns (Glish, Eilton, Altinova ... Angavu Outpost) but not Velia, while Glish and Eilton list both Velia and Shakatu. Hakinza Sanctuary and Aal's Revelation list nine towns from Altinova to Angavu Outpost, and Angavu Outpost lists only Shakatu, Hakinza Sanctuary, Aal's Revelation and itself.
- The record walk was checked against client 3458: all 1594 records end exactly at `string_table_start`, and every list equals `regioninfo.bss` `pc_delivery_region_keys`, which [`regioninfo_bss.md`](regioninfo_bss.md) describes. The handler tests assert that equality, the mutual links and the self entry, so a patch that breaks any of them shows up.
- The file name says "link and check valid" and ends in `2`; no `regioninfo_linkandcheckvalid.bss` without the suffix exists in client 3458.

- **The lists form rings around Edania.** Grouping the 58 regions by their list gives the 12 lists (client 3458), in nine rows here since the four one-region lists only hold their own region; each list is shared by every region that owns it:

  | Size | Owned by | Compared with Velia's list |
  | ---- | -------- | -------------------------- |
  | 44   | Altinova, Asparkan, Sand Grain Bazaar, Muzgar, Velandir | adds Shakatu, Hakinza Sanctuary, Aal's Revelation |
  | 42   | Glish, Eilton, Tarif, Duvencrune, Ahib Conflict Zone, Marcha Outpost, O'draxxia, Salanar Pond, Delmira Plantation | adds Shakatu |
  | 41   | Velia, Heidel, Calpheon City, Olvia, Keplan, Port Epheria, Grána, Old Wisdom Tree and 19 more | the mainland from Velia to Muzgar, without Shakatu, Valencia City or the Edania towns |
  | 18   | Shakatu | the Mediah, Drieghan and Ulukita towns plus Hakinza Sanctuary, Aal's Revelation, Angavu Outpost |
  | 9    | Hakinza Sanctuary, Aal's Revelation | Altinova, Asparkan, Shakatu, Sand Grain Bazaar, Muzgar, Velandir and the three Edania towns |
  | 7    | the Land of the Morning Light towns | each other |
  | 4    | Angavu Outpost | Shakatu, Hakinza Sanctuary, Aal's Revelation, itself |
  | 2    | Valencia City, Ancado Inner Harbor | each other |
  | 1    | Lema Island, Iliya Island, Arehaza, Oquilla's Eye | itself |

  The deeper a town sits toward Edania, the smaller its list: Angavu Outpost reaches only Shakatu and the Edania towns, the Mediah and Ulukita towns reach both the mainland and Edania, and Velia's group reaches the mainland only. Valencia City, the islands and the Land of the Morning Light stand apart.

## Open Questions

### What `unknown_06` holds

The u32 between `link_count` and the keys is `0` in every record (1,066 on client 1784, 1,595 on 3474). It may be the upper half of a u64 `link_count`: the PABR reader of the client 1784 server reads string lengths as u64, and other PABR tables store u64 list counts. The server opens this file but reads no record from it in that build, so no code shows the width.
