# `cronenchant.bss` Format

## Purpose

The Caphras enhancement table: for each gear category and each of TRI, TET
and PEN, the 20 Caphras levels with the total Caphras Stones needed to reach
the level and the stat bonus the item has at that level.

The file name is the system's old name. The KR patch that added Caphras
Stones replaced the "Cron Energy" system with Caphras enhancement
([Inven Global](https://www.invenglobal.com/blackdesertonline/articles/4822/100-pen-is-not-going-to-be-that-easy-the-caphras-stone-and-caphras-enhancement-added-in-kr)),
and the client still calls it cron enchant: `panel_tooltip_item.luac` reads
the item's level with `ToClient_GetCronEnchantWrapper` and labels it with
`LUA_TOOLTIP_CRONENCHANTGRADE_CAPHRAS`.

Cron Stones are a separate item that is still in the game: they protect an
item from downgrading when an enhancement attempt fails. This file does not
hold their counts; the client reads those through
`ToClient_GetCronStoneStaticStatus`, from a table I have not found yet (see
[enchantstaticstatus.dbss](enchantstaticstatus_dbss.md), Notes).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes  | Records                                     | Row bytes |
| ------ | -------------- | ------- | ----------------- | ------ | ------------------------------------------- | --------- |
| 1      | 1784 and later | 3473    | `cronenchant.bss` | 23,580 | 600 Step, 30 Grade Block, 10 Category Block | 39        |

| Layout | File              | Known             | Unknown    |
| ------ | ----------------- | ----------------- | ---------- |
| 1      | `cronenchant.bss` | 23,580 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None. All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                            | Field              | Notes                                                    |
| ------------------- | ------------------------------- | ------------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]                         | magic              | `PABR` (ASCII)                                           |
| `+0x04`             | u32                             | category_count     | `10` on client 3464                                      |
| `+0x08`             | Category Block[category_count]  | categories         | See Category Block                                       |
| `categories+0x00`   | String Table                    | string_table       | The PABR string table, present but empty                 |
| `string_table+0x00` | u32                             | string_table_start | Absolute offset of `string_count`, where the categories end |
| `string_table+0x04` | u32                             | zero               | Always `0`                                               |

On client 3464 the file is `8 + 10 × (4 + 3 × (4 + 20 × 39)) + 12 = 23,580`
bytes. The parser rejects a file whose categories do not end exactly at
`string_table_start`.

### Category Block (variable: 4 bytes + grade blocks)

| Offset  | Type                     | Field       | Notes                                     |
| ------- | ------------------------ | ----------- | ----------------------------------------- |
| `+0x00` | u32                      | grade_count | `3` in every category (TRI, TET and PEN)  |
| `+0x04` | Grade Block[grade_count] | grades      | See Grade Block                           |

### Grade Block (variable: 4 bytes + steps)

| Offset  | Type             | Field      | Notes                                    |
| ------- | ---------------- | ---------- | ---------------------------------------- |
| `+0x00` | u32              | step_count | `20` in every grade, one per Caphras level |
| `+0x04` | Step[step_count] | steps      | See Step; byte-packed                    |

### Step (39 bytes)

| Offset  | Type | Field                   | Notes |
| ------- | ---- | ----------------------- | ----- |
| `+0x00` | u16  | category                | The category key, `1` to `10`; the same on every step of a category block |
| `+0x02` | u8   | enchant_level           | Item enhancement level the step applies to: `18` TRI, `19` TET, `20` PEN |
| `+0x03` | u32  | total_stones            | Caphras Stones from level 0 to this level; rises on every step |
| `+0x07` | f32  | ap                      | AP bonus at this level |
| `+0x0B` | f32  | accuracy                | |
| `+0x0F` | f32  | evasion                 | |
| `+0x13` | f32  | hidden_evasion          | |
| `+0x17` | f32  | damage_reduction        | |
| `+0x1B` | f32  | hidden_damage_reduction | |
| `+0x1F` | f32  | hp                      | Max HP bonus |
| `+0x23` | u32  | mp                      | Max MP (and other resource) bonus; an integer, unlike the other stats |

The Caphras level is not stored: it is the step's position in its grade
block, 1 to 20. The stats are the totals at that level, not the gain from
the previous one (category 1 at TRI: AP 1, 2, 3, 4, 4, 4, 4, 5, ...). The
stones for one level are `total_stones` minus the previous step's.

The eight stats follow the order of the tooltip keys in
`panel_tooltip_item.luac`: `LUA_TOOLTIP_CRONENCHANT_ATTACK`, `_HIT`,
`_DODGE`, `_DODGEB`, `_REDUCE`, `_REDUCEB`, `_HP`, `_MP`. Every f32 holds a
whole number on client 3464, and `mp` is `0` to `30` in steps of 5.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Categories

The file has no names for the categories, and I have not found the field
that gives an item its category, see Open Questions. The names come from the
Caphras sheets on [grumpygreen.cricket](https://grumpygreen.cricket/caphras-sheet/)
(PEN totals and stats) and its
[TRI page](https://grumpygreen.cricket/caphras-sheet-tri/) (per-level costs,
2021-06-01), and from bdocodex item pages at TRI with Caphras 20/20
(2026-10-11) where the sheet is out of date.

TRI columns are the stones for one level, as the TRI sheet lists them; the
TET and PEN columns are totals to level 20. All from client 3464.

| Key | Gear                  | TRI level 1 | TRI level 20 | TET total | PEN total | Checked against |
| --: | --------------------- | ----------: | -----------: | --------: | --------: | ----- |
| 1   | Boss main weapon      | 20 | 105 | 15,378 | 29,403 | Sheet: boss main weapon: TRI 20 / 105, PEN total 29,403 |
| 2   | Boss awakening weapon | 20 | 105 | 15,378 | 29,403 | bdocodex: [Dandelion Lancia](https://bdocodex.com/us/item/14752/) TRI 20/20 is AP 8, accuracy 12, 1,590 stones in total (the sheet lists TRI 24 / 128) |
| 3   | Blue weapon           | 12 | 118 | 10,763 | 20,964 | Sheet: blue main and awakening weapon: TRI 16 / 118 |
| 4   | Green weapon          | 4  | 59  | 3,990  | 9,615  | bdocodex: [Yuria Longsword](https://bdocodex.com/us/item/10014/) TRI 20/20 is AP 8, accuracy 12, 494 stones in total; the sheet lists green awakening weapons as TRI 4 / 59 and green main weapons as TRI 4 / 39 |
| 5   | Boss sub-weapon       | 20 | 105 | 15,378 | 29,403 | Sheet: boss and Fiery sub-weapon: TRI 20 / 105, PEN total 29,403 |
| 6   | Green sub-weapon      | 4  | 59  | 3,990  | 9,615  | Sheet: green sub-weapon: TRI 4 / 59, PEN total 9,615 |
| 7   | Boss armor            | 19 | 103 | 9,729  | 21,744 | Sheet: boss armor: TRI 19 / 103, PEN total 21,744 |
| 8   | Dim Tree armor        | 19 | 103 | 9,729  | 21,744 | bdocodex: [Dim Tree Spirit's Armor](https://bdocodex.com/us/item/11017/) TRI 20/20 is evasion 3 (+8), damage reduction 1 (+3), HP 80, MP 30, 1,483 stones in total (the sheet lists TRI 22 / 116) |
| 9   | Blue armor            | 6  | 40  | 3,630  | 10,104 | Sheet: blue armor: TRI 6 / 40 |
| 10  | Green armor           | 3  | 30  | 1,950  | 6,612  | Sheet: green armor: TRI 3 / 30, PEN total 6,612 |

The stats of every category match the sheet's gear of that kind. Categories
1, 5, 6, 7, 9 and 10 match the sheet's costs exactly. Category 4 holds both
green main and green awakening weapons: Yuria Longsword, a main weapon,
costs the sheet's green awakening values. Categories
1 and 2 are identical in every step, and so are 7 and 8: the boss awakening
weapon and Dim Tree armor now cost what the boss main weapon and boss armor
do, while the 2021 sheet still lists them higher.

Stats at Caphras level 20 per stat group (client 3464):

| Categories | Grade    | AP | Accuracy | Evasion | Hidden evasion | DR | Hidden DR | HP  | MP |
| ---------- | -------- | -: | -------: | ------: | -------------: | -: | --------: | --: | -: |
| 1 to 4     | TRI, TET | 8  | 12       | 0       | 0              | 0  | 0         | 0   | 0  |
| 1 to 4     | PEN      | 10 | 12       | 0       | 0              | 0  | 0         | 0   | 0  |
| 5, 6       | TRI, TET | 2  | 8        | 1       | 5              | 0  | 2         | 30  | 25 |
| 5, 6       | PEN      | 2  | 12       | 3       | 9              | 3  | 3         | 60  | 0  |
| 7 to 10    | TRI, TET | 0  | 0        | 3       | 8              | 1  | 3         | 80  | 30 |
| 7, 8       | PEN      | 0  | 0        | 8       | 8              | 8  | 8         | 160 | 0  |
| 9, 10      | PEN      | 0  | 0        | 5       | 5              | 5  | 5         | 100 | 0  |

## Notes

- How the client reads the file (`panel_tooltip_item.luac`, decompiled with
  unluac): `ToClient_GetCronEnchnatInfoCount(cronKey, enchantLevel)` is the
  step count of one grade block, and
  `ToClient_GetCronEnchantWrapper(cronKey, enchantLevel, index):getCount()`
  is that step's `total_stones`. The item itself stores only the stones put
  into it (`getCronEnchantFailCount()`); its Caphras level is the number of
  steps whose `total_stones` is at most that count. The stat bonus in the
  tooltip comes from the item (`getAddedDD()`, `getCronHDV()`,
  `getCronHPV()`, ...), not from this file directly.
- The enhancement window asks for the next and current step with
  `ToClient_GetNextLevelCronEnchantForLua` and
  `ToClient_GetCurrentLevelCronEnchantForLua`
  (`panel_widget_enchant_main_all_1.luac`).
- Caphras costs change with patches: the 2019-03-20 KR patch cut the stones
  for PEN gear by 25%
  ([Inven Global](https://www.invenglobal.com/articles/7846/bdo-kr-patch-notes-march-20th-new-areaitems-added-devour-and-caphras-enhancement-improved)),
  so the totals above are a snapshot of client 3464.
- bdocodex writes a hidden stat in brackets after the visible one:
  "Evasion: 3 (+8)" is `evasion` 3 and `hidden_evasion` 8.
- No category has blue sub-weapon costs or stats of its own; they share a
  category with other gear, but which one is not in this file.

## Open Questions

### Item to Category Link

The tooltip reads the category with `itemSSW:getCronKey()`, on the static
status of the item at its enhancement level (`panel_tooltip_item.luac`),
and passes it straight to `ToClient_GetCronEnchantWrapper` with that
level. The static status is what `itemenchant.dbss` holds, but the key is
not stored there as a plain byte: a byte-level diff of Liverto Longsword (3)
against Yuria Longsword (4) and of Lemoria Helmet (9) against Grunil Helmet
(10) at TRI finds no byte that holds the two categories at matching
positions. A byte scan found no field that holds the
expected key for Kzarka Longsword (1), Liverto Longsword (3), Yuria Longsword
(4), Kutum Shield (5), Griffon's Helmet (7), Dim Tree Spirit's Armor (8) and
Grunil Helmet (10): not at any offset from the block start, the block end or
the icon string end of their `itemenchant.dbss` blocks (levels 0 and 18), nor
from the start or end of their `enchantstaticstatus.dbss` blocks (levels 0
and 17 to 20), nor at a fixed offset in their `itemenchantbackend.dbss`
blocks. A second scan over all 772 tables in `gamecommondata/binary`
(client 3464) looked within 512 bytes of each sample's item ID, TRI item key
and enchant key, as u16 and u32, for a byte that holds the category for
every sample; none does. The scans also catch the low byte of a u16 or u32,
so the item side either stores other values that the client maps to these
keys, or the client works the category out from other item fields. Grade
plus gear type (main, awakening, sub-weapon, armor) would explain every
sample except Dim Tree armor, which has a key of its own. Until the link is found, the table cannot list the items
per category.
