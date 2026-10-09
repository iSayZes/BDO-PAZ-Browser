# `buff.dbss` Format

## Purpose

The master buff table: every buff and debuff the game can apply, from potions,
food and scrolls to title effects, furniture, boss mechanics and monster-only
debuffs. Each record carries an internal Korean name, a level, an effect type,
ten numeric parameters, a duration, an optional icon and an optional Korean
description whose English form lives in LOC type 5.

Example:

```text
buff_id 48830
  name         수렵 숙련도 +70 3시간   (internal label, "Hunting Mastery +70 3 hours")
  icon         New_Icon/04_PC_Skill/03_Buff/HuntingBuff.dds
  description  Hunting Mastery +70      (LOC str_type=5, str_id1=48830)
```

## Companion Files

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `buffoffset.dbss`     | Required | `buff_id → (offset, size)` index into this file   |
| `languagedata_en.loc` | Optional | English descriptions, `str_type=5`                |
| `skill.dbss`, `itemenchant.dbss` | Optional | Applied By and inherited titles, through the `BUFF_ITEMS` and `SKILL_BUFFS` lookup indexes |
| `exploration.bss`, `mapdata_realexplore2.bwp` | Optional | Sub-node names of type 37 (`Bambu Valley - Mining`), through the `NODE_PARENT` lookup index |
| `instancefield.dbss` | Optional | Field names of type 176 (`A1_001`), through the `INSTANCE_FIELD_NAME` lookup index |

[`buffsimply.bss`](buffsimply_bss.md) holds the same buff IDs in fixed 32-byte
rows with the icon path, `unknown_str`, `is_shown` and a few stats bytes. It is
not needed to read this file.

All multi-byte values are little-endian.

## File Layout

| Offset  | Type | Field   | Notes                                              |
| ------- | ---- | ------- | -------------------------------------------------- |
| `+0x00` | u32  | count   | Number of records; see below                       |
| `+0x04` | ...  | records | Variable-length records, located via the offset file |

The records tile the file exactly: sorted by offset, each ends where the next
begins, and the last ends at EOF.

Observed records: 44,609 in the pre-2026-09-27 test fixture, 44,645 in the
2026-09-27 client (3458), 44,683 on client 3464. The row counts elsewhere in
this doc are from the pre-2026-09-27 fixture.

## Record Structure

A record is a chain of fixed blocks and length-prefixed strings. The strings use
the shared 8-byte prefix (u32 length, u32 zero, no terminator); UTF-16 lengths
count characters, ASCII lengths count bytes.

| Order | Type               | Field       | Notes                                                    |
| ----- | ------------------ | ----------- | -------------------------------------------------------- |
| 1     | u32                | buff_id     | Always equals the offset row's `buff_id`; a u16 before client 3464, see Notes |
| 2     | prefixed UTF-16    | name        | Internal Korean label; no LOC counterpart                |
| 3     | 133 bytes          | stats block | See Stats Block below                                    |
| 4     | prefixed UTF-16    | unknown_str | Short digit text, `"0"` in 39,455 rows; 186 distinct     |
| 5     | prefixed ASCII     | icon_path   | Relative to `ui_texture/icon/`; see Notes                |
| 6     | u8                 | is_shown    | See Notes; `1` in 12,746 rows                            |
| 7     | u32                | apply_rate  | `1000000` (100%) in 44,427 rows; per-million scale       |
| 8     | prefixed UTF-16    | description | Korean, with `<PAColor>` tags; empty in 30,290 rows      |
| 9     | 27 bytes           | tail block  | See Tail Block below                                     |

Record sizes range from 205 to 2,200 bytes, median 239, on client 3464.

### Stats Block (133 bytes)

Offsets are relative to the end of the name string.

| Offset  | Type    | Field           | Notes                                                                 |
| ------- | ------- | --------------- | --------------------------------------------------------------------- |
| `+0x00` | i16     | buff_level      | 1 to 999; `1` in 32,071 rows. Ranks buffs within a `group`; staged buffs count up, e.g. boss stages 1 to 10 |
| `+0x02` | u8[2]   | reserved        | Always `0`                                                            |
| `+0x04` | u16     | group           | `0` in 28,199 rows. Buffs of one group replace each other by level, see Stacking |
| `+0x06` | i16     | condition_type  | `0` in 44,390 rows; the trigger of types 1 and 4, see `condition_type` |
| `+0x08` | u8      | effect_type     | 173 distinct values; see Enum Values                                  |
| `+0x09` | u8      | flag_09         | `1` in 44,489 rows                                                    |
| `+0x0A` | u8      | flag_0a         | `1` in 31,950 rows                                                    |
| `+0x0B` | u8      | flag_0b         | `1` in 14,707 rows                                                    |
| `+0x0C` | u8[7]   | flag_0c..flag_12 | Each byte is `0` or `1`                                              |
| `+0x13` | i64[10] | param_1..param_10 | Effect parameters; meaning depends on `effect_type`. Percentages use a per-million scale (`100000` = 10%) |
| `+0x63` | u8      | flag_63         | `0` or `1`                                                            |
| `+0x64` | u8      | flag_64         | `0` or `1`                                                            |
| `+0x65` | u16     | reserved        | Always `0`                                                            |
| `+0x67` | u8      | flag_67         | `0` or `1`                                                            |
| `+0x68` | u32     | duration_ms     | `0` in 30,016 rows; max `86400000` (24 h). `3600000` = 60 min        |
| `+0x6C` | u32     | tick_ms         | Tick interval of periodic effects in milliseconds (`10000` = every 10 sec); see Notes |
| `+0x70` | u8[14]  | reserved        | `0` in every row but one                                              |
| `+0x7E` | u8      | flag_7e         | `1` in 44,514 rows                                                    |
| `+0x7F` | u8      | unknown_7f      | Always `2`                                                            |
| `+0x80` | u8      | reserved        | Always `0`                                                            |
| `+0x81` | u8      | unknown_81      | `46` in every row but one                                             |
| `+0x82` | u8      | unknown_82      | `2` in every row but one                                              |
| `+0x83` | u8      | flag_83         | `0` or `1`                                                            |
| `+0x84` | u8      | flag_84         | `0` or `1`                                                            |

### Tail Block (27 bytes)

Offsets are relative to the end of the description string. Mostly zero.

| Offset  | Type | Field       | Notes                                        |
| ------- | ---- | ----------- | -------------------------------------------- |
| `+0x00` | u8   | flag_00     | `1` in 34 rows                               |
| `+0x01` | u8   | flag_01     | `1` in 6 rows                                |
| `+0x02` | u32  | unknown_02  | `0`, `1` or `2`                              |
| `+0x06` | u8   | unknown_06  | `3` in 44,575 rows                           |
| `+0x07` | i32  | unknown_07  | `0`, `1000000` or `-1000000`                 |
| `+0x0B` | u8[12] | reserved  | Always `0`                                   |
| `+0x17` | u8   | flag_17     | `1` in 221 rows                              |
| `+0x18` | u8   | stacking_category | 61 distinct values; item type such as food, draught or perfume, see Stacking |
| `+0x19` | u8   | is_exclusive | `1` in 2,069 rows on client 3458, never with category `0`; applying the buff ends the other buffs of its category, see Stacking |
| `+0x1A` | u8   | unknown_1a  | `6` in 18,895 rows, else `0` or `1`          |

## `buffoffset.dbss`

`PABR` index into `buff.dbss` with u32 IDs, the layout of
`mentalcardoffset.dbss` (`parse_pabr_u32_offset_rows`). `data_offset` points
*at* the inline `buff_id` and `size` includes it.

### Header (8 bytes)

| Offset  | Type  | Field | Notes                                      |
| ------- | ----- | ----- | ------------------------------------------ |
| `+0x00` | u8[4] | magic | ASCII `PABR`                               |
| `+0x04` | u32   | count | Always equals the `buff.dbss` count        |

### Index Row (12 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                           |
| ------- | ---- | ----------- | ----------------------------------------------- |
| `+0x00` | u32  | buff_id     | Unique; 43 to 65,528, plus five IDs from 700,000 to 4,100,000,000 on client 3464 |
| `+0x04` | u32  | data_offset | Absolute offset of the record in `buff.dbss`    |
| `+0x08` | u32  | size        | Record size in bytes, including the `buff_id`   |

Before client 3464 the row was 10 bytes with a u16 `buff_id`, the layout of
`characterstaticoffset.dbss`. The parser reads only the u32 layout.

### Trailer (12 bytes)

| Offset  | Type | Value  | Notes                                         |
| ------- | ---- | ------ | --------------------------------------------- |
| `+0x00` | u32  | `0`    |                                               |
| `+0x04` | u32  | varies | End offset of the index rows (`536204` on client 3464) |
| `+0x08` | u32  | `0`    |                                               |

## Enum Values

`effect_type` (stats block `+0x08`). Labels are inferred from the internal names
of the buffs that use each value.

| Value | Rows  | Observed buffs                                     | Parameters, where confirmed                          |
| ----- | ----- | -------------------------------------------------- | ---------------------------------------------------- |
| 1     | 1,662 | HP over time or per trigger                        | `param_1` = HP per tick (`tick_ms`) or per trigger (`condition_type`), signed: positive heals, negative damages |
| 2     | 443   | Max HP                                             | `param_1` = amount                                   |
| 18    | 3,386 | Summons                                            | `param_1` = summoned character (LOC type 6 name); see Effect text |
| 25    | 1,597 | Combat, skill and life EXP gain                    | `param_1` = bonus per million; `param_2` 0 combat, 1 skill, 2 life, 3 party (2 buffs, unlabelled); under 2, `param_3` = life skill as in type 80, `15` all |
| 34    | 287   | Display buff (title, text and icon)                | All parameters `0` on 228; see Effect text           |
| 38    | 5,683 | Knowledge unlock                                   | `param_1` = knowledge ID (LOC type 34 name); see Effect text |
| 39    | 1,732 | All AP, positive or negative                       | `param_1` = `3`, `param_2` = amount                  |
| 40    | 870   | All Accuracy                                       | `param_1` = `3`, `param_2` = amount                  |
| 43    | 1,730 | All Damage Reduction                               | `param_1` = `3`, `param_2` = amount                  |
| 45    | 8,311 | Damage multipliers (summons, monsters, siege, cannons) | `param_4` = damage per million (`5790000` = `Attack Damage 579%`); `param_1` maybe the attack type, see Effect text |
| 46    | 1,831 | Species extra AP                                   | `param_1` = species: `0` Humans, `1` Demihumans, `2` Beasts, `3` Kamasylvian Monsters, `4` Edanian Monsters; `param_2` = amount, can be negative. `5` is unused ("Not in Use", Korean `미사용`), `6` mixes hunting effects whose amounts do not follow `param_2`; both unlabelled. 1,296 of 1,313 one-line texts match |
| 49    | 1,378 | Crowd-control resistance                           | `param_1` = kind as in type 105: `0` Knockback/Floating, `1` Knockdown/Bound, `2` Grapple, `3` and `5` Stun/Stiffness/Freezing (stun and stiffness in Korean), `7` Fear, `8` All; `param_2` per million. `6` (bound in Korean) reads "Not in Use", unlabelled. 745 of 873 one-line texts match; the rest are kind 7 "Not in Use" |
| 58    | 1,132 | Display buff (title, text and icon)                | All parameters `0` on 1,095; `param_1` is set on a few vision buffs, see Effect text |

These are also confirmed against the English LOC type 5 text of their buffs. Percentages use the same per-million scale.

| Value | Rows | Effect                        | Parameters                                                        |
| ----- | ---: | ----------------------------- | ----------------------------------------------------------------- |
| 3     | 291  | HP Recovery                   | `param_1` = amount                                                |
| 5     | 85   | Max MP/WP/SP                  | `param_1` = amount                                                |
| 6     | 268  | MP Recovery                   | `param_1` = amount                                                |
| 8     | 205  | Max Stamina                   | `param_1` = amount                                                |
| 9     | 383  | Movement Speed                | `param_1` per million (`25000` = 2.5%)                            |
| 10    | 320  | Attack Speed                  | `param_1` per million                                             |
| 11    | 312  | Casting Speed                 | `param_1` per million                                             |
| 30    | 509  | Critical Hit Rate             | `param_1` per million                                             |
| 41    | 804  | All Evasion                   | `param_1` = `3`, `param_2` = amount                               |
| 80    | 180  | Life-skill EXP                | `param_1` = life skill, see below; `param_2` = amount             |
| 93    | 238  | Special-attack extra damage   | `param_1` = attack kind: `0` all, `1` back, `2` down, `3` air, `4` critical, `5` speed, `6` counter; `param_2` per million |
| 105   | 123  | Ignore resistance             | `param_1` = resistance kind: `0` knockback/floating, `1` knockdown/bound, `2` grapple, `3` stun/stiffness/freezing, `8` all; `param_2` per million |
| 128   | 78   | Weather resistance            | `param_1` = `0` heatstroke, `1` hypothermia; `param_2` per million |

These are confirmed the same way, and where their buffs have little or no
English text, by item names and bdocodex tooltips (see Effect text).

| Value | Rows | Effect                        | Parameters                                                        |
| ----- | ---: | ----------------------------- | ----------------------------------------------------------------- |
| 4     | 268  | MP/WP/SP over time            | `param_1` per tick, signed; `tick_ms` the interval; `condition_type` `1` = per hit instead. Without either it is a one-off refill, unlabelled (see Effect text) |
| 14    | 172  | Crowd control                 | `param_1` = kind, `param_2` = duration in ms (`Stun for 5 sec`), see Effect text; `param_4` `1` on every labelled kind |
| 16    | 355  | Remove buffs                  | `param_1` = buff `group` to remove (`Remove Group 44812`); `param_2` `15` on the bleed, poison and burn cures, others open |
| 17    | 177  | Learn skill                   | `param_1` = skill (LOC type 10 name); `param_3` `1` on all |
| 19    | 6    | Sailor EXP                    | `param_1` per million                                             |
| 23    | 654  | Teleport                      | `param_1` = [teleport.dbss](teleport_dbss.md) section, `param_2` = key within it; see Effect text |
| 24    | 95   | One-off EXP                   | `param_1` = amount, flat; `param_2` = `0` Combat, `1` Guild, `2` Skill |
| 29    | 249  | Weight Limit                  | `param_1` in ten-thousandths of an LT (`1000000` = 100 LT)        |
| 37    | 1,031 | Node registration            | `param_1` = node key (LOC type 29 name); `param_2` `1` on 37 town, city and investment bank nodes, meaning unknown |
| 47    | 6    | Horse Capture Rate            | `param_1` per million                                             |
| 48    | 123  | Set effect points             | `param_1` = set skill (LOC type 10 name), `param_2` = points the piece adds; see Effect text |
| 50    | 144  | Mount EXP                     | `param_1` per million                                             |
| 51    | 7    | Mount Skill EXP               | `param_1` per million                                             |
| 52    | 40   | Fall Damage reduction         | `param_1` per million, stored positive and shown negative (`500000` = `Fall Damage -50%`); `param_2` `1` on one 15 sec buff, meaning unknown |
| 53    | 9    | Discovery Radius              | `param_1` in centimetres (`1000` = `+10m`); `param_2` `2000` / `4000` on two old grape salads that read `Vision Range Increase`, unlabelled |
| 56    | 28   | Amity                         | `param_1` per million (`Amity +10%`)                              |
| 57    | 225  | Item Drop Rate                | `param_1` per million; `param_2` `1` or `2` on 6 buffs with the same text, meaning unknown |
| 59    | 31   | Jump Height                   | `param_1` = amount                                                |
| 60    | 59   | One-off Contribution EXP      | `param_1` = `0` on all, `param_2` = amount; `param_3` `1` on all, meaning unknown |
| 62    | 10   | Skill points                  | `param_1` = `0` combat (`전투`) on all, `param_2` = points (`Skill Points (5)`) |
| 63    | 11   | Worker Stamina recovery       | `param_1` = amount, one-off (`Recover 2 Worker Stamina`)          |
| 66    | 87   | Energy Recovery               | `param_1` = amount (natural regeneration, `기운 자연 회복량`)        |
| 67    | 660  | Stat ranks                    | `param_1` = stat: `0` Movement Speed, `1` Attack Speed, `2` Casting Speed, `3` Critical Hit, `4` Luck, `5` Fishing Speed, `6` Gathering Speed; `param_2` = ranks, can be negative |
| 68    | 16   | Stat limits                   | `param_1` = stat as in type 67, worded `0` Movement Speed, `1` Attack Speed, `2` Casting Speed, `3` Critical Hit Rate, `4` Luck, `5` Fishing, `6` Gathering; `param_2` = steps (`Attack Speed Limit +1`) |
| 69    | 670  | Accept quest                  | `param_1` = quest chain, `param_2` = quest (LOC type 18 title); see Effect text |
| 71    | 31   | Inventory slots               | `param_1` = slots (`Inventory +8 Expansion`); `param_2` `1` on time-limited variants, which store no duration |
| 72    | 214  | Storage, stable, wharf and lodging slots | `param_1` = town (LOC type 17), `0` all towns; `param_2` = slots; `param_4` = `0` Storage, `1` Stable, `2` Wharf, `3` Worker's Lodging; `param_3` `1` on time-limited variants |
| 73    | 66   | Trade refresh                 | `param_1` = `0` territory, `1` trade manager; `param_2` = territory (`0` Balenos, `1` Serendia, `5` Southwestern Calpheon, `6` Southeastern Calpheon; `2` to `4` open) or NPC (LOC type 6) |
| 76    | 39   | Karma and fame                | `param_1` = amount, signed; `param_2` = `0` Karma, `1` Guild Karma, `2` Naval Fame |
| 79    | 44   | Energy recovery               | `param_1` = amount, one-off (`Recover 10 Energy`); every buff has no duration |
| 84    | 50   | Reveal hidden names           | No amount; `param_1` `10`, `3` or `300` on 4 buffs, meaning unknown |
| 89    | 62   | Breath/Strength/Health EXP    | `param_1` = `0` Breath, `1` Strength, `2` Health; `param_2` = amount |
| 90    | 42   | Death Penalty Resistance      | `param_1` per million (`30000` = +3%)                             |
| 91    | 18   | Durability Reduction Resistance | `param_1` per million                                           |
| 94    | 19   | Max Energy                    | `param_1` = amount                                                |
| 95    | 22   | Underwater Breathing          | `param_1` in milliseconds (`15000` = +15 sec)                     |
| 97    | 226  | Packages                      | `param_1` = package, `param_2` = duration in minutes (`21600` = 15 days); see Effect text |
| 98    | 1,093 | Mount and ship stats         | `param_1` = `0` Acceleration, `1` Movement Speed (shown as `Movement Speed (Mount)`), `2` Turn, `3` Brake; `param_2` per million |
| 100   | 1    | Character slots               | `param_1` = slots                                                 |
| 101   | 191  | Gain knowledge of a theme     | `param_1` = knowledge theme (LOC type 9, `mentaltheme.dbss`); bookshelves and their parchments |
| 103   | 535  | Worker contract               | `param_1` = worker (LOC type 6), `param_2` = town (LOC type 17)   |
| 106   | 163  | All Damage Reduction rate     | `param_1` = `3`, `param_2` per million                            |
| 107   | 64   | Gathering Item Drop Rate      | `param_1` per million; `param_2` `2` to `7` limit it to one gathering tool, unlabelled |
| 108   | 102  | Knowledge Gain Chance         | `param_1` per million                                             |
| 109   | 66   | Higher Grade Knowledge Gain Chance | `param_1` per million                                        |
| 111   | 196  | Craft time and success rate   | `param_1` = `0` Alchemy Time, `1` Cooking Time, `2` Processing Success Rate; `param_2` = time cut per million of 20 sec (`250000` = `-5 sec`), or the rate per million. `3` (farming time, 2 buffs) does not fit the time scale and stays unlabelled |
| 112   | 21   | Item Drop Amount              | `param_1` per million; `param_2` `1` or `2` on 5 buffs with the same text, meaning unknown |
| 120   | 116  | Monster Damage Reduction      | `param_1` = `0` rate, `param_2` per million; `param_1` = `2` flat, `param_2` = amount |
| 121   | 58   | Auto-fishing Time             | `param_1` per million, stored positive and shown negative (`50000` = `-5%`) |
| 126   | 48   | Fish grade chance             | `param_1` = `1` Rare Fish (yellow, `희귀`), `2` High-quality Fish (blue, `고급`); `param_2` per million |
| 131   | 2    | Trade Item Price              | `param_1` per million (desert trade tokens)                       |
| 134   | 9    | Swimming Speed                | `param_1` per million                                             |
| 136   | 219  | Extra AP Against Monsters / Adventurers | `param_1` = against monsters, `param_2` = against adventurers; no buff sets both |
| 142   | 673  | Obtain title                  | `param_1` = title ID (LOC type 1 name, `title.dbss` key)         |
| 149   | 246  | Life skill mastery            | `param_1` = life skill (type 80 numbering), `15` all; `param_3` = amount; `param_2` see below |
| 160   | 29   | Movement, attack and casting speed rates | `param_1` Movement Speed, `param_2` Attack Speed, `param_3` Casting Speed, each per million and signed |
| 168   | 16   | No Guard Gauge recovery       | No parameters                                                     |
| 169   | 37   | Healing reduction             | `param_1` per million, shown negative (`Target's Recovery -10%`)  |
| 176   | 48   | Teleport to an instance field | `param_3` = [instancefield.dbss](instancefield_dbss.md) key (`Teleport to Instance Field A1_001`); `param_1` `17` on all, meaning unknown |
| 181   | 58   | Breath/Strength/Health EXP %  | `param_1` = kind as in type 89, `3` one training-EXP passive (unlabelled); `param_2` per million |
| 186   | 4    | Black Shrine aura stat        | `param_1` = `1` fixed aura, `0` the aura the player picks (Light Orb); `param_2` = points; `param_3` = aura as type 187: `0` Sun, `1` Moon, `2` Earth |
| 187   | 298  | Flat AP and DP                | `param_1` = AP, `param_2` = DP, both can be set; `param_3` = Land of the Morning Light attribute: `0` Sun, `1` Moon, `2` Earth |
| 196   | 1    | Set level                     | `param_1` = level (`Patrigio's Pocket Watch`, 61)                 |
| 200   | 1    | Prize Catch Fish Rate         | `param_1` per million (Oceanbound Otter Fishing Rod, `+3%`)       |

The `param_1` life skills of type 80, from the English text of its buffs:
`0` Gathering, `1` Fishing, `2` Hunting, `3` Cooking, `4` Alchemy, `5`
Processing, `6` Training, `7` Trading, `8` Farming, `9` Sailing, `11` Barter.
This is the client's `CppEnums.LifeExperienceType` numbering (see
[lifeexp.dbss](lifeexp_dbss.md)), and the browser names each life skill from
the loaded LOC, as `lifeexp.dbss` does. `10` is the spare slot `temp1`, which
has no name and no buff with text. Kinds `5` and `6` of type 93 each appear on a
single buff with text. Kind `2` of type 128 appears only on
`Mermaid's Wish III`, so it stays unlabelled.

Type 149 `param_2` is fixed per life skill on every buff with text: `0` for
Gathering, Fishing, Processing and all (`15`), `1` for Hunting, Cooking,
Alchemy, Training and Sailing. The [Life Skill Season] buffs pair Gathering and
Processing with `2` to `7` for single tools (`Processing_Hoe Mastery`); those
stay unlabelled. Type 89 `param_3` is `1` on 8 food buffs and `0` elsewhere;
food that grants Health EXP is limited by the Satiated buff (type 184), which
may be what it marks, unconfirmed.

### Effect text

The browser's Effect column renders the parameters of every type above in the
game's wording (`All AP +8`, `Life EXP +15%`, `Alchemy EXP +2,560,350`), from
`_dbss/buff/effect/`; types 84 and 168, which store no amount, read one
fixed text each; other types, the kinds left unlabelled and a zero
amount show a dash. The same entry per type (`formats.py`, or `named.py` for
the types whose parameters name a LOC entry) labels the Param columns,
so `param_1` of a type 46 buff reads `3 (Kamasylvian Monsters)`. Of the 8,458 buffs with a
one-line LOC type 5 text and an Effect, 82% start with exactly that text on
client 3458, and 87% leaving out types 23, 48, 142 and 187, whose texts name
the place, set, title or event first (`Morning Earth: AP -60 for 3600 sec`). The rest
are the drift described in Notes (`Weight Limit +100 LT` on a buff that stores
150 LT), a `- Effect:` prefix, or placeholder text such as `UNKNOWN` and `Not
in Use`.

The second table above was checked three ways:

- **LOC type 5 text.** 29, 50, 57, 67, 90, 94, 95, 108, 109, 120, 136 and 149
  have 6 to 328 one-line texts each, and 85% to 100% of them start with the
  rendered text. Two type 149 buffs with `param_1` `15` read
  `Hunting Mastery +100`; the other 32 read `Life Skill Mastery`.
- **Item names.** `[Trial] Breath/Strength/Health Lv. 50` store type 89
  `param_1` `0`, `1` and `2`, and the `Recover 2 Energy` to
  `Recover 200 Energy` items store that amount in type 79 `param_1`.
- **bdocodex tooltips** of 85 items picked one or two per kind, buffs without
  English text first. 29, 50, 63, 95, 108, 136 and 149 match on every item.
  The type 89 items only say `Gain Breath EXP` or `Gain Strength EXP`, without
  an amount; `Stamina Experience` (574), from before Stamina became Breath,
  stores `0`. Items and the pet skill Death Penalty Resistance +3% (49134,
  buff 49134, `30000`) word type 90 as `Death Penalty Resistance +3%`, which
  the column follows; the six buff texts say `Death Penalty -0.5%` instead,
  for the same value. Item
  886, `Knowledge Gain Chance +10% (120 min)`, applies a 30% type 108 buff and
  a 10% type 109 buff, so its name is the stale part. Whale Meat Salad (9456)
  lists only its type 94 `Max Energy +10`, not the type 79 recovery of 10 it
  also applies.

The batch of 2026-10-03 was checked the same three ways:

- **98** mount and ship stats, on bdocodex: Light Iron Horseshoe (52902)
  reads `Movement Speed +2%` at +0 (buff 53512, `20000`), Kaia Fishing Boat
  Prow (49310) `Movement Speed +4%` with an `Acceleration +3%` set effect,
  Epheria: Old Wind Sail (49757) `Turn +0.5%` (52648, `5000`) and Krogdalo's
  Stirrups - Wind (52812) `Brake +3%` to `+8%`. Krogdalo's Feathers and the
  sea crystals word kind 1 as `Speed`; the gear tooltips and the 11 one-line
  texts read `Movement Speed`, and so does horse gear in game (`Max Stamina
  +7500, Movement Speed +6%, Turn +3%`). The column writes `Movement Speed
  (Mount) +2%`, so it does not read like the player's type 9, and the 11 texts
  then match up to that suffix.
  The Korean names give the kinds too (가속도, 속도, 회전력, 제동).
- **187** flat AP and DP: 256 of the 296 one-line texts contain the
  rendered amounts (`Morning Earth: AP -60 for 3600 sec`); the rest are
  prose (`Sun Buff +5`), `UNKNOWN`, or stale (41778 reads `DP -200`, stores
  `-30`). `param_3` follows the Korean name on all 252 attribute buffs (아침
  해 / 달 / 땅, "morning sun / moon / earth"); the Morning Light bosses
  (Duoksini, Bulgasal, Imoogi) store `2`.
- **53** Discovery Radius, on bdocodex: Chenga - Sherekhan Tome of Wisdom
  (12808) reads `+150m` (53476, `15000`), Magic Crystal of Infinity - Vision
  `+15m` (`1500`), the Magic Crystal of Enchantment - Vision and its Ancient
  version `+10m` (`1000`). `1999` reads `+20m` in its text and `+19.99m` in
  the column. Hunter's Clothes (Costume) (14321) lists `Discovery Radius
  +10m`, `Fall Damage -50%` and `Hunting EXP +10%`, which are its skill's
  buffs 52021 (type 53), 52023 (type 52) and 56286 (type 25, `param_3` `2`).
  The same costume line shows on other costumes in game ([Warrior] Red Gat:
  Song of Red Winds, 604186). `Vision Range` is the old English name of the
  stat: Magic Crystal of Infinity - Vision read `Vision Range +15m` on older
  sites (Altar of Gaming) and reads `Discovery Radius +15m` now, on the same
  type 53 buff, and the type 53 texts that never got updated still say
  `Increase Vision Range.`
- **52** Fall Damage: 19 of 22 one-line texts match; the others are prose
  (`You won't take fall damage.`) and a placeholder `1`.
- **59** Jump Height and **91** Durability Reduction Resistance, from the
  functional costume tooltips (`Jump Height +80`, `Durability Reduction
  Resistance +10%`): all 19 one-line type 59 texts match, and 8 of 10 type 91
  (the misses read `Gear Durability Reduction Resistance`, and `+10%` on a
  buff that stores `999999`).
- **14** crowd control: the kinds come from the Korean names (`[액션제한]
  넉다운`, "action limit: knockdown"): `1` Knockback, `2` Knockdown, `4` Stun,
  `6` Stiffness, `7` Bound, `12` Floating, `13` Air Smash, `14` Down Smash,
  `22` Freezing, and `15`, `17`, `20`, `23`, `24` the same that ignore the
  target's resistance (`저항 무시`). The kind word appears in 113 of the 127
  labelled names, the rest use a synonym (`기절`, also stun). Flashbang (206)
  stores kind `4` for `5000` and reads `Targets within the range will be
  stunned for a while` in game. Kind `0` mixes resistances and stuns, `5`
  guard crush and knockback, `19` (groggy) has two buffs; all three stay
  unlabelled. Keeper Marg's stiffness (850, `6`, `1350`) reads `Stiffness for
  1.35 sec`.
- **24** and **60** one-off EXP: the amount equals the number in all 47 item
  names that carry one (`Guild EXP (200,000)`, `60 Contribution EXP`; one
  `5 Contribution EXP` item stores `1`). The [Event] Delicious Jeon, Sikhye and
  Braised Short Ribs descriptions (1000347 to 1000349) read `Contribution EXP
  +1,000`, the rendered text exactly, for a stored `1000`. The Skill EXP item
  reads only `Skill EXP` in game; its buff 47499 stores `27500000`.
- **48** set effect points: a set piece applies a type 48 buff that adds
  `param_2` points to the set skill of `param_1`, and each level of that skill
  holds one tier of set effects. Combined Magic Crystal - Gervish (15662)
  applies 57863 (`56050`, `1`); skill 56050 level 1 is Weight Limit +75 LT,
  Movement Speed +1 and Critical Hit +1, the `2 crystal set effects` of its
  tooltip, and level 2 adds Combat EXP +5% and Skill EXP +3%, the 4-crystal
  lines. Korean names state the points (`세트 효과 2포인트`, "set effect 2
  points", stores `2`). 84 of the 123 skills have a LOC type 10 name; the
  rest show the skill number.
- **97** packages: the duration equals the one in all 267 item names that
  state one (`Value Pack (30 Days)` stores `43200`). A Value Pack applies three
  of them, kinds `1` (the pack), `4` (`Unlimited Customization`) and `5`
  (`Unlimited Use of Merv's Palette`), the last two worded as on its tooltip;
  the pack's other lines are other buffs. Named after their items: `0`
  Blessing of Kamasylve, `2` Shining Pearl Blessing, `7` Cliff's Skill Add-on
  Guide, `8` Armstrong's Skill Guide, `10` Book of Training - Combat, `12`
  Premium Value Pack, `13` Book of Training - Skill, `14` Artisan's Blessing,
  `15` Secret Book of Old Moon, `18` Viano's Guide to the Desert, `20`
  Millennial Wild Ginseng. Unlabelled: `9` (Premium Package III) and `19`
  (Manos life skill guide) have no item, `21` holds siege and honour family
  buffs with a buff ID in `param_3`, `22` is shared by Premium Value Pack Plus
  (`param_3` `1`) and Blessing of Cron Stones (`2`, which grants Cron Stone
  x300 via a daily Challenge), and `23` to `25` are guild skills.
- **111**: from the costume tooltips (`Cooking Time -2 sec`) and LOC, 30 of
  32 one-line texts match (`Alchemy Time -5 sec` on Eileen's Cheer, 48808,
  `250000`; `Cooking Time -0.3 sec` on `15000`). The misses are 48868, which
  reads `+5%` while its Korean name and value say `+10%`, and one prose text.
  The time scale is odd but holds on every English text; the Korean names
  that give percentages (`연금 시간 -11%`) do not follow any one scale.
- **25** `param_3`: 205 one-line life EXP texts name the life skill of
  `param_3` (`Hunting EXP +10%` on `2`, `Life EXP` on `15`), so the column
  now names it too instead of always `Life EXP`.

The batch of 2026-10-04 was checked the same way, mostly against item names
and bdocodex tooltips, since most of these buffs have no text:

- **103** worker contracts: `param_1` is the worker (LOC type 6) and
  `param_2` the town (LOC type 17); every one of the 535 buffs has both names.
  Item 64639 reads `Usage effect: Employment Contract: Goblin Worker` and
  `Affiliation: Calpheon City` on bdocodex, and its buff 64039 stores `7552`
  (Skilled Goblin Worker) and `77` (Calpheon City). `Giant Worker (Velia)`,
  the column's name, equals an item name on 393 of 533 buffs; the rest differ
  in wording (`Worker for QA: Time` against the LOC name `QA Worker: Time`,
  `Artisan Demibeast Worker` against `Demibeast Artisan Worker`).
- **16** remove buffs: `param_1` is a buff `group`. 50 of the 54 names that
  say `Group 44679 제거` ("remove group 44679") store that number (the four
  misses are one Enslar run shifted by one), 18 English texts read `Remove
  Group 44812`, and 331 of the 355 values are a group in this file; the others
  look like groups of other buff files (furniture, NPC buffs). Summon: Keeper
  Marg's removal buffs clear its own effects: 8974 removes group 521, which
  holds the movement speed buff 8972, 8975 group 2341 (the MP recovery 8973)
  and 19117 group 2300 (the `Marg's Rage` headline 19113). The bleed, poison
  and burn cures (`출혈 해제`, 51265 to 51267) store `param_2` `15`; groups
  2061 to 2063 hold over 200 levels each, so it is not a level cap.
- **72** storage expansions: 163 of 176 coupons name what the column writes
  (`Trent Stable +1 Expansion Coupon` stores town `126`, kind `1`, `1` slot).
  The misses are Byeot County and Moodle Village, which LOC type 17 calls
  `Nopsae's Byeot County` and `Nampo's Moodle Village`, one wharf filed under
  Dallae Pier, and `Change Velia Storage Slot Limit (4)`, which stores 8.
  Town `0` is every town (`모든 지역`, 19 buffs). `param_3` `1` marks the
  `- 30일` and `- 기간` ("period") variants, which have no item and no
  duration.
- **71** inventory slots: every item name matches (`Inventory +8 Expansion`
  stores `8`); `param_2` `1` is the time-limited variant as in type 72.
- **76**: the amount equals the one in 29 of the 31 item names that state
  one (`Guild Karma (1,500)`, `Reduce Karma -30,000`); the misses are test
  items (`Increase Guild Karma +100` stores 5000). Naval Fame Recovery Scroll
  (970072) reads `Naval Fame +100,000` on bdocodex and stores 100000.
  Hans' Contract (65838) reads `Raises Naval Fame by 2,500` on bdocodex,
  which its buff stores, while its Korean name says `+5000`.
- **17** learn skill: the Secret Books apply it with the skill in `param_1`
  (`Wizard/Witch Secret Book - Lightning Chain`, buff 58322, skill 827
  `Lightning Chain I`); 130 of 175 item names contain the skill name, the
  rest are renamed skills (`[Secret Book] Pilgrim's Steps V` teaches
  `Pilgrim's Blessing V`). The ten buffs with text all read `UNKNOWN`.
- **101**: bookshelves and their parchments. `param_1` is a knowledge theme
  (LOC type 9): Fleece Decorated Bookshelf (18517) reads `There is a chance
  you may obtain Knowledge` and `Furniture - Wardrobe (Gain Cooking
  Knowledge)` on bdocodex, and its buff 51509 stores theme 30010, `Cooking`,
  with the text `Get one piece of Cooking knowledge.` 125 of 186 parchment
  names (`Bookshelf with Knowledge on Officers of the Western Camp`, theme
  104 `Western Camp Officer`) contain the theme name; the rest reword it.
- **73** trade refresh: under `param_1` `1`, `param_2` is a trade manager
  (LOC type 6 `Bahar`, secondary label `<Trade Manager>`), named in Korean
  by town (`무역 Refresh : 벨리아`, "trade refresh: Velia"). Under `0`, a
  territory: the seven Trade Pass items 63001 to 63007 read `Restocks the
  trading items available for purchase in trading shops of Balenos`, then
  Serendia, Calpheon Territory, Mediah, Balenos Territories, Southwestern
  and Southeastern Calpheon. The Korean names give Balenos, Northern and
  Southern Serendia, Calpheon, Mediah and the same two Calpheon halves, so
  `2` to `4` disagree and stay unlabelled.
- **68** stat limits: the Breakthrough Crystals 15642 to 15648 apply
  59001 to 59007 (kinds `0` to `6`, `1` step) and read `Attack Speed Limit
  +1`, `Casting Speed Limit +1`, `Luck Limit +1` and `Gathering Limit +1` on
  bdocodex; the Movement Speed and Critical Hit crystals leave out "Limit",
  and the buff texts read `Costume - Attack Speed Limit Increased`. The
  `+2` buffs (59977 to 59983) belong to a QA earring.
- **19**, **47**, **51**, **62**, **100**, **134**, **196** and **200**: from
  their items, which I checked in game. Endless Ocean Draught (890074) lists
  `Sailor EXP +15%` (48934, `150000`), [Event] Giddy-up Ghost Horsie!
  (830271) `Mount Skill EXP +15%` and `Horse Capture Rate +15%` (47528 and
  47529), the Oceanbound Otter Fishing Rod (59455) `Prize Catch Fish Rate
  +3%` (48060, `30000`); the Skill Points (1) to (10) items store their
  count, the Character Slot Expansion Coupon `1`, Patrigio's Pocket Watch
  `61`. The type 134 texts match on all three that state one (`Swimming
  Speed +90%`).
- **131**: Token of Desert Trading 409 reads `Trade Goods Price Doubled` on
  bdocodex for `1000000`; 408 reads `Trade Item Price +50%` but stores
  `750000`, which its Korean name (`무역품 가격 상승(75%)`) gives.
- **84** and **168** store no amount and always read one text. Firecracker
  (Red) (219) applies 50425 and reads `Subjects within the range cannot
  hide their name` and `cannot conceal themselves`; I confirmed in game that
  it shows hidden names. The skill buffs read `Reveals hidden enemies and
  names` (Shai's Come Out, Come Out) and `Remove stealth, Reveal hidden
  names` (Archer's Shadebound Beam and Arrow Explosion). All 16 type 168
  buffs read `No Guard Gauge recovery` (Corsair's Flow: Raging Torrent and
  Mareca: Spiral Soak).
- Read but left as a dash: **83** crop growth (`param_2` `0` fertilizer,
  `1` water, `2` temperature; the windbreaks read `Crop Growth Buff:
  Temperature 15` in game while storing `150000` in `param_3`, and the
  waters named 15 store `350000`, so the amount scale is open), **125**
  idle training (Book of Training, `1000000` on all), **153** light
  radius (Light of Illezra, Atanis Firefly; `5` on all), **164** Central
  Market Silver Collection +5% (`param_1` `1` on Old Moon Trade Pass, "for
  one transaction", `-1` on Rich Merchant's Ring; the 5% is not stored),
  **179** the Elvia weapon blessings (`param_1` `153` Valtarra, `154`
  Okiara, `155` Narc) and **184** Satiated (no parameters).
- **186**: the Black Shrine (Boss Blitz) aura orbs. Sun Orb (66664) stores
  `param_3` `0` but reads `Moon's Aura Fixed Stat +1` on bdocodex, and Moon
  Orb (66665, `1`) reads `Sun's Aura`. The icons settle it: the Sun Orb is
  red, the Moon Orb blue and the Earth Orb green, the colours of the fixed
  orb in each aura of the Black Shrine window (Sun Aura red, Moon Aura blue,
  Earth Aura green), so `param_3` follows type 187 and the two tooltips are
  swapped. Light Orb (66667, `param_1` `0`) reads `Selected Aura Stat +1`
  and goes to the aura the player picks in that window.
- **56** (Amity) and **160** (speeds) match the numbers of every text that
  states one, 23 and 29 (`Attack/Casting Speed +10%` stores `100000` in
  `param_2` and `param_3`; the column writes each speed on its own).
- **66**, **106**, **107**, **112**, **121**, **126**, **169** and **181**
  have English text: 15 of 15, 19 of 69 (the other numbers agree on 67 of
  68 texts, which word monster buffs as `Monster - Damage -10% for 120 sec`),
  12 of 14, 18 of 18, 28 of 28, 17 of 18, 28 of 28 and 22 of 25 one-line
  texts match; the misses are `UNKNOWN` placeholders, prose and one stale
  `+2%`. 106 is the rate counterpart of type 43 (`모든 피해 감소율`, "all
  damage reduction rate") and writes `All Damage Reduction +5%`. Type 181
  kind `2` (Health, `건강`) has no English text but follows type 89. Type 107
  `param_2` `2` to `7` read only `Gathering Luck increases.` and stay
  unlabelled.
- **126** fish grades: fish are white, green, blue, yellow and red (prize
  fish), and the fish item descriptions name the middle three on a line of
  their own: the 104 that say `- Common Fish` are all green, the 46 `-
  High-quality Fish` all blue and the 86 `- Rare Fish` all yellow. The skills that apply the buffs name the kind in
  LOC type 10: kind `1` (`희귀`, "rare") on `Increase chance to catch a rare
  fish (5%)` (skills 53080 to 53090), kind `2` (`고급`, "high grade") on
  `Increase chance to catch a high-quality fish (5%)` (53069 to 53079 and
  53091 to 53094) and the older `Chance to Catch Large Fish +1%` (52301 to
  52305). The kind 2 buff texts read `Chance to Catch Rare Fish`, the
  stale side.

The batch of 2026-10-08 took the two largest types left. Neither has an
English text that states an amount.

- **176** test teleports: the 48 buffs (`A1 : VN_00` to `A1 : VN_53`,
  hidden, no text or icon) store `param_1` `17` and `param_3` `4001` to
  `4024`, each value on two buffs. The skills that apply them, 51001 to 51054
  (LOC type 10 `A1_001` to `A1_054`), read `A1 Teleport`; the second set,
  56901 to 56954, is named after the buffs and reads `A1`. Items A1_001 to
  A1_024 (720601 to 720624) apply buffs 54901 to 54924, which store 4001 to
  4024. [instancefield.dbss](instancefield_dbss.md) has keys 4001 to 4066,
  named `A1_001` to `A1_066`, so item, skill and field share one name.
  Items A1_031 to A1_054 apply the same 24 buffs again, and the second 24
  buffs (54931 to 54954) belong to skills only. The fields have no LOC name,
  so the column writes the internal one, `Teleport to Instance Field
  A1_001`, through the `INSTANCE_FIELD_NAME` lookup index, and the key
  without it. `A1` looks like Abyss One: the waypoint graph of field 4001
  (`mapdata_instancedungeon_4001explore.bwp`) names its points
  `road(magnus)_001` onwards, and the type 23 test buffs next to these read
  `A1 : 마그누스 내 A로 이동` ("A1: move to A inside Magnus").
- **180**, read but left as a dash: extra damage to one group of monsters.
  9 of the 41 Korean names say `프로퍼티스` ("properties"), some with a rate
  the buff does not store (`에다니아 수렵 프로퍼티스 300%`, "Edania hunting
  properties 300%"). `param_1` is the only parameter set, apart from
  `param_3` `-1000000` on 44186, and it follows the target of the English
  texts:

  | `param_1` | Buffs | Target in the English text |
  | --------- | ----- | -------------------------- |
  | 51 | 42107 | `Honglim Base bandits` |
  | 52 | 42187, 42197 | `certain monsters` (Orbita's Light) |
  | 57 | 44133 | `Edania Hunting Monsters` |
  | 59 | 44186, 46003 | `World Boss Muraka` |
  | 61 | 44191 | `certain monsters` (Flame of Arrogance II) |
  | 65 | 44203 | `Elion's followers` |
  | 67, 68, 69 | 46005, 46006, 46007 | `Aresion Temple`, `Scales of Judgment` and `Event Horizon monsters` |
  | 168 | 43538 | `Elvia Calpheon monsters` (Blessing of the Ancient Spirits) |
  | 169 | 43532, 51751 | `Elvia Calpheon monsters` (Essence of Living Hope, Corrupted Darkness) |
  | 189 | 41819 | `certain monsters` (Seculion's energy) |
  | 193, 194 | 41899, 41902 | `<Void Burned> Lava Tribe`; 194 is the Mareca version (`[마레카]`) |
  | 195 to 198 | 41909 to 41912 | `monsters that appear from the Fear of the Frost`, Rift, Ancients, Void (Limbo's Blessing) |

  That is 21 texts. The other 20 buffs have none that names a target: 53
  (Power of Azureach: Black Spirit), 55, 56 (Time of Sycraia), 58 (Altar of
  Blood Golden Pig King, `150%`), 63 (Monster Basher, `대괴수탄`, "giant
  monster shell"), 70 (Remnant of Markthanan's Authority, `150%`), 153 to 155
  (Blessing of Valtarra, Okiara and Narc, buffs 59493 to 59495: the
  Elvia weapons, orbs that drop from Elvia monsters and give a 10-minute
  weapon buff with a 20-minute cooldown; see the Elvia weapons table
  below), 164 to 167 (Gyfin Rhasia), 178
  (Bamboo Legion soul cleanse), 183, 185 and 199 (Essence and Rumblings of
  Ulukita), and 195 on Limbo's Blessing: Trial (47077). The two Essence of
  Ulukita keys are the two Ulukita hunting grounds of the Pearl Abyss wiki
  (wikiNo 350): in City of the Dead, CC on the Tehmelun Messenger at the
  right moment knocks the nearby monsters down and gives the player the
  buff "which will let you easily defeat the monsters"; in Tungrad Ruins,
  detonating a Tungrad Visionary gives it, and "all the surrounding monsters
  will be stunned and have their DP decreased". Which key is which zone is
  not confirmed: 183 is on buffs 41801, 41802 and 55283 (item 65333, skills
  42249, 42250 and 57081, all named Essence of Ulukita), 199 on 41914 (skill
  42334, no LOC name). The action charts of the Tehmelun Messenger (21016,
  `m0134_witch_03_normal.paac`) and the Tungrad Visionary (21011,
  `m0097_ancient_wizard_f_normal.paac`) hold none of the four skill numbers.
  The key is not a
  `dropuihuntinggroundinfo.bss` key: those run 0 to 119, and 51 is
  Sherekhan Necropolis (Day), 67 Orc Camp [Elvia], where the texts name
  Honglim Base (95) and Aresion Temple (117). It is not the characterstatic
  `unknown_p3` either (51 there is on Mask Owls, 67 on pirates). 193 and 194
  reach one target from two attackers, the player and Mareca, so the key
  looks like a property the bearer gains and the target monsters take extra
  damage from; the rate lives outside this file. Blessing of Crimsonflare,
  Everlight and Voidreach add `※ While this effect is active, buff effects
  targeting specific monsters will not activate`. Type 179 uses 153 to 155
  too (see the batch of 2026-10-04). See Open Questions.

  Elvia weapons, keys 153 to 155 of types 179 and 180. The zones are where
  Garmoth's Elvia Realm (Serendia) guide says each orb colour is "most
  useful"; while the buff is on, the player can use the Elvia skill, which
  gives the monsters -20 AP / DP:

  | `param_1` | Buff | Orb | Zones (Garmoth) |
  | --------- | ---- | --- | --------------- |
  | 153 | 59493 Blessing of Valtarra | Red | Bloody Monastery, Birgahi Den, Swamp Naga Habitat |
  | 154 | 59494 Blessing of Okiara | Blue | Castle Ruins, Orc Camp |
  | 155 | 59495 Blessing of Narc | Yellow | Swamp Fogan Habitat, Altar Imp Habitat |

  For these three keys the type 180 key stands for a set of hunting
  grounds, not one monster. The damage bonus is still not stored in the
  buff.

  Most of these buffs come from zone pickups, which is how most of the
  game's random zone events work. As far as I know: a monster drops a
  hidden item, picking it up uses it on the spot, and it either applies a
  buff or spawns something. Time of Sycraia (56343) is one. The Elvia orbs
  work the same way: the hidden item spawns the orb, and interacting with
  the orb (R, per Garmoth) gives the weapon buff. The orb characters look
  like Young Valtarra, Young Okiara and Young Narc (24890 to 24892, model
  `monster/hadum/elementalweapon_h_normal`); no item places them through
  `character_id`. Each colour has two buff items, a main weapon one
  (757395 to 757397, icons `mainweapon_fire`, `_water`, `_thunder`) and an
  awakening weapon one (757398 to 757400, `awakenweapon_*`), and both
  cast the same skill.

  The 16 items that apply type 180 buffs (the Elvia weapon items 757395
  to 757400, Time of Sycraia, Essence and Rumblings of Ulukita 65333 and
  65338, Dark Crimson Gem Fragment 980114, the Lingering Powers 980144 to
  980146, Corrupting Darkness 56506, Limbo's Blessing: Trial 56289 and
  Monster Basher 56084) carry no flag for being used on pickup in
  `itemenchant.dbss`: all but Monster Basher (a cannonball, `item_type` 6)
  are `item_type` 2, `category` 18, like 11,067 of the 13,275
  consumables, and none of the fixed bytes before `+0xF2` is shared by the
  15 and rare elsewhere. The flag is likely on the hidden drop, not on
  these buff items.

Type 142 renders as `Obtain Title: Back Home Again`, from LOC type 1; the
items that apply it read `Using this item will grant you the Olvium Frontia!
title` or `Effect: Obtain the ... title`. 53 titles have no LOC name and show
their ID. Type 37 renders as `Register Node: Bambu Valley - Mining`: LOC type
29 names a sub-node by its work alone (`Mining`), so the parent node is put in
front, found as the one node a sub-node links to in the worldmap graph (the
`NODE_PARENT` index, 465 sub-nodes on client 3458). Of the 1,022 buffs whose
node has a name, 804 equal the item's own `Node Registration:` name, and the
rest differ only in wording: the item says `Fish Drying Yard: Taramura Island
1` or the older `Altas Farm`, the worldmap `Taramura Island - Fish Drying Yard
1` and `Altas Farmland`. Nine nodes have no LOC name and show their key.

Type 23 renders as `Teleport to point 0/371, near Marni's Lab (12 m)`:
section and key of a [teleport.dbss](teleport_dbss.md) point, then the
nearest worldmap node and its distance (the `TELEPORT_NEAREST_NODE` lookup
index), as the points have no names. Without the index, or for a point
missing from the file, it shows `Teleport to point 0/340`. 652 of the 654 buffs name a point
that exists (section 0 travel items, section 5 boss rooms and unstuck moves);
the other two are town return stones on the empty sections 3 and 4. The
points land on the places the English texts name: `Footprints: Flower-sunken
Swamp`, `Mongryong's Exile` and `Martial God Tournament` lie within 1 m of
their worldmap node, `Holbon Entrance` 3 m. 574 of the 654 buffs are the only
buff at their point, so naming a point after its buffs would mostly repeat the
buff's own Applied By item; the nearest node adds where it is.

Type 38 renders as `Learn Knowledge: Tuntaros`. Its buffs have no text, icon
or duration and are all hidden; the items that apply them are quest rewards
used the moment they reach the inventory, described as `You can learn about
Tuntaros.` (item 66397, buff 39562, knowledge 11216). 5,651 of the 5,683
`param_1` values have a LOC type 34 name; the other 32 (four `개발용 지식`
developer entries, old Altar of Blood illusions such as 15074) show the ID.

Type 18 renders as `Summon Incarnation of Corruption` (buff 48806, item
970013), with the ID when LOC has no name. 2,127 of the 2,199 distinct
`param_1` values have a LOC type 6 character name, against 39% of random IDs
in the same range, and the Korean buff names match them (`암석의 거상 소환` is
Rock Golem 28254, `제단 임프 전사` is Altar Imp Warrior 20067). The event
gimmicks show the character's name plate rather than the buff text:
`[Event] Summon Satto Gimmick` summons `Mayor` (사또, a magistrate). Buffs
40871 to 40876 read `Summon Young Kamasylve` but are named `눈사람 소환 :
벨리아` ("summon snowman: Velia") and summon Baby Snowman 37223, so the English
text is the stale side. 68 buffs on 22912 (Suspicious Broom) are placeholder
slots, named `사용 불가능한 인덱스` ("unusable index") or `UNKNOWN`.

The other type 18 parameters are open:

- `param_2` (0 to 6) groups summons: `0` monster and skill summons, `1`
  event, season and invasion spawns, `2` bosses and event gimmicks, `3` siege
  objects (Hwacha, siege towers, fences), `4` boss scrolls and guild hunts,
  `5` and `6` one buff each.
- `param_3` looks like the action the summon performs. The Wizard's keepers
  show it best: Keeper Marg (60143) uses `0` for Flow: Fire Breath Marg (buff
  9015), `1` for Flow: Fire Fist Marg (9016, the Hellfire follow-up), `2`
  for the Bolide of Destruction add-on (19125), `3` for the enhanced Hellfire
  (9017) and `4` for the Cataclysm add-on (19121); Keeper Arne (60142) runs
  `0` to `4` the same way. Buffs 41456 to 41475, named `가넬 궁수
  소환(인덱스 1)` to `(인덱스 20)` ("Ganelle Archer summon, index 1 to 20"),
  store 1 to 20, but the world raid fragments 40723 to 40726 (`인덱스1` to
  `4`) store 0 to 2.
- `param_4` looks like a facing angle: `180` on 432 buffs, then `90`, `-90`,
  `-180`, `±135`, `±40`. Group boss scrolls do not show it: Cartian Spell
  (41587) applies 54156, which summons Mediah Ancient Relic Crystal (23053,
  `param_4` `180`), a floating object that then spawns three bosses in front
  of itself, so the bosses do not come from a buff. Solo boss scrolls spawn
  the boss directly and are the test case still to do.
- `param_6` is `1000000` on 429 buffs, mostly damage summons named
  `피해 : ...` ("damage: ..."); maybe a per-million damage scale.
- [Altar of Blood] Flame Tower (761902) spawns a flame tower in the Altar of
  Blood minigame, but its buff 48677 (`피의 제단 화염탑 소환`, "Altar of Blood
  flame tower summon") points at 26701, `Ahib Salun Wolf Spearmaiden`, whose
  model is `infinitydefence/monster/4/m0004_defence_knightwolf`, one of the
  defence-mode monsters at 26829 to 26879. The tower comes from somewhere
  else, or the item was repointed without its buff; see In-Game Checks.

The Wizard's Summon: Keeper Marg skill (2250) shows how a skill splits one
tooltip over several buffs, all lasting 60 min:

| buff_id | effect_type | Parameters                    | Role                                              |
| ------- | ----------- | ----------------------------- | ------------------------------------------------- |
| 19113   | 34          | none                          | Headline with the text: `Marg's Rage`, Movement Speed +10%, Recover 250 MP per tick |
| 8972    | 9           | `param_1` `100000`            | The Movement Speed +10% itself                    |
| 8973    | 4           | `param_1` `250`, `tick_ms` `10000` | The MP recovery: 250 every 10 sec            |
| 8999    | 18          | `param_1` `60136`             | Summons Keeper Marg                               |
| 8974, 8975, 19117 | 16 | `param_1` `521`, `2341`, `2300` | Remove the groups of 8972, 8973 and 19113, the previous summon's effects |

Summon: Keeper Arne (2246) shares 8972 to 8975 and has its own 19114
(`Arne's Touch`), 8998 and 19118. The in-game skill tooltip reads `Marg's
attack damage 579%`, `Recover 250 MP every 10 sec` and `Stiffness on Marg's
special attack hits`. The damage is type 45 in the `Marg Effect` skill
(10072): 8992 basic attack `param_4` `5790000` (579%), 8993 special attack
`8220000`, 9004 Fire Fist `23800000`, each with a lower PvP twin (8990
basic PvP `5430000`). The stiffness is type 14 buff 850 (`[액션제한] 경직`,
"action limit: stiffness", `param_1` `6`, `param_2` `1350`). Every keeper
damage buff stores type 45 `param_1` `2`, which fits the attack-type reading
(`0` melee, `1` ranged, `2` magic; cannon shots store `1`); the Wizard is a
magic class.

Types 45 and 4 were checked further on bdocodex. Summon: Keeper Arne (skill
2246) reads `Arne's attack damage 579%` (buff 8986, `5790000`) and `Recover
250 MP every 10 sec` (8973). Against buildings and vehicles, Cannonball's
buff 1988 stores 400% and [Guild] Cannonball's 15709 stores 310%, the
`around 30% more damage` the Cannonball (56003) tooltip claims. In LOC, 87
monster and test skills state a damage percentage equal to `param_4`; the 13
misses are descriptions copied between skills, while the skill names still
match (`Samsin: Final Damage 200%` stores 200%). The skill tooltip itself is
a LOC type 46 template (`Marg's attack damage {p0}%`), filled from data.
Player attacks do not use type 45.

Type 4 renders as `Recover 250 MP/WP/SP every 10 sec`, `MP/WP/SP -50 every 5
sec` or, under `condition_type` `1`, `Recover 9 MP/WP/SP on Hits`
(Immortal: Perfume of Spirits, 1166, whose buff 56897 has no English text).
The 174 type 4 buffs without a tick or a condition are one-off refills that
serve players and mounts alike: High-quality Carrot (54004) stores 3000 for a
horse's stamina, MP Potion (Beginner) (503) 50 for the player's MP, so they
show a dash. Short buffs are worded both ways in the game, `every 1 sec` (14
buffs) and `5 times over 5 sec` (42), with nothing in the record to tell them
apart; the column always uses `every`.

Type 1 is the HP counterpart: `Recover 25 HP every 1 sec`, `HP -200 every 1
sec`, or one of the trigger lines below. On the 77 ticking texts that state
numbers, 72 match both the amount and the interval; the misses are 65209
(the stale "every 3 sec") and four `1,000,000 burn damage` placeholders. The
game names ticking damage by kind (`200 poison damage every 2 sec for 10
sec`), and only the icon tells the kinds apart. `dot_poison.dds` (294 texts
say poison), `dot_burns.dds` (229 burn) and `dot_pains.dds` (211 pain) agree
with their text on all but one or two buffs each, so the column names those
kinds and adds the duration as `for N sec` (it equals the stated one on 35 of
36 texts). `dot_bleeding.dds` does not: 201 of its texts say burn and 9
bleed, so those buffs read `HP -200 every 1 sec`. 80 of the 151 one-line
texts match exactly; most of the rest name an effect without numbers
(`Poisonous`, `Syca's Chance`).

[bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor/blob/HEAD/FORMATS.md) agrees on 29, 50, 57, 63, 67, 79, 89, 90 and 95. It gives 149 as life-skill mastery with `param_1` the life skill, and reads `15` as "all life skills", which the LOC text bears out.

Type 69 renders as `Accept Quest: [Co-op] Eliminating the Threats to
Mediah`, with `chain/quest` when LOC has no title. Cartian Spell (41587)
applies buff 57217 (`244`, `1`, Korean `메디아 주술서 보스 3종 처치 의뢰`, "Mediah
spellbook, defeat three bosses quest"), and its tooltip says `[Co-op]
Eliminating the Threats to Mediah will automatically be accepted when this
summon scroll is used`; quest 244/1 has exactly that title. 610 of the 670
buffs name a quest. That alone proves little, since a random quest number
of the same chain also has a title 68% of the time, but the Korean names
follow the quest numbers: the Black Spirit's special alchemy quests 9501/4
and 9501/7 are Clear Liquid Reagent in both, 9501/3 and 9501/6 Clown's
Blood. The 176 field gimmick buffs on chain 15000 all reach the same title,
`Catch a large rabbit.`, and the 60 misses are mostly chain 11485 (`그믐달
실습서`, "new moon practice book" per life skill).

### Display buffs (types 34 and 58)

Types 34 and 58 carry a consumable's or skill's title, tooltip text and icon,
and do nothing themselves; the other buffs of the same skill hold the effects.
`[Event] It's Boba Time Drink` (skill 57057) applies headline 55251 (type 58,
all parameters `0`, text `Extra AP Against Monsters +15, Combat EXP +...`)
and seven effect buffs of types 136, 29, 25, 1, 67, 25 and 120; Summon:
Keeper Marg's `Marg's Rage` (19113) is the type 34 headline of its skill. 1,095
of the 1,132 type 58 and 228 of the 287 type 34 buffs store no parameter.
Even region bonuses such as `Item Drop Rate +8% upon defeating monsters at
Sherekhan Necropolis (Night)` (62639) are type 58 with all parameters `0`, so
their effect is applied outside this table. The Effect column shows a dash.

The type 58 buffs that set `param_1` look like vision range: Sea Bugle
(58799) and the Ancient Magic Crystal vision effect (50088) store `10` and
read `Vision Range +10m`, Hunter's Clothes (52022, Korean `탐험가 의복`,
"explorer's clothes") store `500`, and two GM and test buffs `1000`. Seven
`아이템 획득 증가 이펙트` ("item drop increase visual effect") buffs also store
`10` with no vision text, so the field and its unit stay open. The tooltips do
not settle it. `Vision Range` is the old name of Discovery Radius (type 53,
see Effect text), and the Ancient Magic Crystal of Enchantment - Vision
(15623) reads `Discovery Radius +10m` on bdocodex while its skill (50268)
applies only 50088 (type 58, `10`) and All Evasion +12, no type 53 buff. Sea
Bugle's skill likewise applies only its type 58 `10`. So `param_1` may be the
same radius in metres, which type 53 stores in centimetres. Against that, the
Korean names keep two terms apart (type 53 `탐험 발견 거리`, "exploration
discovery distance"; type 58 `시야 거리`, "sight distance"), Hunter's Clothes
apply both (type 53 `1000` and type 58 `500`) while listing only `Discovery
Radius +10m`, and the drop-rate scroll companions store `10` too. The column
shows a dash until one reading holds for all of them. No in-game check is
left: the Ancient vision crystal can no longer be obtained, and Sea Bugle is
not an item a player keeps, so neither can be looked at in the character
window.

### `condition_type` (stats block `+0x06`)

The trigger of a type 1 or type 4 buff, confirmed against the English text of
its buffs (counts are type 1 buffs):

| Value | Buffs | Trigger | Text |
| ----- | ----: | ------- | ---- |
| 0     | 1,524 | None: per tick (`tick_ms`) or one-off | |
| 1     | 34    | On hits | `Recover 9 HP on Hits`; type 4 `Recover 9 MP/WP/SP on Hits` |
| 3     | 28    | When struck, healing | `Recover 250 HP when struck` (no buff text; Infinite Fortitude 2805 and Purga: Sanguine Heart 9837 on bdocodex, buffs 12647 and 12648) |
| 4     | 6     | When struck | `Retaliate 15 Fixed Damage when struck` |
| 6     | 19    | On back attack hits | `Deal 15 Fixed Damage on Back Attack Hits` |
| 9     | 16    | On critical hits, healing | `Recover 15 HP on Critical Hits` |
| 10    | 34    | On critical hits, damage | `Deal 30 Fixed Damage on Critical Hits` |

Type 4 uses `8` for "when struck" instead of `3`: Fury of the Beast (354)
reads `Recover 5 WP each time when struck` on bdocodex, and its buff 80
stores `5` under `8`. `2` (one buff, 50046, `HP -100`, Ancient Magic Crystal
- Temptation on the target) and `5` (12 buffs, the "To_Self" effects of
crystals and Giant's Belt, types 29 and 67) are open; their skills have no
tooltip on bdocodex (see Open Questions). Fixed damage is stored negative and written as a
positive amount.

### Stacking (`stacking_category`, `is_exclusive`, `group`, `buff_level`)

Two mechanisms decide which buffs replace each other:

- **Category.** `stacking_category` (tail `+0x18`) is the item type the
  tooltips name (`※ Type: Draught`, `※ Type: Perfume`). A buff with
  `is_exclusive` (tail `+0x19`) ends every active buff of its category, so
  only the last item of that type used applies. Buffs without the flag
  leave their category alone.
- **Group.** Buffs of one `group` are one slot, ranked by `buff_level`; no
  two buffs share a group and a level. Adventurer's Luck I to V (57484 to
  57488) are group 6382 at levels 1 to 5, and their scrolls read `Lower
  Adventurer's Luck cannot be applied while the higher effect is active`.

Exclusive families do not need shared groups, since the category already
replaces the whole set; the families without the flag do. That is why the
18 food Max HP buffs share group `5616` (ordinary food, category 1, not
exclusive) while each Adventure's Boon buff has its own (category 38, all
exclusive). On client 3458, 119 of the 193 groups of non-exclusive
categorised buffs hold more than one buff, against 36 of the 1,989
exclusive ones (Perfume of Courage and its Immortal and event versions).

Checked against the `※` lines of the English item descriptions (LOC type
0), joined to the buffs through `BUFF_ITEMS`:

- 155 items read `Only the effects of the last draught / perfume /
  high-quality food / Golden Pig's Blessing ... used will be applied`. All
  149 that apply buffs apply exclusive buffs of one category (72 draughts,
  41 perfumes, 19 foods, 7 Golden Pig's Blessings, 5 each of the Glorious
  Combat and Life Scrolls), plus category `0` buffs on the foods.
- The 17 residence scrolls that read `Only the most recently applied scroll
  or furniture buff will take effect` are all category 35, exclusive.
- The Item Collection Increase scrolls (`Effects of same item types cannot
  be stacked`) are category `0` or `8`, not exclusive; their limit comes
  from groups.

Draughts and elixirs share category 2. Every draught buff is exclusive (344
buffs), as are the item-less `최상위 비약` ("top-tier elixir") draught
buffs and the GM buffs; the 247 ordinary elixir buffs are not, and stack
with each other except within a group: Elixir of Human Hunt (level 2),
[Mix] Manhunt-Rage Elixir (3) and Elixir of Perfect Human Hunt (4) share
groups 5647 and 8939. A draught therefore ends every active elixir and
draught, which is the tooltip's `Draught effects do not stack with other
elixir/draught effects`. Perfumes (6) and the whale tendon elixirs (21)
have their own categories, which is the tooltip's exception list.

Two effect-less buffs exist only to end a category. Harmony Draught keeps
its last six effects (Critical Hit +5, the fixed damage and HP on hit
lines, All Special Attack Extra Damage +18%) in category 26, apart from the
category 2 ones. Every other draught applies 47321 (`영약 추가 효과
초기화`, "draught bonus effect reset", type 58, no parameters, 20 min,
exclusive in 26), so it ends those six as well. The 62 items that apply it
are the 61 draughts without Harmony effects and Overflowing Earth Energy
(42242), which applies draught buffs too; Glorious Giant's Draught applies
no skill. Food does the same: 55793 (`서브 음식 효과`, "sub food effect", 1
sec) is exclusive in category 10, the second effects of high-quality food,
and the 7 high-quality foods that apply it have no category 10 effect of
their own. bdo-data-extractor calls 26 a single
draught-reset record; that is 47321, and the other 81 buffs of 26 are the
Harmony effects.

An ordinary elixir does not end an active draught, as the flag predicts;
I checked it in game on 2026-10-06: Elixir of Mastery (1155) drunk after
Beast's Draught left the draught's buffs in place. The tooltip's `do not
stack` line only holds in one direction: a draught ends elixirs, an elixir
leaves a draught alone. Whether an equal level replaces a buff of the same
group is in In-Game Checks.

| Value | Buffs | Exclusive | Item type |
| ----- | ----: | --------- | --------- |
| 0     | 41,892 | never    | None; buffs stack, limited only by group |
| 1     | 428   | 88        | Food; the exclusive ones are high-quality food (`최상위 음식`), ordinary food stacks |
| 2     | 647   | 400       | Elixir (not exclusive) and draught (exclusive) |
| 3     | 131   | all       | Villa, camp and scroll body buffs (`[Villa] Body Enhancement`) |
| 6     | 118   | all       | Perfume |
| 7     | 64    | none      | Event consumables (clovers, lollipops) |
| 8     | 14    | none      | Item Collection Increase scrolls |
| 9     | 16    | 2         | Damage reducers and AP enhancers |
| 10    | 39    | all       | High-quality food second effects, and the 55793 reset |
| 14    | 8     | all       | Golden Pig's Blessing |
| 21    | 4     | all       | Whale tendon elixirs, plus `[Event] Sweet Pumpkin Pie`, which gives the same buff in game |
| 24, 25 | 10, 12 | all     | Glorious Combat Scroll, Glorious Life Scroll |
| 26    | 82    | all       | Harmony Draught bonus effects, and the 47321 reset |
| 35    | 515   | all       | Event items and residence furniture scrolls (822 items) |
| 36, 37 | 6, 2 | all       | [Fame] Combat EXP and Skill EXP scrolls |
| 38    | 18    | all       | Adventure's Boon |

The other values each hold one item family, all exclusive: GM's Blessing
(12, 13), the event bundles (18, 19, 22, 27, 209 to 212), the Korean
holiday feasts (28 to 32), Token of Desert Trading (20), test and
development items (233 to 250, 252). 248 to 251 are not exclusive.

## Suggested UI Layout

| Column      | Type | Notes                                                               |
| ----------- | ---- | ------------------------------------------------------------------- |
| Buff ID     | num  | `buff_id`; right-aligned                                            |
| Icon        | text | `icon_path`, resolved under `ui_texture/icon/`; dash when empty     |
| Title       | text | Coloured first line of the description when more lines follow; else the title of the headline buff it is applied with, dimmed (see Notes); dash otherwise |
| Internal Name | text | Korean `name`; labelled internal because LOC has no form of it in any language. Kept as its own column next to Title by choice (2026-10-04): it is the only text on many untitled buffs |
| Description | text | LOC `str_type=5`, `str_id1=buff_id`; falls back to the inline Korean description, `<null>` counts as empty |
| Effect      | text | The parameters as text for the confirmed effect types (see Effect text); dash otherwise |
| Applied By  | list | Base items whose skills apply the buff (`BUFF_ITEMS` lookup index), with item icons and grade colours; sorts by count |
| Level       | num  | `buff_level`                                                        |
| Effect Type | num  | `effect_type`                                                       |
| Duration    | text | `duration_ms` formatted as h/min/s; dash when `0`, stored as `None` so it sorts last                   |
| Param 1     | num  | `param_1`, then what it means for the effect type where confirmed: `3 (Kamasylvian Monsters)`, `25000 (2.5%)`, `10 (Monster AP)`, `250 (every 10 sec)`. Labels over 24 characters (character and quest names) are cut, in full on hover. Sorts by the raw value |
| Param 2     | num  | `param_2`, labelled the same way                                    |
| Param 3     | num  | `param_3`, labelled the same way                                    |

## Notes

- Client 3464 widened `buff_id` from u16 to u32 in this file, in
  `buffoffset.dbss` (10-byte rows to 12), in `buffsimply.bss` (30-byte rows
  to 32) and in the `skill.dbss` buff slots. The other fields kept their
  layout. The five new buffs above 65,535 are the effects of
  `아그리스의 축복 주문서` ("Agris blessing scroll", one hour each):
  700000 Combat EXP +300%, 1000000 item drop rate +30%, 10000000 monster
  damage reduction +10, 100000000 death penalty resistance +5% and
  4100000000 Max Weight +100 LT. Their IDs are round numbers far above the
  old 65,528 maximum.
- `icon_path` is set in 15,272 records over 1,017 distinct paths. 221 of those
  hold the literal placeholder `UNKNOWN`, a few use backslash separators and
  three double a separator (`04_PC_Skill//04_Debuff`). Resolve by
  lowercasing, normalizing `\` to `/`, collapsing repeated `/` and prefixing
  `ui_texture/icon/`, e.g. `ui_texture/icon/new_icon/04_pc_skill/03_buff/huntingbuff.dds`.
- `is_shown` looks like a "visible in the buff bar" flag: 11,882 of its 12,746
  set rows have both an icon and a description, against 312 of the 31,863
  clear rows.
- The buff name has no English form anywhere in LOC. Of 13,658 names with at
  least two numbers, the best match under any type and sub-field keyed by
  `buff_id` is 48 of 3,522 in type 10, which is chance. Names are internal
  labels such as `테스트용 토레스 일꾼` (test Torres worker); the game shows
  players only the description.
- The inline Korean description matches LOC type 5 by content; numbers agree
  in every checked row apart from thousands separators.
- LOC type 10 was once assumed to be buff text keyed by `buff_id`. It is not:
  only half of the IDs overlap and the text disagrees (see the LOC doc).
- `group` is not a LOC key: 8827 resolves to an unrelated item in type 0 and
  a skill in type 10. Some families share one value: the 18 food Max HP buffs
  (+100 to +300) all use `5616`. Others do not: each buff of Adventure's Boon
  has its own (9056 to 9061 below), and the same effect in the 60 and 300
  minute variants uses 9050 and 9062, since its exclusive category already
  replaces them (see Stacking). `+0x00` to `+0x07` used to be read as
  two u32 fields; bytes `+0x02` and `+0x03` are zero in every record.
- `group` is a u16. Its keys run from `1` to `22100` and from `40001` to
  `60016`; the upper range holds 411 keys on 1,181 rows. Earlier versions of
  the parser read it as an i16, which turned those into negative numbers.
- No two buffs share a `group` and a `buff_level`: the 16,410 grouped buffs
  form 16,410 distinct pairs in the fixture, and 16,414 of 16,414 in the
  2026-09-27 client. Within a group the level orders the variants by
  strength, then duration: the 18 food Max HP buffs of group `5616` run from
  level 1 (+30, 30 min) to 12 (+100, 120 min), 13 to 16 (+150) and 17 to 18
  (+300 event foods). 1,082 buffs with no group also have a level above 1.
- One buff record holds one effect, so a consumable with several effects
  applies a run of consecutive buffs. Only the first carries the description
  and `is_shown`, and its description opens with the display title. The icon
  can repeat on the others: all six below store `SilverBless.dds`.
  Example: item 761880, `[Blessing] Adventure's Boon (120 min)` (LOC type 0),
  applies buffs 48723 to 48728:

  | buff_id | Effect                   | effect_type | param_1  | param_2 |
  | ------- | ------------------------ | ----------- | -------- | ------- |
  | 48723   | All AP +8                | 39          | 3        | 8       |
  | 48724   | All Accuracy +8          | 40          | 3        | 8       |
  | 48725   | All Damage Reduction +8  | 43          | 3        | 8       |
  | 48726   | Max HP +150              | 2           | 150      | 0       |
  | 48727   | Combat EXP +30%          | 25          | 300000   | 0       |
  | 48728   | Skill EXP +30%           | 25          | 300000   | 1       |

  The 60 and 300 minute variants sit either side, at 48717 and 48729.
- Only headline buffs have a display name, and it is not a field: their
  description opens with it on a coloured line of its own
  (`<PAColor0xffe9bd23>[Blessing] Adventure's Boon<PAOldColor>`), then the
  effects. Against LOC type 5 the buffs split as follows:

  | Type 5 text                          | Buffs  | First line                                  |
  | ------------------------------------ | ------ | ------------------------------------------- |
  | None or `<null>`                     | 30,488 | Nothing; hidden and group-member buffs      |
  | One line                             | 11,846 | The effect itself, e.g. `Mount EXP +3%`     |
  | Coloured first line, then effects    | 2,038  | The title; 2,020 of these have `is_shown`   |
  | Several lines, no colour             | 237    | Sometimes a title, sometimes an effect list |

  421 titles equal an item name once its `(120 min)`-style suffix is dropped.
  A few are flavour lines rather than names
  (`Time in Sycraia surges forward.`). The inline Korean description uses the
  same convention, so the title survives when LOC is not loaded. It writes
  each line break as the two characters `\n` (6,580 in 2,264 descriptions
  on client 3458, where LOC has real newlines); the parser decodes them
  (`_common/inline_text.py`), or the title would not split off.
- The parameters are the only reliable effect value; the name and the
  description can each be stale. Of 11,766 buffs whose name and description
  both hold numbers, about 500 disagree beyond a change of scale, and either
  side can be the outdated one:

  | buff_id | Name              | Description | Applied parameter | Matches     |
  | ------- | ----------------- | ----------- | ----------------- | ----------- |
  | 48866   | Life EXP +15%     | +3%         | `150000` (15%)    | name        |
  | 48321   | All Evasion -6    | -8          | `-6`              | name        |
  | 48661   | HP Regen +75      | +50         | `50`              | description |
  | 48766   | Olvia pass (2594.61) | Trade EXP +53630 | `129731`  | neither     |

  The inline Korean description and LOC type 5 always agree with each other,
  so this is drift in the game data, not a parsing or translation error.
- Item IDs do not appear in this file: 761880 is not stored anywhere in it as
  a u32 or i64. The item-to-buff link runs through a skill: the item's
  `itemenchant.dbss` skill keys name [`skill.dbss`](skill_dbss.md) records,
  whose `buff_ids` are the buffs (item 761880 -> skill 47683 -> buffs 48723
  to 48728). On client 3458, 15,091 base items name a skill and 14,471 buffs
  are applied by at least one item; one buff is applied by 270 items.
- The headline buff is not always first in its skill's `buff_ids`, and some
  skills apply several headline buffs. The browser gives an untitled buff the
  title of the headline buffs of every skill that applies it, but only when
  they all share one title (the lowest buff ID is the source). A buff reached
  by two titles keeps none, e.g. 59496 (`Blessing of the Elvia Spirits` and
  `Reminiscence of the Elvia Spirits`). On client 3458 that titles 2,488 more
  buffs and leaves 396 ambiguous. The record keeps the source in
  `title_buff_id`.
- `tick_ms` (stats `+0x6C`) is the tick interval of a periodic effect. It
  equals the stated interval on 105 of 112 English texts and 104 of 108
  Korean descriptions with "every N sec" (`N초마다`), including the keeper
  MP recovery 8973 (`10000`, "Recover 250 MP every 10 sec" in game). Most
  misses are headline buffs of type 34 or 58 that store `0` because a
  component buff carries the tick; the rest are drift such as 65209 ("every
  3 sec", `2000`) and 18056 ("every 1 sec", `3000`).

## Open Questions

### What does `unknown_str` hold?

A short UTF-16 string of digits (`"0"`, `"90"`, `"158"`), and occasionally `*`.
It could be a group or stacking key stored as text, but no table has been
matched against it.

### What do the ten parameters mean per effect type?

`param_1` through `param_10` change meaning with `effect_type`. The types in
Enum Values are confirmed; the rest have not been worked out. For 39, 40, 41
and 43 `param_1` is `3`; bdo-data-extractor reads it as the target (`0` melee,
`1` ranged, `2` magic, `3` all).

### What names the type 180 property keys?

`param_1` of type 180 (and 153 to 155 of type 179) picks the monsters a buff
deals extra damage to (see Effect text), but no client table read so far
names the keys or holds the damage rate (`150%`, `300%` in the Korean
names). The bdocodex item pages of Dark Crimson Gem Fragment (980114, buff
46003) and Essence of Ulukita (65333, buff 55283) show only the effect name
(`World Boss Muraka Properties`, `Essence of Ulukita`), no rate or target
(checked 2026-10-08).

The keys look like hunting ground property IDs: every target named so far
is a zone or its monsters (the Elvia weapon zones, the two Ulukita zones,
Aresion Temple, Scales of Judgment, Event Horizon, Elvia Calpheon, Honglim
Base), and six Korean names say `사냥터` ("hunting ground"), such as `아알
사냥터 프로퍼티스` ("Aal hunting ground properties") and `엘리언 영역
사냥터 프로퍼티스` ("Elion's realm hunting ground properties"). 56, Time of
Sycraia, would then be Sycraia Underwater Ruins. They are not
`regiongroupinfo.bss` keys either: 153 is Valtarra Mountains there, but 155
is Tooth Fairy Forest and 199 Pit of the Undying. A client file that lists
these numbers next to zones or character IDs would settle it; otherwise
they are server data and the column keeps the dash.

### What is type 176 `param_1`?

It is `17` on all 48 buffs. `instancefield.dbss` key 17 is `CrimsonField`,
which does not fit test teleports into the `A1_` fields, so it is probably a
teleport kind or mode. A second value on any buff would show what it does.

### What do `condition_type` 2 and 5 mean?

`2` is on one buff, 50046 (`HP -100` on the target), from Ancient Magic
Crystal - Temptation (15504). `5` is on 12 `(Self)` buffs, among them 50048,
50042 and 50039 from the Agony, Destruction and Enchantment crystals (15505,
15503, 15502) and the Giant's Belt `To_Self` buffs 50294, 50296 and 50299
(skill [Giant's Belt_Lv. 1](https://bdocodex.com/us/skill/50112/)), which no
item in `itemenchant.dbss` casts. bdocodex lists only the crystals' transfuse
stats, not the triggered effects. LOC ties each crystal to a weapon of the
same name and a skill used with it (`Only available by using a Temptation
skill with a Temptation weapon`). The crystals cannot be checked in game:
[Grumpy Green's crystal list](https://grumpygreen.cricket/crystal-npc/) names
Magic Crystal - Temptation, Destruction, Agony and Enchantment among the
crystals deleted on 2024-01-31. A Giant's Belt tooltip or a skill text that
names the trigger would settle `5`.

### Is `buff_level` a level or a category?

bdo-data-extractor splits `+0x00` into `i16 Category`, `u8 CategoryLevel` and
`u8 Level`. The two bytes are zero in every record here, the i16 counts up
on staged buffs such as boss stages, and it ranks the buffs of one `group`
(see Notes), so it is kept as `buff_level` until the client names it.

## In-Game Checks

### Altar of Blood Flame Tower Name Plate

Needs item: [[Altar of Blood] Flame Tower](https://bdocodex.com/us/item/761902/)

Needs zone: Altar of Blood

The item's buff 48677 points at character 26701, `Ahib Salun Wolf
Spearmaiden`, a defence-mode wolf knight model (see Notes). Use the item in
the Altar of Blood and read the spawned tower's name plate. `Ahib Salun Wolf
Spearmaiden` means the buff does spawn 26701 and the tower look comes from
elsewhere; a Flame Tower name means the tower is another character and the
item was repointed without its buff.

### Equal Buff Level in a Group

Needs item: [[Scroll] Adventurer's Luck I](https://bdocodex.com/us/item/761895/)

A higher `buff_level` blocks a lower one in its `group` (see Stacking), but
whether the same level refreshes or replaces the active buff is not known.
Use the scroll, wait a minute, then use a second one and read the buff's
remaining time. A full duration again means an equal level replaces or
refreshes the active buff; an error message or an unchanged timer with the
scroll kept means an equal level is blocked like a lower one.
