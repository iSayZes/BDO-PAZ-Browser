# `guaranteeenchantss.dbss` Format

## Purpose

The Ancient Anvil table: for each enhancement type and current enhancement
level, how many Agris Essences a failed attempt has to stack before the next
attempt at that level is guaranteed. The enhancement window shows this count
as the hammer gauge (`getSSEnchantCount()` in the client Lua). The enhancement
type is the item's `enhancement_type` in `itemenchant.dbss`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------- | --------- |
| 1      | 3473 and later | 3474    | `guaranteeenchantss.dbss` | 2,307 | 329 Row | 7         |

| Layout | File                      | Known            | Unknown    |
| ------ | ------------------------- | ---------------- | ---------- |
| 1      | `guaranteeenchantss.dbss` | 2,307 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File               | Required | Role                                                                 |
| ------------------ | -------- | -------------------------------------------------------------------- |
| `itemenchant.dbss` | Optional | The items of each enhancement type; the handler reads them from the `ENHANCEMENT_TYPE_ITEMS` lookup index, not as a companion |

There is no `guaranteeenchantssoffset.dbss`.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                              |
| ------- | ---------- | ----- | ---------------------------------- |
| `+0x00` | u32        | count | Number of rows; 329 on client 3464 |
| `+0x04` | Row[count] | rows  | See Row                            |

There is no `PABR` magic and no trailer: the file is `4 + count × 7` bytes
(2,307 on client 3464).

### Row (7 bytes)

| Offset  | Type | Field            | Notes                                                       |
| ------- | ---- | ---------------- | ----------------------------------------------------------- |
| `+0x00` | u32  | enhancement_type | `enhancement_type` of the item in `itemenchant.dbss`        |
| `+0x04` | u8   | enchant_level    | The item's current level; the attempt goes to the next level |
| `+0x05` | u16  | agris_count      | Agris Essences needed for a guaranteed success; `0` means no gauge at that level |

The row is unaligned: `agris_count` starts at an odd offset. `(enhancement_type,
enchant_level)` is unique. Rows are not sorted by either field (the first rows
are `24/7`, `3/10`, `2/17`, `1/0`).

`enchant_level` is the current level and not the target: types of items that
go to PEN at level 20 run 0 to 19 and types of five-level accessories run 0
to 4, so no row exists for the highest level. Levels 0 to 6 of types 1, 2
and 7 store `0`.

## Enhancement Types

The items of each enhancement type on client 3464, from `enhancement_type` in
`itemenchant.dbss`; base items only, with each item's highest level.

| Type  | Levels | Items (client 3464) | Example items                                                    |
| ----: | ------ | ------------------: | ---------------------------------------------------------------- |
| 1     | 0-19   | 3,678 | Kzarka Longsword, Kutum Shotgun, Offin Tett's Radiant Kyve, Rebar Helmet |
| 2     | 0-19   | 382   | Blackstar Longsword, Blackstar Kunai, Fiery Blackstar Hexround      |
| 3     | 0-19   | 0     | None; Naru gear until 2025-12-18 (see Notes)                      |
| 4     | 0-19   | 0     |                                                                   |
| 5     | 0-4    | 0     | None; Godr-Ayed weapons until 2026-03-26 (see Notes)              |
| 6     | 0-4    | 12    | Fallen God's Armor, Labreska's Helmet, Ator's Shoes, Dahn's Gloves |
| 7     | 0-19   | 24    | Manos Cook's Clothes, Loggia Hunter's Clothes, Crio Fisher's Clothes |
| 8     | 0-9    | 184   | [Donkey] Steel Combat Barding, Trade Wagon Wheel, [Hunting] Master Matchlock |
| 9     | 0-9    | 11    | Epheria Galleass: Enhanced Plating, Epheria Caravel: Verisha Cannon |
| 10    | 0-9    | 11    | Epheria Galleass: Mayna Cannon, Epheria Caravel: Black Dragon Figurehead |
| 11    | 0-9    | 8     | Panokseon: Haemo's Sail, Epheria Carrack: Toro Cannon               |
| 12    | 0-9    | 24    | Epheria Carrack: Valor (Chiro's Cannon), Panokseon: Byukgye's Enhanced Sail |
| 13    | 0-4    | 176   | Deboreka Necklace, Talis Earring, Yuria Necklace, Red Coral Ring     |
| 14    | 0-4    | 10    | Capotia Earring, Tidal Capotia Belt                                 |
| 15    | 0-4    | 12    | Manos Ring, Loggia Necklace, Geranoa Belt                           |
| 16    | 0-9    | 4     | Tuvala Belt, Ring, Earring and Necklace                             |
| 17    | 0-4    | 15    | Asula's Crimson Eye Earring, Ring of Sealed Magical Power, [Event] Terrmina Necklace |
| 18    | 0-2    | 4     | Forest's Eye Earring, Rock Heart Belt, Red Sand Crystal Ring, Tears of the Wind Necklace |
| 19    | 0-9    | 212   | Sovereign Longsword, Sovereign Dual Glaives                          |
| 20    | 0-19   | 1     | [Event] Tarnished Sword                                             |
| 21    | 0-9    | 8     | Kharazad Necklace, Moonhushed Kharazad Earring                      |
| 22    | 0-9    | 4     | Preonne Belt, Ring, Earring and Necklace                            |
| 23    | 0-24   | 168   | Tuvala Helmet, Tuvala Shotgun, Combatant's Tuvala Longsword         |
| 24    | 0-9    | 4     | Edana - Furystride, Edana - Oathgrip, Edana - Abyssveil, Edana - Heavensmite |
| 25    | 0      | 3     | Imperfect Alchemy Stone of Life, Protection and Destruction          |
| 26    | 0      | 3     | Sturdy Alchemy Stone of Life, Protection and Destruction             |
| 27    | 0      | 9     | Sharp Alchemy Stone of Destruction, Resolute Alchemy Stone - Protection |
| 28    | 0      | 20    | Resplendent Alchemy Stone of Life, Resplendent Khan's Heart: Protection |
| 29    | 0      | 20    | Splendid Alchemy Stone of Life, Blessed Splendid Vell's Heart        |
| 30    | 0-9    | 8     | Ekleta Necklace, Duskborne Ekleta Belt                              |
| 31    | 0-9    | 8     | Apeiron Necklace, Sunstarved Apeiron Ring                           |
| 32    | 0-9    | 16    | Epheria Carrack: Valor (Falasi's Sail), Epheria Carrack: Balance (Falasi's Plating) |
| 33    | 0-15   | 0     |                                                                   |

Type 0 (65,174 base items) has no rows. Types 25 to 29 are alchemy stones
with one level; the LOC note on alchemy stone growth (type 37, id1
1288266772) reads "A full Ancient Anvil and 80%+ EXP guarantees a higher
grade".

## Notes

- How the client uses the count (`panel_widget_enchant_main_all`,
  `updateAgrisStack`): the gauge is shown when `getSSEnchantCount()` is not
  `0` and the target cannot be changed to Tuvala. It reads
  `getCurrentEnchantCount() / getSSEnchantCount()`, and at a full gauge the
  hammer effect `fUI_SpiritEnchant_New_Hammer_01A` plays.
  `ToClient_IsGuaranteeEnchant()` then sets the shown success rate to
  `1000000`, which is `CppDefine.e100Percent` (100%).
- The gauge tooltip (`LUA_ANVILOFANCIENT_TOOLTIP_DESC`) reads "Upon failed
  enhancement, Agris Essence is accumulated for the gear and its enhancement
  level. Once enough Agris Essence has accumulated, enhancement success is
  guaranteed." The count is per item and per level, as the table is.
- `enhancement_type` is the u32 of the same name in the After the Icon
  section of [itemenchant.dbss](itemenchant_dbss.md). On client 3464 every
  type an item carries has rows here, and only types 3, 4, 5 and 33 have
  rows but no items.
- Garmoth's Ancient Anvil guide lists the same counts, e.g. 35 for a yellow
  TET weapon to PEN (type 1, level 19) and 15 for a TET Blackstar to PEN
  (type 2, level 19).
- `agris_count` is not the `enchantstaticstatus.dbss` count: Blackstar
  Longsword stores 3,670 there at PEN, against 15 here.
- On client 3464, `agris_count` runs 0 to 1,000; 1,000 is type 6, level 4
  (Fallen God gear at TET).
- Type 4 stores the same counts as the first 20 levels of type 23
  (Tuvala), including `0` at levels 15 to 17.
- Type 5 is left over from the Godr-Ayed weapons. Pearl Abyss's
  [notice for the 2026-03-26 update](https://blackdesert.pearlabyss.com/Asia/en-us/News/Notice/Detail?_boardNo=13023)
  removed them and turned each into a Blackstar weapon (PRI to TET into TET
  Blackstar plus Silver, PEN into PEN Blackstar), and Garmoth's Ancient Anvil
  guide lists type 5's counts (7, 9, 11, 15, 18) under Godr-Ayed ("After").
  Its five levels fit the PRI to PEN range of those weapons. Godr-Ayed
  Celestial Bo Staff (954005), the one item still named Godr-Ayed on client
  3464, stores type `0`.
- Type 3 is left over from the Naru gear. The Season Changes FAQ for the
  [2025-12-18 maintenance](https://www.naeu.playblackdesert.com/en-us/News/Detail?groupContentNo=9477&countryType=de-DE)
  says Naru Gear "has been replaced by Tuvala Gear", which now enhances from
  +0 to PEN on every character, and Garmoth's Ancient Anvil guide lists type
  3's counts under Naru. Its levels 0 to 19 fit gear that goes from +0 to
  PEN. No English item name on client 3464 starts with "Naru ".

## Open Questions

### Enhancement Types Without Items

No item on client 3464 carries `enhancement_type` 4 or 33, so those rows
have no items to name them by (types 3 and 5 are removed Naru and Godr-Ayed
gear, see Notes). Removed gear would explain them too. Type 4 stores the same
counts as the first 20 levels of type 23 (Tuvala); type 33 stores one count,
10 at level 15. A patch notice that removes gear with those levels, or a
patch that adds items with these values, would settle it.
