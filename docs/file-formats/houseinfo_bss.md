# `houseinfo.bss` Format

## Purpose

The node houses of the world map: one variable-length row per house with
the house's character key, the contribution points it costs, its town and
worldmap node, its house group and floor, the houses that must be bought
before it, and its uses ("crafts": a `houseinforeceipe.dbss` receipe and the
highest level the house reaches with it). After the rows comes a product
list that maps each item to the houses whose uses make it. The client Lua
reads a row through `ToClient_GetHouseInfoStaticStatusWrapper(houseKey)`.

On client 3474 the 823 rows cover 32 towns and 78 nodes; the product list
holds 2,521 items.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes   | Records                                   | Row bytes |
| ------ | -------------- | ------- | --------------- | ------- | ----------------------------------------- | --------- |
| 2      | 2519 and later | 3474    | `houseinfo.bss` | 172,181 | 3,056 Craft, 823 House Row, 2,521 Product | 8         |
| 1      | 1230 to 2107   | 2107    | `houseinfo.bss` | 48,568  | 2,861 Craft, 766 House Row                | 8         |

| Layout | File            | Known             | Unknown        |
| ------ | --------------- | ----------------- | -------------- |
| 2      | `houseinfo.bss` | 169,712 B (98.6%) | 2,469 B (1.4%) |
| 1      | `houseinfo.bss` | 47,036 B (96.8%)  | 1,532 B (3.2%) |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                                             |
| ---------------------------- | -------- | ------------------------------------------------------------------------------------------------ |
| `houseinforeceipe.dbss`      | Optional | Korean receipe names for the uses when LOC has none; see [`houseinforeceipe.dbss`](houseinforeceipe_dbss.md) |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a house key without a row shows as plain text                |
| `languagedata_en.loc`        | Optional | House names (type 6), town names (type 17), node names (type 29), receipe names (type 16), item names (type 0) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

The PABR frame of `buffsimply.bss`: magic, row count, rows, string table and
an 8-byte trailer. The string table is empty; between the rows and the
string table sits the product list.

| Offset              | Type                    | Field         | Notes                                                    |
| ------------------- | ----------------------- | ------------- | -------------------------------------------------------- |
| `+0x00`             | char[4]                 | magic         | ASCII `PABR`                                             |
| `+0x04`             | u32                     | count         | Number of house rows; 823 on client 3474                 |
| `+0x08`             | House Row[count]        | rows          | See House Row                                            |
| `rows+0x00`         | u32                     | product_count | Number of product entries; 2,521 on client 3474          |
| `rows+0x04`         | Product[product_count]  | products      | See Product                                              |
| `products+0x00`     | String Table            | string_table  | See String Table                                         |
| `string_table+0x00` | u32                     | table_start   | Offset of the string table, where the product list ends  |
| `string_table+0x04` | u32                     | zero          | Always 0                                                 |

The rows are not sorted by key; client 3474 opens with 3823, 3822, 3821.

### House Row (variable: 33 bytes + need house keys and crafts)

| Offset                 | Type                    | Field                | Notes                                                                                   |
| ---------------------- | ----------------------- | -------------------- | --------------------------------------------------------------------------------------- |
| `+0x00`                | i16                     | need_explore_point   | Contribution points to buy the house; `getNeedExplorePoint()`, `1` to `3` on client 3474 |
| `+0x02`                | u16                     | affiliated_town      | Town the house belongs to, a `regioninfo.bss` region key (LOC type 17: `5` Velia, `32` Heidel) |
| `+0x04`                | u32                     | parent_node_key      | Worldmap node of the house (LOC type 29); `getParentNodeKey()`                          |
| `+0x08`                | u16                     | character_key        | Row key: the house's `characterstatic.dbss` character; `getHouseKey()`                  |
| `+0x0A`                | u16                     | unknown_0a           | `0xFFFF` on every row (clients 1784 and 3474); see Field Names                          |
| `+0x0C`                | u32                     | house_group          | Building the house is a floor of, `0` for a house of its own; see House Groups          |
| `+0x10`                | i32                     | house_floor          | Floor in the building, `1` up, `-1` on 3 rows; `0` when `house_group` is `0`            |
| `+0x14`                | u64                     | need_house_count     | Number of `need_house_keys`; `0` or `1` on every row (client 3474)                      |
| `+0x1C`                | u16[need_house_count]   | need_house_keys      | Houses to own before this one can be bought, keys of other rows                         |
| `need_house_keys+0x00` | u32                     | craft_count          | Number of `crafts`                                                                      |
| `need_house_keys+0x04` | Craft[craft_count]      | crafts               | The uses the house can be set to; see Craft                                             |
| `crafts+0x00`          | u8                      | unknown_after_crafts | `1` on the four Dokkebi Jar houses (3837 to 3840), `0` on every other row (client 3474) |

### Craft (8 bytes)

| Offset  | Type | Field       | Notes                                                                                      |
| ------- | ---- | ----------- | ------------------------------------------------------------------------------------------ |
| `+0x00` | u32  | receipe_key | [`houseinforeceipe.dbss`](houseinforeceipe_dbss.md) receipe key; all 106 keys used have a row (client 3474) |
| `+0x04` | u32  | level       | Highest level of the use in this house, `1` to `5`                                         |

The first craft of every row (client 3474) is receipe `2` (Storage); 777 of
the 823 rows hold receipe `0` (Residence) at level `1`, as their last craft.

### Product (variable: 12 bytes + house keys)

| Offset  | Type               | Field       | Notes                                                                  |
| ------- | ------------------ | ----------- | ---------------------------------------------------------------------- |
| `+0x00` | u32                | item_key    | Item the houses make; entries sorted by `item_key`, unique            |
| `+0x04` | u64                | house_count | Number of `house_keys`                                                 |
| `+0x0C` | u16[house_count]   | house_keys  | `character_key` of a house row, once per exchange that makes the item |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                 |
| ------- | ------------------ | ------------ | ------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3474          |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries; none in the file |

## Layout 1

Clients 1230 to 2107 have no product list: the string table follows the
rows. The House Row ends after `crafts`, with no `unknown_after_crafts`.
Only the File Layout and the House Row differ from Layout 2.

### File Layout

| Offset              | Type             | Field        | Notes                                           |
| ------------------- | ---------------- | ------------ | ----------------------------------------------- |
| `+0x00`             | char[4]          | magic        | ASCII `PABR`                                    |
| `+0x04`             | u32              | count        | 759 on client 1784                              |
| `+0x08`             | House Row[count] | rows         | See House Row                                   |
| `rows+0x00`         | String Table     | string_table | See String Table                                |
| `string_table+0x00` | u32              | table_start  | Offset of the string table, where the rows end  |
| `string_table+0x04` | u32              | zero         | Always 0                                        |

### House Row (variable: 32 bytes + need house keys and crafts)

| Offset                 | Type                  | Field              | Notes                                   |
| ---------------------- | --------------------- | ------------------ | --------------------------------------- |
| `+0x00`                | i16                   | need_explore_point | `1` to `15` on client 1784              |
| `+0x02`                | u16                   | affiliated_town    |                                         |
| `+0x04`                | u32                   | parent_node_key    |                                         |
| `+0x08`                | u16                   | character_key      |                                         |
| `+0x0A`                | u16                   | unknown_0a         |                                         |
| `+0x0C`                | u32                   | house_group        |                                         |
| `+0x10`                | i32                   | house_floor        |                                         |
| `+0x14`                | u64                   | need_house_count   |                                         |
| `+0x1C`                | u16[need_house_count] | need_house_keys    |                                         |
| `need_house_keys+0x00` | u32                   | craft_count        |                                         |
| `need_house_keys+0x04` | Craft[craft_count]    | crafts             |                                         |

## House Groups

`house_group` joins the floors of one building, each floor a house row of
its own with `house_floor` `1`, `2` and up. On client 3474, 375 rows sit in
179 groups (162 of two floors, 17 of three) and 448 rows have group `0`.
The second floor of group 1, house 2109, needs 2108, the first floor. The
three rows with floor `-1` are 2190 (group 64), 2612 (group 126) and 2696
(group 101); the private server sheet holds `-1` for the same three keys.

## Field Names

The `HouseInfo_New` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `CharacterKey`, `HouseGroup`, `HouseFloor`,
`NeedExplorePoint`, `NeedHouseKey`, `AffiliatedTown`, `ParentNode` and
`CraftList` (`2:5, 1:3, 1556:2, 0:1`, receipe and level pairs). Matched by
`CharacterKey`:

| Field                                  | Client 1784  | Client 3474 | Misses                                                              |
| -------------------------------------- | ------------ | ----------- | ------------------------------------------------------------------- |
| `need_explore_point`                   | 759 of 759   | 306 of 766  | Client 3474 lowers the points to `1` to `3`; the sheet holds up to `15` |
| `affiliated_town`, `parent_node_key`   | 759 of 759   | 766 of 766  |                                                                     |
| `house_group`, `house_floor`           | 759 of 759   | 766 of 766  | The sheet's `<null>` reads as `0`                                   |
| `need_house_keys`                      | 759 of 759   | 766 of 766  | The sheet's single `NeedHouseKey`, `<null>` for an empty list       |
| `crafts`                               | 758 of 759   | 745 of 766  | 1784: house 3133 holds receipe 1207 at level 3, the sheet 4; 3474: rebalanced uses |

The sheet has 766 keys; the client 1784 file holds 759 of them, the client
3474 file all 766 and 57 more.

The 2016 `gc::HouseInfoStaticStatus` declares `_needExplorePoint` (short),
`_affiliatedTown`, `_parentNodeKey` (int), `_needHouseKeyList`,
`_nextHouseList`, `_houseCraftList`, `_key`, `_isBlockedNpcWork` (bool),
`_territoryKey` (`KeyType<short,-1>`), `_houseGroup` (unsigned int) and
`_houseFloor` (int); `gc::HouseInfoCraft` holds `_receipeKey` and `_level`.
The file keeps that order for the fields it stores, with the two lists
moved to the end. The client Lua calls `getNeedExplorePoint()`,
`getParentNodeKey()`, `getHouseKey()`, `getNextHouseCount()`,
`getReceipeCount()` and `getReceipeByIndex()` on the row. `unknown_0a`
sits where the 2016 struct puts `_territoryKey` after `_key`, and `-1` is
that key's unset value; with `0xFFFF` on every row nothing confirms it.

`products` is in neither the sheet nor the 2016 struct. On client 3474 the
`house_keys` of each of the 2,521 entries equal, as a multiset, the houses
reached by walking every craft of every row through the
`houseinforeceipe.dbss` level lists up to the craft's `level` and taking
the `product_item_keys` of each [`itemexchangesource.bss`](itemexchangesource_bss.md)
exchange there. A house is listed once per such exchange, so 142 entries
repeat a house. 110 rows have no entry.

## Notes

- `need_house_keys` and `products` name only keys of house rows in the same
  file (580 and 44,569 keys, client 3474).
- The four manor lands and buildings of
  [`mansionlandinfo.bss`](mansionlandinfo_bss.md) are house rows here, each
  with Storage and Residence at level 1 only. The client Lua shows a manor
  land's contribution cost from `ToClient_getNeenPointMansion()` in place
  of `getNeedExplorePoint()` (`panel_window_explorepoint_usinginfo_1.luac`).
- `unknown_after_crafts` and the product list first appear on client 2519;
  client 2107 has neither.

## Open Questions

### What does `unknown_after_crafts` hold?

The byte is `1` on the four Dokkebi Jar houses of Dokkebi Forest (3837 to
3840, town 1210 Dalbeol Village, node 1788) and `0` on the other 819 rows
(client 3474). One of them holds receipe 2002 (Dokkebi Tool Workshop). The
2016 struct's `_isBlockedNpcWork` bool is a lead only; no Lua getter reads a
per-house flag that fits these four houses.
