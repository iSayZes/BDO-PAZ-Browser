# `itemenchant.dbss` Format

## Purpose

The per-item enchant table, and in practice the closest thing the client data has
to a master item table. It holds one variable-length block per
(item, enchant level) pair, keyed through a required offset companion. Each block
carries the item's icon path as an inline string, which makes this file the
authoritative item ID to icon mapping, the one thing that cannot be derived from
an item ID alone. Items that place or summon something (furniture, fences,
crops, pets) also name that character, which links them to
`characterobject.dbss` and `characterstatic.dbss`.

At roughly 194 MB it is the largest file in the game data.

Example:

```text
item 24626 (King Clam Wall Ornament)
  -> New_Icon/03_ETC/06_Housing/InHouse_Cultivate_Sea_Clam_01_Wall.dds
item 58011 ([Event] Fence)
  -> New_Icon/03_ETC/06_Housing/00058003.dds
  -> places character 2053 ([Event] Fence)
```

## Companion Files

| File                      | Required | Role                                          |
| ------------------------- | -------- | --------------------------------------------- |
| `itemenchantoffset.dbss`  | Required | Maps the packed key to a block offset and size |
| `languagedata_en.loc`     | Optional | Item name and description for the item ID (`str_type=0`, `str_id4` 0 and 1) |
| `skill.dbss`              | Optional | The buffs of `skill_key_1` and `skill_key_2`, through the `SKILL_BUFFS` lookup index |
| `lightstoneset.bss`       | Optional | The Lightstone sets an item counts toward, through the `LIGHTSTONE_SETS` lookup index |

All multi-byte values are little-endian.

## File Layout

| Offset  | Type | Field   | Notes                                                |
| ------- | ---- | ------- | ---------------------------------------------------- |
| `+0x00` | u32  | count   | Record count, matching the companion; observed 169,965 before 2026-09-27, 170,322 after |
| `+0x04` | ...  | blocks  | Variable-length blocks, contiguous, in key order      |

Blocks are addressed only through the companion. The first block starts at byte
`4`, and the last block ends exactly at end of file (203,540,909 bytes observed),
so the block stream is gap-free. The 2026-09-27 client file is 203,937,007 bytes.

## `itemenchantoffset.dbss`

| Offset  | Type  | Field  | Notes                            |
| ------- | ----- | ------ | -------------------------------- |
| `+0x00` | u8[4] | magic  | `PABR` (ASCII)                   |
| `+0x04` | u32   | count  | Number of rows; observed 169,965 before 2026-09-27, 170,322 after |
| `+0x08` | ...   | rows   | `count` × 12-byte rows           |
| end-12  | ...   | trailer | 12-byte file trailer            |

### Row (12 bytes)

| Offset  | Type | Field       | Notes                                        |
| ------- | ---- | ----------- | -------------------------------------------- |
| `+0x00` | u32  | key         | Packed item ID and enchant level, see below |
| `+0x04` | u32  | data_offset | Byte offset of the block in `itemenchant.dbss` |
| `+0x08` | u32  | data_size   | Block length in bytes                        |

Rows are contiguous: `data_offset + data_size` of one row equals the next row's
`data_offset`.

### Trailer (12 bytes)

The same trailer shape used by
[fairyupgraderate.bss](fairyupgraderate_bss.md) and
[zodiacsignindex.bss](zodiacsignindex_bss.md).

| Offset  | Type | Field          | Observed  | Notes                              |
| ------- | ---- | -------------- | --------- | ---------------------------------- |
| `+0x00` | u32  | reserved_a     | 0         | Always zero                        |
| `+0x04` | u32  | end_of_rows    | 2,039,588 | Equals `8 + count × 12` (2,043,872 after 2026-09-27) |
| `+0x08` | u32  | reserved_b     | 0         | Always zero                        |

## Key Packing

```text
key = (enchant_level << 24) | item_id
```

| Field         | Bits   | Observed range |
| ------------- | ------ | -------------- |
| enchant_level | 31..24 | 0-25           |
| item_id       | 23..0  | 1-1,000,827 (1-1,000,841 after 2026-09-27) |

The low 24 bits are confirmed item IDs: 69,292 of them match a name in
`languagedata_en.loc`. The high byte is the enhancement level. Every item has
one record per level from `0` up to its maximum, with no gaps, and the maximum
matches the item's enhancement range in game. Level `0` is the base item, which
is all the icon index needs. Earlier versions of this doc called the field
`key_variant`, because 25 looked wider than BDO's enhancement range.

Per-item maximum on the 2026-09-27 client, checked in game (2026-09-28):

| Max | Items  | Example                                   | In game                     |
| --- | ------ | ----------------------------------------- | --------------------------- |
| 0   | 60,873 | Non-enhanceable items                     | -                           |
| 1   | 4,147  | Basteer Longsword (10011); 4,093 of them are Pearl Shop outfit tops (`09_Cash/01_Equip/03_Upperbody` icons) | Basteer: enhanceable, "※ Enhancement is available by using only Black Stone (Basteer)."; the level count is not shown |
| 2   | 2      | Sealed Spirit's Earring (11826)           | +1 to +2                    |
| 3   | 4      | Tears of the Wind Necklace (11654)        | +1 to +3                    |
| 5   | 251    | Deboreka Earring (11882), Sicil's Necklace (11625) | +1 to +5 (PRI to PEN) |
| 7   | 50     | Ultimate Basteer Longsword (10070)        | +1 to +7                    |
| 10  | 518    | Kharazad Necklace (11697), Sovereign Scythe (747402) | +1 to +10        |
| 15  | 105    | Adventurer's Longsword (10073)            | +1 to +15                   |
| 20  | 4,167  | Kzarka Gauntlet (11210), Blackstar Greatsword (731101) | +1 to +15, then PRI to PEN |
| 25  | 167    | Tuvala Helmet (695105), Tuvala Noble Sword (695135) | +1 to +15, PRI to PEN, then VI to X |

## Block Structure

A block opens with its packed key and a header of fixed fields, then counted
lists, the Korean name and the icon path, and ends with a large run of
enchant-related fields that are not yet decoded. On client 3464 both copies of
the key, at `+0x00` and at end-6, equal the offset row's key in all 168,680
blocks. An earlier version of this doc called both the item ID, which holds
only for the level-0 blocks.

The header holds one counted field, `unknown_5d`. The offsets below hold for
blocks where its count is `0`; every field after it moves by the count. On
client 3464 the count is `1` in 740 blocks and `4` in one (all levels; 120
base items with `1`, Ashen Crow Horse Gear with `4`), all of them mount or
ship gear: horse and donkey barding, saddles, stirrups, champrons and
horseshoes, Oquilla and Epheria Carrack parts, Galley parts. Read at the
fixed offsets, the 120 base items with `1` named character `1`, cast skill
key `1` and stored `0xFFFFFF00` at `+0x65`; read past the count they name no
character, cast no skill and store `0x7FFFFFFF` like other gear. Required
level, dyeable and durability change with them.

| Offset  | Type | Field    | Notes                                    |
| ------- | ---- | -------- | ---------------------------------------- |
| `+0x00` | u32  | key          | Repeats the packed key of the offset row, enchant level included |
| `+0x04` | u8   | item_type    | Tooltip class (`EItemType`), see below                       |
| `+0x05` | u8   | category     | Item classification                                          |
| `+0x06` | u8   | grade        | `0` to `5`, the item name colour, see below                  |
| `+0x07` | u8   | equip_type   | Equipment type; `0` on items that are not equipment. See below |
| `+0x08` | u8[6] | unknown     | Numeric fields                                               |
| `+0x0E` | u8   | equip_slot   | Equipment slot, `__eEquipSlotNo`; `46` when the item goes in no slot. See below |
| `+0x0F` | u8   | unknown      | `2` (60,289 base items), `0` (8,581) or `1` (1,343) on client 3464 |
| `+0x10` | u8[46] | extended_slots | Further slots the item fills, the rest filled with `46`; see `equip_slot` below |
| `+0x3E` | u8   | unknown_3e   |                                                              |
| `+0x3F` | i32  | weight       | Divide by 10,000 for LT                                      |
| `+0x43` | u8   | stackable    | `1` when copies of the item share one inventory slot; see below |
| `+0x44` | u8   | unknown_44   | `1` in 10,027 base items on client 3464, see Open Questions  |
| `+0x45` | u32  | expiration_minutes | `0` when the item does not expire; set in 4,580 base items |
| `+0x49` | u8   | vested_type  | When the item binds: `0` never (34,516 base items), `1` when obtained (17,372), `2` when equipped (18,396) |
| `+0x4A` | u8   | family_bound | `1` binds to the family, `0` to the character; set in 5,942 base items |
| `+0x4B` | u8   | for_trade    | `1` on trade goods that Trade Managers buy; 2,007 base items |
| `+0x4C` | u8   | trade_type   | Kind of trade good, only set with `for_trade`, see below     |
| `+0x4D` | u64  | class_mask   | Classes that can use the item, bit `n` for class ID `n`. All-class items set most bits, so test single bits |
| `+0x55` | u32  | servant_kinds | Servants that can use the item, bit `n` for `CppEnums.ServantKind` `n`; `0` on everything but servant gear. See `equip_slot` below |
| `+0x59` | u8[4] | unknown     | Numeric fields                                               |
| `+0x5D` | u32  | unknown_5d   | Count, followed by that many bytes; `0` except on mount and ship gear, see above. The bytes are `1` to `4` on the Epheria Carrack parts, matching Advance, Balance, Volante and Valor, and `1, 4, 5, 10` on Ashen Crow Horse Gear |
| `+0x61` | u8   | required_level | Character level needed to use the item; `0` or `1` when there is none, above `1` in 3,734 base items |
| `+0x62` | u8[3] | unknown     | Numeric fields                                               |
| `+0x65` | u32  | unknown_65   | bdo-data-extractor: max stack. See In-Game Checks            |
| `+0x69` | ...  | unknown      | Numeric fields                                               |
| `+0x6E` | i64  | buy_price    |                                                              |
| `+0x76` | i64  | sell_price   |                                                              |
| `+0x7E` | i32  | repair_price |                                                              |
| `+0x82` | ...  | unknown      | Numeric fields                                               |
| `+0xA8` | u8   | dyeable      | `0`: the item cannot be dyed (45,780 base items on client 3464). `1` (24,433): it can, if it also has dye parts, which this file does not hold, see below |
| `+0xA9` | u8   | unknown_a9   |                                                              |
| `+0xAA` | u16  | character_id | Character the item places or summons; `0` when none. See below |
| `+0xAC` | u8   | unknown_ac   | Not the number of dye slots, see below. `0` on all 3,960 object links; across base items `0` (61,650), `1` (4,786), `2` (2,165), `5` (1,052), `10` (218) |
| `+0xAD` | u8   | unknown_ad   | `0` in 69,875 base items                                     |
| `+0xAE` | ...  | unknown      | Numeric fields                                               |
| `+0xC4` | u8   | personal_trade | `1` when the item can be traded between players; 330 base items |
| `+0xC5` | u16  | max_durability | `32,767` for items without durability (51,959 base items); equipment mostly `100` or `120` |
| `+0xC7` | u8   | unknown_c7   |                                                              |
| `+0xC8` | u8   | market_category | Central Market category, LOC type 44 `str_id1`; `255` when the item is not listed (56,870 base items) |
| `+0xC9` | u8   | market_sub_category | Subcategory, in the market's menu order; `255` when not listed |
| `+0xCA` | u16  | unknown_ca   |                                                              |
| `+0xCC` | u32  | skill_key_1  | Skill a consumable casts, a [`skill.dbss`](skill_dbss.md) key; its `buff_ids` are the item's buffs; `0` when none |
| `+0xD0` | u32  | skill_key_2  | Second skill, used by composite meals; `0` when none          |
| `+0xD4` | ...  | lists        | Counted lists up to the name, see below                      |
| varies  | u32  | enchant_key  | With the block's level, the key of [enchantstaticstatus.dbss](enchantstaticstatus_dbss.md); `0` in 40,025 base items (client 3458), which have no enhancement data. Every level of an item stores the key of its base block (all 70,213 items on client 3464) |
| varies  | ...  | name_kr      | Korean item name: u64 character count, then UTF-16LE text. Present in all 70,284 base blocks (client 3458) |
| varies  | ...  | icon         | Icon path, a length-prefixed ASCII string; see below          |
| varies  | ...  | unknown  | Remaining enchant data, see After the icon |

Checked on Balacs Lunchbox (`9359`): `item_type` 2, `grade` 3, `weight`
1,000 (0.1 LT), `buy_price` 38,775, `sell_price` 1,551, and a non-zero
`skill_key_1`.

I checked the fields from `expiration_minutes` to `market_sub_category`
against bdocodex (2026-10-05, client 3458) on 16 items: Kzarka Gauntlet and
Longbow, Kharazad Necklace, Tuvala Helmet, Basteer Longsword, Black Stone,
Caphras Stone, Balacs Lunchbox, Magic Crystal of Infinity - Valor,
Inventory 30% DC Coupon, Cano Toadfish, Young Crow Earring, Kansha
Hexround, [Seraph] Glorious Arsha Purgatum (180 Days), Fiery Sovereign
Mareca and Deboreka Earring. Weight, buy, sell and repair price matched on
all of them, and `max_durability` on every item bdocodex shows durability
for (100 or 200).

- `expiration_minutes`: the coupon stores 4,320 (3 days, "must be
  registered within 3 days of receipt") and the 180-day Arsha 259,200.
- `vested_type` and `family_bound`: Basteer Longsword (`1`, `1`) shows
  "Bound when obtained (Family)", Kansha Hexround (`1`, `0`) "Bound when
  obtained (Character)", the Arsha (`2`, `0`) "Bound when equipped
  (Character)". bdocodex prints a plain "Bound when obtained" on every item
  with `0`. The tooltip script (`widget/tooltip/panel_tooltip_item`) picks
  the same texts: vested type `1` shows `LUA_TOOLTIP_ITEM_GETBIND_*`, `2`
  `LUA_TOOLTIP_ITEM_EQUIPBIND_*`, with `_FAMILY` when `isUserVested()`.
- `class_mask`: Kzarka Gauntlet `0x880000` is Striker and Mystic, Kzarka
  Longbow `0x10` Ranger, Basteer Longsword Warrior and Valkyrie, Kansha
  Hexround bit 35 Agent, the Arsha bit 32 Seraph and Fiery Sovereign Mareca
  bit 10 Corsair, all as bdocodex lists them.
- `personal_trade`: Balacs Lunchbox is the only one of the 16 at `1` and
  the only one bdocodex marks "Personal transaction available".
- `for_trade`: Cano Toadfish, which Trade Managers buy.
- `market_category`: Kzarka Gauntlet is `1`/`9` and Kzarka Longbow `1`/`2`,
  Gauntlet and Longbow in bdocodex's Main Weapon menu (Longsword, Longbow,
  Amulet, Axe, Blade, Shortsword, Staff, Kriegsmesser, Gauntlet).
- `trade_type`, from the bdocodex pages of two items per value:

  | Value | Base items | Examples | bdocodex |
  | ----: | ---------: | -------- | -------- |
  | 0 | 1,805 | Cano Toadfish, Coal Dust Pouch | Sold to Trade Managers |
  | 1 | 33 | Pumpkin Ghost Seed, Black Spirit Control Stone | "Selling this item will drop your Karma and amity of the trader" |
  | 3 | 54 | Apprentice's and Guru's Medicine Box | Delivered to the Imperial Crafting Delivery Manager |
  | 4 | 109 | Redfin Anthias, Opah, Ribbon Eel | Sold to Trade Managers or used for Cooking; what sets it apart from `0` is open |
  | 5 | 6 | [Guild] Balenosian Specialty, [Guild] Imperial Trade Package | Guild trade missions |

- `required_level`: every Dandelion Kamasylven Sword row stores `56`, the
  level its tooltip asks for in game (2026-10-05). Main weapons like Kzarka
  Gauntlet store `1`, and need no level.

bdo-data-extractor also names a max stack at `+0x65` and a Pearl Shop flag
at `+0xA4`. Neither bdocodex nor my own items could show those, so they stay
unchecked here (see Open Questions and In-Game Checks).

The skill keys are fixed fields, read at `+0xCC` and `+0xD0` whatever the
strings hold. Every enchant level of an item stores the same keys as its base
block (client 3458). Simple Cron Meal (`9692`) uses both: the buffs of its
two skills give the effects its tooltip lists on bdocodex (Combat EXP +20%,
Skill EXP +10%, Max HP +150, Back Attack and Critical Hit Extra Damage +5%,
Heatstroke/Hypothermia Resistance +10% and more). A few items store `1`
(skill 0 level 1), which has no `skill.dbss` record and links nothing.

The fixed part of this layout, and the names of `item_type`, `category`,
`grade` and the skill keys, come from
[bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor/blob/HEAD/FORMATS.md),
which decodes the whole header from `+0x00` to `+0xD4` (class mask, stack
size, market category, durability and more). The offsets above were checked
against this file; the name `category` was not.

The tooltip script shows dye slots only when `isDyeable()` is true and
`getDyeingPartCount()` is above 0, and "Cannot be dyed"
(`LUA_TOOLTIP_ITEM_DYE_DYEIMPOSSIBLE`) otherwise, so `dyeable` is one of two
conditions. Checked in game (2026-10-05):

- Kzarka Gauntlet, [Wizard] Canape Dagger and [Wizard] Python Boxer Briefs
  store `1`, and have 3, 3 and 1 dye slots.
- PEN: Sovereign Staff and Fallen God's Armor store `1` but say "Cannot be
  dyed", so they must have no dye parts.
- Obsidian Blackstar Armor stores `0` and says "Cannot be dyed".
- All 553 accessories store `0`, and accessories cannot be dyed. Wagon
  covers, lamps and wheels store `1`, the parts the dye window's wagon tab
  offers (`LUA_DYENEW_DYEPART_CARRIAGE_*`).

The part count is not in this block: no header byte, and none of the 18
bytes after the icon, holds 3 for the dagger and 1 for the briefs.
bdo-data-extractor calls `unknown_ac` the dye parts, but the dagger and the
briefs store `0` there and the staff `1`.

#### `grade`

The colour the game draws the item name in. The colours are the ones
`PAGlobalFunc_SetItemTextColorByItemGrade` in the client Lua
(`include/global_util`) sets, in this order; the same file wraps a name in
the grade's `<PAColor>` tag for text. Grade 5 purple is confirmed in game.
Other tables read the grade from the `ITEM_GRADE` lookup index. Counts are
base items on client 3458.

| Value | Colour       | Example                         | Base items |
| ----: | ------------ | ------------------------------- | ---------: |
| 0     | `0xFFC4C4C4` | Memory Fragment                 | 7,334      |
| 1     | `0xFF83A543` | Faint Dream Box                 | 4,182      |
| 2     | `0xFF438DCC` | Caphras Stone                   | 6,904      |
| 3     | `0xFFF5BA3A` | Kzarka Longsword, Cron Stone    | 17,155     |
| 4     | `0xFFD05D48` | Blackstar Longsword, Black Stone | 34,433    |
| 5     | `0xFFA070EF` | Sovereign Longsword, Kharazad Earring | 276  |

#### `item_type`

`EItemType`, which selects the tooltip label. Names from bdo-data-extractor;
the counts are base items here.

| Value | Name         | Tooltip label       | Base items |
| ----: | ------------ | ------------------- | ---------: |
| 0     | Normal       | General             | 6,243      |
| 1     | Equip        | Equipment           | 29,763     |
| 2     | Skill        | Consumable          | 13,245     |
| 3     | Tent         | Holding Tool        | 279        |
| 4     | Installation | Installable Object  | 3,597      |
| 5     | Jewel        | Socket Item         | 565        |
| 6     | CannonBall   | Cannonball          | 22         |
| 7     | Mapae        | License             | 246        |
| 8     | Material     | Crafting Material   | 1,630      |
| 10    | ContentsEvent | Special Items      | 13,272     |

Values 11 to 20 also occur (1,092 items) and are unnamed. Every one of the
3,597 `Installation` items and the 279 `Tent` items names a placed character.

#### `equip_type`

The type the item tooltip names after "Equipment": `panel_tooltip_item`
passes `getEquipType()` to `PaGlobalFunc_Util_ClassEquipParts`
(`include/global_util_ui`), which maps it to a slot label. On client 3464
the values it lists match the slots the items store, except `43`: the Lua
labels it Matchlock, and its four items, such as Bird-Hunting Matchlock, go
in slot 0.

| `equip_type` | Lua labels | `equip_slot` | Examples |
| ------------ | ---------- | ------------ | -------- |
| 1, 2, 3, 6, 28, 29, 31, 63, 65, 67, 73, 78, 80, 83, 86, 88, 89, 93, 96, 97, 100, 109, 112, 114, 116 | main weapon | 0 | Basteer Longsword (1), Arsha's Kriegsmesser IV (63) |
| 8, 32, 33, 34, 36, 37, 55, 56, 66, 70, 74, 79, 81, 87, 90, 94, 98, 99, 108, 110, 113, 115, 117 | sub-weapon | 1 | Sovereign Kunai (55) |
| 9, 11, 12, 13 | upper body, gloves, boots, helm | 3, 4, 5, 6 | Golden Crow Armor, Tuvala Helmet |
| 15, 16, 17, 18 | necklace, ring, earring, belt | 7, 8, 10, 12 | Kharazad Necklace, Young Crow Ring, Young Crow Earring, Young Crow Belt |
| 22, 24, 25, 26 | avatar chest, gloves, boots, helm | 14, 15, 16, 17 | Outfits |
| 30, 35, 38 to 41 | avatar weapons, underwear, face decorations | 18 to 23 | |
| 44, 59, 48, 53 | fishing rod, float, harpoon, matchlock | 40, 41, 42, 43 | Thin Harpoon (48), Verti Matchlock (53) |
| 46, 54, 57, 58, 72, 92 | gathering tool, alchemy stone, awakening weapon and its outfit, Adventurer's Tome, artifact | 2, 27, 29, 30, 31, 32 | |

`PaGlobalFunc_Equipment_All_AccSlotNo` (`panel_window_equipment_all_3`)
picks the first or second ring, earring or artifact slot for types `16`,
`17` and `92`; the items store only the first (8, 10 and 32; no base item
stores 9, 11 or 33 on client 3464). Equipment (`item_type` 1) always
stores a non-zero type and a slot below `46`, and every other item stores
`0` and `46` (29,918 and 40,295 base items on client 3464).

The client Lua has no name per value. For main and sub-weapons the Central
Market menu has one: on client 3464 every listed item of a weapon type stores
the same `market_category` / `market_sub_category` pair, each type its own,
and LOC type 44 names the pair under `str_id1` / `str_id2`. The in-game menu
lists the same names in the same order (checked 2026-10-14), with no "All"
entry. About 15 of the 90 to 180 items of a main weapon type are listed, so
the browser takes the pair from the listed items of a type and names every
item of that type with it. Sub-weapon type 118 (Hexround) is listed there but
missing from the `PaGlobalFunc_Util_ClassEquipParts` values above.

| Category | `equip_type` and subcategory (client 3464) |
| -------- | ------------------------------------------ |
| 1, Main Weapon | 1 Longsword (1), 31 Longbow (2), 28 Amulet (3), 29 Axe (4), 2 Shortsword (5), 3 Blade (6), 6 Staff (7), 63 Kriegsmesser (8), 65 Gauntlet (9), 67 Crescent Pendulum (10), 73 Crossbow (11), 78 Florang (12), 83 Battle Axe (13), 80 Shamshir (14), 86 Morning Star (15), 88 Kyve (16), 89 Serenaca (17), 93 Slayer (18), 97 Swallowtail Fan (19), 96 Foxspirit Charm (20), 100 Hammers (21), 109 Hwando (22), 112 Revolvers (23), 114 Power Pole (24), 116 Sacramentum (25) |
| 5, Sub-weapon | 8 Shield (1), 32 Dagger (2), 33 Talisman (3), 34 Ornamental Knot (4), 37 Trinket (5), 36 Horn Bow (6), 55 Kunai (7), 56 Shuriken (8), 66 Vambrace (9), 70 Noble Sword (10), 74 Ra'ghon (11), 79 Vitclari (12), 81 Haladie (13), 87 Quoratum (14), 90 Mareca (15), 94 Shard (16), 99 Do Stave (17), 98 Binyeo Knife (18), 108 Gravity Cores (19), 110 Gombangdae (20), 113 Shotgun (21), 115 Gourd Bottle (22), 117 Clavis (23), 118 Hexround (24) |

Other types add nothing to the slot: armour and accessory types sit in their
slot's subcategory (Armor, Accessories), outfits spread over the Pearl Item
menu, and all awakening weapons share type `57`.

#### `equip_slot`

`__eEquipSlotNo`, the slot `ToClient_getEquipmentItem` and the servant's
`getEquipItem` take in `panel_tooltip_item`. `CppEnums.EquipSlotNo` in
`include/global_define_cpp_enum` numbers `rightHand` (0) to `artifact2`
(33), the life tools `Axe` (34) to `Pickaxe` (39) and `Fishing` (40), then
ends with `Hunting = 41` and a count of 42. The client is past that list:
items store 41 to 46, and `CppEnums.SlotNoIdToString` labels 12 slots from
`__eEquipSlotNoAxe` to `__eEquipSlotNoTemp`, in that order. The numbers 41 to
45 follow from the items and from `equip_type` above: floats store 41
(type 59, `LUA_LIFEEQUIP_TOOLTIP_08`), harpoons 42, matchlocks 43, sniper
rifles 44, and the Lil' Otter and Lil' Papu carriers 45 (`__eEquipSlotNoTemp`,
labelled `LUA_EQUIPMENT_AVATAR_BACK`, Accessory (Back)). 46 is the slot
count, stored by every item that goes in no slot. The numbers of slots 41 to
45 are our reading from those items, not from a client table: the client
lists no number for them.

The browser shows the `SlotNoIdToString` label in the app language (LOC type
37, see [stringtable.bss](stringtable_bss.md)). Slots 24 to 26 are not in that
table and use `CppEnums.EquipSlotNoString` instead.

The 46 bytes at `+0x10` are the extended slots, filled up with `46`: the
tooltip reads them with `getExtendedSlotCount()` and `getExtendedSlotIndex()`,
skips entries equal to the count, and prints "Equipped on: {selfSlotNo}
{extendedSlotString}" (`PANEL_TOOLTIP_EQUIP_EXTENDEDSLOT`). They are set in
3,770 base items on client 3464, always from the first byte: outfits in slot
14 list 15, 16 and often 17, the `[Agent]` armour sets in slot 3, such as
[Agent] Shroud Knight Armor, list 4, 5 and 6, and Ashen Crow Horse Gear (14)
lists 15, 16 and 17.

Servant gear stores the same slot numbers with other meanings (a barding in
3, a wagon wheel in 4). `servant_kinds` says which servants use the item; on
client 3464 it is set on all 927 base items with `class_mask` `0` and an
`equip_slot` below `46`, and `0` on all other equipment. The stable dialog
(`panel_dialog_servantinfo_all_2`, `GetItemEquipServantType`) tests the kinds
in the order of the table below and takes the first group that matches; its
`_SERVANT_KIND_TYPESTRING` (`panel_dialog_servantinfo_all`) labels the slots
per group. The labels below are its English LOC texts.

| Group | `ServantKind` values | Slot labels |
| ----- | -------------------- | ----------- |
| Wagon | 4, 5, 12, 18 | 3 Frame, 4 Wheel, 5 Flag, 6 Emblem, 13 Lamp, 25 Cover, and Costume versions in 14, 15, 16, 17 and 26 |
| Horse | 0, 1, 2, 9, 29 | 3 Barding, 4 Saddle, 5 Stirrups, 6 Champron, 12 Horseshoe, and Costume versions in 14 to 17 |
| Elephant | 3, 13 | 3 Elephant Armor, 4 Saddle, 5 Stirrups, 6 Elephant Mask, 12 Horseshoe, the same in 14 to 17 (`LUA_VEHICLEINFO_ELEPHANT_SLOTNO*`) |
| Ocean ship | 10, 14, 15, 20 to 28 | 3 Plating, 4 Figurehead, 5 Cannon, 6 Ornament, 7 Fishing Rod, 12 Sea Crystal, 25 Sail, and 14, 15, 16, 26 as 3, 4, 5, 25 |
| Boat | 6, 11 | 3 Hull, 4 Prow, 5 Cargo Container, 6 Totem, 25 Ornament, and 14, 15, 16, 26 as 3, 4, 5, 25 |
| Camping tent | 16 | 3 Container, 4 Anvil, 5 Shop, 6 Appearance, 7 Move to Residence (camp window, `RESOURCE` sheet) |

The item names agree with every group's labels, with one exception: the
client table has the horse costume saddle and stirrups the other way round
(15 Stirrups, 16 Saddle), but all 28 horse items in slot 15 are saddles
(Orzekel Saddle) and all 28 in 16 are stirrups. The browser follows the
items. Two older client tables disagree with the items in more places and
are not used: the tooltip's `servantKindTypeString` (`panel_tooltip_item`)
calls wagon slot 25 Frame and Carrack slot 5 Sail, and the ship window
(`panel_window_shipinfo_all`) labels ocean ship slot 25 Decor
(`LUA_VEHICLEINFO_SHIP_OCEAN_INDEX4`, Korean `장식`). Ocean ship slot 12
holds 333 items on client 3464: sea crystals, Ebenruth's Nol and 36 Sailor
Contract items (Epheria, Frigate and Galley sailors). Both client tables call
it Sea Crystal.

Personal Battle Ship (17) is in no group, but every item that allows it also
allows an ocean ship kind. `GetItemEquipServantType` has no camping tent
group: the item tooltip handles the tent as its own servant type
(`__eServantTypeCampingTent`), comparing an item with
`isServantTypeUsable(servantKind)` and the tent's `getEquipItem(slot)`. The
camp window (`panel_window_camp_all`, `_menuStr`) labels those slots, and
the 15 kind 16 items on client 3464 fit them: containers and storage in 3,
anvils in 4, shops in 5, tents in 6 and Star of Nostos, a teleport item, in
7. The browser tests kind 16 after the dialog's groups.

#### `stackable`

`1` on 14,708 of the 70,213 base items on client 3464. The client's item
slot (`global_util_ui_slot`) draws an item's stack count when
`isStackableXXX()` is true. The flag fits the item kinds:

- `0` on every equipment item (29,918 base items) and in every block above
  enchant level 0 (98,467).
- `1` on currencies, seals and tokens, Black Stone, Memory Fragment, Caphras
  Stone, ores and logs, HP Potion (Beginner) and Balacs Lunchbox.
- `0` on fish sold to Trade Managers, such as Requiem Shark and all 109
  trade goods of trade type 4; `1` on trade goods such as Coal Dust Pouch.
- `1` on all four items whose `unknown_65` is not `0x7FFFFFFF` (the two
  beginner potions, Deputy Token, Combat EXP Scroll).

calpheonlabs names `+0x43` "isStackable" and `+0x44` "appliesDirectly".

### Before the name

From `+0xD4` (plus the `unknown_5d` count) to the icon, a block is a fixed
sequence of counted lists and strings:

| Order | Type | Field | Notes |
| ----: | ---- | ----- | ----- |
| 1 | u32 count, 5-byte entries | unknown_d4 | A class type (u8) and a u32 per entry. Set in 28,101 base items on client 3464, and every entry's class is one `class_mask` allows; 32 entries on armour for all classes |
| 2 | u32 count, 5-byte entries | unknown | Set in 498 base items on client 3464: one entry in 330, two in 164, six in 4. 490 of them are `category` 9 or 11 (`eItemClassify_PearlGoods`, `eItemClassify_Vehicle`), mostly mount, wagon and ship gear |
| 3 | u8[4] | unknown | `0` in 67,081 base items on client 3464; most others set only the third byte, `1` to `10` |
| 4 | u32 count, u32 entries | unknown | Up to three entries; set in 2,575 base items on client 3464 |
| 5 | u32 | enchant_key | See Block Structure |
| 6 | u64 count, UTF-16LE | name_kr | Korean name |
| 7 | length-prefixed ASCII | icon | Icon path |

This walk reaches the name and the icon in all 168,680 blocks on client 3464,
and gives the same `enchant_key`, `name_kr` and icon as reading backwards
from the icon in every block, which is how the browser found them before.
calpheonlabs reads this region as four layouts (one list of 5-byte entries
and a u32 list, two lists of 5-byte entries, or two lists with one or four
bytes between them). On client 3464 those are this one layout: the two-list
layouts are blocks whose first list is empty and second is not, and the
"one byte" and "four bytes" between the lists are the `unknown_5d` entries
of mount and ship gear, which moved the whole header.

### Placed or summoned character

`character_id` sits in the fixed numeric part, at `+0xAA` plus the `unknown_5d` count: in every block, at every level, the first string's prefix starts at `+0xF2` (242) or later (client 3458), and every block is at least 693 bytes long.

| Measure (level-0 blocks)                         | Value |
| ------------------------------------------------ | ----: |
| Characters named by at least one item            | 5,095 |
| ... that have a `characterobject.dbss` record    | 3,960 |
| ... named by exactly one item (kept as a link)   | 5,090 |
| Characters named by more than one item           |     5 |

Measured before the 2026-09-27 update. After it, 5,103 characters are named by at least one item, still 5 by more than one, so 5,098 are kept as links.

All 5,095 are `characterstatic.dbss` IDs; the ones without an object record are mostly pets.

Examples: `58001` Strong Fence Garden (item) → `2001` Strong Fence Garden; `820908` Truffle Mushroom Hypha → `1436` Truffle Mushroom Crop; `860014` [Pet] Striped Cat (Tier 3) → `9425` Cat. Of the 3,960 object links, 2,961 have identical item and character names; the rest pair a seed with its crop or a `[Guild]` item with its structure.

The counts above include character `1`, which 120 unrelated items seemed to name: those are the mount and ship gear read without their `unknown_5d` entries (see Block Structure). Read past them, no item names character `1`. On client 3464, 5,112 characters are named by at least one item and 4 by more than one. The browser keeps only characters named by exactly one item.

### Length-prefixed string

| Offset  | Type   | Field  | Notes                          |
| ------- | ------ | ------ | ------------------------------ |
| `+0x00` | u32    | length | Byte length of `text`          |
| `+0x04` | u32    | zero   | Always 0 in observed data      |
| `+0x08` | char[] | text   | ASCII, not null-terminated     |

The strings do not sit at a fixed block offset: 47 distinct offsets were
observed across a 400-block sample. The browser reaches the icon through the
lists before the name (see Before the name). A block holds at most two ASCII
strings:

| Position | Content                                                        |
| -------- | -------------------------------------------------------------- |
| first    | Icon path, relative to `ui_texture/icon/`                       |
| second   | Optional `second_string` such as `ITEM_BIC_HIT_1`; absent in most blocks, meaning unconfirmed |

The second string sits in the undecoded part after the icon, so the browser
scans for the `(length, 0, ascii × length)` shape from the end of the icon.

### Resolving the icon path

The PAZ path is the stored value prefixed with `ui_texture/icon/`, matched
case-insensitively:

```text
New_Icon/03_ETC/06_Housing/InHouse_Cultivate_Sea_Clam_01_Wall.dds
  -> ui_texture/icon/new_icon/03_etc/06_housing/inhouse_cultivate_sea_clam_01_wall.dds
```

On client 3464 every icon path ends in `.dds` and all but one begin with
`New_Icon` in some case: item `66022` stores `Item_Icon/00724507.dds`, and
`1000525` stores `New_icon/`. Seven base items (`9707`, `9708`, `9724`,
`9725`, `720707`, `790810`, `810580`) separate some folders with
backslashes, such as `New_Icon/03_ETC\03_Quest_Item/00042393.dds`.

### After the icon

Layout from bdo-data-extractor; it reads cleanly in all 70,284 base blocks
(client 3458). Offsets are relative to the end of the icon text.

| Offset  | Type      | Field         | Notes |
| ------- | --------- | ------------- | ----- |
| `+0x00` | u8        | marketable    | `1` when the item can be listed on the Central Market; 13,071 base items |
| `+0x01` | u8[12]    | unknown_01    |       |
| `+0x0D` | u8        | family_inventory | `2` when the item can be stored in the Family Inventory (1,106 base items), `0` when not |
| `+0x0E` | u8        | unknown_0e    |       |
| `+0x0F` | u8        | unknown_0f    | bdo-data-extractor: bind type. Neither the bound text nor "Cannot be enhanced" comes from it, see below |
| `+0x10` | u8[2]     | unknown_10    |       |
| `+0x12` | 3 strings | messages_kr   | Three u64-prefixed UTF-16LE strings, all empty in 56,320 base items. The first is a script on pets (`PETSKILL_REGISTER();`, 8,065 items). The second is the Korean prompt a box shows before it is used, listing what it gives (10,832). The third is the Exchange Info of 110 items, mostly old trash loot, see below |
| varies  | i64       | unknown_limit | bdo-data-extractor: the market registration limit. In game (2026-10-05) it is neither the listing limit nor the pre-order limit: Black Stone stores 1,000, but I can list 1,001 and more, and pre-order up to 5,000. What it holds is open |
| varies  | u8        | unknown       |       |
| varies  | u32       | enhancement_group | `enhancement_type × 1000` plus a family index in 70,268 base items, e.g. Kharazad necklace 21000 |
| varies  | u32       | enhancement_type  | Enhancement system: `0` none, `1` ordinary weapons and armour, `13` ordinary accessories, `19` Sovereign weapons, `21` Kharazad, `23` Tuvala weapons and armour; the full list is in bdo-data-extractor. Also the `group` of the Ancient Anvil table, [guaranteeenchantss.dbss](guaranteeenchantss_dbss.md) |
| varies  | ...       | unknown       | Undecoded remainder, holding `second_string` about 330 bytes in |
| end-6   | u32       | key           | Repeats the packed key, like `+0x00` |
| end-2   | u16       | unknown_crystal_group | `0xFFFF` except in 481 base items, e.g. Magic Crystal of Infinity - Valor `100`, which is no longer in the game; bdo-data-extractor: the crystal transfusion group |

`marketable` matches bdocodex on the 16 items checked above: Kharazad
Necklace, Tuvala Helmet, Basteer Longsword, the coupon, the toadfish and
the Magic Crystal of Infinity (bdocodex: "cannot be processed nor registered
on the Central Market") store `0`; Kzarka, Deboreka, Black Stone, Caphras
Stone and Balacs Lunchbox, all sold on the market, store `1`. The
`enhancement_type` values above fit the items they were read from.

`family_inventory` is `2` on exactly the kinds of item the Family Inventory
guide ("What Items to Store") lists: food and elixirs (Balacs Lunchbox,
Ocean Draught), scrolls (Skill EXP +300% Scroll), pet feed (Organic Feed,
Cheap Feed), mount feed (Carrot, Dried Briar) and event coins and seals
([Event] Golden Troupe Coin, [Event] Drieghan Seal). Cooking ingredients such
as White Truffle Mushroom and Millennial Wild Ginseng store `0`. The tooltip
script shows a family bag mark when `checkPushFamilyInventory()` is true.

`unknown_0f` is `0` on Kzarka Gauntlet (which I can move freely), `1` on
Kansha Hexround, `2` on Basteer Longsword and Tuvala Helmet, `3` on Young
Crow Earring. The bound text on those tooltips comes from `vested_type` and
`family_bound`. "Cannot be enhanced" does not come from it either: in game
(2026-10-05) Arsha's Crossbow IV (`0`), [Event] Urugon's Shoes (`2`),
Kansha Hexround (`1`) and Young Crow Earring (`3`) all say it, and none of
them has enchant levels, which fits the line better. What it holds is open.

The third string is the tooltip's Exchange Info. Mutant Enhancer stores
`<오염된 농장지> - 20개 교환: 마녀의 귀장식 1개`, twice more for Mark of Shadow
and Ogre Ring, and its tooltip in game (2026-10-05) shows the same in
English under "Exchange Info": `<Contaminated Farm>`, `Exchange 20: Witch's
Earring x1`, `Exchange 20: Mark of Shadow x1`, `Exchange 100: Ogre Ring x1`.
The English text is not in the item's LOC rows, so the client must build or
translate it from somewhere else.

## Icon Coverage

Measured against the 73,947 item IDs in `languagedata_en.loc` (`str_type=0`):

| Measure                                        | Value          |
| ---------------------------------------------- | -------------- |
| Items with a level-0 record                     | 69,292 (93.7%) |
| Sampled icon paths resolving to a real PAZ file | 99.3%          |
| Level-0 records carrying an icon path           | 100%           |

For comparison, deriving `product_icon_png/{item_id:08d}.png` from the ID alone
reaches only 14.9% of items, and indexing every ID-named icon under
`ui_texture/icon` by basename reaches 28.8%. The icon path stored here is the
only approach that covers items whose icon is named after a 3D asset
(furniture) or keyed by a cash-product ID rather than the item ID.

## Suggested UI Layout

One row per item, read from its level-0 block. Higher levels only feed Max Level: most repeat the base icon, and nothing else in them is decoded yet. The 551 items of [specialenchantitem.bss](specialenchantitem_bss.md) are the exception: their level blocks store the icon of that level, which differs from the base icon in 1,356 of their 3,081 keys on client 3458, and that file holds the same paths in fixed rows. The offset table keeps one row per key, with an Enchant Level column.

| Column        | Type | Notes                                             |
| ------------- | ---- | ------------------------------------------------- |
| Item ID       | num  | `item_id` from the key                            |
| Icon          | text | First block string, prefixed `ui_texture/icon/`   |
| Item          | text | LOC `str_type=0`, `str_id1=item_id`, else `name_kr` (483 items on client 3458, mostly dev and Hardcore server items), in its `grade` colour |
| Description   | text | LOC `str_type=0`, `str_id4=1`, in its game colours, on one line and cut; the file stores no description. 61,837 of 70,284 items have one on client 3458 |
| Max Level     | num  | Highest `enchant_level` among the item's keys; `0` when it cannot be enhanced. [itemmaxlevel.dbss](itemmaxlevel_dbss.md) stores the same value for every item with an `enchant_key` |
| Enchant Key   | num  | `enchant_key`, the item's key in [enchantstaticstatus.dbss](enchantstaticstatus_dbss.md); dash when `0` |
| Enhancement Type | num | `enhancement_type`, after the icon; the item's rows in [guaranteeenchantss.dbss](guaranteeenchantss_dbss.md); dash when `0` |
| Slot          | text | `equip_slot` as the tooltip's slot label, LOC type 37; dash for `46`. Servant gear (`servant_kinds` not `0`) shows its group's label from the table under `equip_slot`, or the bare number when no group labels its slot |
| Weapon Type   | text | Main and sub-weapons: LOC type 44 name of the market subcategory their type's listed items share, see `equip_type`; dash for other items |
| Req. Level    | num  | `required_level`; dash when `0` or `1` |
| Classes       | text | `class_mask` as LOC type 21 class names; "All" when every playable class is set, "All except ..." when up to three are missing |
| Binding       | text | `vested_type` and `family_bound`: "On obtain (Family)", "On equip (Character)" and so on; dash when the item never binds |
| Durability    | num  | `max_durability`; dash for `32,767` |
| Stackable     | flag | `stackable` |
| Marketable    | flag | `marketable`, after the icon |
| Family Inventory | flag | `family_inventory` is `2`, after the icon |
| Trade         | text | `trade_type` of trade goods: Trade Manager (`0` and `4`), Trade Manager (Karma loss) (`1`), Imperial Crafting Delivery (`3`), Guild trade (`5`); dash for other items |
| Dyeable       | flag | `dyeable`; a tick still needs dye parts on the model, so PEN: Sovereign Staff shows one and cannot be dyed |
| Object ID     | num  | `character_id` of the placed object or summoned pet; dash when `0` |
| Object        | text | LOC `str_type=6`, `str_id1=character_id`          |
| Buffs         | list | Buffs of `skill_key_1`, then `skill_key_2` (`SKILL_BUFFS` lookup index), each once, with buff icon and the first line of its LOC type `5` text in its game colours; sorts by count |
| Lightstone Sets | list | Sets of [lightstoneset.bss](lightstoneset_bss.md) that list the item as a member or substitute (`LIGHTSTONE_SETS` lookup index), as set ID and LOC type `113` name in its colour; sorts by count |

## Notes

- `itemenchantbackendtest.dbss` (73 MB) contains the identical set of 169,962
  icon path references and 21,768 unique paths; it looks like a test copy and
  adds nothing. `itemenchantbackend.dbss` (121 MB) contains no icon paths at all.
- 17 `gamecommondata` tables store inline icon paths this way. After this file
  the largest are `cashproduct.dbss` (14,750 unique paths, keyed by cash product
  ID rather than item ID), `quest.dbss` (6,366) and `skilltype.dbss` (3,530).
- The icon path is why ~14,400 ID-named icons match no LOC item name: cash-shop
  items reference a product-ID icon such as
  `Icon/New_Icon/09_Cash/03_Product/00105099.dds` while the item itself is a
  different ID. Those icons are reachable only through a stored path.
- Reading the whole file to build an index costs a 194 MB decompress, which is
  too slow to repeat per launch; an index built from this file should be cached
  on disk and invalidated on the PAZ meta version, the way `paz/bdo_cache.py`
  already caches the entry list.
- Blocks are contiguous and the companion is sorted by key, so a targeted lookup
  can read a single block by offset without parsing the whole file.

## Open Questions

### Enchant Data Fields

Only the fields named in Block Structure and After the icon are checked
here. The entries of the lists between `+0xD4` and the name, and the
remainder after `enhancement_type`, are undecoded here and in
bdo-data-extractor. The fields below have a name there that neither bdocodex
nor my own items could confirm (2026-10-05):

- **Pearl Shop flag** (`+0xA4`): `1` in 28,511 base items, which fits the
  outfits, but no tooltip line shows it.
- **Trade type `4`**: Redfin Anthias, Opah and 107 other fish. bdocodex says
  they sell to Trade Managers, like the `0` fish (Cano Toadfish); what sets
  them apart is open. The Trade column shows both as Trade Manager.
- **`unknown_0f`** (after the icon, bind type there): neither the bound text
  nor "Cannot be enhanced" comes from it, see After the icon.
- **`unknown_limit`** (market registration limit there): neither the
  listing nor the pre-order limit.
- **`unknown_crystal_group`** (crystal transfusion group there): the only
  example, Magic Crystal of Infinity, is no longer in the game.
- **Dye parts**: `unknown_ac` is not the count, and no byte of the block
  holds it; where the client gets it (likely the model) is open.

### Header Fields Without a Meaning

These fields have a known shape on client 3464 but no confirmed meaning:

- `unknown_44` is `1` in 10,027 base items, among them 6,780 of the 6,862
  items whose icon sits in `03_ETC/12_DoApplyDirectlyItem`, the folder the
  quest reward window (`panel_dialog_reward`) takes its EXP icons from.
  Advice of Valks (+10) and copies of Silver, Milk and Beer that are type
  `2` also store `1`. calpheonlabs calls it "appliesDirectly"; no Lua getter
  ties it to the offset.
- `unknown_5d` lists bytes on mount and ship gear only. The Epheria Carrack
  and Oquilla parts store `1` to `4` in the order Advance, Balance, Volante,
  Valor. It is not the servant kind, which is `servant_kinds`; the bytes may
  pick a model or tier within one kind.
- The entries of the lists before the name: the first holds a class type and
  a u32 per allowed class.

### Items Without a Record

4,655 of the 73,947 LOC item IDs have no level-0 record. Whether these are
unreleased, region-specific, or simply not enchantable is unknown, and it is
also unconfirmed whether they have an icon reachable some other way.

### Second Block String

The optional second string (`second_string` in the parser; it has no fixed
offset, so it cannot be named `unknown_<offset>`) looks like an effect or sound tag
(`ITEM_BIC_HIT_1` through `ITEM_BIC_HIT_4` were observed) and appeared in 46 of
350 sampled blocks, all of them weapons or armour. What consumes it, and whether
other tag families exist, is unconfirmed. Earlier versions called it
`effect_tag` and showed it as an Effect Tag column; it stays on the record for
search and CSV but is no longer shown.

## In-Game Checks

### Max Stack at `+0x65`

Needs item (any one):

- [HP Potion (Beginner)](https://bdocodex.com/us/item/502/), 21 or more
- [MP Potion (Beginner)](https://bdocodex.com/us/item/503/), 21 or more

bdo-data-extractor names `+0x65` (`unknown_65`) max stack. On client 3464
it is `0x7FFFFFFF` on every base item, stackable or not, except four that
store a small number: 20 for both potions, 99 for Deputy Token (65208) and
61 for Combat EXP Scroll (848). All four have `stackable` set. An earlier
version also listed `0xFFFFFF00` on 120 items and 1 on Ashen Crow Horse Gear
(336064); those were mount and ship gear read without their `unknown_5d`
entries. Deputy Token is a moderator item ("It is used to control abusers of
the Megaphone item"), so the potions are the test items. Put more than 20 of
one potion in the inventory and look at the slots. If it splits into a
second stack at 20, `+0x65` is the max stack. If it stays in one stack, the
field is something else.
