# `panel_tooltip_item.luac`

## Purpose

The item tooltip: name, grade, bind and use limits, durability, the
enhancement and extraction lines. Its `source` is
`widget\tooltip\panel_tooltip_item.lua`. The bytes follow
[`luascript_luac.md`](luascript_luac.md); on client 3482 the script is
245,350 bytes.

## Calls Into Client Data

| Call                                        | What the script does with it                                                                  | Format doc field                                                                        | Client |
| ------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------ |
| `itemSSW:get():getEnchantDifficulty()`      | In `Panel_Tooltip_Item_ShowInfo`: shows the difficulty line when the value is above `__eEnchantDifficulty_None`, with the text `LUA_TOOLTIP_ENCHANTDIFFICULTY_EASY`, `_NORMAL` or `_HARD` (`_HARD` for both `__eEnchantDifficulty_Hard` and `__eEnchantDifficulty_NotExtractHard`); hidden on console | [`itemenchantbackend.dbss`](../dbss/itemenchantbackend_dbss.md) `enchant_difficulty` | 3482   |
| `itemSSW:get()._maxLevel`                   | The highest character level of the use limit line                                             | [`itemenchant.dbss`](../dbss/itemenchant_dbss.md) `max_level`                         | 3482   |

## Enums Used

`__eEnchantDifficulty_None`, `_Easy`, `_Normal`, `_Hard` and
`_NotExtractHard` are client constants the Lua compares against but does
not define.

## Versions

Checked on client 3482 only.

## Open Questions

### The Numbers of the Difficulty Constants

The script never gives the values of the five `__eEnchantDifficulty_*`
constants, so which stored value (`1` to `4`) reads as Easy, Normal or Hard
is open.
