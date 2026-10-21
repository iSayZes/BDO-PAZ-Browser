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

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes      | Records                         | Row bytes               |
| ------ | -------------- | ------- | -------------------------------- | ---------- | ------------------------------- | ----------------------- |
| 2      | 3473 and later | 3474    | `enchantstaticstatus.dbss`       | 23,776,392 | 100,512 Lane Dice, 33,504 Block | 18 to 28, 22 on average |
| 2      | 3473 and later | 3474    | `enchantstaticstatusoffset.dbss` | 402,068    | 33,504 Offset Row               | 12                      |
| 1      | 1784 to 2519   | 2519    | `enchantstaticstatus.dbss`       | 22,892,802 | 96,561 Lane Dice, 32,187 Block  | 18 to 28, 22 on average |
| 1      | 1784 to 2519   | 2519    | `enchantstaticstatusoffset.dbss` | 386,264    | 32,187 Offset Row               | 12                      |

| Layout | File                             | Known                | Unknown             |
| ------ | -------------------------------- | -------------------- | ------------------- |
| 2      | `enchantstaticstatus.dbss`       | 19,621,896 B (82.5%) | 4,154,496 B (17.5%) |
| 2      | `enchantstaticstatusoffset.dbss` | 402,068 B (100.0%)   | 0 B (0.0%)          |
| 1      | `enchantstaticstatus.dbss`       | 18,901,614 B (82.6%) | 3,991,188 B (17.4%) |
| 1      | `enchantstaticstatusoffset.dbss` | 386,264 B (100.0%)   | 0 B (0.0%)          |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3474   | Layout 2             |
| 3473   | Layout 2             |
| 3251   | No documented layout |
| 3002   | No documented layout |
| 2519   | Layout 1             |
| 2107   | Layout 1             |
| 1784   | Layout 1             |
| 1485   | No documented layout |
| 1230   | No documented layout |
| 794    | No file              |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                  |
| --------------------------------- | -------- | ----------------------------------------------------- |
| `enchantstaticstatusoffset.dbss`  | Required | Maps the packed key to a block offset and size        |
| `languagedata_en.loc`             | Optional | Names of the material and aid items (`str_type=0`)    |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type         | Field  | Notes                                                      |
| ------- | ------------ | ------ | ---------------------------------------------------------- |
| `+0x00` | u32          | count  | Block count, matching the companion; 33,503 on client 3458 |
| `+0x04` | Block[count] | blocks | Variable-length blocks, contiguous; see Block              |

The first block starts at byte `4` and the last ends at end of file
(23,775,679 bytes on client 3458), with no gaps. Blocks are not in key order.

### Block (variable: 419 bytes + strings and aid items)

A block is one sequential stream: fixed fields to `+0xFF`, two u64-prefixed
UTF-16LE strings, then a variable tail. All 33,503 blocks read to their exact
end with this layout.

| Offset                | Type                  | Field                   | Notes |
| --------------------- | --------------------- | ----------------------- | ----- |
| `+0x00`               | u32                   | enchant_key             | Repeats the key's low 24 bits, in every block |
| `+0x04`               | u8                    | level                   | Repeats the key's level, in every block |
| `+0x05`               | u32                   | material_item_id        | Item consumed by the attempt to reach this level; `0` on every level-0 block |
| `+0x09`               | u64                   | material_count          | How many |
| `+0x11`               | u64                   | perfect_count           | Materials a perfect enhancement (100% chance) takes; `0` when it is not offered |
| `+0x19`               | u64                   | black_count_for_item_market | Grows with the level, see Field Names |
| `+0x21`               | bytes[8]              | unknown_21              | Always `0` |
| `+0x29`               | u32                   | success_rate            | Base chance of the attempt in millionths: 1,000,000 is 100% |
| `+0x2D`               | u32                   | downgrade_rate          | Chance that a failed attempt drops a level, in millionths: 1,000,000 (4,782 blocks on client 3464), 500,000 or 100,000 (22 each), `0` on the rest. Goes with `fail_result` 3, see Failure results |
| `+0x31`               | bytes[4]              | unknown_31              | Always `0` |
| `+0x35`               | u16                   | max_durability          | Durability at this level |
| `+0x37`               | u16                   | fail_durability_loss    | Durability lost when the attempt fails |
| `+0x39`               | u16                   | recover_max_endurance   | `10` (28,823 blocks on client 3473), `0` (4,660) or `1` (21) |
| `+0x3B`               | u8                    | unknown_3b              | `0` in every block |
| `+0x3C`               | u16                   | perfect_durability_loss | Durability a perfect enhancement costs; only meaningful when `perfect_count` is set |
| `+0x3E`               | f32                   | max_hp                  | Max HP the item adds; ships and wagons show it as Max Durability, their HP. See Checked on bdocodex |
| `+0x42`               | i32                   | varied_max_mp           | Max MP the item adds; set on 1,540 blocks |
| `+0x46`               | f32                   | varied_recov_hp         | HP recovery the item adds |
| `+0x4A`               | i32                   | varied_recov_mp         | MP recovery the item adds |
| `+0x4E`               | bytes[72]             | unknown_4e              | Always `0`, see Field Names |
| `+0x96`               | i64                   | varied_possessable_weight | Weight limit the item adds, LT x 10,000; set on 1,764 blocks |
| `+0x9E`               | bytes[8]              | unknown_9e              | Always `0` |
| `+0xA6`               | u8                    | socket_count            | Crystal sockets: `2` (14,804 blocks), `0` (14,468) or `1` (4,232) |
| `+0xA7`               | f32[7][3]             | lane_stats              | Seven stats, each for the melee, ranged and magic lanes, below |
| `+0xFB`               | u32                   | skill_key               | `skill_no << 16 \| level` as in [skill.dbss](skill_dbss.md); `0` when the item has no skill, level `1` on all 23,303 others |
| `+0xFF`               | str16                 | description_kr          | Korean text with `<PAColor>` tags; empty in most blocks, set on ship equipment |
| `description_kr+0x00` | str16                 | effects                 | The effect script, one `NAME(args);` per line: `ITEM_EFFECT();`, `PLAYER_DAM_ADD(10);`, `ALL_AP_INCRE();` |
| `effects+0x00`        | u8                    | is_notify_world         | `1` on 4,363 blocks |
| `effects+0x01`        | u8                    | fail_result             | The sheet's `EnchantType`, see Failure Results |
| `effects+0x02`        | u32                   | item_market_added_price | Millionths: 1,000,000, or 1,150,000 on 395 blocks |
| `effects+0x06`        | u32                   | unknown_effects_06      | 700,000 on 32,646 blocks, else 200,000 to 500,000 |
| `effects+0x0A`        | u8                    | market_filter_1         | 22 values |
| `effects+0x0B`        | u8                    | market_filter_2         | `0`, `2`, `3` or `4` |
| `effects+0x0C`        | u8                    | unknown_effects_0c      | Always `0` |
| `effects+0x0D`        | Lane Dice[3]          | dice_accuracy           | Per lane: the AP roll as dice text (`1D5+85` is 86 to 90, `1D1-1` is none), then the accuracy; see Lane Dice |
| `dice_accuracy+0x00`  | f32[3][4]             | defense                 | Per lane: evasion, hidden evasion, damage reduction, hidden damage reduction |
| `dice_accuracy+0x30`  | i32[3]                | unknown_dice_accuracy_30 | Always `-1` |
| `dice_accuracy+0x3C`  | u8                    | life_main_type          | `15` on 31,056 blocks |
| `dice_accuracy+0x3D`  | u8                    | life_sub_type           | |
| `dice_accuracy+0x3E`  | f32                   | life_stat               | Set on life skill gear rows of the sheet |
| `dice_accuracy+0x42`  | u8                    | group_level             | 20 values |
| `dice_accuracy+0x43`  | u32                   | new_perfect_enchant_item_id | Item of the newer perfect enhancement; `0` on most blocks |
| `dice_accuracy+0x47`  | i64                   | new_perfect_enchant_item_count | How many |
| `dice_accuracy+0x4F`  | u16                   | new_perfect_enchant_durability_loss | `10`, `20` or `30` |
| `dice_accuracy+0x51`  | i64                   | prevent_cron_count      | Set on 4,620 blocks |
| `dice_accuracy+0x59`  | f32                   | adjust_strength         | Equals `adjust_speed` in every block |
| `dice_accuracy+0x5D`  | f32                   | adjust_speed            | |
| `dice_accuracy+0x61`  | f32                   | adjust_health           | `0` in every block |
| `dice_accuracy+0x65`  | i64                   | varied_max_food         | Set on 548 blocks |
| `dice_accuracy+0x6D`  | i32                   | varied_cannon_cool_time | `10000` (44 blocks) or `20000` (22) |
| `dice_accuracy+0x71`  | i32[3]                | unknown_dice_accuracy_71 | Always `0`; the sheet's `VariedCannonAccuracy`, `VariedCannonMaxLength` and `VariedCannonMaxAngle` by column order |
| `dice_accuracy+0x7D`  | u32                   | aid_item_count          | 0 to 3 |
| `dice_accuracy+0x81`  | u32[aid_item_count]   | aid_item_ids            | Hammers and crystals, see Notes |
| `aid_item_ids+0x00`   | u8                    | is_cronable             | `1` on 610 blocks |
| `aid_item_ids+0x01`   | u8                    | is_guild_rental         | `1` on 1,197 blocks |
| `aid_item_ids+0x02`   | u16                   | need_perfect_enchant_stack | `300` on 7 blocks, else `0` |
| `aid_item_ids+0x04`   | bytes[2]              | unknown_aid_item_ids_04 | Always `0` |

Strings are a u64 UTF-16 code-unit count, then the text with no terminator.
Counts in the rows from `is_notify_world` on are blocks on client 3473.

Earlier versions of this doc called `unknown_dice_accuracy_30` `sentinels`.

The seven lane stats, in order:

| Index | Field         | Notes |
| ----: | ------------- | ----- |
| 0     | added_damage  | `AddedDDD`, `AddedRDD`, `AddedMDD`, see Field Names |
| 1     | unknown       | `0` in every block |
| 2     | ap_min        | Lowest AP |
| 3     | ap_max        | Highest AP |
| 4     | ap_display    | `round((ap_min + ap_max) / 2)` in every lane of every block |
| 5     | damage_reduction | Equals the tail's lane value 2 in every block |
| 6     | evasion       | Equals the tail's lane value 0 in every block |

A weapon fills the lanes it attacks with (Kzarka Gauntlet melee and magic, a
bow ranged); accessories fill all three alike. The browser shows the highest
lane.

### Lane Dice (variable: 12 bytes + dice text)

| Offset         | Type  | Field    | Notes |
| -------------- | ----- | -------- | ----- |
| `+0x00`        | str16 | dice     | The AP roll as dice text |
| `dice+0x00`    | f32   | accuracy | The lane's accuracy |

### `enchantstaticstatusoffset.dbss`

The shared PABR layout with u32 keys (`parse_pabr_u32_offset_rows`): `PABR`, a
u32 row count, `count` 12-byte rows, then the 12-byte trailer
`(0, 8 + count × 12, 0)`.

| Offset              | Type              | Field        | Notes |
| ------------------- | ----------------- | ------------ | ----- |
| `+0x00`             | char[4]           | magic        | ASCII `PABR` |
| `+0x04`             | u32               | count        | Number of rows |
| `+0x08`             | Offset Row[count] | rows         | See Offset Row |
| `rows+0x00`         | String Table      | string_table | See String Table |
| `string_table+0x00` | u32               | table_start  | `8 + count × 12`, where the rows end |
| `string_table+0x04` | u32               | zero         | Always `0` |

Levels run 0 to 25 with no gaps per key. There are 4,811 enchant keys
(1 to 62,304) on client 3458.

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                      |
| ------- | ---- | ----------- | ------------------------------------------ |
| `+0x00` | u32  | key         | `level << 24 \| enchant_key`               |
| `+0x04` | u32  | data_offset | Byte offset of the block                   |
| `+0x08` | u32  | data_size   | Block length in bytes                      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0` |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Layout 1

On client 1784 the block had 4 fewer zero bytes in `unknown_4e`, an
extra u32 after the defense values, and one aid item with no count and no
`is_cronable`. Only the Block differs from Layout 2. Field names keep
Layout 2's offsets, so `skill_key` sits at `+0xF7` here. The parser reads
only Layout 2.

### Block (variable: 418 bytes + strings)

| Offset                | Type         | Field                   | Notes |
| --------------------- | ------------ | ----------------------- | ----- |
| `+0x00`               | u32          | enchant_key             |       |
| `+0x04`               | u8           | level                   |       |
| `+0x05`               | u32          | material_item_id        |       |
| `+0x09`               | u64          | material_count          |       |
| `+0x11`               | u64          | perfect_count           |       |
| `+0x19`               | u64          | black_count_for_item_market | |
| `+0x21`               | bytes[8]     | unknown_21              |       |
| `+0x29`               | u32          | success_rate            |       |
| `+0x2D`               | u32          | downgrade_rate          |       |
| `+0x31`               | bytes[4]     | unknown_31              |       |
| `+0x35`               | u16          | max_durability          |       |
| `+0x37`               | u16          | fail_durability_loss    |       |
| `+0x39`               | u16          | recover_max_endurance   |       |
| `+0x3B`               | u8           | unknown_3b              |       |
| `+0x3C`               | u16          | perfect_durability_loss |       |
| `+0x3E`               | f32          | max_hp                  |       |
| `+0x42`               | i32          | varied_max_mp           |       |
| `+0x46`               | f32          | varied_recov_hp         |       |
| `+0x4A`               | i32          | varied_recov_mp         |       |
| `+0x4E`               | bytes[68]    | unknown_4e              | Always `0` on client 1784 |
| `+0x92`               | i64          | varied_possessable_weight | |
| `+0x9A`               | bytes[8]     | unknown_9e              |       |
| `+0xA2`               | u8           | socket_count            |       |
| `+0xA3`               | f32[7][3]    | lane_stats              |       |
| `+0xF7`               | u32          | skill_key               |       |
| `+0xFB`               | str16        | description_kr          |       |
| `description_kr+0x00` | str16        | effects                 |       |
| `effects+0x00`        | u8           | is_notify_world         |       |
| `effects+0x01`        | u8           | fail_result             |       |
| `effects+0x02`        | u32          | item_market_added_price |       |
| `effects+0x06`        | u32          | unknown_effects_06      |       |
| `effects+0x0A`        | u8           | market_filter_1         |       |
| `effects+0x0B`        | u8           | market_filter_2         |       |
| `effects+0x0C`        | u8           | unknown_effects_0c      |       |
| `effects+0x0D`        | Lane Dice[3] | dice_accuracy           |       |
| `dice_accuracy+0x00`  | f32[3][4]    | defense                 |       |
| `dice_accuracy+0x30`  | u32          | unknown_old_30          | 1,000,000 in all 33,805 blocks on client 1784 |
| `dice_accuracy+0x34`  | i32[3]       | unknown_dice_accuracy_30 |      |
| `dice_accuracy+0x40`  | u8           | life_main_type          |       |
| `dice_accuracy+0x41`  | u8           | life_sub_type           |       |
| `dice_accuracy+0x42`  | f32          | life_stat               |       |
| `dice_accuracy+0x46`  | u8           | group_level             |       |
| `dice_accuracy+0x47`  | u32          | new_perfect_enchant_item_id | |
| `dice_accuracy+0x4B`  | i64          | new_perfect_enchant_item_count | |
| `dice_accuracy+0x53`  | u16          | new_perfect_enchant_durability_loss | |
| `dice_accuracy+0x55`  | i64          | prevent_cron_count      |       |
| `dice_accuracy+0x5D`  | f32          | adjust_strength         |       |
| `dice_accuracy+0x61`  | f32          | adjust_speed            |       |
| `dice_accuracy+0x65`  | f32          | adjust_health           |       |
| `dice_accuracy+0x69`  | i64          | varied_max_food         |       |
| `dice_accuracy+0x71`  | i32          | varied_cannon_cool_time |       |
| `dice_accuracy+0x75`  | i32[3]       | unknown_dice_accuracy_71 |      |
| `dice_accuracy+0x81`  | u32[1]       | aid_item_ids            | One item or `0`; `45077` or `45078` on the 776 blocks that set it on client 1784 |
| `dice_accuracy+0x85`  | u8           | is_guild_rental         | Matches Layout 2's `is_guild_rental` on every block both clients share |
| `dice_accuracy+0x86`  | u16          | need_perfect_enchant_stack | |
| `dice_accuracy+0x88`  | bytes[2]     | unknown_aid_item_ids_04 |       |

## The Link From Items

`itemenchant.dbss` stores the enchant key in the u32 just before the u64
length of the Korean name. Combining an item block's level with that key
always finds a block here: all 130,297 item blocks with a non-zero key hit
one, none miss (client 3458). 3,729 of the 4,811 keys are used by an item;
40,025 base items store `0` and have no enhancement data. Every level of an
item stores the same key, so the base block is enough. The browser shows
the key as the `itemenchant.dbss` Enchant Key column, and the
`ENCHANT_KEY_ITEMS` lookup index turns it around for the Items column here.
On client 3464 the largest key, 21201, holds 3,503 items (Pearl Shop
outfits).

| Item                     | Item ID | Enchant key |
| ------------------------ | ------: | ----------: |
| Kzarka Gauntlet          | 11210   | 662         |
| Sicil's Necklace         | 11625   | 8017        |
| Kharazad Necklace        | 11697   | 12336       |
| Tuvala Helmet            | 695105  | 6130        |

## Failure Results

`fail_result`, byte 1 after the effect script and the sheet's `EnchantType`
column, says what a failed attempt does to the item. The client knows four danger types (`Safe`, `Gradedown`,
`Broken`, `DownAndBroken` in `panel_widget_enchant_main_all_1.luac`); their
numbers are set by the game code, so the values below come from the data.
Counts are blocks above level 0 on client 3464.

| Value | Meaning | Blocks | Evidence |
| ----: | ------- | -----: | -------- |
| 0     | The attempt cannot fail | 8,206 | 8,203 of them have a 100% success rate |
| 1     | Safe: a failure costs durability only | 14,537 | Griffon's Helmet up to DUO, Kharazad Necklace I |
| 2     | Destroyed: a failure deletes the item | 1,143 | Black Distortion Earring (`11853`, enchant key `8590`) and Sicil's Necklace on every level |
| 3     | Downgrade: a failure drops a level | 4,806 | Griffon's Helmet from TRI, Kharazad Necklace from II |

No block stores a fourth value for `DownAndBroken`. The window prints "{percent}%
chance for enhancement level to drop upon failure" for `Gradedown` from
`ToClient_GetTargetEnchantDownRate()`, which is `downgrade_rate`: 4,745 of
the 4,806 downgrade blocks store 1,000,000, so a failure past that level
always drops a level, as it does in game. [Hunting] Gauche Marni Sniper
Rifle (`56520`, enchant key 28303) is the exception with 10% for +8 and 50%
for +9. 61 downgrade blocks store `0` and 4 safe blocks a rate.

## Checked on bdocodex

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

A second check (2026-10-11, client 3464) named the defense values and the
max HP:

- Dim Tree Spirit's Armor (`11017`, enchant key `5293`) at TRI: bdocodex
  shows "Evasion: 36 (+108)" and "Damage Reduction: 43 (+14)"; block 18
  stores 36, 108, 43 and 14 in each lane's defense values. bdocodex writes
  the hidden value in brackets.
- `max_hp`: bdocodex shows Max HP +200 on Dim Tree Spirit's Armor, which
  stores `200` on every level, and Max Durability 125,000 at +0 and 200,000
  at +10 on Panokseon: Cheongun's Enhanced Plating (`59472`), 10,000 and
  20,000 on Forest Path Wagon Cover (`53511`), the values blocks 0 and 10
  of their keys store. Item durability is the separate `max_durability`.
- bdocodex shows the chance of the next attempt on each level: Dandelion
  Lancia, Yuria Longsword and Dim Tree Spirit's Armor read 6.25%, 2% and
  0.3% at DUO, TRI and TET, the `success_rate` of blocks 18, 19 and 20.

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
- Cron Stones are not in this file, nor in any other table of
  `gamecommondata/binary`. bdocodex shows 34, 127 and 531 for Kzarka
  Gauntlet TRI, TET and PEN, and 40 / 146 / 611 (Dandelion Lancia), 19 / 37
  / 69 (Yuria Longsword) and 43 / 131 / 493 (Dim Tree Spirit's Armor) at
  DUO, TRI and TET. None of these is stored at a common position in the
  blocks of those levels (as u16, u32, u64 or f32), and a scan of all 772
  tables on client 3464 finds none of the three runs at any row spacing up
  to 200 bytes. The client
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
    `black_count_for_item_market` (u64).
  - It calls the 25 floats at `+0x42` AP per species. The sheet places max
    MP, HP and MP recovery, weight and the socket count there, and the rest
    is 0 in every block.
  - It says durability goes "base 100 → PRI 120 / DUO 140 / TRI 160 / TET 180
    / PEN 200". That holds only for some lines, see above.
  - It calls `+0x3E` max HP, "0 unless the DSL carries `HP_UP(n)`". Max HP
    holds (Checked on bdocodex), the `HP_UP` rule does not: 832 blocks have
    `HP_UP` in the script and store `0`, 865 store a value with no or a
    different `HP_UP`.
  - It calls the dice strings accuracy dice. The dice are the AP roll (Kzarka
    Gauntlet PRI `1D5+85`, AP 86 to 90); the f32 after each one is the
    accuracy.

## Field Names

The names follow the `Enchant_Weapon`, `Enchant_Armor`, `Enchant_Accessory`, `Enchant_Servant`, `Enchant_Cash`, `Enchant_LifeEquipment` and `Enchant_Equipment` sheets of a private server's `DataSheets.bexcel` on client 1784 (one layout of 105 columns, keyed by `Index` and `Enchant`), which share 27,761 (key, level) blocks with client 3473. Matched value by value at every offset of the fixed part and of the tail regions:

| Column | Field | Equal (non-zero rows) |
| ------ | ----- | --------------------- |
| `BlackCountForItemMarket` | `black_count_for_item_market` | 22,365 of 22,561 |
| `RecoverMaxEndurance` | `recover_max_endurance` | 24,076 of 24,076 |
| `VariedMaxMP` | `varied_max_mp` | 1,224 of 1,257 |
| `VariedRecovHP` | `varied_recov_hp` | 332 of 332 |
| `VariedRecovMP` | `varied_recov_mp` | 61 of 61 |
| `VariedPossessableWeight` | `varied_possessable_weight` | 1,312 of 1,536 |
| `Socket` | `socket_count` | 12,927 of 15,917 |
| `AddedDDD`, `AddedRDD`, `AddedMDD` | lane stat 0, melee, ranged and magic | 6,536 of 6,751 (`AddedDDD`) |
| `SkillNo` | high half of `skill_key` | 16,569 of 16,569 |
| `IsNotifyWorld` | `is_notify_world` | 3,001 of 3,196 |
| `EnchantType` | `fail_result` | 16,373 of 17,132 |
| `ItemMarketAddedPrice` | `item_market_added_price` | 395 of 395 (`1150000`; empty rows store 1,000,000) |
| `MarketFilter1`, `MarketFilter2` | `market_filter_1`, `market_filter_2` | 20,022 of 20,023, 825 of 825 |
| `LifeMainType`, `LifeSubType`, `LifeStat` | the three life fields | 1,451 of 1,451, 1,778 of 1,778, 2,043 of 2,049 |
| `GroupLevel` | `group_level` | 14,345 of 14,362 |
| `NewPerfectEnchantItemKey`, `NewPerfectEnchantItemCount`, `NewPerfectEnchantDecraseMaxEndurance` | the three `new_perfect_enchant_*` fields | 2,005 of 2,005, 2,131 of 2,131, 2,178 of 2,178 |
| `PreventCronCount` | `prevent_cron_count` | 3,103 of 3,153 |
| `AdJustStrenght`, `AdJustSpeed` | `adjust_strength`, `adjust_speed` | 110 of 130 each |
| `VariedMaxFood` | `varied_max_food` | 466 of 513 |
| `VariedCannonCoolTime` | `varied_cannon_cool_time` | 44 of 44 |
| `Cronable`, `GuildRental` | `is_cronable`, `is_guild_rental` | 16 of 16, 991 of 991 |
| `NeedPerfectEnchantStack` | `need_perfect_enchant_stack` | 7 of 7 |

The rest of the gap between columns is later rebalancing; the file sets several flags on more blocks than the sheet (`is_cronable` on 610). `AdJustStrenght` and `AdJustSpeed` hold the same value on every row, so their order, and the all-zero `AdJustHealth` after them, follow the sheet's column order. The sheet's `ItemProtecter` (`45077` J's Hammer of Loyalty, `45078` J's Hammer of Precision and others) is one of the `aid_item_ids` on 401 of its 404 rows; the file lists up to three.

The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::EnchantStaticStatus` holds `_enchantNeedItemKey`, `_enchantNeedItemCount`, `_perfectEnchantNeedItemCount`, `_enchantNeedCountForItemMarket`, the success, broken and down rates, `_maxEndurance`, `_reduceMaxEnduranceAtFail`, `_recoverMaxEndurance`, `_reduceMaxEnduranceAtPerfectEnchant`, `_variedHp`, `_variedMp`, the regen values, the tribe, critical, luck and speed values, `_variedPossessableWeight`, `_variedSuspension`, `_socketCount`, the dice, the added damage, the min, max and average damage, `_pv`, `_dv`, `_skillKey`, `_description`, `_isNotifyWorld`, `_enchantType` and `_itemMarketAddedPricePercent`, in the order the fixed part and the bytes after the script store them. The sheet's tribe, critical, luck and speed columns are 0 on every row, which fits the 72 zero bytes at `+0x4E`; the data cannot place them one by one.

`black_count_for_item_market` is the `BlackCountForItemMarket` column, the 2016 `_enchantNeedCountForItemMarket`. It is neither the Cron Stone count nor the Ancient Anvil count: Dim Tree Spirit's Armor needs 43, 131 and 493 Cron Stones at DUO, TRI and TET (bdocodex), and Garmoth's Ancient Anvil guide lists 15 for a TET Blackstar main weapon going to PEN, where Blackstar Longsword (enchant key 84) stores 3,670. The anvil counts are in [guaranteeenchantss.dbss](guaranteeenchantss_dbss.md). Kzarka Gauntlet stores 11, 12, 35, 182 and 1,330 for PRI to PEN.

## Open Questions

### What the Unknown u32 After the Script Holds

Bytes 6 to 9 after the effect script hold 700,000 on 32,646 blocks and 200,000, 300,000, 400,000 or 500,000 on the rest. It is not `EnchantAddRateByWorldMarket` (2,000,000 to 3,000,000 on 939 sheet rows, all 700,000 here), and no other sheet column holds these values.

### Remaining Unknown Fields

`unknown_3b` and lane stat 1 are `0` in every block, as are the 8 bytes at `+0x21` and the 4 at `+0x31`. The 2016 struct has a broken rate between the success and down rates, but the sheet's `EnchantBrokenRate` and `EnchantDownRate` are `0` on every row, so the data cannot say whether `+0x2D` or `+0x31` is the 2016 `_enchantDownRate`; `+0x2D` reads as the down rate from the window Lua (Failure Results).
