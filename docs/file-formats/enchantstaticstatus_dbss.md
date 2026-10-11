# `enchantstaticstatus.dbss` Format

## Purpose

The enhancement table: one variable-length block per (enchant key, level),
keyed through a required offset companion. Block `level` holds the stats of an
item at that level (AP, accuracy, evasion, durability, the effect script) and
what the attempt to reach that level costs (material and count, success
chance, durability lost on failure, perfect enhancement).

The enchant key is not an item ID. It is the u32 that
[itemenchant.dbss](itemenchant_dbss.md) stores just before an item's Korean
name, and many items share one key (Pearl Shop outfits put up to 3,498 items
on one).

Example, Kzarka Gauntlet (item `11210`, enchant key `662`):

```text
level 8   Black Stone x1                     90%       fail -5 durability   perfect: 2 stones, -10 durability   AP 43 ~ 47, accuracy 90
level 16  Concentrated Magical Black Stone x1  11.7647%  fail -10 durability  AP 86 ~ 90, accuracy 168
```

## Companion Files

| File                              | Required | Role                                                  |
| --------------------------------- | -------- | ----------------------------------------------------- |
| `enchantstaticstatusoffset.dbss`  | Required | Maps the packed key to a block offset and size        |
| `languagedata_en.loc`             | Optional | Names of the material and aid items (`str_type=0`)    |

All multi-byte values are little-endian.

## File Layout

| Offset  | Type | Field  | Notes                                                    |
| ------- | ---- | ------ | -------------------------------------------------------- |
| `+0x00` | u32  | count  | Block count, matching the companion; 33,503 on client 3458 |
| `+0x04` | ...  | blocks | Variable-length blocks, contiguous                       |

The first block starts at byte `4` and the last ends at end of file
(23,775,679 bytes on client 3458), with no gaps. Blocks are not in key order.

## `enchantstaticstatusoffset.dbss`

The shared PABR layout with u32 keys (`parse_pabr_u32_offset_rows`): `PABR`, a
u32 row count, `count` 12-byte rows, then the 12-byte trailer
`(0, 8 + count × 12, 0)`.

| Offset  | Type | Field       | Notes                                      |
| ------- | ---- | ----------- | ------------------------------------------ |
| `+0x00` | u32  | key         | `level << 24 \| enchant_key`               |
| `+0x04` | u32  | data_offset | Byte offset of the block                   |
| `+0x08` | u32  | data_size   | Block length in bytes                      |

Levels run 0 to 25 with no gaps per key. There are 4,811 enchant keys
(1 to 62,304) on client 3458.

### The link from items

`itemenchant.dbss` stores the enchant key in the u32 just before the u64
length of the Korean name. Combining an item block's level with that key
always finds a block here: all 130,297 item blocks with a non-zero key hit
one, none miss (client 3458). 3,729 of the 4,811 keys are used by an item;
40,025 base items store `0` and have no enhancement data.

| Item                     | Item ID | Enchant key |
| ------------------------ | ------: | ----------: |
| Kzarka Gauntlet          | 11210   | 662         |
| Sicil's Necklace         | 11625   | 8017        |
| Kharazad Necklace        | 11697   | 12336       |
| Tuvala Helmet            | 695105  | 6130        |

## Block Structure

A block is one sequential stream: fixed fields to `+0xFF`, two u64-prefixed
UTF-16LE strings, then a variable tail. All 33,503 blocks read to their exact
end with this layout.

### Fixed part

| Offset  | Type      | Field                   | Notes |
| ------- | --------- | ----------------------- | ----- |
| `+0x00` | u32       | enchant_key             | Repeats the key's low 24 bits, in every block |
| `+0x04` | u8        | level                   | Repeats the key's level, in every block |
| `+0x05` | u32       | material_item_id        | Item consumed by the attempt to reach this level; `0` on every level-0 block |
| `+0x09` | u64       | material_count          | How many |
| `+0x11` | u64       | perfect_count           | Materials a perfect enhancement (100% chance) takes; `0` when it is not offered |
| `+0x19` | u64       | unknown_19              | Not the Cron Stone count, see Open Questions |
| `+0x21` | u8[8]     | zero                    | `0` in every block |
| `+0x29` | u32       | success_rate            | Base chance of the attempt in millionths: 1,000,000 is 100% |
| `+0x2D` | u32       | unknown_2d              | A rate in millionths: `0` (28,677 blocks), 1,000,000 (4,782), 500,000 or 100,000 (22 each); see Open Questions |
| `+0x31` | u8[4]     | zero                    | `0` in every block |
| `+0x35` | u16       | max_durability          | Durability at this level |
| `+0x37` | u16       | fail_durability_loss    | Durability lost when the attempt fails |
| `+0x39` | u16       | unknown_39              | `10`, `0` or `1` |
| `+0x3B` | u8        | unknown_3b              | `0` in every block |
| `+0x3C` | u16       | perfect_durability_loss | Durability a perfect enhancement costs; only meaningful when `perfect_count` is set |
| `+0x3E` | f32       | unknown_3e              | bdo-data-extractor: max HP, see Open Questions |
| `+0x42` | f32[25]   | unknown_42              | bdo-data-extractor: AP per species slot |
| `+0xA6` | u8        | unknown_a6              | `0`, `1` or `2` |
| `+0xA7` | f32[7][3] | lane stats              | Seven stats, each for the melee, ranged and magic lanes, below |
| `+0xFB` | u32       | unknown_fb              |       |
| `+0xFF` | string    | description_kr          | Korean text with `<PAColor>` tags; empty in most blocks, set on ship equipment |
| varies  | string    | effects                 | The effect script, one `NAME(args);` per line: `ITEM_EFFECT();`, `PLAYER_DAM_ADD(10);`, `ALL_AP_INCRE();` |

Strings are a u64 UTF-16 code-unit count, then the text with no terminator.

The seven lane stats, in order:

| Index | Field         | Notes |
| ----: | ------------- | ----- |
| 0     | unknown       |       |
| 1     | unknown       |       |
| 2     | ap_min        | Lowest AP |
| 3     | ap_max        | Highest AP |
| 4     | ap_display    | `round((ap_min + ap_max) / 2)` in every lane of every block |
| 5     | unknown       | bdo-data-extractor: damage reduction; equals the tail's lane value 2 in every block |
| 6     | evasion       | Equals the tail's lane value 0 in every block |

A weapon fills the lanes it attacks with (Kzarka Gauntlet melee and magic, a
bow ranged); accessories fill all three alike. The browser shows the highest
lane.

### Tail

| Order | Type                     | Field       | Notes |
| ----: | ------------------------ | ----------- | ----- |
| 1     | u8[13]                   | unknown     | Mostly `00 0? 40 42 0F 00 60 AE 0A 00 ?? 00 00`: two u32 that are 1,000,000 and 700,000 in most blocks |
| 2     | 3 × (string, f32)        | dice, accuracy | Per lane: the AP roll as dice text (`1D5+85` is 86 to 90, `1D1-1` is none), then the accuracy |
| 3     | 3 × f32[4]               | defense     | Per lane: evasion, hidden evasion, then two values bdo-data-extractor calls damage reduction and hidden damage reduction |
| 4     | u8[12]                   | sentinels   | Three i32 `-1`, in every block |
| 5     | u8[65]                   | unknown     |       |
| 6     | u32 + u32 × count        | aid_item_ids | 0 to 3 item IDs: hammers and crystals, see Notes |
| 7     | u8[6]                    | unknown     | Zero in 31,777 blocks |

### Checked on bdocodex

bdocodex (2026-10-06, client 3458) embeds its per-level enhancement table in
the item page. Every field the browser shows matched on all 38 levels of
Kzarka Gauntlet (`662`, levels 0 to 20), Sicil's Necklace (`8017`, 0 to 5) and
Kharazad Necklace (`12336`, 0 to 10): AP min and max, accuracy, evasion,
hidden evasion, durability, and for the step to each level the material, its
count, the chance, the durability lost on failure, the perfect enhancement
count and its durability cost.

bdocodex lists the cost of level `n + 1` on row `n`; this file stores it in
block `n + 1`. So level 0 is the base item and pays nothing.

- Kzarka Gauntlet: +1 to +15 take a Black Stone (`16001`), PRI to PEN a
  Concentrated Magical Black Stone (`16004`). The chances read 100% for +1 to
  +7, then 90, 20.4081, 14.2857, 10, 6.6666, 4, 2.5 and 2% for +8 to +15, and
  11.7647, 7.6923, 6.25, 2 and 0.3% for PRI to PEN. Failure costs 5
  durability below PRI, 10 from PRI. Perfect enhancement exists for +8 to
  +15, taking 2, 3, 5, 7, 11, 17, 23 and 29 stones and 10 to 100 durability.
- Sicil's Necklace takes a copy of itself, loses 10 durability on failure,
  and its tail stores evasion 3 and hidden evasion 6 at level 0, as bdocodex
  shows.
- Kharazad Necklace has 200 durability, loses 20 on failure, and takes 1 to
  15 Essence of Dawn (`820979`) for I to IX and a Dawn Black Stone (`820984`)
  for X.

## Suggested UI Layout

| Column                  | Type | Notes |
| ----------------------- | ---- | ----- |
| Enchant Key             | num  | `enchant_key` |
| Level                   | num  | `level` |
| Material                | text | `material_item_id` with its icon and LOC type 0 name; dash on level 0 |
| Count                   | num  | `material_count` |
| Chance                  | num  | `success_rate / 10,000` as a percentage |
| Fail Durability Loss    | num  | `fail_durability_loss` |
| Perfect Count           | num  | `perfect_count`; dash when `0` |
| Perfect Durability Loss | num  | `perfect_durability_loss`; dash without a perfect enhancement |
| Durability              | num  | `max_durability` |
| AP                      | num  | `ap_min ~ ap_max`, highest lane; dash when both are 0; sorts by `ap_max` |
| Accuracy                | num  | Highest lane |
| Evasion                 | num  | Highest lane |
| Hidden Evasion          | num  | Highest lane |
| Aid Items               | text | `aid_item_ids` with icons and names |
| Effects                 | text | The effect script on one line, cut |
| Description             | text | `description_kr` in its game colours, on one line |

Rows are sorted by enchant key, then level. The offset table shows the key
split into Enchant Key and Level, then Data Offset and Data Size.

## Notes

- The aid items are the enhancement hammers and crystals: J's Hammer of
  Loyalty (`45077`, 384 blocks, e.g. Kzarka Gauntlet TRI and TET), J's Hammer
  of Precision (`45078`), [Event] Fiery Crystal of Fate (`767176`), Primordial
  Hammer (`767130`), Causality Hammer (`790876`), Obsidian Hammer (`767291`)
  and Distorted Crystal of Origin (`761802`). What exactly each does at that
  level is not stored here.
- Durability rises with the level on some lines: Obsidian Blackstar armor
  (enchant keys 6146 to 6149) stores 100 up to +15, then 120, 140, 160, 180
  and 200 for PRI to PEN. 145 keys change durability across levels; Kzarka
  Gauntlet stays at 100.
- Cron Stones are not in this file. bdocodex shows 34, 127 and 531 for
  Kzarka Gauntlet TRI, TET and PEN, and nothing here matches. The client
  reads them through `ToClient_GetCronStoneStaticStatus`, which suggests a
  table of its own. It is not `cronenchant.bss`: despite the name, that file
  is the Caphras enhancement table ([cronenchant](cronenchant_bss.md)).
- The client Lua (`window/enchant/panel_widget_enchant_main_all`) names the
  concepts this file feeds: `ToClient_GetNeedMaterialItemStaticStatus`,
  `ToClient_GetPerfectEnchantEndurancePenalty`,
  `ToClient_GetTargetReducedEnduranceWhenFail`,
  `ToClient_GetTargetEnchantDownRate` and the danger types `Safe`,
  `Gradedown`, `Broken` and `DownAndBroken`.
- The layout follows
  [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor/blob/HEAD/FORMATS.md)
  (section 5, and `internal/tables/enchant.go`), checked against these files.
  The stream itself, the success rate at `+0x29`, the lane stats, the two
  strings, the tail and the aid items hold. Some claims do not:
  - It reads `+0x04` to `+0x17` as five u32 values. They are the level (u8),
    the material (u32), the material count (u64), the perfect count (u64) and
    `unknown_19` (u64).
  - It says durability goes "base 100 → PRI 120 / DUO 140 / TRI 160 / TET 180
    / PEN 200". That holds only for some lines, see above.
  - It calls `+0x3E` max HP, "0 unless the DSL carries `HP_UP(n)`". 1,697
    blocks break that: 832 have `HP_UP` in the script and store `0`, 865
    store a value with no or a different `HP_UP`.
  - It calls the dice strings accuracy dice. The dice are the AP roll (Kzarka
    Gauntlet PRI `1D5+85`, AP 86 to 90); the f32 after each one is the
    accuracy.

## Open Questions

### What `unknown_19` holds

A u64 that grows with the level: Kzarka Gauntlet stores 1 for +1 to +7, then
4, 11, 20, 33, 55, 80, 120 and 170 for +8 to +15, and 11, 12, 35, 182 and
1,330 for PRI to PEN. Sicil's Necklace stores 2 to 120. It is not the Cron
Stone count bdocodex shows (34, 127 and 531 for Kzarka TRI to PEN).

### Whether `unknown_2d` is the downgrade chance

It is 1,000,000 on 4,782 blocks, 500,000 or 100,000 on 22 each (enchant key
28303 at levels 9 and 8) and `0` on the rest. Kzarka Gauntlet sets 1,000,000
for TRI, TET and PEN, Kharazad Necklace for X. That fits the chance to drop a
level on failure (`ToClient_GetTargetEnchantDownRate`), but no source shows
the downgrade per level.

### What `unknown_3e` holds

bdo-data-extractor calls it max HP. It matches the script's `HP_UP(n)` on
most blocks, but not on 1,697 (e.g. enchant key 3624 at level 20 stores 585
with `HP_UP(60)`).

### Damage reduction

Lane stat 5 and the tail's third defense value agree in every block, and
bdo-data-extractor calls them damage reduction (and the fourth hidden damage
reduction). The three items checked on bdocodex store `0` there, so the names
are unconfirmed and the browser does not show them.

### Remaining unknown fields

`unknown_39`, `unknown_3b`, the 25 floats at `+0x42`, `unknown_a6`, lane
stats 0 and 1, `unknown_fb`, the 13 bytes after the script, the 65-byte block
before the aid items and the last 6 bytes are not decoded.
