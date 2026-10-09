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

Only the item ID, the placed character and the strings are confirmed. A block
opens with the item ID and ends with a large run of enchant-related numeric
fields that are not yet decoded.

| Offset  | Type | Field    | Notes                                    |
| ------- | ---- | -------- | ---------------------------------------- |
| `+0x00` | u32  | item_id      | Repeats the item ID from the key                             |
| `+0x04` | u8   | item_type    | Tooltip class (`EItemType`), see below                       |
| `+0x05` | u8   | category     | Item classification                                          |
| `+0x06` | u8   | grade        | `0` to `5`, the item name colour, see below                  |
| `+0x07` | ...  | unknown      | Numeric fields                                               |
| `+0x13` | u8[43] | unknown_13 | Always `0x2E` in all 70,284 base blocks                     |
| `+0x3E` | u8   | unknown_3e   |                                                              |
| `+0x3F` | i32  | weight       | Divide by 10,000 for LT                                      |
| `+0x43` | ...  | unknown      | Numeric fields                                               |
| `+0x45` | u32  | expiration_minutes | `0` when the item does not expire; set in 4,580 base items |
| `+0x49` | u8   | vested_type  | When the item binds: `0` never (34,516 base items), `1` when obtained (17,372), `2` when equipped (18,396) |
| `+0x4A` | u8   | family_bound | `1` binds to the family, `0` to the character; set in 5,942 base items |
| `+0x4B` | u8   | for_trade    | `1` on trade goods that Trade Managers buy; 2,007 base items |
| `+0x4C` | u8   | trade_type   | Kind of trade good, only set with `for_trade`, see below     |
| `+0x4D` | u64  | class_mask   | Classes that can use the item, bit `n` for class ID `n`. All-class items set most bits, so test single bits |
| `+0x55` | ...  | unknown      | Numeric fields                                               |
| `+0x61` | u8   | required_level | Character level needed to use the item; `0` or `1` when there is none, above `1` in 3,734 base items |
| `+0x62` | ...  | unknown      | Numeric fields                                               |
| `+0x6E` | i64  | buy_price    |                                                              |
| `+0x76` | i64  | sell_price   |                                                              |
| `+0x7E` | i32  | repair_price |                                                              |
| `+0x82` | ...  | unknown      | Numeric fields                                               |
| `+0xA8` | u8   | dyeable      | `0`: the item cannot be dyed (45,895 base items). `1` (24,373): it can, if it also has dye parts, which this file does not hold, see below. 16 wagon parts store `3` |
| `+0xA9` | u8   | unknown_a9   |                                                              |
| `+0xAA` | u16  | character_id | Character the item places or summons; `0` when none. See below |
| `+0xAC` | u8   | unknown_ac   | Not the number of dye slots, see below. `0` on all 3,960 object links; across base items `0` (61,650), `1` (4,786), `2` (2,165), `5` (1,052), `10` (218) |
| `+0xAD` | u8   | unknown_ad   | `0` in 69,875 base items                                     |
| `+0xAE` | ...  | unknown      | Numeric fields                                               |
| `+0xC4` | u8   | personal_trade | `1` when the item can be traded between players; 330 base items |
| `+0xC5` | u16  | max_durability | `32,767` for items without durability (51,959 base items); equipment mostly `100` or `120` |
| `+0xC7` | u8   | unknown_c7   |                                                              |
| `+0xC8` | u8   | market_category | Central Market category; `255` when the item is not listed (56,870 base items) |
| `+0xC9` | u8   | market_sub_category | Subcategory, in the market's menu order; `255` when not listed |
| `+0xCA` | u16  | unknown_ca   |                                                              |
| `+0xCC` | u32  | skill_key_1  | Skill a consumable casts, a [`skill.dbss`](skill_dbss.md) key; its `buff_ids` are the item's buffs; `0` when none |
| `+0xD0` | u32  | skill_key_2  | Second skill, used by composite meals; `0` when none          |
| `+0xD4` | ...  | unknown      | Numeric fields up to the name: 16 or 21 bytes in most base blocks, 176 in 597 gear blocks, then a u32 that bdo-data-extractor calls the enchant key (0 in 40,025 base items, never the item ID); with the block's level it is the key of [enchantstaticstatus.dbss](enchantstaticstatus_dbss.md) |
| varies  | ...  | name_kr      | Korean item name: u64 character count, then UTF-16LE text that ends where the icon's prefix starts. Present in all 70,284 base blocks (client 3458) |
| varies  | ...  | strings      | One or two length-prefixed ASCII strings                     |
| varies  | ...  | unknown  | Remaining enchant data                   |

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

### Placed or summoned character

`character_id` sits in the fixed numeric part: in every block, at every level, the first string's prefix starts at `+0xF2` (242) or later (client 3458), and every block is at least 693 bytes long.

| Measure (level-0 blocks)                         | Value |
| ------------------------------------------------ | ----: |
| Characters named by at least one item            | 5,095 |
| ... that have a `characterobject.dbss` record    | 3,960 |
| ... named by exactly one item (kept as a link)   | 5,090 |
| Characters named by more than one item           |     5 |

Measured before the 2026-09-27 update. After it, 5,103 characters are named by at least one item, still 5 by more than one, so 5,098 are kept as links.

All 5,095 are `characterstatic.dbss` IDs; the ones without an object record are mostly pets.

Examples: `58001` Strong Fence Garden (item) → `2001` Strong Fence Garden; `820908` Truffle Mushroom Hypha → `1436` Truffle Mushroom Crop; `860014` [Pet] Striped Cat (Tier 3) → `9425` Cat. Of the 3,960 object links, 2,961 have identical item and character names; the rest pair a seed with its crop or a `[Guild]` item with its structure.

Character `1` is named by 120 unrelated items, so there the value is not a link. The browser keeps only characters named by exactly one item.

### Length-prefixed string

| Offset  | Type   | Field  | Notes                          |
| ------- | ------ | ------ | ------------------------------ |
| `+0x00` | u32    | length | Byte length of `text`          |
| `+0x04` | u32    | zero   | Always 0 in observed data      |
| `+0x08` | char[] | text   | ASCII, not null-terminated     |

The string does **not** sit at a fixed block offset: 47 distinct offsets were
observed across a 400-block sample, so a parser must scan for the
`(length, 0, ascii × length)` shape rather than seek a constant. The browser
starts the scan at `+0xD4`, where the fixed fields end.

A block holds at most two strings:

| Position | Content                                                        |
| -------- | -------------------------------------------------------------- |
| first    | Icon path, relative to `ui_texture/icon/`                       |
| second   | Optional `second_string` such as `ITEM_BIC_HIT_1`; absent in most blocks, meaning unconfirmed |

The first string is always the icon path. In a 400-block sample the length
prefix matched the string length 400 out of 400 times.

### Resolving the icon path

Stored paths always begin with `New_Icon/`, so the PAZ path is the stored value
prefixed with `ui_texture/icon/`, matched case-insensitively:

```text
New_Icon/03_ETC/06_Housing/InHouse_Cultivate_Sea_Clam_01_Wall.dds
  -> ui_texture/icon/new_icon/03_etc/06_housing/inhouse_cultivate_sea_clam_01_wall.dds
```

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
| varies  | u32       | enhancement_type  | Enhancement system: `0` none, `1` ordinary weapons and armour, `13` ordinary accessories, `19` Sovereign weapons, `21` Kharazad, `23` Tuvala weapons and armour; the full list is in bdo-data-extractor |
| varies  | ...       | unknown       | Undecoded remainder, holding `second_string` about 330 bytes in |
| end-6   | u32       | item_id       | Repeats the item ID, in all 70,284 base blocks |
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
| Max Level     | num  | Highest `enchant_level` among the item's keys; `0` when it cannot be enhanced |
| Req. Level    | num  | `required_level`; dash when `0` or `1` |
| Classes       | text | `class_mask` as LOC type 21 class names; "All" when every playable class is set, "All except ..." when up to three are missing |
| Binding       | text | `vested_type` and `family_bound`: "On obtain (Family)", "On equip (Character)" and so on; dash when the item never binds |
| Durability    | num  | `max_durability`; dash for `32,767` |
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
here. The variable bytes between `+0xD4` and the name, and the remainder
after `enhancement_type`, are undecoded here and in bdo-data-extractor. The
fields below have a name there that neither bdocodex nor my own items could
confirm (2026-10-05):

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

bdo-data-extractor names `+0x65` max stack. It is `0x7FFFFFFF` on almost
every base item, stackable or not, and `0xFFFFFF00` on 120 items such as
`336063` and `607880` to `607895`. Five store a small number: 20 for both
potions, 99 for Deputy Token (65208), 61 for Combat EXP Scroll (848) and 1
for Ashen Crow Horse Gear (336064). Deputy Token is a moderator item
("It is used to control abusers of the Megaphone item") and horse gear does
not stack, so the potions are the test items. Put more than 20 of one potion in the inventory and
look at the slots. If it splits into a second stack at 20, `+0x65` is the
max stack. If it stays in one stack, the field is something else.
