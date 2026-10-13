# `characterfunction.dbss` Format

## Purpose

The dialog functions of every NPC: one record per character, holding the buttons its dialog window offers (Shop, Repair, Stable, Conversation, Node Management and so on), each with its Korean button text and an optional condition script that hides it. The Node Management slot also lists the nodes the NPC manages and the town it represents, the shop, guild shop and trade slots point at the [`itemmaingroup.bss`](itemmaingroup_bss.md) item lists of their Buy and Sell tabs, and the stable slot lists the vehicle types it keeps.

Example:

```text
character 40025 Emma Bartali  -> Trade, Conversation, Node Management
                                 manages Bartali Farm (21), Potato Farming (131), ... Specialties (104)
character 40017 Igor Bartali  -> represents Velia (node 1)
character 24646 Cradle - Sol Magia -> Shop, Repair
character 47459 Benyamin      -> Shop: buy group 50503 (potions), sell group 52001
character 59279 Miles         -> Stable: 53 RaceHorse
```

## Companion Files

| File                           | Required | Role                                                              |
| ------------------------------ | -------- | ----------------------------------------------------------------- |
| `characterfunctionoffset.dbss` | Required | Maps `character_id` to the byte offset and size of its record     |
| `languagedata_en.loc`          | Optional | NPC names (type `6`), button text (type `32`), node names (type `29`) |

All multi-byte values are little-endian. A string is a u64 length in UTF-16 code units followed by UTF-16LE text with no terminator.

## File Layout

### `characterfunction.dbss`

| Offset  | Type | Field   | Notes                                                            |
| ------- | ---- | ------- | ---------------------------------------------------------------- |
| `+0x00` | u32  | count   | Record count; `2,146` on client 3458, equal to the offset count  |
| `+0x04` | ...  | records | Back to back: a u16 `character_id`, then the record it keys      |

Each record is preceded by a u16 inline copy of its `character_id`; `data_offset` points just past it, as in `characterstatic.dbss`. The first record's ID sits at `+0x04` and its data at `+0x06`, every gap between records is exactly those 2 bytes, and the last record ends at end of file. Records are not stored in key order.

### `characterfunctionoffset.dbss`

PABR index with 10-byte rows.

| Offset  | Type  | Field | Notes                          |
| ------- | ----- | ----- | ------------------------------ |
| `+0x00` | u8[4] | magic | `PABR` (ASCII)                 |
| `+0x04` | u32   | count | Number of rows; `2,146`        |

#### Index Row (10 bytes, repeated `count` times)

| Offset  | Type | Field        | Notes                                                   |
| ------- | ---- | ------------ | ------------------------------------------------------- |
| `+0x00` | u16  | character_id | Unique; observed `9,999` to `64,780`, unsorted          |
| `+0x02` | u32  | data_offset  | Absolute offset of the record, just past its inline ID  |
| `+0x06` | u32  | data_size    | Record size; observed `740` to `3,102`                  |

#### Trailer (12 bytes)

| Offset  | Type | Field       | Observed | Notes                       |
| ------- | ---- | ----------- | -------- | --------------------------- |
| `+0x00` | u32  | reserved_a  | `0`      |                             |
| `+0x04` | u32  | end_of_rows | `21,468` | `8 + count * 10`            |
| `+0x08` | u32  | reserved_b  | `0`      |                             |

## Record Structure

A record is a 4-byte head, 37 function slots in a fixed order, then a 7-byte tail. Nothing is optional: a slot the NPC does not use still stores its two strings (empty) and its fields. With every string and list empty a record is 732 bytes; 1,434 of 2,146 records are exactly that plus their string text. The offsets below are positions in such an all-empty record and name the `unknown_<hex>` fields; in a real record every string and list moves what follows it.

Walking head, slots and tail ends exactly at `data_size` in all 2,146 records.

### Head (4 bytes)

| Offset   | Type | Field       | Observed                                                            |
| -------- | ---- | ----------- | ------------------------------------------------------------------- |
| `+0x000` | u8   | unknown_000 | `0` (1,521) to `16`; `14` on 22 Central Market NPCs without a shop  |
| `+0x001` | u8   | unknown_001 | `1`, or `2` on characters 45011, 45012 and 45209                    |
| `+0x002` | u8   | unknown_002 | Always `0`                                                          |
| `+0x003` | u8   | unknown_003 | `6` (1,975), `0` (111) or `1` (60)                                  |

### Function Slot

| Order | Type   | Field       | Notes                                                                                   |
| ----- | ------ | ----------- | --------------------------------------------------------------------------------------- |
| 1     | string | name        | Korean button text, empty when the NPC lacks the function                               |
| 2     | string | condition   | Script that must pass for the button to show, e.g. `isContentsGroupOpen(0,4004);`       |
| 3     | ...    | slot fields | Per slot, see below                                                                     |

`give_gift`, `cleanse_gear` and `black_spirit_adventure` store `condition` before `name`. Conditions use the client's script calls (`isContentsGroupOpen`, `checkexplore`, `clearquest`, `getlevel`, `getIntimacy`), joined with `;` and alternatives split by `<or>`.

On the slots with a `has_button` field, that u8 is `1` exactly when `name` is not empty, in every record.

### Slots

`LOC` is the `str_id4` of the slot's button in LOC type `32`, whose `str_id1` is the character ID. Its English text for each Korean `name` is listed alongside; slots with `-` have no LOC text. Counts are records with button text on client 3458.

| #  | Offset   | Slot                         | LOC | Records | Korean names                                                       | LOC text                                                        | Slot fields |
| -- | -------- | ---------------------------- | --- | ------: | ------------------------------------------------------------------ | --------------------------------------------------------------- | ----------- |
| 1  | `+0x004` | `shop`                       | 0   | 893     | 상점, 환전소, 비밀 상점, 일꾼 계약, 그믐달 상점, ... (25 names)      | Shop, Currency Exchange, Secret Shop, Contract Workers, Old Moon Shop, War Shop (Tier 1) ... | u32 `shop_buy_group` |
| 2  | `+0x018` | `shop_sell`                  | -   | 0       |                                                                    |                                                                 | u32 `shop_sell_group` |
| 3  | `+0x02C` | `guild_shop`                 | 4   | 63      | 길드 상점, 길드 군수품, 길드 대장 상점                              | Guild Shop, Guild Military Supply, Guild Master Shop            | u32 `guild_shop_buy_group` |
| 4  | `+0x040` | `guild_shop_sell`            | -   | 0       |                                                                    |                                                                 | u32 `guild_shop_sell_group` |
| 5  | `+0x054` | `trade`                      | 2   | 125     | 무역                                                               | Trade, Trading                                                  | u32 `trade_group` |
| 6  | `+0x068` | `auction`                    | 6   | 48      | 일꾼거래소, 황실 경매, 길드 하우스 경매, 경매 : 천년의 걸작          | Worker Exchange, Imperial Auction, Guild House Auction, Auction: Thousand Years Masterpiece | u32 `unknown_078`, u8[14] `unknown_07c`, u32 `unknown_08a`, u8[32] `unknown_08e` |
| 7  | `+0x0AE` | `learn_skill`                | 10  | 53      | 기술 배우기                                                        | Learn Skills                                                    | u8 `has_button` |
| 8  | `+0x0BF` | `repair`                     | 11  | 260     | 수리                                                               | Repair                                                          | u8 `has_button` |
| 9  | `+0x0D0` | `traces_of_blood`            | -   | 9       | 피의 흔적                                                          |                                                                 | u8 `has_button` |
| 10 | `+0x0E1` | `storage`                    | 12  | 34      | 창고                                                               | Storage                                                         | u8 `has_button` |
| 11 | `+0x0F2` | `stable`                     | 13  | 171     | 마구간, 선착장, 길드 선착장, 길드 탑승물 관리                       | Stable, Wharf, Guild Wharf, Manage Guild Mounts                 | u8 `servant_where_type`, u8 list `vehicle_types` |
| 12 | `+0x107` | `transport`                  | 14  | 32      | 수송                                                               | Transport                                                       | u8 `has_button` |
| 13 | `+0x118` | `unknown_118`                | -   | 0       |                                                                    |                                                                 | u8 `has_button` |
| 14 | `+0x129` | `conversation`               | 16  | 1,133   | 이야기 교류                                                        | Conversation                                                    | u8 `has_button`, u8 `unknown_13a` |
| 15 | `+0x13B` | `create_guild`               | 17  | 17      | 길드 창설                                                          | Create Guild                                                    | u8 `has_button` |
| 16 | `+0x14C` | `node_management`            | 18  | 523     | 탐험 거점 관리                                                     | Node Management                                                 | u32 list `managed_node_keys`, u32 list `town_node_keys` |
| 17 | `+0x164` | `lord_information`           | 19  | 5       | 영주 정보                                                          | Lord Information                                                | u8 `has_button` |
| 18 | `+0x175` | `unknown_175`                | -   | 0       |                                                                    |                                                                 | u8 `has_button`, u8 `unknown_186` |
| 19 | `+0x187` | `extraction`                 | 21  | 53      | 추출                                                               | Extract, Extraction                                             | u8 `has_button` |
| 20 | `+0x198` | `imperial_delivery`          | 23  | 7       | 황실 납품                                                          | Imperial Delivery                                               | u16 `unknown_1a8` |
| 21 | `+0x1AA` | `unknown_1aa`                | -   | 0       |                                                                    |                                                                 | u16 `unknown_1ba` |
| 22 | `+0x1BC` | `knowledge_management`       | 24  | 9       | 지식관리                                                           | Knowledge Management                                            | u8 `has_button` |
| 23 | `+0x1CD` | `imperial_crafting_delivery` | 25  | 13      | 황실제작 납품                                                      | Imperial Crafting Delivery                                      | u8 `has_button`, u8 `unknown_1de` |
| 24 | `+0x1DF` | `imperial_fishing_delivery`  | 26  | 13      | 황실낚시 납품                                                      | Imperial Fishing Delivery                                       | u8 `has_button` |
| 25 | `+0x1F0` | `unknown_1f0`                | -   | 0       |                                                                    |                                                                 | u8 `has_button` |
| 26 | `+0x201` | `skill_addon`                | 28  | 55      | 기술 특화                                                          | Skill Add-on                                                    | u8 `has_button`, u8 `unknown_212` |
| 27 | `+0x213` | `give_gift`                  | 29  | 24      | 선물하기                                                           | Give Gift                                                       | u8 `has_button` |
| 28 | `+0x224` | `cleanse_gear`               | 30  | 29      | 장비 정화                                                          | Cleanse Gear                                                    | u8 `has_button` |
| 29 | `+0x235` | `black_spirit_adventure`     | -   | 1       | 흑정령의 모험                                                      |                                                                 | u8 `has_button` |
| 30 | `+0x246` | `central_market`             | 31  | 22      | 통합 거래소                                                        | Central Market                                                  | u16 `unknown_256` |
| 31 | `+0x258` | `maritime_trade`             | -   | 91      | 해상 교역                                                          |                                                                 | u16 `unknown_268` |
| 32 | `+0x26A` | `hire_sailor`                | 32  | 23      | 선원 고용                                                          | Hire Sailor                                                     | u8 `unknown_27a`, u8 `has_button`, u8 `unknown_27c`, u16 `unknown_27d` |
| 33 | `+0x27F` | `season_special_gift`        | 34  | 1       | 시즌 특별 선물                                                     | Season Special Gift                                             | u8 `unknown_28f` |
| 34 | `+0x290` | `hall_of_honor`              | 35  | 1       | 영광의 전장                                                        | Hall of Honor                                                   | u8 `has_button` |
| 35 | `+0x2A1` | `yar`                        | 36  | 8       | 야르                                                               | Yar, Yar!                                                       | u8 `unknown_2b1` |
| 36 | `+0x2B2` | `pet_training`               | 38  | 6       | 반려동물 5세대 훈련                                                | Tier 5 Pet Training                                             | u8 `has_button`, u8 `unknown_2c3` |
| 37 | `+0x2C4` | `lightstone`                 | 39  | 1       | 광명석 교환/정화                                                   | Lightstone                                                      | u8 `unknown_2d4` |

A list is a u32 count followed by that many items. The slot keys are the parser's names, after the button text; `shop_sell` and `guild_shop_sell` are named after their item group (see Slot Fields). They and the four `unknown_*` slots never have button text.

### Tail (7 bytes)

| Offset   | Type | Field       | Observed                                         |
| -------- | ---- | ----------- | ------------------------------------------------ |
| `+0x2D5` | u8   | unknown_2d5 | `2`, or `1` on the 125 records with a Trade button |
| `+0x2D6` | u8   | unknown_2d6 | `0`, or `1` on character 62327 only             |
| `+0x2D7` | u32  | unknown_2d7 | Always `0`                                       |
| `+0x2DB` | u8   | unknown_2db | Always `1`                                       |

### Slot Fields

| Field               | Slot               | Observed                                                                                     |
| ------------------- | ------------------ | -------------------------------------------------------------------------------------------- |
| `shop_buy_group`    | `shop`             | `itemmaingroup.bss` group of the Shop window's Buy tab; non-zero on 884 of the 893 shop records and nowhere else; 491 values in `32,002` to `55,053` |
| `shop_sell_group`   | `shop_sell`        | Group of the Sell tab: `52001` (683), `52002` (41), `32001` (16), `52004` (3), else `0`; the slot never has a button |
| `guild_shop_buy_group` | `guild_shop`    | Group of the guild shop's Buy tab; non-zero exactly on the 63 guild shop records; 11 values in `51,100` to `51,908` |
| `guild_shop_sell_group` | `guild_shop_sell` | Group of the guild shop's Sell tab: `52003` on 61 of the 63 guild shop records, else `0` |
| `trade_group`       | `trade`            | `itemmaingroup.bss` group; non-zero exactly on the 125 trade records; 62 values in `54,002` to `54,146` |
| `unknown_078`       | `auction`          | `140` Worker Exchange, `1001` Imperial Auction, `101` to `143` Guild House Auction, `1002`/`1003` Thousand Years Masterpiece; also `105` on 46 records without an auction button, 44 of them shop NPCs |
| `unknown_08a`       | `auction`          | `104` on 46 shop NPCs without an auction button, 44 of them with `unknown_078` = `105`; the two `u8` spans around it are always zero |
| `servant_where_type` | `stable`          | `CppEnums.ServantWhereType`, see Vehicle Types; `9` without a stable                         |
| `vehicle_types`     | `stable`           | u8 list of `CppEnums.VehicleType` values, see Vehicle Types; empty without a stable          |
| `managed_node_keys` | `node_management`  | `exploration.bss` node keys whose `manager_family_id` is this character, in all 957 entries  |
| `town_node_keys`    | `node_management`  | One node on 21 records, each a town whose `exploration.bss` `representative_id` is this character (Velia `1` -> 40017) |
| `unknown_13a`       | `conversation`     | `1` on 1,127 of the 1,133 Conversation records and on 16 others, else `0`                     |
| `unknown_1a8`       | `imperial_delivery` | `0` to `7` on the seven Imperial Delivery NPCs (one value each), else `0xFFFF`              |
| `unknown_1ba`       | `unknown_1aa`      | Always `0xFFFF`                                                                              |
| `unknown_256`       | `central_market`   | `0` to `6` on Central Market NPCs (`0` on 16), else `0xFFFF`                                 |
| `unknown_268`       | `maritime_trade`   | A different value on each of the 91 records, `92` to `1,557`, else `0`                       |
| `unknown_27a`       | `hire_sailor`      | `0` on the 23 Hire Sailor records, `2` on all others                                         |
| `unknown_27d`       | `hire_sailor`      | `1` to `23`, a different one per Hire Sailor record                                          |
| `unknown_28f`       | `season_special_gift` | `1` only on the record with button text                                                  |
| `unknown_2b1`       | `yar`              | `1` on the 8 Yar records and two more                                                        |
| `unknown_2c3`       | `pet_training`     | `1` on 23 records, all with Shop, Repair and Stable buttons                                  |
| `unknown_2d4`       | `lightstone`       | `1` on the Lightstone record and on 32 stable NPCs                                           |
| `unknown_186`, `unknown_1de`, `unknown_212`, `unknown_27c` | | `unknown_1de` is `1` exactly on the 13 Imperial Crafting Delivery records; `unknown_212` is `1` on 3; the others are always `0` |

The `<Null>` text is a placeholder: `season_special_gift` stores it as `name` in 2,139 records, and LOC type `32` index `34` holds `<Null>` for 138 of them. It is not a button.

### Item Groups

The five `*_group` fields are [`itemmaingroup.bss`](itemmaingroup_bss.md) group IDs; all 884, 743, 63, 61 and 125 non-zero values are in its ID set (client 3464). The client's shop window (`panel_dialog_npcshop_all_1.luac`) has a Buy and a Sell tab, filled from `npcShop_getBuyCount()` / `npcShop_getItemBuy()` and `npcShop_getSellCount()` / `npcShop_getItemSell()`, and opens for `npcShop_isShopContents()` or `npcShop_isGuildShopContents()`. Each shop and guild shop NPC stores two groups, and their items tell them apart:

| Field                   | Example (client 3464)                                                                                       |
| ----------------------- | ----------------------------------------------------------------------------------------------------------- |
| `shop_buy_group`        | General store Benyamin (47459): group 50503, HP and MP potions; Currency Exchange Lafi Bedmountain (47745): 50022, Gold Bar 1G to 10,000G |
| `shop_sell_group`       | 52001, 11,556 items on 683 NPCs, holding Black Stone and Iron Ore but not Memory Fragment or Cron Stone; 52002 on 41 NPCs, 36 of them Currency Exchange, Gold Bars and Bartali Gold Bar; 52004 on the 3 Crow Shop NPCs, ocean materials such as Luminous Cobalt Ingot |
| `guild_shop_buy_group`  | Edan (47754): 51100, `[Guild]` potions, Parchment, Seal                                                      |
| `guild_shop_sell_group` | 52003, 390 items such as `[Guild] HP Potion (Small)`                                                                                   |
| `trade_group`           | Isobelle Encarotia (47747): 54146; every trade group lists subgroup 54001 (item 55151) under `checkexplore(103, 1)` |

`shop_sell_group` sits in its own slot right after `shop` and `guild_shop_sell_group` after `guild_shop`. 11 records set `shop_sell_group` without a shop button; all of them hold `52001`.

Checked in game (2026-10-14, client 3464): Benyamin's Shop Sell tab lists 14 items from a full inventory, Black Stone among them, and every one of them is in group `52001`, his `shop_sell_group`. The Memory Fragment in the same inventory, which `52001` does not hold, is not listed. His Purchase tab lists exactly the 18 items of his `shop_buy_group`, `50503` (HP and MP potions, Medical Kit, the two Alchemy Tools, Empty Crystal and the two Atanis Fireflies), in the order the subgroup stores them.

### Vehicle Types

`vehicle_types` is a u32 count and that many u8 `CppEnums.VehicleType` values (`global_define_cpp_enum.luac`). Every stored value is an enum member. The list is in stored order and can repeat a value: 8 stables store `53` twice.

| Button               | `servant_where_type` | `vehicle_types` (client 3464)                                                                                   |
| -------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------- |
| Stable (91)          | `0` User             | `0` Horse, `2` Camel, `3` Donkey, `9` Carriage, `28` CowCarriage, `32` MountainGoat, `40` RidableBabyElephant, `48` RepairableCarriage, `53` RaceHorse; 88 stables take all nine |
| Wharf (40)           | `0` User             | `18` Boat, `29` Raft, `33` FishingBoat, `44` PersonalBattleShip, `46` PersonTradeShip, `52` PersonalBoat, `55` FastShip, `56` CashPersonalTradeShip, `57` CashPersonalBattleShip, `60` Carrack; 34 wharves take all ten, 5 only the first three, 1 all but FastShip |
| Guild Wharf (20)     | `1` Guild            | `34` SailingBoat                                                                                                |
| Manage Guild Mounts (18) | `1` Guild        | `4` Elephant, `35` Train, `63` GuildDragon                                                                      |
| Stable, Forward Supply Depot (37094) | `2` Siege | `0` Horse, `2` Camel                                                                                  |
| Stable, Miles (59279) | `5` RaceHorse       | `53` RaceHorse                                                                                                  |

`servant_where_type` follows `CppEnums.ServantWhereType` (`ServantWhereTypeUser` 0, `Guild` 1, `Siege` 2, `RaceHorse` 5); the enum gives `5` to both `Camping` and `RaceHorse`, and the one stable with `5` takes only race horses. The `9` on the 1,975 records without a stable is past `ServantWhereTypeCount` (8).

## Suggested UI Layout

| Column        | Type | Notes                                                                                   |
| ------------- | ---- | --------------------------------------------------------------------------------------- |
| Character ID  | num  | `character_id`                                                                          |
| Name          | text | LOC type `6`; shown only when LOC is loaded                                             |
| Functions     | text | Button of each slot with button text, in slot order: LOC type `32` (`str_id1` = character ID, `str_id4` = the slot's LOC index), else the Korean `name` |
| Managed Nodes | text | `managed_node_keys` by LOC type `29` name (`Bambu Valley - Mining` for sub-nodes), else the key |
| Town          | text | `town_node_keys` the same way                                                           |
| Item Groups   | text | Each non-zero `*_group` field as a label (Shop, Shop (Sell), Guild Shop, Guild Shop (Sell), Trade) and the group ID linking to its `itemmaingroup.bss` row, one per line |
| Mounts        | text | `vehicle_types` as `value EnumName` (`0 Horse`), each value once, in stored order        |

Conditions, `servant_where_type` and the `unknown_*` fields stay out of the table.

## Notes

- 97 records have no button text in any slot.
- LOC type `32` names buttons for 2,049 of the 2,146 characters. It also holds 69 characters this file has no record for, and an index `33` (`temp` or `[PH]`) on 436 records, 414 of them Node Management NPCs, that matches no slot.
- The slot order is close to, but not the same as, the client's `CppEnums.ContentsType` (`Contents_Shop`, `Contents_Skill`, `Contents_Repair`, `Contents_Auction`, `Contents_Warehouse`, `Contents_IntimacyGame`, `Contents_Stable`, ... in `global_define_cpp_enum.luac`), and the LOC indexes do not follow the slot order either (Trade is LOC `2` but the fifth slot).
- `itemtradegrouptonpc.dbss` is keyed by character ID too (47747 is a trade NPC), so `trade_group` is not its key.
- `unknown_268` values are not `exploration.bss` node keys: only 31 of 91 match a node, and those nodes belong to other managers.

## Open Questions

### Auction Keys

`unknown_078` (`140` Worker Exchange, `1001` Imperial Auction, `101` to `143` Guild House Auction) and `unknown_08a` (`104`) look like keys into another table, but none of their values is an `itemmaingroup.bss` group ID (0 of 94 and 0 of 46 records, client 3464), and no other client table with these keys has been found.

### Head and Tail Bytes

`unknown_000` takes 16 values and is `14` on Central Market NPCs without a shop, so it is not a shop type alone. `unknown_003` is `6` on most records, and `unknown_2d5` is `1` exactly on the trade NPCs. None of them has been tied to a client enum.

### Slots Without Button Text

Four slots (`unknown_118`, `unknown_175`, `unknown_1aa`, `unknown_1f0`) never carry button text; their fields are always `0`, or `0xFFFF` for `unknown_1ba`. They may be functions whose button text the client builds itself, such as Inn or Socket.

### Territory-like Values

`unknown_1a8` (Imperial Delivery) runs `0` to `7` and `unknown_256` (Central Market) `0` to `6`, one value per town NPC (Velia `0`, Heidel `1`, Calpheon `2`), which suggests a territory index, but no table confirms it.

### Maritime Trade and Hire Sailor Values

`unknown_268` is unique per maritime trade NPC and `unknown_27d` numbers the 23 Hire Sailor NPCs `1` to `23`. What either one indexes is not known.
