# `abyssoneequipmentpreset.bss` Format

## Purpose

The gear the Magnus (`AbyssOne`) hands out, per equipment slot: a list of
presets, each a class type, an item key and a coin price. The armor and
accessory slots hold one item for every class, the weapon slots one item
per class type, and four armor slots and the weapon slots end with a
Magic Crystal for every class. The file has no PABR magic. The client
reads it through `ToClient_GetAbyssOnePresetStaticStatus(equipSlotNo,
classType, presetLevel, isSocket)`, whose result gives
`getEquipItemKey()` and `getAbyssCoin()` (`panel_abyssone_equippresetlist.luac`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes | Records            | Row bytes |
| ------ | -------------- | ------- | ----------------------------- | ----- | ------------------ | --------- |
| 1      | 2011 and later | 3482    | `abyssoneequipmentpreset.bss` | 2,221 | 113 Preset, 14 Row | 19        |

| Layout | File                          | Known           | Unknown       |
| ------ | ----------------------------- | --------------- | ------------- |
| 1      | `abyssoneequipmentpreset.bss` | 1,543 B (69.5%) | 678 B (30.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3454   | Layout 1 |
| 3412   | Layout 1 |
| 3381   | Layout 1 |
| 3349   | Layout 1 |
| 3314   | Layout 1 |
| 3283   | Layout 1 |
| 3251   | Layout 1 |
| 3212   | Layout 1 |
| 3177   | Layout 1 |
| 3144   | Layout 1 |
| 3103   | Layout 1 |
| 3062   | Layout 1 |
| 3037   | Layout 1 |
| 3002   | Layout 1 |
| 2959   | Layout 1 |
| 2923   | Layout 1 |
| 2900   | Layout 1 |
| 2872   | Layout 1 |
| 2834   | Layout 1 |
| 2803   | Layout 1 |
| 2765   | Layout 1 |
| 2736   | Layout 1 |
| 2703   | Layout 1 |
| 2665   | Layout 1 |
| 2637   | Layout 1 |
| 2606   | Layout 1 |
| 2583   | Layout 1 |
| 2545   | Layout 1 |
| 2519   | Layout 1 |
| 2498   | Layout 1 |
| 2468   | Layout 1 |
| 2438   | Layout 1 |
| 2414   | Layout 1 |
| 2384   | Layout 1 |
| 2358   | Layout 1 |
| 2335   | Layout 1 |
| 2313   | Layout 1 |
| 2290   | Layout 1 |
| 2250   | Layout 1 |
| 2224   | Layout 1 |
| 2203   | Layout 1 |
| 2179   | Layout 1 |
| 2151   | Layout 1 |
| 2134   | Layout 1 |
| 2107   | Layout 1 |
| 2073   | Layout 1 |
| 2052   | Layout 1 |
| 2011   | Layout 1 |
| 1996   | No file  |
| 1969   | No file  |
| 1937   | No file  |
| 1914   | No file  |
| 1886   | No file  |
| 1866   | No file  |
| 1838   | No file  |
| 1818   | No file  |
| 1794   | No file  |
| 1784   | No file  |
| 1749   | No file  |
| 1717   | No file  |
| 1698   | No file  |
| 1674   | No file  |
| 1636   | No file  |
| 1608   | No file  |
| 1587   | No file  |
| 1565   | No file  |
| 1537   | No file  |
| 1509   | No file  |
| 1485   | No file  |
| 1466   | No file  |
| 1445   | No file  |
| 1426   | No file  |
| 1409   | No file  |
| 1390   | No file  |
| 1372   | No file  |
| 1360   | No file  |
| 1348   | No file  |
| 1338   | No file  |
| 1324   | No file  |
| 1316   | No file  |
| 1309   | No file  |
| 1286   | No file  |
| 1256   | No file  |
| 1230   | No file  |
| 1211   | No file  |
| 1194   | No file  |
| 1177   | No file  |
| 1156   | No file  |
| 1127   | No file  |
| 1109   | No file  |
| 1076   | No file  |
| 1058   | No file  |
| 1016   | No file  |
| 990    | No file  |
| 955    | No file  |
| 911    | No file  |
| 885    | No file  |
| 855    | No file  |
| 822    | No file  |
| 794    | No file  |
| 748    | No file  |
| 711    | No file  |
| 683    | No file  |
| 656    | No file  |
| 630    | No file  |
| 606    | No file  |
| 577    | No file  |
| 542    | No file  |
| 526    | No file  |
| 508    | No file  |
| 485    | No file  |
| 457    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler names the equipment slot with its item tooltip label
and each item with its LOC type 0 name from `languagedata_*.loc` when it
is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type           | Field     | Notes          |
| ------- | -------------- | --------- | -------------- |
| `+0x00` | u32            | row_count | Number of rows |
| `+0x04` | Row[row_count] | rows      | See Row        |

### Row (variable: 5 bytes + presets)

| Offset  | Type                   | Field        | Notes                                                                      |
| ------- | ---------------------- | ------------ | -------------------------------------------------------------------------- |
| `+0x00` | u8                     | equip_slot   | `__eEquipSlotNo*` value, the `equip_slot` of `itemenchant.dbss`; unique per row |
| `+0x01` | u32                    | preset_count | Number of `presets`                                                        |
| `+0x05` | Preset[preset_count]   | presets      | See Preset                                                                 |

### Preset (19 bytes)

| Offset  | Type | Field          | Notes                                                                       |
| ------- | ---- | -------------- | --------------------------------------------------------------------------- |
| `+0x00` | u8   | class_type     | Class type (`0` Warrior, LOC type 21), or `101` on the presets for every class |
| `+0x01` | u8   | unknown_01     | Equals the row's `equip_slot` on every preset; see Open Questions          |
| `+0x02` | u8   | unknown_02     | `0` on every client checked                                                 |
| `+0x03` | u32  | item_key       | Item key: `enchant_level << 24 \| item_id`; level `0` on every preset        |
| `+0x07` | i32  | unknown_07     | `-1` on every client checked                                                |
| `+0x0B` | u64  | abyss_coin     | Coin price of the preset; `0` on every client checked                       |

## Slots

Client 3482, in file order: each slot's item tooltip label and its
presets.

| `equip_slot` | Slot             | Presets                                                                      |
| ------------ | ---------------- | ---------------------------------------------------------------------------- |
| 12           | Belt             | `101` Belt of Instinct                                                       |
| 11, 10       | Earring          | `101` Earring of Change                                                      |
| 9, 8         | Ring             | `101` Ring of Fate                                                           |
| 7            | Necklace         | `101` Necklace of Spacetime                                                  |
| 6            | Helmet           | `101` Helmet of Reverie, `101` HAN Combined Magic Crystal - Hoom             |
| 5            | Shoes            | `101` Shoes of Flight, `101` Ancient Magic Crystal of Nature - Adamantine    |
| 4            | Gloves           | `101` Gloves of Resolve, `101` JIN Magic Crystal - Viper                     |
| 3            | Armor            | `101` Armor of Balance, `101` Magic Crystal of Infinity - Max HP             |
| 1            | Sub-weapon       | 32 class types (Shield of Harmony for Warrior), then `101` Magic Crystal of Infinity - Critical Hit |
| 0            | Main Weapon      | 32 class types (Longsword of the Challenger for Warrior), then `101` Crystal of Elkarr |
| 29           | Awakening Weapon | 31 class types (Greatsword of Serenity for Warrior), then `101` HAN Combined Magic Crystal - Hoom |
| 27           | Alchemy Stone    | `101` Rift's Alchemy Stone                                                   |

## Field Names

The Magnus is newer than client 1784: the file is not in its archives and
no sheet of a private server's `DataSheets.bexcel` on that client has
`Abyss` in its name. The names come from the client Lua (client 3482):
`ToClient_GetAbyssOnePresetStaticStatus` takes the equip slot, the class
type and the preset's index, and the Lua shows the item of
`getEquipItemKey()` (an item key it passes to
`getItemEnchantStaticStatus`) and the price of `getAbyssCoin()`, an s64
that the u64 `abyss_coin` holds; a price of `0` marks a basic item there
(`isBasicItem = needCoin_s64 <= 0`). `equip_slot` values match the
tooltip slot of each item (Belt `12`, Helmet `6`, Main Weapon `0`). On
client 3482 the `class_type` values of the main and sub-weapon slots are
the 32 class types `0` to `35` without `13`, `14`, `18` and `22`, each
with its own weapon; the awakening weapon slot lacks `35`.

## Notes

- The Lua passes `__eClassType_Count` as the class type for every slot
  except the main, sub and awakening weapons, where it passes the
  player's class; the file stores `101` exactly on those slots and on the
  crystals that close the weapon lists.
- The weapon lists grow with the clients as classes were added: 26, 26
  and 25 presets on client 2107, 33, 33 and 32 on client 3474.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/abyssone_tables.py`: the
  slot with its label, then each preset as class, item name and item ID,
  with the coin price when it is not `0`.

## Open Questions

### How the Client Tells Crystals From Gear

`ToClient_GetAbyssOnePresetStaticStatus` takes an `isSocket` flag, but no
preset field marks a crystal: the Magic Crystals sit in the same lists as
the gear with the same `unknown_07` `-1` and class `101`. The item type
of the item key may decide it; `unknown_07` is `-1` on every preset of
every client checked.

### Why Each Preset Repeats Its Slot

`unknown_01` equals the row's `equip_slot` on every preset of every
client checked, and `unknown_02` after it is always `0`. The two bytes may
be one u16 slot number of the preset; the Lua reads neither.
