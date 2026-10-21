# `buildingupgrade.dbss` Format

## Purpose

The siege buildings a guild can upgrade after placing them: a Barricade
into an Iron Barricade, a Hwacha into a Big Hwacha, a Flame Tower into an
Enhanced Flame Tower. Each row names the placed building by its character
key, the character it becomes, the upgrade time and the items the upgrade
takes. Companion `buildingupgradeoffset.dbss` lists where every row sits.
The build and repair data of the guild building kits (forts, command
posts, Indomitable Flags) is in [`buildingsource.bss`](buildingsource_bss.md).

The interaction window reads a row when the server sends
`FromClient_InteractionBuildingUpgrade` for a placed building
(`panel_interaction_renew.luac`): it takes the building's
`getCharacterStaticStatusWrapper():getBuildingUpgradeStaticStatus()`, names
the target with `getTargetCharacter():getName()` in the
`LUA_INTERACTION_UPGRADE_BARRICADE` line, lists each source item with
`getSourceItemEnchantStaticStatus(index)` and `getSourceItemNeedCount(index)`,
and on Yes calls `toClient_RequestBuildingUpgrade(actorKeyRaw)`. The upgrade
then runs under progress bar type 12, `LUA_PROGRESSBAR_UPGRADING`, while
the player's action is `BUILDING_UPGRADE`
(`panel_widget_progressbar_renew.luac`).

On client 3474 the 32 rows are these upgrades; names are LOC type 6:

| Building                                   | Upgrades to                                     | Character keys                                                       |
| ------------------------------------------ | ----------------------------------------------- | -------------------------------------------------------------------- |
| Barricade                                  | Iron Barricade                                  | `12605` to `12609`, `12742`, `12805`, `12828`                        |
| Balenos/Serendia, Calpheon/Ulukita, Valencia/Edania Barricade | the same region's Iron Barricade | `12791` to `12793`                                                  |
| Barricade                                  | Sturdy Iron Barricade                           | `2022`                                                               |
| Savage Barricade                           | Savage Iron Barricade                           | `2056`                                                               |
| Hwacha                                     | Big Hwacha                                      | `12637` to `12639`, `12811`, `12834`, `2036`                         |
| Calpheon/Ulukita, Valencia/Edania Hwacha   | the same region's Big Hwacha                    | `12763`, `12764`                                                     |
| Flame Tower                                | Enhanced Flame Tower                            | `12632` to `12634`, `12810`, `12833`, `2035`                         |
| Calpheon/Ulukita, Valencia/Edania Flame Tower | the same region's Enhanced Flame Tower       | `12760`, `12761`                                                     |
| `[장미 전쟁]` (War of the Roses) buildings | their upgrades                                  | `12688`, `12690`, `12698`                                            |

The three War of the Roses rows have no LOC type 6 name; their
`characterstatic.dbss` Korean labels are the Flame Tower (`12688` to
`12691`), the Hwacha (`12690` to `12692`) and the Barricade (`12698` to
`12699`). The Name and Target Name columns show that Korean label
(`[장미 전쟁] 화염탑`) through `character_name()`. Every row on client 3474 takes Iron Ingot x10 and Melted Copper
Shard x10, except the Savage Barricade, which takes [Savage] Iron Ingot
x10. Client 1784 has 16 rows: the `12605` to `12609` and `12632` to `12639`
rows, `2022`, `2035`, `2036`, `2056`, and `2013` (Sturdy Barricade to
`2027`), which client 3474 no longer lists. Its Barricades take Iron Ingot
x30 and Melted Copper Shard x15 (`2013`: x10 and x5), its Hwachas and Flame
Towers Steel x100 and Melted Platinum Shard x50.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                         | Bytes | Records                | Row bytes |
| ------ | -------------- | ------- | ---------------------------- | ----- | ---------------------- | --------- |
| 1      | 1784 and later | 3474    | `buildingupgrade.dbss`       | 1,288 | 63 Source Item, 32 Row | 12        |
| 1      | 1784 and later | 3474    | `buildingupgradeoffset.dbss` | 324   | 32 Index Row           | 10        |

| Layout | File                         | Known            | Unknown    |
| ------ | ---------------------------- | ---------------- | ---------- |
| 1      | `buildingupgrade.dbss`       | 1,288 B (100.0%) | 0 B (0.0%) |
| 1      | `buildingupgradeoffset.dbss` | 324 B (100.0%)   | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                     |
| ---------------------------- | -------- | ------------------------------------------------------------------------ |
| `buildingupgradeoffset.dbss` | Optional | `character_key -> (offset, size)` of every row; the rows are walked without it |
| `characterstaticoffset.dbss` | Optional | Which character keys have a `characterstatic.dbss` row to link to        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of variable rows with an empty string table.

| Offset      | Type       | Field        | Notes                                       |
| ----------- | ---------- | ------------ | ------------------------------------------- |
| `+0x00`     | char[4]    | magic        | `PABR`                                      |
| `+0x04`     | u32        | count        | Number of rows                              |
| `+0x08`     | Row[count] | rows         | See Row                                     |
| `rows+0x00` | u32        | string_count | `0`: the empty PABR string table            |
| `rows+0x04` | u32        | table_start  | End of the rows                             |
| `rows+0x08` | u32        | zero         | Always `0`                                  |

### Row (variable: 16 bytes + items)

| Offset  | Type                     | Field                | Notes                                                              |
| ------- | ------------------------ | -------------------- | ------------------------------------------------------------------ |
| `+0x00` | u16                      | character_key        | The placed building; unique; LOC type 6 names it                   |
| `+0x02` | u32                      | upgrade_time         | `90000`, `5000` on the Savage Barricade (clients 1784 and 3474); see In-Game Checks |
| `+0x06` | i32                      | upgrade_level        | `1` on every row of clients 1784 and 3474; see Open Questions       |
| `+0x0A` | u16                      | target_character_key | The character the building becomes                                 |
| `+0x0C` | u32                      | item_count           | Number of source items, at most 5                                  |
| `+0x10` | Source Item[item_count]  | items                | See Source Item                                                    |

### Source Item (12 bytes)

| Offset  | Type | Field    | Notes                                                                 |
| ------- | ---- | -------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | item_key | Item enchant key (`enchant_level << 24 \| item_id`); level `0` on every item of clients 1784 and 3474 |
| `+0x04` | i64  | count    | Number of that item                                                   |

### `buildingupgradeoffset.dbss`

A bare index: no `PABR` magic and no trailer. Read by
`parse_bare_offset_rows()` in `_common/pabr_offset.py`.

| Offset  | Type             | Field | Notes                          |
| ------- | ---------------- | ----- | ------------------------------ |
| `+0x00` | u32              | count | Equals the main file's `count` |
| `+0x04` | Index Row[count] | rows  | See Index Row                  |

### Index Row (10 bytes)

| Offset  | Type | Field         | Notes                                                          |
| ------- | ---- | ------------- | -------------------------------------------------------------- |
| `+0x00` | u16  | character_key | The main row's `character_key`                                 |
| `+0x02` | u32  | offset        | Start of the row in `buildingupgrade.dbss`, at its `character_key` |
| `+0x06` | u32  | size          | Full row length, `16 + 12 x item_count`                        |

On clients 1784 and 3474 the index rows run in the main file's order and
tile it from `0x08` to `table_start` with no gap.

## Field Names

The names are the columns of the `BuildingUpgrade_Table` sheet: `Index`,
`UpgradeTime`, `SourceItemKey00` to `SourceItemKey04` with `ItemCount00` to
`ItemCount04`, `TargetCharacterKey` and `UpgradeLevel`. `Index` holds the
building's character key, so the field is `character_key`.

| Source                                   | Rows | Matches                                                                            |
| ---------------------------------------- | ---- | ---------------------------------------------------------------------------------- |
| Private server `DataSheets.bexcel`, client 1784 | 17 | 16 of 16 client 1784 rows in every column; client 3474 shares 15 keys, with the same time, level and target on all 15 and the same items on 1 (`2056`) |
| Private server `BuildingUpgrade_Table`, client 519 | 5 | `2022`, `2013`, `2056`, `2035`, `2036`, every column as in the client 1784 file |

The 17th sheet row, `2085` with item `720767`, is not in any client file.
The 14 client 3474 rows whose items differ from the sheet take Iron Ingot
x10 and Melted Copper Shard x10 instead.

The server dump of the same private server on client 1784 loads the sheet in
`Load_BuildingUpgrade_Table` (VA `0x140934ae0`). It reads `Index` as an int,
keeps the low u16 and rejects a key the character table does not hold, does
the same for `TargetCharacterKey`, then reads `SourceItemKey%02d` and
`ItemCount%02d` for 0 to 4 as ints, stopping at the first empty
`SourceItemKey`, and rejects an item key of `0` or one the item table does
not hold. Each item goes into a vector of 16-byte (item key, int64 count)
pairs. `UpgradeTime` and `UpgradeLevel` are read as ints into one 8-byte
block, time first. The 2016 `gc::BuildingUpgradeStaticStatus` has `_key`
(u16), `_isBlockedUpgrade` (bool), `_sourceItemKey`
(`pa_vector<std::pair<gc::ItemEnchantKey,__int64>>`), `_upgradeTime`
(unsigned int) and `_targetCharacterKey` (u16); it has no upgrade level, and
the file stores no `_isBlockedUpgrade`.

## Notes

- The item descriptions (LOC type 0, `str_id4` `1`) of the placeable guild
  buildings still list the client 1784 materials on client 3474: "Iron
  Ingot x30, Melted Copper Shard x15" for `[Guild] Barricade (Tier 1)`
  (`44702`) and `[Guild] [Tier 2] Barricade (Conquest War)` (`767193`),
  "Steel x100, Melted Platinum Shard x50" for `[Guild] Hwacha (Tier 3)`
  (`56743`). The LOC type 108 Hwacha text keyed `59791` / `12834` lists
  "Iron Ingot x10, Melted Copper Shard x10", as the file does. The message
  box before an upgrade reads the items from this file.

## Open Questions

### What `upgrade_level` Counts

Every row of clients 1784 and 3474 and of the client 519 table has
`UpgradeLevel` `1`. The 2016 struct has no such member, and the Lua reads
only the target, the source items and their counts. It may be the step of a
building that upgrades more than once, but no row upgrades a building that
is itself an upgrade target.

## In-Game Checks

### Upgrade Time in Milliseconds

Needs item (all):

- [Iron Ingot](https://bdocodex.com/us/item/4052/) x10
- [Melted Copper Shard](https://bdocodex.com/us/item/4057/) x10

Needs zone: a Node War or Conquest War fort where your guild has placed a
Barricade, Hwacha or Flame Tower

This checks whether `upgrade_time` is in milliseconds.

1. Interact with the placed building and pick the upgrade action.
2. Confirm the message box that lists the materials.
3. Time the Upgrading progress bar from start to end.

Expected result: the bar takes about 90 seconds, so `upgrade_time` `90000`
is milliseconds. A bar of 90,000 seconds or one that ends at once means
another unit.
