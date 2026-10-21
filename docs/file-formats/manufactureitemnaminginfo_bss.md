# `manufactureitemnaminginfo.bss` Format

## Purpose

The items that get a player's name stamped on them through processing
(manufacture). On client 3474 the list holds four Kamasylvia spirit
essences: Ornette's Spirit Essence (`40747`), Ancient Ornette's Spirit
Essence (`40748`), Odore's Spirit Essence (`40750`) and Ancient Odore's
Spirit Essence (`40751`).

For items other than equipment above +15 and enhanced accessories (those
have their own branch), the item tooltip (`panel_tooltip_item`) shows the stamped name when
`itemSSW:isNamingAbleItem()` is true and the item is not a cash item. The
line depends on the item type:

| Item type | Tooltip string key               | English text (LOC type 37, client 3474)                                          |
| --------- | -------------------------------- | -------------------------------------------------------------------------------- |
| Equip     | `LUA_TOOLTIP_ITEM_MAXENCHANTER`  | Equipment created by a great adventurer. Creator: `{name}`                       |
| Skill     | `LUA_TOOLTIP_RESTOREITEM_NAMING` | "A relic of the Kamasylve restored by a Great Adventurer." Restored by: `{name}` |
| Mapae     | `LUA_TOOLTIP_VEHICLE_NAMING`     | Built by: `{name}`                                                               |

The spirit essences are reusable items ("This item will not disappear after
being used"), which matches the Skill line.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ----- | -------------- | --------- |
| 1      | 1784 and later | 3474    | `manufactureitemnaminginfo.bss` | 36    | 1 String Table | 4         |

| Layout | File                            | Known         | Unknown    |
| ------ | ------------------------------- | ------------- | ---------- |
| 1      | `manufactureitemnaminginfo.bss` | 36 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler names the items from LOC type 0.

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of u32 rows with an empty string table, read by
`u32_rows()` in `_common/pabr_strings.py`.

| Offset              | Type         | Field        | Notes                              |
| ------------------- | ------------ | ------------ | ---------------------------------- |
| `+0x00`             | char[4]      | magic        | `PABR`                             |
| `+0x04`             | u32          | count        | Number of items; `4` on client 3474 |
| `+0x08`             | u32[count]   | item_ids     | `count` item IDs (LOC type 0)      |
| `item_ids+0x00`     | String Table | string_table | Empty string table                 |
| `string_table+0x00` | u32          | table_start  | End of the rows (`8 + 4 * count`)  |
| `string_table+0x04` | u32          | zero         | `0`                                |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Field Names

`item_ids` is the `ItemKey` column of the `ManufactureNaming_Table` sheet
of a private server's `DataSheets.bexcel` on client 1784: 4 of 4 keys match
client 3474, in the same order. The same sheet in the 1784
`datasheet_alchemydatatable.xlsm` has no developer comment beyond the
column name. The 1784 server binary loads the sheet in
`loadManufactureNamingInformation` into `ManufactureItemNamingStaticStatus`,
and keeps the stamped names per item in its database
(`uspRegistItemNaming`, `uspListItemNaming`).

## Notes

- All four items are materials of the Simple Alchemy recipes in
  [`manufacture.bss`](manufacture_bss.md) that combine one essence with a
  Fire Horn into the Central Market version. The other two essences those
  recipes take, Ornette's (`40712`) and Odore's (`40713`) Spirit Essence
  from the Dawnwish and Duskwish Petal quests, are not on the list.
- `panel_window_deletemaxenchantername` removes a stamped name through
  `ToClient_DeleteNamingItem`.

## Open Questions

### Which Recipe Stamps the Name

The list names the item, not the recipe. Recipes `19701` to `19704` of
`manufacture.bss` (Heating or Simple Alchemy of `40712` or `40713` with a
Dawnwish or Duskwish Petal) look like the ones that make the listed
essences, but their result groups are not in the client's
`itemmaingroup.bss`, and the 1784 sheets list no items for subgroups
`11311` to `11314`. Whether the name is stamped when a listed item is made,
or when it goes into the Fire Horn recipe, is open.

### Whether `isNamingAbleItem` Reads This List

The tooltip calls `itemSSW:isNamingAbleItem()` on the item's static status.
No client Lua reads this table directly, so the client may take the flag
from the item table instead.

## In-Game Checks

### Maker's Name on a Spirit Essence

Checks whether a listed item carries the name of the player who made it, and
at which step it is stamped. This answers both Open Questions.

Needs item (one of):

- [Ornette's Spirit Essence](https://bdocodex.com/us/item/40747/)
- [Odore's Spirit Essence](https://bdocodex.com/us/item/40750/)

1. Make one of the essences through processing.
2. Hover over it in the inventory and read the tooltip.
3. Expected: a line "A relic of the Kamasylve restored by a Great Adventurer.
   Restored by: {your family or character name}".
4. If the line is missing, use the essence in its Fire Horn Simple Alchemy
   recipe and read the tooltip of the result instead.
