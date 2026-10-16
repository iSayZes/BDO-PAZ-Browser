# `fairypotion.dbss` Format

## Purpose

The potions a fairy can be set to use. The file holds one item list per
potion type: list `0` is the HP potions for the fairy's HP slot, lists `1`,
`2` and `3` the potions for the MP slot of classes that use MP, WP and SP.
`fairypotionoffset.dbss` is the type-keyed index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records       | Row bytes                  |
| ------ | -------------- | ------- | ------------------------ | ----- | ------------- | -------------------------- |
| 1      | 1784 and later | 3473    | `fairypotion.dbss`       | 1,200 | 4 Potion List | 257 to 313, 299 on average |
| 1      | 1784 and later | 3473    | `fairypotionoffset.dbss` | 44    | 4 Offset Row  | 10                         |

| Layout | File                     | Known            | Unknown    |
| ------ | ------------------------ | ---------------- | ---------- |
| 1      | `fairypotion.dbss`       | 1,200 B (100.0%) | 0 B (0.0%) |
| 1      | `fairypotionoffset.dbss` | 44 B (100.0%)    | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                                      |
| ------------------------ | -------- | --------------------------------------------------------- |
| `fairypotionoffset.dbss` | Optional | `potion_type -> (data_offset, data_size)` index           |
| `languagedata_en.loc`    | Optional | Item name for `item_id` (`str_type=0`, `str_id1=item_id`) |

Each list stores its own item count, so the handler walks the main file
without the offset companion.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type               | Field | Notes                |
| ------- | ------------------ | ----- | -------------------- |
| `+0x00` | u32                | count | Number of lists      |
| `+0x04` | Potion List[count] | lists | See Potion List      |

### Potion List (variable: 5 bytes + items)

| Offset          | Type             | Field       | Notes                                   |
| --------------- | ---------------- | ----------- | --------------------------------------- |
| `+0x00`         | u32              | item_count  | Number of item IDs that follow          |
| `+0x04`         | u32[item_count]  | item_ids    | Items the fairy may use for this type   |
| `item_ids+0x00` | u8               | potion_type | List key, see Potion Types              |

A list is `4 + 4 * item_count + 1` bytes. The key is the last byte of the
list, not the first, and the last list ends at the end of the file.

On client 3464 the file is 1,200 bytes: 4 lists stored in key order `3`, `2`,
`1`, `0` with 77, 77, 77 and 63 items (294 rows in the handler).

Every `item_id` has a zero top byte, so it reads the same as an item key with
enhancement level 0 (`_common/item_key.py`).

### `fairypotionoffset.dbss`

| Offset  | Type              | Field | Notes                                |
| ------- | ----------------- | ----- | ------------------------------------ |
| `+0x00` | u32               | count | Equals the `fairypotion.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                       |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                              |
| ------- | ---- | ----------- | -------------------------------------------------- |
| `+0x00` | u16  | potion_type | List key                                           |
| `+0x02` | u32  | data_offset | Absolute offset of the list's `item_count`         |
| `+0x06` | u32  | data_size   | Whole list, trailing `potion_type` byte included   |

There is no `PABR` magic and no trailer (`parse_bare_offset_rows`). Rows are
in the same order as the lists. Unlike most offset tables, `data_offset`
points at the start of the list, since the key sits at its end.

## Potion Types

| Type | Resource | Items on client 3464                                                       |
| ---- | -------- | -------------------------------------------------------------------------- |
| 0    | HP       | HP potions, Grain Juice, HP Spirit Essence items, Odore's Spirits         |
| 1    | MP       | MP, WP and SP potions, Herbal Juice, MP Spirit Essence items, Ornette's Spirits |
| 2    | WP       | The type `1` items with Odore's Spirits in place of Ornette's Spirits      |
| 3    | SP       | The type `2` items in the same order                                       |

Type `0` is HP: on client 3464 every named item in it is an HP item by its
English LOC name or description. The names of types `1` to `3` come from the
client Lua (see Notes); the lists themselves no longer tell them apart.

## Notes

- The Fairy Settings window (`panel_window_fairy_all_4.luac`,
  `PaGlobal_FairySetting_All`) has one HP slot and one MP slot. Its inventory
  list shows the items for which `ToClient_checkUsableFairyPotion(itemKey,
  classType)` is true. On a click, `ToClient_getFairyPotionType(itemKey,
  classType)` returns `-1` (message `LUA_FAIRYSETTING_NOT_ITEM`), `0` (HP
  slot) or another value (MP slot). Both calls take the player's class type,
  which fits one list per class resource.
- The same Lua file still holds hard-coded lists: `fairyMainPotionData[0]`
  (HP potions) and `fairySubPotionData[1]`, `[2]` and `[3]`. Index `1` holds
  MP potions and is the default; index `2` holds WP potions and is picked for
  the class types in its `spiritClass` table (0 Warrior, 11 Lahn, 12
  Berserker, 19 Striker, 20 Musa, 21 Maehwa, 23 Mystic, 25 Kunoichi, 26
  Ninja, 30 Woosa); index `3` holds SP potions and is picked for class type
  24 (Valkyrie). Indexes `2` and `3` also hold the Herbal Juice items. Only
  `isMP()` and `isHP()` read these tables, and they are passed `mpKeyStr`
  and `hpKeyStr`, which no fairy Lua file sets. The Resource names in this
  doc follow these indexes.
- On client 3464 every item of the Lua lists is in the matching list of this
  file except `[Savage] HP Potion (Extra Large)` (56093), which the Lua HP
  list has and list `0` lacks. Its MP counterpart (56094) is in lists `1` to
  `3`. The file lists add the Spirit Essence items, the Gourd Bottles (1041,
  1042) and others the Lua lists lack.
- Lists `1` to `3` each hold the MP, WP and SP potions together on client
  3464, while the Lua lists keep them apart (index `1` MP only, `2` WP only,
  `3` SP only).
- The two "Spirits" items are named the other way round from the two
  "Spirit Essence" items: Odore's Spirits (40734) and Ornette's Spirit
  Essence (40747) restore 550 HP, Ornette's Spirits (40733) and Odore's Spirit
  Essence (40713) restore 375 MP/WP/SP (English LOC item descriptions).
  List `0` and list `1` follow the descriptions; lists `2` and `3` hold
  Odore's Spirits (HP) and lack Ornette's Spirits.
- On client 3464, 26 rows have no English LOC item name: items 46901 and
  46907 in list `0`, and 46902 to 46904, 46908 to 46910, 720752 and 720753
  in each of lists `1` to `3`. The handler shows their item ID.

## Open Questions

### Potion Types 1 to 3

Type `0` is HP by its content. The MP, WP and SP names of types `1`, `2` and
`3` rest on the indexes of the Lua's `fairySubPotionData` table; the file
lists are near copies of each other, and the class-to-list choice happens in
`ToClient_getFairyPotionType`, which the Lua cannot show.

## In-Game Checks

### Ornette's Spirits for a WP Class

Needs item: [Ornette's Spirits](https://bdocodex.com/us/item/40733/)

Needs class: Warrior, or another class in the Lua's `spiritClass` list

Lists `2` and `3` lack Ornette's Spirits (MP/WP/SP) and hold Odore's Spirits
(HP) instead. Open the fairy's potion settings with Ornette's Spirits in the
inventory. If it is missing from the list on a Warrior but shows on an MP
class such as Sorceress, the client reads list `2` for WP classes, which
confirms type `2` as WP. If it shows on both, the client does not pick the
list by these types the way the Lua does.
