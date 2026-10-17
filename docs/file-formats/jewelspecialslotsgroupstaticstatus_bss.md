# `jewelspecialslotsgroupstaticstatus.bss` Format

## Purpose

The crystal groups each special crystal preset slot accepts: one row per
special slot with its list of [`jewelgroupstaticstatus.bss`](jewelgroupstaticstatus_bss.md)
group numbers. The crystal inventory window greys out a crystal whose group
the selected slot does not accept (`ToClient_IsJewelInSpecialGroup` in
`panel_window_jewelinven_all_1.luac`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                     | Bytes | Records            | Row bytes |
| ------ | -------------- | ------- | ---------------------------------------- | ----- | ------------------ | --------- |
| 1      | 3473 and later | 3473    | `jewelspecialslotsgroupstaticstatus.bss` | 69    | 7 Special Slot Row | 7         |

| Layout | File                                     | Known         | Unknown    |
| ------ | ---------------------------------------- | ------------- | ---------- |
| 1      | `jewelspecialslotsgroupstaticstatus.bss` | 69 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                            |
| ---------------------------- | -------- | ----------------------------------------------- |
| `jewelgroupstaticstatus.bss` | Optional | Group limit and Korean name for the LOC lookup  |
| `languagedata_en.loc`        | Optional | Group names (type 121) and equipment slot names |

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR block of variable rows, followed by the counted string table and
8-byte trailer of [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`). The string table is empty on client 3473.

| Offset              | Type                    | Field              | Notes                            |
| ------------------- | ----------------------- | ------------------ | -------------------------------- |
| `+0x00`             | char[4]                 | magic              | ASCII `PABR`                     |
| `+0x04`             | u32                     | count              | Number of rows; 7 on client 3473 |
| `+0x08`             | Special Slot Row[count] | rows               | See Special Slot Row             |
| `rows+0x00`         | String Table            | string_table       | No strings on client 3473        |
| `string_table+0x00` | u32                     | string_table_start | Where the rows end               |
| `string_table+0x04` | u32                     | zero               | Always `0`                       |

The rows are not sorted by slot.

### Special Slot Row (variable: 5 bytes + groups)

| Offset  | Type              | Field       | Notes                                                    |
| ------- | ----------------- | ----------- | -------------------------------------------------------- |
| `+0x00` | u8                | slot        | Special preset slot, see Special Slots                   |
| `+0x01` | u32               | group_count | Number of `groups`; 1 on every row (client 3473)         |
| `+0x05` | u16[group_count]  | groups      | Accepted crystal groups, `jewelgroupstaticstatus.bss` `group` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Special Slots

A crystal preset has 23 slots, 0 to 22. Slots 0 to 11 are the normal ones,
12 to 22 the `__eJewelSpecialSlot*` ones. The equipment slot is the one the
preset window reads the item from (`panel_window_jewelpreset_all_1.luac`).
Rows on client 3473:

| Slot | `__eJewelSpecialSlot*` | Equipment slot          | Groups                |
| ---- | ---------------------- | ----------------------- | --------------------- |
| 12   | AwakenWeapon1          | 29 AwakenWeapon         | No row                |
| 13   | AwakenWeapon2          | 29 AwakenWeapon         | No row                |
| 14   | PearlAvatarChest       | 14 AvatarChest          | 101 Ancient Spirit    |
| 15   | 1MorningLand           | None                    | No row                |
| 16   | 2MorningLand           | None                    | No row                |
| 17   | Necklace               | 7 Necklace              | 103 Dawn              |
| 18   | Ring1                  | 8 Ring1                 | 103 Dawn              |
| 19   | Ring2                  | 9 Ring2                 | 103 Dawn              |
| 20   | Earing1                | 10 Earing1              | 103 Dawn              |
| 21   | Earing2                | 11 Earing2              | 103 Dawn              |
| 22   | Belt                   | 12 Belt                 | 103 Dawn              |

The numbers come from the client Lua and UI XML, and match where the
slots unlock in game:

- `panel_window_jewelpreset_all.xml` has 12 `Static_NormalSlotBg_NN` and
  11 `Static_SpecialSlotBg_NN` controls. `PaGlobal_JewelPreset:initialize()`
  gives slot `idx` below `__eJewelSpecialSlotAwakenWeapon1` the control
  `Static_NormalSlotBg_<idx + 1>` and the others `Static_SpecialSlotBg_<idx - 11>`,
  with a leading `0` below `__eJewelSpecialSlotEaring2`. Every slot finds
  a control, and all 23 controls get a slot, only with `AwakenWeapon1` = 12
  and `Earing2` = 21.
- The other nine values follow the order of `_lockSlotTooltip` in
  `panel_window_jewelpreset_all.luac`, which lists the eleven slots from
  `AwakenWeapon1` to `Belt`, with `Earing2` tenth.
- The control positions in the XML (`Pan`, all `Center Top`, 85 x 85) put
  each slot where Black Desert Foundry's
  [crystal socket guide](https://www.blackdesertfoundry.com/crystal-sockets-guide/)
  places its unlock: `_01` (12) top left at `-256 20`, unlocked by a Storm
  Devoured or Fiery Awakening Weapon; `_02` (13) top right at `256 20`,
  Fiery Awakening Weapon only; `_03` (14) in the middle at `0 266`, the
  outfit; `_04` (15) and `_05` (16) bottom left and right at `-256 510` and
  `256 510`, one Kkebiwater each from the Land of the Morning Light quests;
  `_06` to `_11` (17 to 22) the bottom row at `y 620`, Kharazad
  accessories. Any other order of 13, 15 and 16 puts a Morning Land slot
  top right.
- The rows agree for 14 and 17 to 22: the Ancient Spirit crystals are
  transfused into "a crystal outfit socket" and the Dawn crystals into "an
  accessory's crystal socket" (item descriptions, LOC type 0 `str_id4` 1).
  The preset window lists the effect of a crystal in the necklace, ring,
  earring and belt slots only when the equipped item's
  `isKarazardAccessory()` is true.
- In game, the outfit slot takes only Ancient Spirit crystals, the six
  bottom slots take only Dawn crystals while Kharazad accessories are
  equipped, and the awakening weapon and Morning Land slots take any
  crystal once unlocked.

## Notes

- The rows hold only the special slots that limit their groups. Slots 12,
  13, 15 and 16 have no row on client 3473 and take any crystal; their
  unlock condition (awakening weapon, Kkebiwater) is not in this file.
- Neither the 2016 PDB nor a private server's `DataSheets.bexcel` on client
  1784 has this table, and the client 1784 PAZ has no
  `jewelspecialslotsgroupstaticstatus.bss`. The field names come from the
  Lua (`ToClient_IsJewelInSpecialGroup`, `__eJewelSpecialSlot*`).
