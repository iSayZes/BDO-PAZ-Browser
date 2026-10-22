# `limiteditemsubgroup.bss` Format

## Purpose

The purchase limits of shop items: one row per item subgroup, each a list
of the items in it that a character or family can buy only so many times
before a reset. Every `subgroup_key` is an
[`itemsubgroup.dbss`](itemsubgroup_dbss.md) key (53 of 53 on client 3482).
The NPC shop Lua (`panel_dialog_npcshop_all_1.luac`) shows a limited item
through the shop item wrapper's `isLimitedBuyableCount()`,
`getRemainingCount()`, `getBuyableMaxCount()`, `getResetType()` and
`isLimitedByUser()`, and picks the `LUA_LIMITEDITEMSHOP_FAMILY_*` or
`LUA_LIMITEDITEMSHOP_CHARACTER_*` text by the last one.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes  | Records           | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ------ | ----------------- | --------- |
| 2      | 1636 and later | 3482    | `limiteditemsubgroup.bss` | 11,512 | 705 Entry, 53 Row | 16        |
| 1      | 1348 to 1485   | 1485    | `limiteditemsubgroup.bss` | 3,020  | 245 Entry, 15 Row | 12        |

| Layout | File                      | Known            | Unknown         |
| ------ | ------------------------- | ---------------- | --------------- |
| 2      | `limiteditemsubgroup.bss` | 8,692 B (75.5%)  | 2,820 B (24.5%) |
| 1      | `limiteditemsubgroup.bss` | 3,020 B (100.0%) | 0 B (0.0%)      |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3251   | Layout 2 |
| 3002   | Layout 2 |
| 2765   | Layout 2 |
| 2637   | Layout 2 |
| 2519   | Layout 2 |
| 2313   | Layout 2 |
| 2107   | Layout 2 |
| 1937   | Layout 2 |
| 1784   | Layout 2 |
| 1636   | Layout 2 |
| 1485   | Layout 1 |
| 1348   | Layout 1 |
| 1230   | No file  |
| 1156   | No file  |
| 1058   | No file  |
| 911    | No file  |
| 794    | No file  |
| 606    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                 |
| --------------------- | -------- | -------------------- |
| `languagedata_en.loc` | Optional | Item names (type 0)  |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of subgroups                           |
| `+0x08`             | Row[row_count] | rows         | See Row; in no key order                      |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 4 bytes + entries)

| Offset  | Type               | Field       | Notes                                 |
| ------- | ------------------ | ----------- | ------------------------------------- |
| `+0x00` | u32                | entry_count | Number of `entries`; `1` to `44` on client 3482 |
| `+0x04` | Entry[entry_count] | entries     | See Entry; one per limited shop item  |

### Entry (16 bytes)

| Offset  | Type | Field                | Notes                                                                                     |
| ------- | ---- | -------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16  | subgroup_key         | The `itemsubgroup.dbss` key; the same on every entry of one row                          |
| `+0x02` | u32  | item_key             | The item, a packed item key as in `itemsubgroup.dbss` (LOC type 0 name); see Open Questions |
| `+0x06` | u8   | purchase_subject     | `2` on 704 of 705 entries, `1` on one (client 3482); see Open Questions                   |
| `+0x07` | u32  | purchase_count_limit | How many the character or family can buy before the reset                                |
| `+0x0B` | u8   | reset_type           | When the count resets; see Reset Types                                                    |
| `+0x0C` | u32  | unknown_0c           | `0` on every entry (clients 1784 and 3482); see Open Questions                            |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                         |
| ------- | ------------------ | ------------ | --------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on clients 1784 and 3482 |
| `+0x04` | pstr[string_count] | strings      | Empty                                         |

## Layout 1

No `unknown_0c`: an entry is 12 bytes. Only the Entry differs from
Layout 2.

### Entry (12 bytes)

| Offset  | Type | Field                | Notes |
| ------- | ---- | -------------------- | ----- |
| `+0x00` | u16  | subgroup_key         |       |
| `+0x02` | u32  | item_key             |       |
| `+0x06` | u8   | purchase_subject     |       |
| `+0x07` | u32  | purchase_count_limit |       |
| `+0x0B` | u8   | reset_type           |       |

## Reset Types

The NPC shop Lua appends `DAY`, `WEEK`, `MONTH` or `SIEGE` to the limit
text key for `getResetType()` `1` to `4`. Entry counts are from client
3482.

| Value | Lua text key suffix | Sheet `ResetType` | Entries |
| ----- | ------------------- | ----------------- | ------- |
| 1     | `DAY`               | `Day`             | 360     |
| 2     | `WEEK`              | `Week`            | 54      |
| 3     | `MONTH`             | `Month`           | 220     |
| 4     | `SIEGE`             | `Siege`           | 71      |

With `4` the shop also shows its guild limit time line
(`_txt_GuildLimitTime`).

## Field Names

The `LimitedItemSubGroup_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `ItemSubGroupKey`,
`ItemKey`, `EnchantLevel`, `PurchaseSubject`, `PurchaseCountLimit`,
`ResetType` and `ADSummary`, 322 rows. 313 of the 324 entries of the
client 1784 file have a row with the same subgroup and item.

| Field                | Column               | Same value (client 1784 file) |
| -------------------- | -------------------- | ----------------------------- |
| subgroup_key         | `ItemSubGroupKey`    | 313 of 313                    |
| item_key             | `ItemKey`            | 313 of 313                    |
| purchase_subject     | `PurchaseSubject`    | 313 of 313                    |
| purchase_count_limit | `PurchaseCountLimit` | 312 of 313                    |
| reset_type           | `ResetType`          | 313 of 313 (`Day` 260 as `1`, `Siege` 49 as `4`, `Week` 3 as `2`, `Month` 1 as `3`) |

The client 1784 server dump names the sheet's checks
(`LimitedItemSubGroup_Table(ItemSubGroupKey : %#)`,
`(ItemKey : %#, EnchantLevel : %#)`, `ResetType(%#)`,
`PurchaseCountLimit(%#)`, `AdSummary`).

## Notes

- 696 of the 705 entries of client 3482 name an item that the subgroup's
  `itemsubgroup.dbss` record lists. The other nine are items `756300`
  (subgroup 51660), `756301` (51661), `3560` to `3564` (51891) and
  `757010` (51761 and 51762).
- The one entry with `purchase_subject` `1` on client 3482 is Weight Limit
  +400 LT (`450126`, subgroup 51884), 7 per month.
- Client 1784 has 26 rows and 324 entries, every `purchase_subject` `2`.

## Open Questions

### Purchase Subject Values

`purchase_subject` decides whether the limit counts per character or per
family (`isLimitedByUser()` picks the `FAMILY` or `CHARACTER` text), but
which of `1` and `2` is the family is not in the Lua. The single `1`
entry is Weight Limit +400 LT (`450126`).

### Enchant Level and the Last Field

The sheet has seven columns and the entry six fields. `item_key` equals
the packed item keys of `itemsubgroup.dbss`, which hold the enhancement
level in the top byte, but every `item_key` has a top byte of `0` and
every sheet `EnchantLevel` is `0`, so the data cannot tell whether the
level is in `item_key` or in `unknown_0c`. If the level is packed,
`unknown_0c` would be the `ADSummary` text, whose cells are all
`<null>`; the string table is empty on both clients. Clients 1348 and
1485 have no `unknown_0c` at all (Layout 1).
