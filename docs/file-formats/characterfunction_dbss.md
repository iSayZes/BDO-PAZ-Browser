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

A record is a 4-byte head, 40 function slots in a fixed order, then a 7-byte tail. Nothing is optional: a slot the NPC does not use still stores its two strings (empty) and its fields. With every string and list empty a record is 732 bytes; 1,434 of 2,146 records are exactly that plus their string text. The offsets below are positions in such an all-empty record and name the `unknown_<hex>` fields; in a real record every string and list moves what follows it.

Walking head, slots and tail ends exactly at `data_size` in all 2,146 records.

### Head (4 bytes)

| Offset   | Type | Field       | Observed                                                            |
| -------- | ---- | ----------- | ------------------------------------------------------------------- |
| `+0x000` | u8   | shop_type        | `eShopType`, see Shop Types; `0` (1,521) to `16`, `14` (ItemMarket) exactly on the 22 Central Market NPCs |
| `+0x001` | u8   | trade_group_type | `ETradeGroupType`: `1` Normal, or `2` Desert on the desert traders 45011, 45012 and 45209 |
| `+0x002` | u8   | is_smuggle_shop  | Always `0`                                                          |
| `+0x003` | u8   | servant_type     | `eServantType`: `0` Vehicle (111, the stable, guild mount and siege stable NPCs), `1` Ship (60, the wharves), `6` on the 1,975 records without a stable |

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
| 2  | `+0x018` | `shop_sell`                  | -   | 0       | | | u32 `shop_sell_group` |
| 3  | `+0x02C` | `guild_shop`                 | 4   | 63      | 길드 상점, 길드 군수품, 길드 대장 상점                              | Guild Shop, Guild Military Supply, Guild Master Shop            | u32 `guild_shop_buy_group` |
| 4  | `+0x040` | `guild_shop_sell`            | -   | 0       | | | u32 `guild_shop_sell_group` |
| 5  | `+0x054` | `trade`                      | 2   | 125     | 무역                                                               | Trade, Trading                                                  | u32 `trade_group` |
| 6  | `+0x068` | `auction` | 6 | 48 | 일꾼거래소, 황실 경매, 길드 하우스 경매, 경매 : 천년의 걸작 | Worker Exchange, Imperial Auction, Guild House Auction, Auction: Thousand Years Masterpiece | u16 `auction_key` |
| 7  | `+0x07A` | `mating` | - | 0 | | | u16 `mating_key` |
| 8  | `+0x08C` | `inn` | - | 0 | | | u16 `inn_key` |
| 9  | `+0x09E` | `reward_explore` | - | 0 | | | |
| 10 | `+0x0AE` | `learn_skill` | 10 | 53 | 기술 배우기 | Learn Skills | u8 `has_button` |
| 11 | `+0x0BF` | `repair` | 11 | 260 | 수리 | Repair | u8 `has_button` |
| 12 | `+0x0D0` | `traces_of_blood` | - | 9 | 피의 흔적 | | u8 `has_button` |
| 13 | `+0x0E1` | `storage` | 12 | 34 | 창고 | Storage | u8 `has_button` |
| 14 | `+0x0F2` | `stable` | 13 | 171 | 마구간, 선착장, 길드 선착장, 길드 탑승물 관리 | Stable, Wharf, Guild Wharf, Manage Guild Mounts | u8 `servant_where_type`, u8 list `vehicle_types` |
| 15 | `+0x107` | `transport` | 14 | 32 | 수송 | Transport | u8 `has_button` |
| 16 | `+0x118` | `transport_person` | - | 0 | | | u8 `has_button` |
| 17 | `+0x129` | `conversation` | 16 | 1,133 | 이야기 교류 | Conversation | u8 `has_button`, u8 `is_greet` |
| 18 | `+0x13B` | `create_guild` | 17 | 17 | 길드 창설 | Create Guild | u8 `has_button` |
| 19 | `+0x14C` | `node_management` | 18 | 523 | 탐험 거점 관리 | Node Management | u32 list `managed_node_keys`, u32 list `town_node_keys` |
| 20 | `+0x164` | `lord_information` | 19 | 5 | 영주 정보 | Lord Information | u8 `has_button` |
| 21 | `+0x175` | `minor_lord_menu` | - | 0 | | | u8 `has_button`, u8 `unknown_186` |
| 22 | `+0x187` | `extraction` | 21 | 53 | 추출 | Extract, Extraction | u8 `has_button` |
| 23 | `+0x198` | `imperial_delivery` | 23 | 7 | 황실 납품 | Imperial Delivery | u16 `territory_key` |
| 24 | `+0x1AA` | `unknown_1aa` | - | 0 | | | u16 `unknown_1ba` |
| 25 | `+0x1BC` | `knowledge_management` | 24 | 9 | 지식관리 | Knowledge Management | u8 `has_button` |
| 26 | `+0x1CD` | `imperial_crafting_delivery` | 25 | 13 | 황실제작 납품 | Imperial Crafting Delivery | u8 `has_button`, u8 `supply_shop_key` |
| 27 | `+0x1DF` | `imperial_fishing_delivery` | 26 | 13 | 황실낚시 납품 | Imperial Fishing Delivery | u8 `has_button` |
| 28 | `+0x1F0` | `guild_supply_shop` | - | 0 | | | u8 `has_button` |
| 29 | `+0x201` | `skill_addon` | 28 | 55 | 기술 특화 | Skill Add-on | u8 `has_button`, u8 `is_stallion_skill_training` |
| 30 | `+0x213` | `give_gift` | 29 | 24 | 선물하기 | Give Gift | u8 `has_button` |
| 31 | `+0x224` | `cleanse_gear` | 30 | 29 | 장비 정화 | Cleanse Gear | u8 `has_button` |
| 32 | `+0x235` | `black_spirit_adventure` | - | 1 | 흑정령의 모험 | | u8 `has_button` |
| 33 | `+0x246` | `central_market` | 31 | 22 | 통합 거래소 | Central Market | u16 `territory_key` |
| 34 | `+0x258` | `maritime_trade` | - | 91 | 해상 교역 | | u16 `barter_region_key` |
| 35 | `+0x26A` | `hire_sailor` | 32 | 23 | 선원 고용 | Hire Sailor | u8 `employee_job`, u8 `has_button`, u8 `unknown_27c`, u16 `employee_key` |
| 36 | `+0x27F` | `season_special_gift` | 34 | 1 | 시즌 특별 선물 | Season Special Gift | u8 `unknown_28f` |
| 37 | `+0x290` | `hall_of_honor` | 35 | 1 | 영광의 전장 | Hall of Honor | u8 `has_button` |
| 38 | `+0x2A1` | `yar` | 36 | 8 | 야르 | Yar, Yar! | u8 `unknown_2b1` |
| 39 | `+0x2B2` | `pet_training` | 38 | 6 | 반려동물 5세대 훈련 | Tier 5 Pet Training | u8 `has_button`, u8 `unknown_2c3` |
| 40 | `+0x2C4` | `lightstone` | 39 | 1 | 광명석 교환/정화 | Lightstone | u8 `unknown_2d4` |

A list is a u32 count followed by that many items. The slot keys are the parser's names, after the button text; `shop_sell` and `guild_shop_sell` are named after their item group (see Slot Fields). They and the slots `mating`, `inn`, `reward_explore`, `transport_person`, `minor_lord_menu`, `unknown_1aa` and `guild_supply_shop` never have button text.

### Tail (7 bytes)

| Offset   | Type | Field       | Observed                                         |
| -------- | ---- | ----------- | ------------------------------------------------ |
| `+0x2D5` | u8   | unknown_2d5 | `2`, or `1` on the 125 records with a Trade button |
| `+0x2D6` | u8   | unknown_2d6 | `0`, or `1` on character 62327 only             |
| `+0x2D7` | u32  | unknown_2d7 | Always `0`                                       |
| `+0x2DB` | u8   | unknown_2db | Always `1`                                       |

### Slot Fields

Offsets are positions in the all-empty record, like the Slots table: a field sits `0x10` past its slot, after the two empty strings. A list counts as its 4-byte count. `has_button` is left out; see Function Slot.

| Offset   | Type       | Field                      | Slot                         | Observed |
| -------- | ---------- | -------------------------- | ---------------------------- | -------- |
| `+0x014` | u32        | shop_buy_group             | `shop`                       | `itemmaingroup.bss` group of the Shop window's Buy tab; non-zero on 884 of the 893 shop records and nowhere else; 491 values in `32,002` to `55,053` |
| `+0x028` | u32        | shop_sell_group            | `shop_sell`                  | Group of the Sell tab: `52001` (683), `52002` (41), `32001` (16), `52004` (3), else `0`; the slot never has a button |
| `+0x03C` | u32        | guild_shop_buy_group       | `guild_shop`                 | Group of the guild shop's Buy tab; non-zero exactly on the 63 guild shop records; 11 values in `51,100` to `51,908` |
| `+0x050` | u32        | guild_shop_sell_group      | `guild_shop_sell`            | Group of the guild shop's Sell tab: `52003` on 61 of the 63 guild shop records, else `0` |
| `+0x064` | u32        | trade_group                | `trade`                      | `itemmaingroup.bss` group; non-zero exactly on the 125 trade records; 62 values in `54,002` to `54,146` |
| `+0x078` | u16        | auction_key                | `auction`                    | `140` Worker Exchange, `1001` Imperial Auction, `101` to `143` Guild House Auction, `1002`/`1003` Thousand Years Masterpiece; also `105` on 46 records without an auction button, 44 of them shop NPCs |
| `+0x08A` | u16        | mating_key                 | `mating`                     | `104` on 46 shop NPCs without an auction button, 44 of them with `auction_key` = `105` |
| `+0x09C` | u16        | inn_key                    | `inn`                        | Always `0` |
| `+0x102` | u8         | servant_where_type         | `stable`                     | `CppEnums.ServantWhereType`, see Vehicle Types; `9` without a stable |
| `+0x103` | u8 list    | vehicle_types              | `stable`                     | `CppEnums.VehicleType` values, see Vehicle Types; empty without a stable |
| `+0x13A` | u8         | is_greet                   | `conversation`               | `1` on 1,127 of the 1,133 Conversation records and on 16 others, else `0` |
| `+0x15C` | u32 list   | managed_node_keys          | `node_management`            | `exploration.bss` node keys whose `manager_family_id` is this character, in all 957 entries |
| `+0x160` | u32 list   | town_node_keys             | `node_management`            | One node on 21 records, each a town whose `exploration.bss` `representative_id` is this character (Velia `1` -> 40017) |
| `+0x186` | u8         | unknown_186                | `minor_lord_menu`            | Always `0` |
| `+0x1A8` | u16        | territory_key              | `imperial_delivery`          | Territory key, `0` to `7` on the seven Imperial Delivery NPCs (one value each), else `0xFFFF` (none) |
| `+0x1AA` | string x 2 | unknown_1aa                | `unknown_1aa`                | The slot's own `name` and `condition`; no record has button text in it |
| `+0x1BA` | u16        | unknown_1ba                | `unknown_1aa`                | Always `0xFFFF` |
| `+0x1DE` | u8         | supply_shop_key            | `imperial_crafting_delivery` | `1` exactly on the 13 Imperial Crafting Delivery records |
| `+0x212` | u8         | is_stallion_skill_training | `skill_addon`                | `1` on 3 records |
| `+0x256` | u16        | territory_key              | `central_market`             | Territory key, `0` to `6` on Central Market NPCs (`0` on 16), else `0xFFFF` (none) |
| `+0x268` | u16        | barter_region_key          | `maritime_trade`             | `regioninfo.bss` region key of the island, port or ship where this NPC barters; a different one on each of the 91 records, else `0`. [`barter_npclist.bss`](barter_npclist_bss.md) lists the same 91 keys, each with this character's ID (all 91 match, client 3464) |
| `+0x27A` | u8         | employee_job               | `hire_sailor`                | `employeestaticstatus.bss` `job`: `0` (Sailor) on the 23 Hire Sailor records, `2` on all others |
| `+0x27C` | u8         | unknown_27c                | `hire_sailor`                | Always `0` |
| `+0x27D` | u16        | employee_key               | `hire_sailor`                | `1` to `23`, a different one per Hire Sailor record. With `employee_job` and `has_button` (`1`, the level) it names the `employeestaticstatus.bss` row of the sailor for hire: all 23 records resolve (client 3464) |
| `+0x28F` | u8         | unknown_28f                | `season_special_gift`        | `1` only on the record with button text |
| `+0x2B1` | u8         | unknown_2b1                | `yar`                        | `1` on the 8 Yar records and two more |
| `+0x2C3` | u8         | unknown_2c3                | `pet_training`               | `1` on 23 records, all with Shop, Repair and Stable buttons |
| `+0x2D4` | u8         | unknown_2d4                | `lightstone`                 | `1` on the Lightstone record and on 32 stable NPCs |

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

### Shop Types

`shop_type` follows the `_shopType` table of `panel_dialog_main_all.luac` (the `eShopType_` members of the 2016 client's `gc::ShopType` stop at `DayRandomShop`; `ItemMarket` and `Instrument` came later). Records per value on client 3464:

| Value | Name          | Records |
| ----- | ------------- | ------: |
| `0`   | None          | 1,521   |
| `1`   | Potion        | 144     |
| `2`   | Weapon        | 105     |
| `3`   | Jewel         | 16      |
| `4`   | Furniture     | 38      |
| `5`   | Collect       | 59      |
| `6`   | Fish          | 38      |
| `7`   | Worker        | 31      |
| `8`   | Alchemy       | 1       |
| `9`   | Cook          | 35      |
| `10`  | PC            | 0       |
| `11`  | Grocery       | 90      |
| `12`  | RandomShop    | 23      |
| `13`  | DayRandomShop | 10      |
| `14`  | ItemMarket    | 22      |
| `15`  | Instrument    | 4       |
| `16`  | (`_Count`)    | 9       |

The 9 records with `16` (47022, 46041, 50973, 49525 to 49529, 49548) store the enum's `_Count`.

## Field Names

Most names above come from two sources. The 2016 client (build of 2016-01-11) ships with debug symbols: its `gc::CharacterFunctionStaticStatus` starts with `_shopType`, `_tradeGroupType`, `_isSmuggleShop` and `_servantType`, then holds a name, a condition and the slot fields for each function in this order: BuyingFromNpc, SellingToNpc, BuyingFromGuildShopNpc, SellingToGuildShopNpc, Trading, Auction (`_auctionKey`), Mating (`_matingKey`), Inn (`_innKey`), RewardExplore, TrainSkill, Repair, Warehouse, Stable, Transfer, TransferPerson, IntimacyGame (`_isIntimacyGame`, `_isGreet`), Guild, Explore (`_exploreWaypoints`, `_guideWaypoints`), LordMenu, MinorLordMenu (`_minorLordRegionKey`), Extract, TerritoryTrade, TerritorySupply, ItemMarket, Knowledge, SupplyShop, FishSupplyShop and GuildSupplyShop. The server-side `CharacterFunction_Table` of the BdoEmu server (about 2021) has a column for each, and I matched every column against every field over the 1,318 characters it shares with the client file.

The LOC index of a button is the function's place in that column order: `0` BuyingFromNpc, `2` Trading, `4` BuyingFromGuildShopNpc, `6` Auction, `10` TrainSkill ... `23` TerritorySupply, `27` GuildSupplyShop, `31` NewItemMarket, `32` Employee.

Matches on client 3464 (1,318 shared characters):

| Field                        | Slot                         | `CharacterFunction_Table` column | Matching |
| ---------------------------- | ---------------------------- | -------------------------------- | -------: |
| shop_type                    | head                         | `ShopType`                       | 1,302    |
| trade_group_type             | head                         | `TradeGroupType`                 | 1,318    |
| auction_key                  | `auction`                    | `AuctionKey`                     | 1,318    |
| mating_key                   | `mating`                     | `MatingKey`                      | 1,318    |
| servant_where_type           | `stable`                     | `StableType`                     | 1,316    |
| vehicle_types                | `stable`                     | `StableKey`                      | 1,305    |
| is_greet                     | `conversation`               | `isGreetNpc`                     | 1,303    |
| managed_node_keys            | `node_management`            | `ExploreWaypoint`                | 1,271    |
| town_node_keys               | `node_management`            | `GuideWaypoint`                  | 1,316    |
| name, territory_key          | `imperial_delivery`          | `TerritorySupplyName`, `TerritoryKeyForTerritorySupply` | 1,317 |
| supply_shop_key              | `imperial_crafting_delivery` | `SupplyShopKey`                  | 1,318    |
| is_stallion_skill_training   | `skill_addon`                | `isStallionSkillExpTraining`     | 1,318    |
| name                         | `black_spirit_adventure`     | `DiceGame`                       | 1,318    |
| name, territory_key          | `central_market`             | `NewItemMarketName`, `TerritoryKeyForNewItemMarket` | 1,317 |
| name, barter_region_key             | `maritime_trade`             | `BarterName`, `isBarter`         | 1,318    |
| employee_job, employee_key   | `hire_sailor`                | `EmployeeJob`, `EmployeeType`    | 1,318    |

The `territory_key` fields hold `0xFFFF` where the server column is empty, and `employee_job` holds `2`. `is_smuggle_shop`, `servant_type`, `inn_key` and the slots `reward_explore`, `transport_person`, `minor_lord_menu` and `guild_supply_shop` have no server column with values; they are named from their place in the 2016 member order between matched fields. `servant_type` follows `gc::ServantType` (`0` Vehicle, `1` Ship, `2` Pet), which the stable records bear out (see Head). The old `auction` slot fields (`unknown_078` u32, 14 skipped bytes, `unknown_08a` u32, 32 skipped bytes) were the auction key and the empty Mating, Inn and RewardExplore slots read across.

## Suggested UI Layout

| Column        | Type | Notes                                                                                   |
| ------------- | ---- | --------------------------------------------------------------------------------------- |
| Character ID  | num  | `character_id`                                                                          |
| Name          | text | LOC type `6`; shown only when LOC is loaded                                             |
| Functions     | text | Button of each slot with button text, in slot order: LOC type `32` (`str_id1` = character ID, `str_id4` = the slot's LOC index), else the Korean `name` |
| Shop Type     | text | `shop_type` member name; `-` for `None`                                                 |
| Managed Nodes | text | `managed_node_keys` by LOC type `29` name (`Bambu Valley - Mining` for sub-nodes), else the key |
| Town          | text | `town_node_keys` the same way                                                           |
| Item Groups   | text | Each non-zero `*_group` field as a label (Shop, Shop (Sell), Guild Shop, Guild Shop (Sell), Trade) and the group ID linking to its `itemmaingroup.bss` row, one per line |
| Mounts        | text | `vehicle_types` as `value EnumName` (`0 Horse`), each value once, in stored order        |

Conditions, `servant_where_type` and the `unknown_*` fields stay out of the table.

## Notes

- 97 records have no button text in any slot.
- LOC type `32` names buttons for 2,049 of the 2,146 characters. It also holds 69 characters this file has no record for, and an index `33` (`temp` or `[PH]`) on 436 records, 414 of them Node Management NPCs, that matches no slot.
- The slot order is close to, but not the same as, the client's `CppEnums.ContentsType` (`Contents_Shop`, `Contents_Skill`, `Contents_Repair`, `Contents_Auction`, `Contents_Warehouse`, `Contents_IntimacyGame`, `Contents_Stable`, ... in `global_define_cpp_enum.luac`), and the LOC indexes do not follow the slot order either (Trade is LOC `2` but the fifth slot): they follow the column order of `CharacterFunction_Table`, see Field Names.
- `itemtradegrouptonpc.dbss` is keyed by character ID too (47747 is a trade NPC), so `trade_group` is not its key.
- `barter_region_key` values are region keys, not `exploration.bss` node keys: the barter windows key their lists by region (`ToClient_barterWrapper(RegionKey(regionKey))` in `panel_window_barterinfosearch_2.luac`).

## Open Questions

### Auction and Mating Keys

`auction_key` (`140` Worker Exchange, `1001` Imperial Auction, `101` to `143` Guild House Auction) and `mating_key` (`104`) are keys of the auction and mating tables (`gc::AuctionStaticStatus` in the 2016 client), but none of their values is an `itemmaingroup.bss` group ID (0 of 94 and 0 of 46 records, client 3464), and the client file holding those tables has not been found.

### Tail Bytes

`unknown_2d5` is `1` exactly on the 125 trade NPCs and `2` elsewhere. Neither the 2016 member list nor the server table has a field for it.

### Slots Without Button Text

`unknown_1aa` (`unknown_1ba` always `0xFFFF`) has no column match. By the LOC column order it is likely TerritoryTrade (`22`, next to TerritorySupply), but this file stores it after `imperial_delivery`, while the 2016 client stores TerritoryTrade first. `minor_lord_menu` stores `0` in both bytes, where the 2016 client had a u16 `_minorLordRegionKey`; the server still lists a region key for 155 characters.
