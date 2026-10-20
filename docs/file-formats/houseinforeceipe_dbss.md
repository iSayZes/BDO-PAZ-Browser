# `houseinforeceipe.dbss` Format

## Purpose

The house uses ("receipes" in the client) a node house can be set to:
Residence, Lodging, Storage, Horse Ranch, the workshops, the processing and
packing workshops, the Shipyard and the Guild Storage levels. A row is the
receipe key, its Korean name, the house use type and icon type the client
enums name, the `houseinfoneeditem.dbss` group that prices each level, and
the item exchange recipes the house unlocks at each level.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes  | Records                 | Row bytes               |
| ------ | -------------- | ------- | ----------------------------- | ------ | ----------------------- | ----------------------- |
| 2      | 3473 and later | 3474    | `houseinforeceipe.dbss`       | 26,166 | 660 Level List, 132 Row | 4 to 376, 31 on average |
| 2      | 3473 and later | 3474    | `houseinforeceipeoffset.dbss` | 1,588  | 132 Index Row           | 12                      |
| 1      | 1784           | 1784    | `houseinforeceipe.dbss`       | 10,819 | 485 Level List, 97 Row  | 4 to 156, 16 on average |
| 1      | 1784           | 1784    | `houseinforeceipeoffset.dbss` | 1,168  | 97 Index Row            | 12                      |

| Layout | File                          | Known            | Unknown        |
| ------ | ----------------------------- | ---------------- | -------------- |
| 2      | `houseinforeceipe.dbss`       | 24,232 B (92.6%) | 1,934 B (7.4%) |
| 2      | `houseinforeceipeoffset.dbss` | 1,588 B (100.0%) | 0 B (0.0%)     |
| 1      | `houseinforeceipe.dbss`       | 10,431 B (96.4%) | 388 B (3.6%)   |
| 1      | `houseinforeceipeoffset.dbss` | 1,168 B (100.0%) | 0 B (0.0%)     |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                                               |
| ----------------------------- | -------- | ---------------------------------------------------------------------------------- |
| `houseinforeceipeoffset.dbss` | Optional | Index `receipe_key -> (offset, size)`, see below; the handler walks the rows in order and does not load it |
| `languagedata_en.loc`         | Optional | LOC type 16, `str_id1` = `receipe_key`: the English receipe name                   |
| `houseinfoneeditem.dbss`      | Optional | Per-level need items, joined by `need_item_key`; see [`houseinfoneeditem.dbss`](houseinfoneeditem_dbss.md) |
| `itemexchangesource.bss`      | Optional | The item exchange recipes the level lists key into; see [`itemexchangesource.bss`](itemexchangesource_bss.md). The handler reads their names from the `EXCHANGE_NAME_KR` lookup index and LOC type 24 (see `docs/handler.md`) and does not open the file |

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type           | Field     | Notes                |
| ------- | -------------- | --------- | -------------------- |
| `+0x00` | u32            | row_count | `132` on client 3464 |
| `+0x04` | Row[row_count] | rows      | See Row              |

Rows are not sorted by key. On client 3464 the file opens with the Guild
Storage keys 50009 down to 50001 and ends with 28 down to 16.

### Row (variable: 25 bytes + name text and lists)

A fixed head, the inline UTF-16LE name, three bytes, five counted level
lists, a u32 and a counted byte list. Rows differ in length; a reader takes
every length from its count.

| Offset                  | Type                   | Field               | Notes                                                                 |
| ----------------------- | ---------------------- | ------------------- | --------------------------------------------------------------------- |
| `+0x00`                 | u32                    | receipe_key         | Unique row key; LOC type 16 `str_id1`                                 |
| `+0x04`                 | u16                    | need_item_key       | `houseinfoneeditem.dbss` key, see Need Item Join                     |
| `+0x06`                 | str16                  | name                | Korean receipe name, such as `무기 단조 공방`                          |
| `name+0x00`             | u8                     | house_use_type      | `CppEnums.eHouseUseType`, see House Use Type                          |
| `name+0x01`             | u8                     | icon_type           | `CppEnums.eHouseIconType`, see Icon Type                              |
| `name+0x02`             | u8                     | unknown_tail_02     | `0` on every row (client 3464)                                        |
| `name+0x03`             | Level List[5]          | level_exchanges     | Levels 1 to 5, see Level List                                         |
| `level_exchanges+0x00`  | u32                    | unknown_after_level_exchanges | `0` on every row (client 3464)                                        |
| `level_exchanges+0x04`  | u32                    | unknown_end_count   | Bytes in `unknown_end`                                                |
| `level_exchanges+0x08`  | u8[unknown_end_count]  | unknown_end         | See Open Questions                                                    |

A level list is empty when the house does nothing at that level (Residence,
Lodging, Storage, Horse Ranch and the Guild Storage rows have five empty
lists). The lists fill from level 1 up with no gap: on client 3464, 13 rows
fill no list, and the others fill 1 to 5 levels. The longest list holds 93
keys.

### Level List (variable: 4 bytes + keys)

| Offset  | Type         | Field          | Notes                       |
| ------- | ------------ | -------------- | --------------------------- |
| `+0x00` | u32          | count          | Number of keys              |
| `+0x04` | u32[count]   | exchange_keys  | Item exchange keys          |

### `houseinforeceipeoffset.dbss`

| Offset  | Type                 | Field     | Notes                                               |
| ------- | -------------------- | --------- | --------------------------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main file's `row_count`; `132` on client 3464 |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                                       |

Every index row points at the main row with the same key, and the rows tile
the main file from `0x04` to the end with no gap. The index order is neither
the main file's order nor sorted by key: it opens 50009, 50008, 50007,
50006, 50005, 50004, 50003, 1106, 50002, 1105.

### Index Row (12 bytes)

| Offset  | Type | Field       | Notes                                              |
| ------- | ---- | ----------- | -------------------------------------------------- |
| `+0x00` | u32  | receipe_key | The main row's `receipe_key`                       |
| `+0x04` | u32  | offset      | Start of the row in `houseinforeceipe.dbss`, at its `receipe_key` |
| `+0x08` | u32  | size        | Full row length, key included                      |

## Layout 1

Client 1784 rows hold `house_use_type` only, without `icon_type` and
`unknown_tail_02`, list their exchange keys as u16, and end after
`unknown_after_level_exchanges`, with no `unknown_end`. Only the Row and the
Level List differ from Layout 2.

### Row (variable: 19 bytes + name text and lists)

| Offset                 | Type          | Field                         | Notes                         |
| ---------------------- | ------------- | ----------------------------- | ----------------------------- |
| `+0x00`                | u32           | receipe_key                   |                               |
| `+0x04`                | u16           | need_item_key                 |                               |
| `+0x06`                | str16         | name                          |                               |
| `name+0x00`            | u8            | house_use_type                |                               |
| `name+0x01`            | Level List[5] | level_exchanges               |                               |
| `level_exchanges+0x00` | u32           | unknown_after_level_exchanges | `0` on every row (client 1784) |

### Level List (variable: 4 bytes + keys)

| Offset  | Type       | Field         | Notes                                    |
| ------- | ---------- | ------------- | ---------------------------------------- |
| `+0x00` | u32        | count         |                                          |
| `+0x04` | u16[count] | exchange_keys | Item exchange keys, 35013 at most on client 1784 |

## House Use Type

`house_use_type` takes the values of `CppEnums.eHouseUseType` in
`global_define_cpp_enum.lua`. The English names in the table are the LOC
type 16 names of the rows that hold each value (client 3464).

| Value | eHouseUseType            | Rows | Receipes                                                                 |
| ----- | ------------------------ | ---- | ------------------------------------------------------------------------ |
| 0     | Empty                    | 1    | Residence                                                                |
| 1     | Lodging                  | 1    | Lodging                                                                  |
| 2     | Depot                    | 10   | Storage, Guild Storage level 2 to 9                                      |
| 3     | Ranch                    | 1    | Horse Ranch                                                              |
| 4     | WeaponForgingWorkshop    | 2    | Weapon Workshop, Duvencrune Weapon Workshop                              |
| 5     | ArmorForgingWorkshop     | 1    | Armor Workshop                                                           |
| 6     | HandMadeWorkshop         | 1    | Handcraft Workshop                                                       |
| 7     | WoodCraftWorkshop        | 2    | Carpentry Workshop, Jangdok Platform                                     |
| 8     | JewelryWorkshop          | 5    | Jeweler, Manos Jeweler, Dokkebi Crystal Workshop, Safe and Risk Asset Management Bank |
| 9     | ToolWorkshop             | 5    | Tool Workshop, Old Moon Workshop, Dokkebi Tool Workshop                  |
| 10    | Refinery                 | 1    | Refinery                                                                 |
| 13    | Shipyard                 | 15   | Shipyard, Guild Shipyard, Mount Part Workshop, the five Specialties Packing rows, Imperial Trade Packing |
| 14    | CarriageWorkshop         | 9    | Wagon Workshop, Elephant Nursery                                         |
| 15    | HorseArmorWorkshop       | 2    | Horse Gear Workshop                                                      |
| 16    | FurnitureWorkshop        | 28   | Furniture Workshop, Old Moon Furniture Workshop, the six town workshops (Florin to O'draxxia) |
| 17    | LocalSpecailtiesWorkshop | 33   | Fish, Mushroom, Crop, Wood and Mineral Workshop                          |
| 18    | Wardrobe                 | 8    | Costume Mill, Old Moon Costume Mill                                      |
| 19    | SiegeWeapons             | 1    | Siege Weapon Workshop                                                    |
| 20    | ShipParts                | 4    | Ship Part Workshop, Iliya, Nampo and Cheongsa Ship Part Workshop         |
| 21    | WagonParts               | 1    | Wagon Part Workshop                                                      |
| 23    | PotteryWorkshop          | 1    | Ceramics Workshop                                                        |

No row holds 11 (ImproveWorkshop), 12 (CannonWorkshop) or 22
(AssetManagementshop); the two Asset Management Bank rows hold 8.

## Icon Type

`icon_type` takes the values of `CppEnums.eHouseIconType`. Values 0 to 23
name the same uses as `eHouseUseType`, and on those rows `icon_type` equals
`house_use_type`. The 40 rows where the two differ all hold an icon past 23
(client 3464):

| icon_type | eHouseIconType       | house_use_type | Receipes                  |
| --------- | -------------------- | -------------- | ------------------------- |
| 24        | Workshop_Florin      | 16             | Florin Workshop           |
| 25        | Workshop_Tarif       | 16             | Tarif Workshop            |
| 26        | Workshop_Arehaza     | 16             | Arehaza Workshop          |
| 27        | Workshop_Duvencrune  | 16             | Duvencrune Workshop       |
| 28        | Workshop_Grana       | 16             | Grána Workshop            |
| 29        | Workshop_Odraxxia    | 16             | O'draxxia Workshop        |
| 30        | Workshop_Fish        | 17             | Fish Workshop (7 rows)    |
| 31        | Workshop_Mushroom    | 17             | Mushroom Workshop (8)     |
| 32        | Workshop_Crop        | 17             | Crop Workshop (7)         |
| 33        | Workshop_Wood        | 17             | Wood Workshop (6)         |
| 34        | Workshop_Mineral     | 17             | Mineral Workshop (5)      |
| 35        | Jangdokdae           | 7              | Jangdok Platform          |

## Need Item Join

`need_item_key` is a key of [`houseinfoneeditem.dbss`](houseinfoneeditem_dbss.md),
whose index holds the u16 keys 1 to 11. Each of its rows holds level slots 0
to 5, and each level a transfer time and a list of (item key, count) pairs;
every item key there is 1 (Silver, LOC type 0).
On client 3464 the receipes use every key except 9, and no row's filled
level lists reach past the last level its group prices:

| need_item_key | Levels priced | Rows | Receipes                                                    |
| ------------- | ------------- | ---- | ----------------------------------------------------------- |
| 1             | 1 to 5        | 2    | Lodging, Horse Ranch                                        |
| 2             | 1 to 5        | 18   | Weapon, Duvencrune Weapon, Armor, Handcraft, Carpentry and Ceramics Workshop, Jeweler, Manos Jeweler, Dokkebi Crystal Workshop, Costume Mill, Old Moon Costume Mill, Jangdok Platform |
| 3             | none          | 1    | Residence                                                   |
| 4             | 2 to 5        | 10   | Storage, Guild Storage level 2 to 9                         |
| 5             | 1 to 2        | 42   | Processing workshops, Specialties Packing, Mount Part Workshop, Asset Management Banks |
| 6             | 1 to 3        | 1    | Refinery                                                    |
| 7             | 1 to 5        | 18   | Shipyard, Guild Shipyard, Wagon Workshop, Siege Weapon Workshop, Elephant Nursery |
| 8             | 1 to 5        | 7    | Ship Part, Wagon Part and Horse Gear Workshops              |
| 10            | 1 to 4        | 5    | Tool Workshop, Old Moon Workshop, Dokkebi Tool Workshop     |
| 11            | 1 to 5        | 28   | Furniture Workshops and the six town workshops              |

The Refinery fills three level lists and its group prices three levels; the
Tool Workshops fill up to four and their group prices four; the processing
workshops fill up to two and group 5 prices two. The house window asks for
the need items by receipe key and level
(`getNeedItemListItemKey(receipeKey, level, index)` and
`getNeedItemListItemCount` in `panel_new_housecontrol.lua`), so the client
needs a receipe-to-group link, and `need_item_key` is the field whose
groups line up with the level lists.

## Notes

- The house window builds its work list per level: it calls
  `ToClient_getHouseWorkableListByDataOnlySize(receipeKey, 1, level)` once
  per level and starts a new level row when the count is reached, and each
  entry is an item exchange
  (`ToClient_getHouseDataWorkableItemExchangeByIndex` returns a wrapper with
  `getFirstDropGroup`) in `panel_new_housecontrol.lua`. The window draws five
  grade buttons per receipe (`for level = 1, 5`).
- For Lodging, Depot and Ranch the window shows a guide line per level
  (`getWorkerCount`, `getExtendWarehouseCount`, `getExtendStableCount`)
  instead of a work list, which fits their empty level lists.
- `getGroupTypeByIndex` and `rentHouse:getHouseUseType()` return
  `eHouseUseType` values: the tutorial compares the group type with
  `CppEnums.eHouseUseType.Empty` (`tutorial_phase11_worldmapbuyhouse.lua`).
  `getIconType()` feeds `CppEnums.HouseIconType_*Texture[iconType]`.
- On client 3474 all 2,405 distinct exchange keys (5002 to 35015) are
  `itemexchangesource.bss` rows: 2,364 NonRecipeCraft, 19 LargeCraft and 22
  GuildHouseLargeCraft. 5026 (Weapon Workshop level 1) is Azwell Longsword:
  Steel x5, Pure Copper Crystal x1, Fine Tough Hide x1 and Black Stone
  Powder x5. 8801 (Shipyard level 1) is Ship License: Rowboat, starting with
  Usable Scantling x10 and Ash Plywood x20.
- The Exchanges column shows one line per filled level, each exchange as its
  name and key (`Azwell Longsword (5026)`) linked to its
  `itemexchangesource.bss` row; past four per level the rest sit behind a
  hoverable count. The `exchanges` record field holds the same texts for
  search and export.
- LOC type 16 also names 1603 "Chariot Workshop", which has no row on
  client 3464.
- Rows 50006 and 50007 both carry the Korean name `길드 창고 7단계` and the
  English "Guild Storage level 7".

## Open Questions

### unknown_end

The trailing byte list holds `0, 1, 2, 3, 4, 5` on 118 rows, `6, 7, 8` on
12 rows (2003 to 2013 and 1416 Old Moon Furniture Workshop) and `6` on 2001
Dokkebi Crystal Workshop and 2002 Dokkebi Tool Workshop (client 3464).
Read as `eHouseUseType` the values would be Empty to ArmorForgingWorkshop and
HandMade, WoodCraft and Jewelry, which does not fit a Fish Workshop. Read as
territory keys (LOC type 12) `6, 7, 8` are Kamasylvia, Drieghan and
O'dyllita, yet 27 Grána Workshop holds `0` to `5`. calpheonlabs reads the
list as accepted `eHouseUseGroupType` codes and cites `getGroupTypeByIndex`;
that call returns one value per receipe, which `house_use_type` already
holds, so it is only a lead.

### unknown_after_level_exchanges

The u32 after the five level lists is `0` on every row. It reads the same as
the count of a sixth, empty level list; `houseinfoneeditem.dbss` prices five
levels and the window draws five grade buttons, so the layout here keeps
five lists and a separate u32. calpheonlabs names it a content group key,
which no client file confirms yet.

### unknown_tail_02

The byte after `icon_type` is `0` on every row (client 3464).
