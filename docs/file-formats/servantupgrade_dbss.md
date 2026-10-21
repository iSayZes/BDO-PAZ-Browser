# `servantupgrade.dbss` Format

## Purpose

Ship upgrade recipes: for each ship that can be upgraded, the ships it can
become, with the four equipped gear pieces (and their enhancement level)
the upgrade takes and up to ten material stacks. On client 3474 the file has
13 upgrades from 8 ships, such as Bartali Sailboat (31053) to Epheria
Sailboat (31001) and Epheria Caravel (31048) to Epheria Carrack: Advance
(31054).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records                       | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | ----------------------------- | --------- |
| 1      | 1485 and later | 3474    | `servantupgrade.dbss`       | 2,272 | 182 Item, 13 Upgrade, 8 Group | 12        |
| 1      | 1485 and later | 3474    | `servantupgradeoffset.dbss` | 182   | 13 Offset Row, 8 Offset Group | 10        |

| Layout | File                        | Known            | Unknown    |
| ------ | --------------------------- | ---------------- | ---------- |
| 1      | `servantupgrade.dbss`       | 2,272 B (100.0%) | 0 B (0.0%) |
| 1      | `servantupgradeoffset.dbss` | 182 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                    |
| ----------------------------- | -------- | ------------------------------------------------------- |
| `servantupgradeoffset.dbss`   | Optional | Index: per ship, per target ship, the upgrade's offset and size |
| `languagedata_en.loc`         | Optional | Ship names (LOC type 6) and item names (LOC type 0)     |
| `characterstaticoffset.dbss`  | Optional | Every `characterstatic.dbss` key, so a ship ID without a row shows as plain text instead of a link |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type                | Field       | Notes                                          |
| ------- | ------------------- | ----------- | ---------------------------------------------- |
| `+0x00` | u32                 | group_count | Ships with upgrades: 8 on client 3474          |
| `+0x04` | Group[group_count]  | groups      | Back to back, up to EOF                        |

### Group (variable: 4 bytes + upgrades)

| Offset  | Type                   | Field         | Notes                                        |
| ------- | ---------------------- | ------------- | -------------------------------------------- |
| `+0x00` | u32                    | upgrade_count | 1 or 2                                       |
| `+0x04` | Upgrade[upgrade_count] | upgrades      | Every upgrade of a group has the same `character_id` |

### Upgrade (172 bytes)

| Offset  | Type      | Field                | Notes                                         |
| ------- | --------- | -------------------- | --------------------------------------------- |
| `+0x00` | u16       | character_id         | The ship before the upgrade (`servant.bss`)   |
| `+0x02` | u16       | upgrade_character_id | The ship after it                             |
| `+0x04` | Item[4]   | main_items           | The four gear pieces, such as `Bartali Sailboat: Old Figurehead` +10 |
| `+0x34` | Item[10]  | sub_items            | Materials; unused slots are all zero          |

### Item (12 bytes)

| Offset  | Type | Field    | Notes                                                          |
| ------- | ---- | -------- | -------------------------------------------------------------- |
| `+0x00` | u32  | item_key | `(enchant_level << 24) \| item_id`, the [itemenchant.dbss](itemenchant_dbss.md#key-packing) key |
| `+0x04` | u64  | count    | 1 on every main item                                           |

### `servantupgradeoffset.dbss`

| Offset  | Type                            | Field        | Notes                          |
| ------- | ------------------------------- | ------------ | ------------------------------ |
| `+0x00` | u32                             | group_count  | Equals the main file's count   |
| `+0x04` | Offset Group[group_count]       | groups       | Not in main file order         |

### Offset Group (variable: 6 bytes + entries)

| Offset  | Type                       | Field         | Notes                     |
| ------- | -------------------------- | ------------- | ------------------------- |
| `+0x00` | u16                        | character_id  | The group's ship          |
| `+0x02` | u32                        | upgrade_count | The group's upgrade count |
| `+0x06` | Offset Row[upgrade_count]  | entries       |                           |

### Offset Row (10 bytes)

| Offset  | Type | Field                | Notes                                            |
| ------- | ---- | -------------------- | ------------------------------------------------ |
| `+0x00` | u16  | upgrade_character_id | The upgrade's target ship                        |
| `+0x02` | u32  | offset               | Start of the upgrade in `servantupgrade.dbss`    |
| `+0x06` | u32  | size                 | 172 on every entry                               |

## Field Names

The names follow the `OceanShipUpgrade_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784, matched value by value over the 12
upgrades it shares with clients 1784 and 3474:

| Column | Field | Equal (client 1784) | Equal (client 3474) |
| ------ | ----- | ------------------- | ------------------- |
| `CharacterKeyShip`, `UpgradeCharacterKeyShip` | `character_id`, `upgrade_character_id` | 12 of 12 | 12 of 12 |
| `UpgradeMainItemKey_0` to `_3` | `main_items[0..3].item_key` low 24 bits | 12 | 12 |
| `MainItemEnchant_0` to `_3` | `main_items[0..3].item_key` high byte | 12 | 12 |
| `UpgradeSubItemKey_0` to `_9` | `sub_items[0..9].item_key` | 12 | 10 |
| `SubItemCount_0` to `_9` | `sub_items[0..9].count` | 12 | 6 |

The sheet has no count column for the main items. The client 3474 misses
are later changes: Bartali Sailboat (31053) to Epheria Sailboat and to
Epheria Frigate take fewer materials and 5 `Gold Bar 1,000G` (item 5) in
place of 100 `Hard Pillar` (4687), and the four upgrades to Epheria
Caravel (31048) and Epheria Galleass (31049) take 4 or 3 of one material
where client 1784 has 6. Client 3474
adds Galley (9090) to Improved Galley (9124).

## Notes

- Client 1784 has the same layout with 7 groups and 12 upgrades.
- `servantupgradeoffset.dbss` lists the groups in another order than the
  main file; on client 3474 its last entry, Galley to Improved Galley, points
  at offset 1,924, the main file's 12th upgrade.
