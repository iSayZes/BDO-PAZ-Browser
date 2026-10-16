# `alchemystonechange.dbss` Format

## Purpose

The Growth recipes for items that grow into a higher tier: alchemy stones,
Vell's and Khan's Hearts and Behelit's Hearts with Brimming Essence of Aether
at Alchemy Apprentice 1, and Totems of the Sea with a Black Stone at a
Fishing level. A row is the item, its Growth material and count, the life
skill condition as an inline script, and the item it grows into.

```text
45228 Splendid Alchemy Stone of Destruction   821322 Brimming Essence of Aether x30  getLifeLevel(4)>10;  45232 Shining Alchemy Stone of Destruction
54287 Refined Totem of the Sea [Amberjack]    16001 Black Stone x1                   getLifeLevel(1)>50;  0
```

## Companion Files

None. The handler reads the rows in file order and does not need
`alchemystonechangeoffset.dbss` (see below). Item names come from LOC type 0
and icons from the `ITEM_ICON` lookup index.

All multi-byte values are little-endian.

## File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type  | Field     | Notes                     |
| ------- | ----- | --------- | ------------------------- |
| `+0x00` | u32   | row_count | `133` on client 3464      |
| `+0x04` | row[] | rows      | `row_count` rows, see Row |

### Row

A fixed head, an inline UTF-16LE condition script and a 12-byte tail. Every
condition on client 3464 is 19 characters long, so every row is 94 bytes
there; a reader takes the length from `condition_len`.

| Offset        | Type      | Field            | Notes                                                    |
| ------------- | --------- | ---------------- | -------------------------------------------------------- |
| `+0x00`       | u32       | key              | Row key; equals `item_id` on every row                   |
| `+0x04`       | u32       | item_id          | The item that grows; unique per row                      |
| `+0x08`       | u32       | unknown_08       | `0` on every row (client 3464)                           |
| `+0x0C`       | u32       | material_item_id | Growth material                                          |
| `+0x10`       | u32       | material_count   | Material units one Growth attempt takes                  |
| `+0x14`       | u8[16]    | unknown_14       | All zero on every row (client 3464)                      |
| `+0x24`       | u64       | condition_len    | UTF-16 code units in `condition`                         |
| `+0x2C`       | utf16le[] | condition        | Client condition script, see Conditions                  |
| after string  | u32       | result_item_id   | The item a successful Growth gives; `0` on Totem rows    |
| `+0x04` after | u32       | unknown_tail_04  | Falls with the stone tier; see Open Questions            |
| `+0x08` after | u32       | unknown_tail_08  | `0` on every row (client 3464)                           |

On client 3464 the rows fall into two families:

| Rows | Items                                                                 | Material                          | material_count   | condition              |
| ---- | --------------------------------------------------------------------- | --------------------------------- | ---------------- | ---------------------- |
| 53   | Alchemy stones (45201 Imperfect to 45292 Splendid), Blessed and Exalted alchemy stones (768181 to 768512), Vell's, Khan's and Behelit's Hearts (761839 to 761876) | 821322 Brimming Essence of Aether | `2` to `30`      | `getLifeLevel(4)>10;`  |
| 80   | Totems of the Sea (54201 to 54292)                                    | 16001 Black Stone                 | `1`              | `getLifeLevel(1)>30;`, `>40;` or `>50;` |

`material_count` and `unknown_tail_04` follow the tier the stone grows into
(client 3464):

| Growth                | material_count | unknown_tail_04 |
| --------------------- | -------------- | --------------- |
| Imperfect to Sturdy   | `2`            | `455000`        |
| Sturdy to Sharp       | `3`            | `176000`        |
| Sharp to Resplendent  | `10`           | `31400`         |
| Resplendent to Splendid | `20`         | `12000`         |
| Splendid to Shining   | `30`           | `3870`          |

The Blessed, Exalted and Heart chains use the same pairs for the same tier
step. Imperfect stones grow straight to Sturdy (45201 to 45216, 45233 to
45248, 45265 to 45280); no row starts at a Rough stone.

## Conditions

The condition is a client condition script, as in the quest tables
(`getLifeLevel(6)>80;` in `newquest.bss`). `getLifeLevel(n)` reads a life
skill level, and the item tooltips name the skill and the rank each
condition stands for:

| condition             | Tooltip text                                                      |
| --------------------- | ----------------------------------------------------------------- |
| `getLifeLevel(4)>10;` | Alchemy stones: "Growth Attempt: At least Alchemy Apprentice 1"   |
| `getLifeLevel(1)>30;` | 54201 Old Totem of the Sea: "Growth available for Fishing Professional 1 and higher." |
| `getLifeLevel(1)>40;` | 54280 Plain Totem of the Sea [Amberjack]: "Fishing Artisan 1"     |
| `getLifeLevel(1)>50;` | 54287 Refined Totem of the Sea [Amberjack]: "Fishing Master 1"    |

So life skill `4` is Alchemy, `1` is Fishing, and level `10` is Beginner 10
(the condition asks for level 11, Apprentice 1).

## `alchemystonechangeoffset.dbss`

A u32 row count (equal to the main file's), then 12-byte rows:

| Offset  | Type | Field   | Notes                                                    |
| ------- | ---- | ------- | -------------------------------------------------------- |
| `+0x00` | u32  | item_id | Row key, the main row's `key`                            |
| `+0x04` | u32  | offset  | Start of the row in `alchemystonechange.dbss` plus 4, at its `item_id` |
| `+0x08` | u32  | size    | Row length minus the 4-byte `key`; `90` on every row (client 3464) |

Every index row points at the main row with the same key. The index rows are
not in the main file's order (the first three keys are 768512, 54205,
768189 where the main file has 768512, 768189, 768188).

## Notes

- The Growth window reads its material from the stone's item key
  (`ToClient_GetAlchemyEvolveNeedItemKey`, `ToClient_GetAlchemyEvolveNeedItemCount`)
  and its result from `getAlchemyEvolveItemStaticStatusWrapper(itemKey, 0)`
  (`panel_window_alchemystoneevolve_all`). The rows agree: 821322 Brimming
  Essence of Aether lists "Usage #1: Alchemy Stone Growth", and every
  `result_item_id` is the next tier of `item_id` (45228 Splendid to 45232
  Shining Alchemy Stone of Destruction).
- The Totem tooltips read "Depending on the amount of EXP, it can be grown
  with Black Stone", which matches the 16001 Black Stone x1 rows.
- The Growth tab lists up to three results per stone
  (`getAlchemyEvolveItemSize`, slots `0` to `2` in `panel_window_alchemystone_all`);
  this file holds one `result_item_id` per row.
- The window shows the Growth chance from `ToClient_requestAlchemyEvolveRate`
  as `rate * 1e-4` with a `%` (`LUA_ALCHEMY_ENCHANT_RATE`), the
  1,000,000 = 100% scale of the Polishing EXP in `alchemyupgrade.dbss`. The
  Lua asks for the rate per stone slot, so it is not read from this file
  directly.

## Open Questions

### Totem Results

The 80 Totem rows hold `result_item_id` `0`, yet each Totem tooltip says it
can be grown. The tier the Totem grows into is not in this file; the
item IDs run in tier blocks per fish (54273 Old, 54280 Plain, 54287 Refined,
54292 Resplendent Totem of the Sea [Amberjack]), but that order is not a
link the client data states.

### unknown_08, unknown_14 and unknown_tail_08

All zero on client 3464. The 16 bytes of `unknown_14` fit two more
(item, count) pairs after `material_item_id` and `material_count`, but no
row fills them.

## In-Game Checks

### unknown_tail_04 as the Growth Chance

Needs item (all):

- [Splendid Alchemy Stone of Destruction](https://bdocodex.com/us/item/45228/)
- [Brimming Essence of Aether](https://bdocodex.com/us/item/821322/)

`unknown_tail_04` falls with the tier, from `455000` (Imperfect to Sturdy)
to `3870` (Splendid to Shining), and reads as a chance on the 1,000,000 =
100% scale the Growth window uses. Polish the stone to 100% and open Growth.
A chance of 0.387% means `unknown_tail_04` is the Growth chance at 100%
Polishing. Read it again at 80% and 150%: a chance that scales from 0.387%
with Polishing confirms it as the base the client scales.
