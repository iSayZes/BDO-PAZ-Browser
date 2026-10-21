# `buildingsource.bss` Format

## Purpose

The guild building kits placed for Node and Conquest Wars: forts, command
posts, field HQs, Indomitable Flags and wooden fence gates. Each row names
the kit by its item key and holds its build time, its work animation, and
the items, percent and time a repair of the placed building takes. The
siege buildings placed around them (Barricades, Hwachas, Flame Towers)
upgrade through [`buildingupgrade.dbss`](buildingupgrade_dbss.md).

On client 3474 the 78 rows fall into five repair groups; names are LOC type
0:

| Repair items          | `repair_time` | Rows | Kits                                                                                           |
| --------------------- | ------------- | ---- | ---------------------------------------------------------------------------------------------- |
| Polished Stone x1     | `40000`       | 39   | Square Forts, the regional Forts (Tier 1 to 5), Indomitable Flags, the `[Node]` forts          |
| Polished Stone x1     | `120000`      | 16   | Command Posts, Field HQs and Field Command Posts (Tier 1, Tier 2, Unlimited, `[Conquest]`)     |
| Usable Scantling x2   | `40000`       | 11   | Wooden Fence Gates and `[Guild] [Tier 1] Wooden Fence (Conquest War)` (`56071`)                |
| Polished Stone x1     | `60000`       | 9    | Strong Square and Sturdy Octagonal Forts, `[Conquest] Square Fort` (`56005`)                   |
| Polished Stone x1     | `3000000`     | 3    | `[Guild] Blue Battlefield Fort` (Tier 3 to 5, `761710` to `761712`)                            |

Every row on client 3474 has one repair item at `repair_percents` `10000`.
Seven keys (`56521` to `56525`, `56535`, `56537`) are `[장미 전쟁]` (War of
the Roses) kits with a Korean name only, and three (`59792`, `59793`,
`59795`) have no item in `itemenchant.dbss` and no LOC type 0 name. Client
1784 has 37 rows, all of them in client 3474. 22 take Impeccably Polished
Stone x1 at `7500` and Polished Stone x1 to x5 at `5000`, 5 (the command
posts and field HQs) Fine Black Stone Powder x1 at `7500` and Black Stone
Powder x5 at `5000`, and the other 10 one item at `5000`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | ------- | --------- |
| 1      | 1784 and later | 3474    | `buildingsource.bss` | 5,250 | 78 Row  | 67        |

| Layout | File                 | Known           | Unknown      |
| ------ | -------------------- | --------------- | ------------ |
| 1      | `buildingsource.bss` | 4,778 B (91.0%) | 472 B (9.0%) |

<!-- versions:end -->

## Companion Files

None. The handler names each kit and repair item through the LOC and the
item lookup index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of variable rows with an empty string table.

| Offset      | Type       | Field              | Notes                                                    |
| ----------- | ---------- | ------------------ | -------------------------------------------------------- |
| `+0x00`     | char[4]    | magic              | `PABR`                                                   |
| `+0x04`     | u32        | count              | Number of rows                                           |
| `+0x08`     | Row[count] | rows               | See Row                                                  |
| `rows+0x00` | u32        | unknown_after_rows | `0` on clients 1784 and 3474; see Open Questions         |
| `rows+0x04` | u32        | string_count       | `0`: the empty PABR string table                         |
| `rows+0x08` | u32        | table_start        | Offset of `string_count`                                 |
| `rows+0x0C` | u32        | zero               | Always `0`                                               |

### Row (variable: 51 bytes + repair lists)

| Offset                    | Type                          | Field                      | Notes                                                                      |
| ------------------------- | ----------------------------- | -------------------------- | -------------------------------------------------------------------------- |
| `+0x00`                   | u32                           | item_key                   | The kit, an item enchant key (`enchant_level << 24 \| item_id`); level `0` on every row of clients 1784 and 3474; unique |
| `+0x04`                   | u32                           | item_key_dup               | Equals `item_key` on every row of clients 1784 and 3474                    |
| `+0x08`                   | u16                           | unknown_08                 | `0` on every row of clients 1784 and 3474; see Open Questions              |
| `+0x0A`                   | u32                           | build_time                 | `50000` on every row of clients 1784 and 3474; see In-Game Checks          |
| `+0x0E`                   | u8                            | work_ani_type              | 2016 `gc::EWorkAniType`; `5` (Architecture) on every row of clients 1784 and 3474 |
| `+0x0F`                   | u64                           | repair_item_keys_count     | Number of repair items                                                     |
| `+0x17`                   | u32[repair_item_keys_count]   | repair_item_keys           | Item enchant keys, level `0` on clients 1784 and 3474                      |
| `repair_item_keys+0x00`   | u64                           | repair_item_counts_count   | Equals `repair_item_keys_count` on clients 1784 and 3474                   |
| `repair_item_keys+0x08`   | i64[repair_item_counts_count] | repair_item_counts         | How many of the repair item at the same index                              |
| `repair_item_counts+0x00` | u64                           | repair_time                | See the table in Purpose and In-Game Checks                                |
| `repair_item_counts+0x08` | u64                           | repair_percents_count      | Equals `repair_item_keys_count` on clients 1784 and 3474                   |
| `repair_item_counts+0x10` | u32[repair_percents_count]    | repair_percents            | One per repair item; see Open Questions                                    |
| `repair_percents+0x00`    | u32                           | unknown_repair_percents_00 | `0` on every row of clients 1784 and 3474; see Open Questions              |

## Work Animations

`work_ani_type` values, named after the 2016 `gc::EWorkAniType` enum, the
same enum as the `work_ani_type` of
[`itemexchangesource.bss`](itemexchangesource_bss.md#work-animations).
Every row of clients 1784 and 3474 has `5`, `eWorkAniType_Architecture`;
the enum runs from `0` Mining to `8` Breeding, and `9` is
`eWorkAniType_Count`, the value the server loader sets before it reads the
`WorkAniType` cell.

## Field Names

The names are the columns of the `BuildingSource_Table` sheet: `Index`,
`IndexType`, `WorkAniType`, `BuildTime`, `SourceItemKey00` to
`SourceItemKey04` with `ItemCount00` to `ItemCount04`, `RepairItemKey`,
`RepairItemCount`, `RepairPercent` and `RepairTime`. `Index` holds the
kit's item key, so the field is `item_key`; `RepairItemKey`,
`RepairItemCount` and `RepairPercent` are comma lists and become
`repair_item_keys`, `repair_item_counts` and `repair_percents`.

| Source                                          | Rows | Matches                                                                            |
| ----------------------------------------------- | ---- | ---------------------------------------------------------------------------------- |
| Private server `DataSheets.bexcel`, client 1784 | 37   | 37 of 37 client 1784 rows in every column; client 1784's file is byte for byte the private server's compiled `buildingsource.bss`. Client 3474 holds all 37 keys, with the same `BuildTime` and `WorkAniType` on 37 and the same `RepairTime` on 36 |
| Private server `BuildingSource_Table`, client 519 | 12 | `44294`, `56005`, `56006`, `56010`, `56011`, `56039`, `56060`, `56061`, `56070`, `56071`, `56073` and `56118`: `BuildTime`, `WorkAniType` and `RepairTime` as in the client 1784 file on all 12; one `RepairItemKey` and `RepairItemCount` per row, the last of the client 1784 lists, and no `RepairPercent` column |

On client 3474 the repair lists of the 37 shared keys differ from the
sheet: each holds one item at `10000` (see Purpose). `56775`, `[Guild]
[Tier 1] Field Command Post (Conquest War)`, has `RepairTime` `60000` in
the sheet and `120000` on client 3474. `IndexType` is `0` and every
`SourceItemKey` cell is empty in both server tables.

The server dump of the same private server on client 1784 loads the sheet
at VA `0x1409336f0` (named `Load_ServantRepair_Table` by the loader label
script, which matches three column names; the only sheet name it references
is `BuildingSource_Table`). It reads `IndexType`, then `Index` as an int:
with `IndexType` `1` it keeps the low u16 as a character key, otherwise the
u32 as an item key, and it inserts the row through a different function for
each (VA `0x140728570` and `0x140940060`). It reads `SourceItemKey%02d` and
`ItemCount%02d` for 0 to 4 into 8-byte (item key, int) pairs, `WorkAniType`
as a byte (preset `9`), `BuildTime` as an int, `RepairItemKey` and
`RepairItemCount` as comma lists into a u32 and an int64 vector,
`RepairTime` as an int into an int64, and `RepairPercent` as an int list.
The 2016 `gc::BuildingSourceStaticStatus` has `_key`
(`gc::ItemEnchantKey`), `_isBlockedBuilding` (bool), `_sourceItemKey`
(`pa_vector<std::pair<gc::ItemEnchantKey,int>>`), `_sourceItemStatic`,
`_totalPoint` (int), `_buildTime` (unsigned int), `_workAniType`
(`gc::EWorkAniType`), one `_repairItemKey`, `_repairItemCount` (`__int64`)
and `_repairTime` (unsigned `__int64`). The file stores no
`_isBlockedBuilding` and no source item list.

## Notes

- The client 3474 Lua has no reader for this table. The progress bar of
  `panel_widget_progressbar_renew.luac` shows `LUA_PROGRESSBAR_REPAIR` for
  bar type 11 while the player's action is `COMMAND_REPAIR`
  (`checkRepairKingOrLordTentAction`), and `PANEL_PROGRESSBAR_INSTALL_TENT`
  for bar type 3 while it is `BUILD_TENT`; the server sends the bar's time.
- The LOC type 0 description of `[Guild] [Tier 2] Field Command Post
  (Conquest War)` (`767208`) says the post "will be completed automatically
  after 1 hour"; its `build_time` is `50000`, as on every row.

## Open Questions

### What `unknown_08` and `unknown_after_rows` Hold

The server loader keeps `Index` as a u16 character key when `IndexType` is
`1` and inserts such a row into a second container. `unknown_08` is a u16
right after the item key, and `unknown_after_rows` is a u32 between the
rows and the string table, where a second row block would start with its
count. No row of clients 519, 1784 or 3474 has `IndexType` `1`, so both
stay `0` and neither reading can be checked. The parser rejects a non-zero
`unknown_after_rows`.

### What `unknown_repair_percents_00` Holds

The last u32 of every row is `0` on clients 1784 and 3474. The 2016 struct
has two members the file does not otherwise show, `_totalPoint` (int) and
the source item list; with no source items both would be `0`. The other
lists of the row have u64 counts, so a u32 source item count would break
the pattern.

### What `repair_percents` Measures

Client 1784 pairs Impeccably Polished Stone and Fine Black Stone Powder
with `7500`, and Polished Stone, Black Stone Powder and Usable Scantling
with `5000`; client 3474 has `10000` on every repair item. A scale of 10,000 for 100% fits, as a share of the building's
durability one repair restores per item, but no Lua or UI text reads the
value.

## In-Game Checks

### Build and Repair Time in Milliseconds

Needs item (all):

- [[Guild] Indomitable Flag](https://bdocodex.com/us/item/44294/)
- [Polished Stone](https://bdocodex.com/us/item/4068/) x1

Needs zone: a Node War or Conquest War where your guild has placed a Square
Fort

This checks whether `build_time` and `repair_time` are in milliseconds.

1. Use the Indomitable Flag at a spot where it can be installed.
2. Time the install progress bar from start to end.
3. Interact with the damaged Square Fort and pick Repair.
4. Time the Repair progress bar from start to end.

Expected result: the install bar takes about 50 seconds (`build_time`
`50000`) and the Repair bar about 40 seconds (`repair_time` `40000` for
`[Node] Square Fort` and the `[Guild] Square Fort` tiers). Bars of 50,000
and 40,000 seconds or bars that end at once mean another unit.
