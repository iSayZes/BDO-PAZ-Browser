# `regioninfo_linkandcheckvalid2.bss` Format

## Purpose

Lists, per world region, the town regions it is linked to. It has one record for every [`regioninfo.bss`](regioninfo_bss.md) region, and each list is the same list that `regioninfo.bss` stores as `unknown_d2_keys`, so this file is a stand-alone copy of those link lists. 58 regions (all of them `MainTown` or `MinorTown`) have a list; the other 1536 have none.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                | Bytes  | Records                  | Row bytes               |
| ------ | -------------- | ------- | ----------------------------------- | ------ | ------------------------ | ----------------------- |
| 1      | 1784 and later | 3473    | `regioninfo_linkandcheckvalid2.bss` | 19,574 | 1,595 Region Link Record | 10 to 98, 12 on average |

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
| `+0x0A` | u16[link_count]     | linked_region_keys | Region keys, in the same order as `regioninfo.bss` `unknown_d2_keys` for this region |

The records are not sorted by key. The file starts with regions 513, 1025, 1 (all `1 mod 512`), then 514, 1026, 2 and so on, which looks like a hash map written out in iteration order. The handler keeps file order.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                       |
| ------- | ------------------ | ------------ | --------------------------- |
| `+0x00` | u32                | string_count | `0`; the table is always empty |
| `+0x04` | pstr[string_count] | strings      | None                        |

## Notes

- **The lists form groups.** Every list holds its own region, and the links are mutual: when A lists B, B lists A. There are 12 distinct lists in client 3458. 27 regions share Velia's 41-key list (the mainland towns from Velia to Muzgar and Velandir, plus town sub-regions such as Ossuary, Velia Beach and the three Calpheon trade zones); the seven Land of the Morning Light towns share one list; Valencia City and Ancado Inner Harbor list each other; Lema Island, Iliya Island, Arehaza and Oquilla's Eye list only themselves.
- **The groups overlap rather than partition.** Shakatu lists 18 towns (Glish, Eilton, Altinova ... Angavu Outpost) but not Velia, while Glish and Eilton list both Velia and Shakatu. Hakinza Sanctuary and Aal's Revelation list nine towns from Altinova to Angavu Outpost, and Angavu Outpost lists only Shakatu, Hakinza Sanctuary, Aal's Revelation and itself.
- The record walk was checked against client 3458: all 1594 records end exactly at `string_table_start`, and every list equals `regioninfo.bss` `unknown_d2_keys`, which [`regioninfo_bss.md`](regioninfo_bss.md) describes (the extractor there calls it a warehouse group). The handler tests assert that equality, the mutual links and the self entry, so a patch that breaks any of them shows up.
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

### What the links are used for

The lists first looked like the towns between which items can be moved: the islands only list themselves, the Land of the Morning Light towns only each other, and Valencia City only Ancado Inner Harbor. Velia's list leaves out Shakatu and Valencia City though. It is not the transport network: in game, Velia's transport window sends to Valencia City (and every other town with a storage), though Valencia City is not in Velia's list. The extractor calls the same list in `regioninfo.bss` a warehouse group, but Velia's list also holds sub-regions such as Velia Beach, Ossuary and the Calpheon trade zones, which suggests the list is copied to every region of a town rather than naming warehouses. The ring shape around Edania (see Notes) points at a reachability rule, perhaps for an Edania restriction or a storage feature, but I have found nothing in the client that reads it.

### What `unknown_06` holds

The u32 between `link_count` and the keys is `0` in every record. It may be the count of a second, always empty list, like the vector list that follows the keys in `regioninfo.bss`; no record has a non-zero value to test that against.
