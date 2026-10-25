# `panel_window_inventory_all_4.luac`

## Purpose

Part of the PC inventory window: slot clicks and the right-click use of an
item. Its `source` is `window\inventory\panel_window_inventory_all_4.lua`.
The bytes follow [`luascript_luac.md`](luascript_luac.md); on client 3482
the script is 82,107 bytes.

## Calls Into Client Data

| Call                                  | What the script does with it                                                                 | Format doc field                                                               | Client |
| ------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------ |
| `itemEnchantWrapper:getConnectUi()`   | In `PaGlobalFunc_Inventory_All_SlotRClickXXX`: when the value is not `eConnectUi_Undefined`, a right click calls `ConnectLetterUI(itemKey)` for `eConnectUi_Letter` and `ConnectUI(value, itemKey)` for the others, which opens that window | [`itemenchantbackend.dbss`](../dbss/itemenchantbackend_dbss.md) `connect_ui` | 3482   |
| `itemStatic._itemMaterial`            | Sound of the item, passed to `audioPostEvent_SystemItem` on the same right click             | [`itemenchant.dbss`](../dbss/itemenchant_dbss.md) `item_material`            | 3482   |

## Enums Used

`eConnectUiType` is a global table of `connectui.luac`
(`window\item\connectui.lua`), which also holds `ConnectUI`: `-1`
`eConnectUi_Undefined`, `0` `eConnectUi_BlackStone` (the Black Spirit's
enhancement window), `1` `eConnectUi_Socket` (the crystal preset window),
`3` `eConnectUi_Improve`, `4` `eConnectUi_DyePalette`, `27`
`eConnectUi_Letter`, `28` `eConnectUi_Caphras`, `29` `eConnectUi_LightStone`,
`38` `eConnectUi_ItemSkillOption` and 34 more up to `eConnectUi_Count`
(`43`).

## Versions

Checked on client 3482 only.
