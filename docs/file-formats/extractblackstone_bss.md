# `extractblackstone.bss` Format

## Purpose

What Black Stone extraction gives back for enhanced gear: per enhancement
difficulty (Easy, Normal, Hard), one entry per enhancement level for weapons
and one for armor, each with the item handed out and two counts. The
extraction window (`panel_window_extraction_blackstone_all_*.luac`) reads
it through `ToClient_GetExtractBlackStoneResultItemKey(isWeapon,
enchantDifficulty, enchantLevel)` and `ToClient_GetExtractBlackStoneResultCount`
with the same arguments.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes | Records            | Row bytes |
| ------ | -------------- | ------- | ----------------------- | ----- | ------------------ | --------- |
| 1      | 3251 and later | 3474    | `extractblackstone.bss` | 2,308 | 108 Entry, 3 Group | 21        |

| Layout | File                    | Known         | Unknown         |
| ------ | ----------------------- | ------------- | --------------- |
| 1      | `extractblackstone.bss` | 580 B (25.1%) | 1,728 B (74.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | No file  |
| 2519   | No file  |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler names the result items through LOC type 0 and the item
icon index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type         | Field  | Notes                                |
| ------- | ------------ | ------ | ------------------------------------ |
| `+0x00` | u32          | count  | Number of groups, one per difficulty |
| `+0x04` | Group[count] | groups | See Group                            |

The groups are not sorted: client 3474 stores difficulties 1, 2, 3 and
client 3251 3, 2, 1, with the same groups. On client 3474 the file is 4 +
3 x (12 + 36 x 21) = 2,308 bytes.

### Group (variable: 12 bytes + entries)

| Offset                | Type                 | Field          | Notes                                                        |
| --------------------- | -------------------- | -------------- | ------------------------------------------------------------ |
| `+0x00`               | u32                  | difficulty     | Enhancement difficulty, see Difficulties; unique             |
| `+0x04`               | u32                  | weapon_count   | Number of `weapon_entries`; `18` in every group of client 3474 |
| `+0x08`               | u32                  | armor_count    | Number of `armor_entries`; `18` in every group of client 3474 |
| `+0x0C`               | Entry[weapon_count]  | weapon_entries | What weapons give, see Entry                                 |
| `weapon_entries+0x00` | Entry[armor_count]   | armor_entries  | What armor gives, see Entry                                  |

### Entry (21 bytes)

| Offset  | Type | Field           | Notes                                                                       |
| ------- | ---- | --------------- | --------------------------------------------------------------------------- |
| `+0x00` | u8   | enchant_level   | Enhancement level of the extracted gear; `1` to `18` in file order on client 3474 |
| `+0x01` | u32  | result_item_key | Item handed out, an item enchant key (`enchant_level << 24 \| item_id`), level `0` on every entry |
| `+0x05` | u64  | unknown_05      | A count; at least `unknown_0d` on every entry                               |
| `+0x0D` | u64  | unknown_0d      | A count                                                                     |

On client 3474 `result_item_key` is `16001` Black Stone for levels 1 to 15
and `16004` Concentrated Magical Black Stone for 16 to 18 (PRI to TRI).

## Difficulties

The developer comment on the `Difficulty` column of the `ExtractBlackStone`
sheet (a private server's `datasheet_contentsoptions.xlsm`, client 1784)
names `1` Easy, `2` Normal and `3` Hard. The item tooltip Lua
(`panel_tooltip_item.luac`) knows `__eEnchantDifficulty_None`, `_Easy`,
`_Normal`, `_Hard` and `_NotExtractHard`, and the extraction window turns
away gear of difficulty None or NotExtractHard, so those two have no group.

Entries of client 3474 for levels 8 and up:

| Level | Easy weapon | Easy armor | Normal weapon | Normal armor | Hard weapon | Hard armor |
| ----- | ----------- | ---------- | ------------- | ------------ | ----------- | ---------- |
| +8    | 8, 8        | 8, 8       | 9, 8          | 10, 8        | 9, 8        | 10, 8      |
| +9    | 9, 9        | 9, 9       | 10, 9         | 11, 9        | 11, 9       | 13, 10     |
| +10   | 10, 10      | 10, 10     | 12, 10        | 13, 10       | 12, 10      | 16, 13     |
| +11   | 11, 11      | 11, 11     | 14, 11        | 16, 12       | 16, 14      | 20, 15     |
| +12   | 12, 12      | 12, 12     | 16, 12        | 18, 14       | 20, 16      | 23, 18     |
| +13   | 13, 13      | 13, 13     | 17, 16        | 28, 21       | 22, 21      | 35, 27     |
| +14   | 14, 14      | 14, 14     | 28, 21        | 31, 25       | 35, 27      | 39, 32     |
| +15   | 15, 15      | 15, 15     | 34, 28        | 36, 31       | 43, 36      | 46, 39     |
| PRI   | 1, 1        | 1, 1       | 3, 2          | 3, 2         | 4, 2        | 4, 2       |
| DUO   | 2, 2        | 2, 2       | 5, 4          | 5, 4         | 6, 4        | 6, 4       |
| TRI   | 3, 3        | 3, 3       | 8, 7          | 8, 7         | 9, 7        | 9, 7       |

Each cell is `unknown_05, unknown_0d`. Below +8 both counts equal the level
in every group.

## Field Names

`difficulty` and the weapon and armor split follow the getters' arguments
(`isWeapon`, `enchantDifficulty`, `enchantLevel`), `result_item_key` the
getter `ToClient_GetExtractBlackStoneResultItemKey`. Neither the 2016 PDB nor
the client 1784 PAZ has the file (clients 3251 and 3474 have it).

The `ExtractBlackStone` sheet of a private server's `DataSheets.bexcel` on
client 1784 is the server-side table of the older extraction: per difficulty
several rows with a `Rate` weight and one count per column (`Weapon8` to
`Weapon15`, `Armor6` to `Armor15`, all `%` server-only). Read with the first
entry list as weapons, `unknown_0d` equals the smallest count of that
column on 52 of the 54 entries for levels the sheet has (34 of 36 outside
Easy, where every row holds the level), and `unknown_05` is at most its
largest count on all 54. Read with the lists swapped, 30 of 54 match. The
first list is the weapon list.

## Notes

- `weapon_count` and `armor_count` both sit before the two lists; the
  armor list starts right after the last weapon entry.
- The extraction window shows `?` when `ToClient_GetExtractBlackStoneResultCount`
  returns `0`, and needs gear whose `ToClient_GetExtractBlackStoneResultItemKey`
  is not `__eItemKeyUndefined`.

## In-Game Checks

### Which Count the Extraction Window Shows

Needs item: any weapon at +15 whose tooltip reads Enhancement Difficulty:
Hard

Open the Black Spirit's Extraction window, pick Black Stone extraction and
place the weapon (do not confirm). The window shows the Black Stone count
it gives. `43` means it shows `unknown_05` (the larger count); `36` means
it shows `unknown_0d`; a number in between means neither is the shown
count and the two are the limits of a random range.
