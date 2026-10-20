# `characterspawntype.dbss` Format

## Purpose

NPC role flags. Each record gives one character (NPC, monster, object) 46 independent 0/1 bytes, one per value of the client's `CppEnums.SpawnType`: skill trainer, warehouse, stable, node manager (`Explorer`), shop merchant and so on. The client uses them for NPC services and town navigation.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes     | Records             | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | --------- | ------------------- | --------- |
| 2      | 3473 and later | 3474    | `characterspawntype.dbss`       | 1,178,548 | 24,553 Record       | 48        |
| 2      | 3473 and later | 3474    | `characterspawntypeoffset.dbss` | 245,550   | 24,553 Index Record | 10        |
| 1      | 1784           | 1784    | `characterspawntype.dbss`       | 690,980   | 15,704 Record       | 44        |
| 1      | 1784           | 1784    | `characterspawntypeoffset.dbss` | 157,060   | 15,704 Index Record | 10        |

| Layout | File                            | Known                | Unknown    |
| ------ | ------------------------------- | -------------------- | ---------- |
| 2      | `characterspawntype.dbss`       | 1,178,548 B (100.0%) | 0 B (0.0%) |
| 2      | `characterspawntypeoffset.dbss` | 245,550 B (100.0%)   | 0 B (0.0%) |
| 1      | `characterspawntype.dbss`       | 690,980 B (100.0%)   | 0 B (0.0%) |
| 1      | `characterspawntypeoffset.dbss` | 157,060 B (100.0%)   | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                           |
| ------------------------------- | -------- | ---------------------------------------------- |
| `characterspawntypeoffset.dbss` | Optional | Maps `character_id` to the record offset; the main file can be walked without it |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                  |
| ------- | ------------- | ------- | -------------------------------------- |
| `+0x00` | u32           | count   | Number of records; observed `24,017` in the pre-2026-09-27 fixture, `24,551` in the 2026-09-27 client |
| `+0x04` | Record[count] | records | See Record                             |

### Record (48 bytes)

| Offset  | Type   | Field        | Notes                                                        |
| ------- | ------ | ------------ | ------------------------------------------------------------ |
| `+0x00` | u16    | character_id | Unique; equals the offset-table key                          |
| `+0x02` | u8[46] | roles        | One byte per `SpawnType` value, each `0` or `1`; see Enum Values |

### `characterspawntypeoffset.dbss`

A parallel lookup index with one entry per main-file record.

| Offset              | Type                | Field          | Notes                                            |
| ------------------- | ------------------- | -------------- | ------------------------------------------------ |
| `+0x00`             | char[4]             | magic          | `PABR` (ASCII)                                   |
| `+0x04`             | u32                 | count          | Number of index records; matches main file count |
| `+0x08`             | Index Record[count] | records        | See Index Record                                 |
| `records+0x00`      | String Table        | string_table   | The 12-byte trailer starts here; see String Table |
| `string_table+0x00` | u32                 | end_of_records | Byte offset of end-of-records in this file       |
| `string_table+0x04` | u32                 | zero           | Always `0`                                       |

### Index Record (10 bytes)

| Offset  | Type | Field        | Notes                                      |
| ------- | ---- | ------------ | ------------------------------------------ |
| `+0x00` | u16  | character_id | Equals the record's own `character_id`     |
| `+0x02` | u32  | offset       | Byte offset into `characterspawntype.dbss` |
| `+0x06` | u32  | size         | Record byte count; always 48               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 1

On client 1784 `roles` holds 42 bytes, `SpawnType` values `0` to `41`, and
the record is 44 bytes; values `42` to `45` came later. On the 15,894
characters both clients hold, each of the 42 bytes agrees with the same
value on client 3473 for at least 15,852 of them. Only the Record differs
from Layout 2; the index `size` is `44`.

### Record (44 bytes)

| Offset  | Type   | Field        | Notes                          |
| ------- | ------ | ------------ | ------------------------------ |
| `+0x00` | u16    | character_id |                                |
| `+0x02` | u8[42] | roles        | `SpawnType` values `0` to `41` |

## Enum Values

### SpawnType

Names come from `CppEnums.SpawnType` in `luacscript/x64/include/global_define_cpp_enum.luac`, in the client's spelling without the `eSpawnType_` prefix. The enum has no name for value `41`, although one record sets it. Counts and examples are from the pre-2026-09-27 fixture.

The Navi label is the text the town NPC navigation widget shows for the role: `luacscript/x64/widget/townnpcnavi/panel_widget_townnpcnavi.luac` builds its label table as `SpawnType.<name>` -> `PAGetString(Defines.StringSheet_GAME, "LUA_WIDGET_TOWNNPCNAVI_NPCTYPETEXT_<n>")`, read from the Lua 5.1 bytecode on client 3458. The column shows `_<n>` and its English LOC text (type `37`, see [`stringtable.bss`](stringtable_bss.md)). 35 values have a label; values 1 to 32 use their own number, `SupplyShop` uses `_39`, `RandomShopDay` `_34` and `Instrument` `_35`. The widget uses no key for the rest, and keys `_33`, `_36`, `_37` and `_38` (Delivery, Black Spirit's Training, Abyssal Well, Silver (Church) Buffs) are not in its table. Three of those name roles the widget leaves out, so the handler uses them too (marked *not in widget* below): `_36` for `TraningVehicleShop` (its holder Hiznak is titled `<Black Spirit's Training>`), `_37` for `AbyssOneEnterPosGuide` and `_38` for `ChurchBuff`. `_33` fits no role clearly. The hash function is unknown but depends on the key string alone, so the handler stores the 38 key hashes (`navi_labels.py`) and a test checks them against `stringtable.bss`.

| Value | Offset  | SpawnType | Navi label | Records | Example |
| ----: | ------- | --------- | ---------- | ------: | ------- |
| 0 | `+0x02` | `NormalNpc` |  | 21,561 | Weakkebi (`47183`) |
| 1 | `+0x03` | `SkillTrainer` | `_1` Skill Instructor | 52 | Valks (`47653`) |
| 2 | `+0x04` | `ItemRepairer` | `_2` Repair | 255 | Alper (`47659`) |
| 3 | `+0x05` | `ShopMerchant` | `_3` General Shop | 299 | Jackson (`47727`) |
| 4 | `+0x06` | `ImportantNpc` | `_4` Important Conversation | 2,272 | Edania Merchant (`47759`) |
| 5 | `+0x07` | `TradeMerchant` | `_5` Trade Manager | 124 | Roig Mills (`47651`) |
| 6 | `+0x08` | `WareHouse` | `_6` Storage | 33 | Erdin (`47665`) |
| 7 | `+0x09` | `Stable` | `_7` Stable | 91 | Alper (`47659`) |
| 8 | `+0x0A` | `Wharf` | `_8` Wharf | 38 | Akin (`47670`) |
| 9 | `+0x0B` | `Transfer` | `_9` Transport | 31 | Erdin (`47665`) |
| 10 | `+0x0C` | `Intimacy` | `_10` Conversation | 2,145 | Jackson (`47727`) |
| 11 | `+0x0D` | `Guild` | `_11` Guild | 16 | Selim (`47666`) |
| 12 | `+0x0E` | `Explorer` | `_12` Exploration | 494 | Zaid (`47741`) |
| 13 | `+0x0F` | `Inn` | `_13` Inn | 0 |  |
| 14 | `+0x10` | `Auction` | `_14` Auction | 38 | Taner (`47657`) |
| 15 | `+0x11` | `Mating` | `_15` Merchant | 45 | Alper (`47659`) |
| 16 | `+0x12` | `Potion` | `_16` General Goods | 141 | Eileen (`47649`) |
| 17 | `+0x13` | `Weapon` | `_17` Weapons/Armor | 99 | Ferit (`47658`) |
| 18 | `+0x14` | `Jewel` | `_18` Jeweler | 15 | Emet (`47662`) |
| 19 | `+0x15` | `Furniture` | `_19` Furniture | 38 | Ergin (`47656`) |
| 20 | `+0x16` | `Collect` | `_20` Material | 58 | Daon (`47301`) |
| 21 | `+0x17` | `Fish` | `_21` Fishing Vendor | 37 | Akin (`47670`) |
| 22 | `+0x18` | `Worker` | `_22` Work Supervisor | 30 | Serdar (`47671`) |
| 23 | `+0x19` | `Alchemy` | `_23` Alchemist | 0 |  |
| 24 | `+0x1A` | `GuildShop` | `_24` Guild Shop | 59 | Zafer (`47661`) |
| 25 | `+0x1B` | `ItemMarket` | `_25` Central Market | 21 | Taner (`47657`) |
| 26 | `+0x1C` | `TerritorySupply` | `_26` Imperial Delivery | 7 | Heira (`46010`) |
| 27 | `+0x1D` | `TerritoryTrade` | `_27` Imperial Trading | 0 |  |
| 28 | `+0x1E` | `Smuggle` | `_28` Smuggle | 0 |  |
| 29 | `+0x1F` | `Cook` | `_29` Cooking | 34 | Vargas (`47740`) |
| 30 | `+0x20` | `PC` | `_30` Oasis Vendor | 0 |  |
| 31 | `+0x21` | `Grocery` | `_31` Stable Merchant | 79 | Alper (`47659`) |
| 32 | `+0x22` | `RandomShop` | `_32` Random Shop | 22 | Patrigio (`47673`), the night vendor |
| 33 | `+0x23` | `SupplyShop` | `_39` Imperial Crafting Delivery | 12 | Faruk (`47663`) |
| 34 | `+0x24` | `RandomShopDay` | `_34` Random Shop | 10 | Morco (`47466`), the day vendor |
| 35 | `+0x25` | `FishSupplyShop` |  | 12 | Burak (`47668`) |
| 36 | `+0x26` | `GuildSupplyShop` |  | 0 |  |
| 37 | `+0x27` | `GuildStable` |  | 17 | Zafer (`47661`) |
| 38 | `+0x28` | `GuildWharf` |  | 19 | Vedat (`47669`) |
| 39 | `+0x29` | `PcRoomStable` |  | 0 |  |
| 40 | `+0x2A` | `Instrument` | `_35` Instruments | 4 | Artina (`59267`) |
| 41 | `+0x2B` | `Unknown41` |  | 1 | Miles (`59279`), the Grand Prix quest giver |
| 42 | `+0x2C` | `TraningVehicleShop` | `_36` Black Spirit's Training (not in widget) | 9 | Hiznak (`47022`) |
| 43 | `+0x2D` | `AbyssOneEnterPosGuide` | `_37` Abyssal Well (not in widget) | 15 | The Magnus Entrance - Well (`61263`) |
| 44 | `+0x2E` | `ChangeMarniStone` |  | 1 | Wacky Toshi (`44638`) |
| 45 | `+0x2F` | `ChurchBuff` | `_38` Silver (Church) Buffs (not in widget) | 21 | Edania Merchant (`47766`) |

Checked in game: Wacky Toshi (`ChangeMarniStone`) exchanges Marni stones, and Miles (value `41`) hands out the Grand Prix quests, `[Daily] Grand Prix, Become the Best` (4549/11) and `[Weekly] Old Moon Grand Prix, Rider of Honor` (4549/10).

The roles fit the NPCs they are set on: stable keepers carry `Stable` and `Mating`, arms dealers `ItemRepairer` and `Weapon`, node managers `Explorer`, and the Magnus entrance wells `AbyssOneEnterPosGuide`.

## Notes

- Every record sets at least one role. 21,561 records set only `NormalNpc` (22,055 in the 2026-09-27 client), and no record sets `NormalNpc` together with another role; the other 2,456 (2,496) are service NPCs.
- Header overrides (`roleLabels` in the handler's `lang/en.json`), for roles without a Navi label or where it is too vague. `role_labels.py` combines them with the Navi labels, and the `npcsimply.bss` Kind column uses the same names:
  - `NormalNpc`: Normal NPC; no game text.
  - `RandomShop` / `RandomShopDay`: Night Vendor / Day Vendor, since both share the Navi label Random Shop (see below).
  - `FishSupplyShop`: Imperial Fishing Delivery, Burak's (`47668`) title and LOC type 32 function label.
  - `GuildStable`: Guild Stable, to match Guild Wharf; Zafer's (`47661`) LOC type 32 function label is "Manage Guild Mounts".
  - `GuildWharf`: Guild Wharf, Vedat's (`47669`) LOC type 32 function label.
  - `41`: Grand Prix, see Value 41.
  - `ChangeMarniStone`: Marni's Stone, Wacky Toshi's (`44638`) LOC type 32 function label.
- On client 3458 the 23 `RandomShop` holders are Patrigio, Dipados and Ruelle, all `<Black Market>` except Patrigio `57157` (`<Cron Gift Shop>`, probably a shop variant), and the game calls Patrigio "the night vendor" in dialogue (LOC type 39). The 10 `RandomShopDay` holders are all Morco, who only spawns in the daytime; LOC titles him `<Crow Merchant Guild>`, but in game he shows `<Day Vendor>`, a title no LOC string holds.
- 103 distinct role patterns occur (102 in the 2026-09-27 client).
- `Inn`, `Alchemy`, `TerritoryTrade`, `Smuggle`, `PC`, `GuildSupplyShop` and `PcRoomStable` are set on no record.
- An earlier version of this doc read `+0x00` as a u32 entity ID and the flags from `+0x04`. That turned the `NormalNpc` and `SkillTrainer` bytes into a fake "entity namespace" in the high 16 bits (entity `82176` is character `16640` with `NormalNpc` set) and shifted every flag index by two.
- Records are stored in offset-table order, not sorted by `character_id`.
- `ChurchBuff` (value `45`) marks the church buff sellers. The NPC's Chat option sells `[Blessing] Adventure's Boon` (120 or 300 minutes; see `buff_dbss.md`). Checked in game on Ottavio Ferre (`40016`, 2026-09-28), and all 16 NPCs in the [Black Desert Foundry, Church Buff Locations guide](https://www.blackdesertfoundry.com/church-buff-locations-guide/) carry `ChurchBuff` in client 3458. The six Land of the Morning Light NPCs among them (`47210`, `47244`, `47276`, `47349`, `47551`, `47596`) also sell the same buff as "Special Revitalizing Gukbap" for Sangpyeong Coins, per the guide. The other four holders are missing from the guide but sell the buff too, checked in game (2026-09-28): Gray Biants (`40606`, Elionian Priest), Bokhee (`47570`, Little Auntie), the Hashashin Statue (`47672`) and Tenochti (`47750`, Priest). So all 20 holders in client 3458 are church buff sellers.
- Earlier versions of this doc took Zario and Resh as `ChurchBuff` examples from the pre-update fixture (the table's example `47766` is from there). The 2026-09-27 update reuses character IDs, and in client 3458 Zario (`47766`) is a Fish Vendor with `Fish` and Resh (`47764`) a Material Vendor with `Collect`, neither with `ChurchBuff`. That matches the game (2026-09-28): Zario sells Ship License: Raft and Breezy Crystal, and Resh runs a shop and an exchange (Magical Lightstone Crystal or Sharp Black Crystal Shard for Margahan's Fragment).

## Open Questions

### Value 41

The client enum skips `41`, but Miles (`59279`) sets it, together with `ItemRepairer`, `ImportantNpc` and `Grocery`. In game Miles gives the Grand Prix quests, so `41` is probably a Grand Prix (horse racing) role. As far as I know he is the only Grand Prix NPC (2026-09-27), which fits a single record, but there is no second case to confirm the name. The table labels the column Grand Prix (`roleLabels`); the parser keeps `Unknown41` because the client enum has no name for it.
