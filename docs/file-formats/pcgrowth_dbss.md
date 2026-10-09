# `pcgrowth.dbss` Format

## Purpose

The class selection record of every class type: the player character key of the class, its gender, the beginner weapons of the class, the main, sub and awakening weapon of the class, the Korean name and description, and the class selection video. Despite the name, the file holds no per-level stat growth; nothing in it is indexed by character level. `pcgrowthoffset.dbss` lists where each record sits, [pcgrowthsimply](pcgrowthsimply_bss.md) is a fixed-row list of the same class types with a playable flag, and [pcgrowthdefaultcharacterkey](pcgrowthdefaultcharacterkey_bss.md) stores one character key.

Example (client 3464):

```text
class type 0   Warrior      character 1   male    starter: Rusty Longsword, Round Shield
               class weapons: Rusty Longsword, Round Shield, Mercenary's Steel Greatsword
               video: UI_Customize/Movie/Movie_ClassSelect/PHM.webm
class type 4   Ranger       character 2   female  starter: items 10201, 10301
class type 25  Kunoichi     character 26  female  starter: Rusty Shortsword, Old Kunai, Old Shuriken
class type 14  Ain (No Use) character 16  male    not playable, no video
```

The class type is the number `getClassType()` returns and the bit of a class mask (`_common/class_type.py`); the character key is the player prototype in `characterstatic.dbss` and LOC type 6. They differ for most classes: Ranger is class type 4 and character 2, Sorceress class type 8 and character 3.

## Companion Files

| File                              | Required | Role                                                        |
| --------------------------------- | -------- | ----------------------------------------------------------- |
| `pcgrowthoffset.dbss`             | Required | `class_type -> (offset, size)` of every record              |
| `pcgrowthsimply.bss`              | Optional | Playable flag per class type, see [pcgrowthsimply](pcgrowthsimply_bss.md) |
| `languagedata_en.loc`             | Optional | Class name and description (type 21), item names (type 0)   |

All multi-byte values are little-endian.

## File Layout

| Offset  | Type  | Field   | Notes                                                                       |
| ------- | ----- | ------- | --------------------------------------------------------------------------- |
| `+0x00` | u32   | count   | Number of records; `47` on client 3464, class types `0` to `46`             |
| `+0x04` | row[] | records | `count` variable-length records, each after a u8 copy of its class type     |

Each record is the u8 class type followed by the record body. The offset table points at the body, one byte past the copy, and its size covers the body only, so the next copy sits at `data_offset + data_size`. The last body ends at the end of the file (55,280 bytes on client 3464).

## Record Structure

### Class Record (variable length)

Offsets count from `data_offset`. `n` is `starter_count`.

| Offset           | Type                 | Field            | Notes                                                                                   |
| ---------------- | -------------------- | ---------------- | --------------------------------------------------------------------------------------- |
| `+0x00`          | u8                   | class_type       | Same as the copy before it and the offset row key                                       |
| `+0x01`          | u16                  | character_key    | Player prototype; LOC type 6 names it like the class (`1` Warrior, `2` Ranger)          |
| `+0x03`          | u16                  | unknown_03       | `101` to `149`; `100 + character_key` on 24 of 47 records                               |
| `+0x05`          | u16                  | unknown_05       | `521` to `536`                                                                          |
| `+0x07`          | u16                  | unknown_07       | `201` to `214`                                                                          |
| `+0x09`          | u32                  | unknown_09       | `0xED819B97` for character 1; the low byte is `0x96 + character_key` on class types 0 to 36 |
| `+0x0D`          | u8                   | unknown_0d       | Always `101`                                                                            |
| `+0x0E`          | u32                  | starter_count    | `0` to `3`                                                                              |
| `+0x12`          | u32[n]               | starter_weapons  | Item IDs of the class's beginner weapons (Rusty Longsword, Round Shield); Wukong, Scholar, Kunoichi, Ninja, Archer, Seraph and Deadeye list three |
| `+0x12 + 4n`     | Setup Block (99 bytes) | setup          | See below                                                                               |
| `+0x75 + 4n`     | u64 + utf16le        | name_kr          | Korean class name (`워리어`); LOC type 21 `str_id4` 0 holds the translation              |
| varies           | u64 + utf16le        | description_kr   | Korean class description; LOC type 21 `str_id4` 1 holds the translation                |
| varies           | u64 + utf16le        | select_movie     | Class selection video, `UI_Customize/Movie/Movie_ClassSelect/<code>.webm`; empty on class types 13, 14 and 36 |
| varies           | u8                   | gender           | `0` male, `1` female (Warrior, Musa and Striker `0`; Ranger, Sorceress and Valkyrie `1`) |
| varies           | 4 x (u64 + ascii)    | consume_actions  | Action names `v<code>_Consume_Lv1` to `Lv4` after a class code (`vPBW_*`, the Tamer code, on 16 records); empty on Guardian |
| varies           | Presentation Block   | presentation     | See below; 71 bytes plus 8 per pair                                                     |
| varies           | Model List           | weapon_models    | See below                                                                               |
| varies           | Model List           | unknown model list | Same paths as `weapon_models` on every record of client 3464                          |

The `u64 + utf16le` strings store a u64 length in UTF-16 units, then the text, with no terminator; the `u64 + ascii` strings store a u64 byte length. No inline text holds a line break.

### Setup Block (99 bytes)

Offsets count from the start of the block. The 99 bytes are the same on all 47 records of client 3464 except `+0x5E`.

| Offset  | Type   | Field      | Notes                                                                    |
| ------- | ------ | ---------- | ------------------------------------------------------------------------ |
| `+0x00` | f32[3] | unknown_00 | `-154408.4`, `-335.9`, `135204.7`                                        |
| `+0x0C` | u32    | unknown_0c | `270`                                                                    |
| `+0x10` | f32[3] | unknown_10 | `-44361.7`, `1303.6`, `-1832.2`                                          |
| `+0x1C` | u32    | unknown_1c | `180`                                                                    |
| `+0x20` | f32[12] | unknown_20 | Values from `-1315839.5` to `1143770.9`                                 |
| `+0x50` | u32    | unknown_50 | `1`                                                                      |
| `+0x54` | u32    | unknown_54 | `1`                                                                      |
| `+0x58` | u32    | unknown_58 | `0`                                                                      |
| `+0x5C` | u8     | unknown_5c | `1`                                                                      |
| `+0x5D` | u8     | unknown_5d | `0`                                                                      |
| `+0x5E` | u8     | unknown_5e | `0` to `3` (22, 16, 6 and 3 records); the only byte that differs per class |
| `+0x5F` | u8     | unknown_5f | `2`                                                                      |
| `+0x60` | u8[3]  | unknown_60 | `0`                                                                      |

### Presentation Block (71 bytes + 8 per pair)

Offsets count from the start of the block.

| Offset            | Type       | Field         | Notes                                                                                 |
| ----------------- | ---------- | ------------- | ------------------------------------------------------------------------------------- |
| `+0x00`           | f32[6]     | unknown_00    | Two triples of values from `0.0` to `1.0`; the triples are equal on 36 of 47 records  |
| `+0x18`           | u8         | unknown_18    | `0` to `2`; `1` on Ranger, Archer, Deadeye and Agent only                             |
| `+0x19`           | u32[3]     | class_weapons | Item IDs of the main, sub and awakening weapon (Warrior: Rusty Longsword, Round Shield, Mercenary's Steel Greatsword); `0` for none |
| `+0x25`           | u16        | unknown_25    | `1` when the main weapon is set, else `0`                                             |
| `+0x27`           | f32[6]     | unknown_27    | First value `230.0` to `270.0`, then `0.3` to `0.8`, `-0.5` to `-0.3`, `-38.0` to `50.0`, `0.0`, `0.0` |
| `+0x3F`           | u32        | pair_count    | `0`, except `2` on Shai (class type 17)                                               |
| `+0x43`           | 8 bytes x pair_count | unknown pairs | Shai: u32 values `0, 31, 4, 31`                                           |
| `+0x43 + 8p`      | u32        | unknown_end   | `0`                                                                                   |

### Model List

| Offset  | Type   | Field | Notes                                                                    |
| ------- | ------ | ----- | ------------------------------------------------------------------------ |
| `+0x00` | u32    | count | `3` on 41 records, `2` on Agent, `0` on class types 13, 14, 18, 22 and 36 |
| `+0x04` | entry[] | entries | `count` entries                                                       |

Each entry is a u8 slot (`1` main, `2` sub, `3` awakening) and a `u64 + ascii` model path, such as `1_Pc/1_PHM/Weapon/1_OneHandSword/PHM_01_OHS_0004_R.pac` for the Warrior main weapon.

## pcgrowthoffset.dbss

Bare offset table into `pcgrowth.dbss` (no PABR magic, no trailer), read with `parse_bare_u8_offset_rows()` from `_common/pabr_offset.py`.

### Header (4 bytes)

| Offset  | Type | Field | Notes                                              |
| ------- | ---- | ----- | -------------------------------------------------- |
| `+0x00` | u32  | count | Number of offset rows; equals the main file count  |

### Offset Row (9 bytes, repeated `count` times)

| Offset  | Type | Field       | Notes                                                        |
| ------- | ---- | ----------- | ------------------------------------------------------------ |
| `+0x00` | u8   | class_type  | Key of the record it points at                               |
| `+0x01` | u32  | data_offset | Absolute byte offset of the record body, one past its u8 copy |
| `+0x05` | u32  | data_size   | Body size in bytes, `437` to `1485` on client 3464           |

The rows are in file order, which is not key order: 46 down to 32, 15 down to 0, then 31 down to 16. The parser checks the u8 copy before each body, that the body holds the same class type, and that it ends exactly at `data_offset + data_size`.

## Localization

| Text        | LOC key                                               |
| ----------- | ----------------------------------------------------- |
| Class name  | type 21, `str_id1` = `class_type`, `str_id4` 0        |
| Description | type 21, `str_id1` = `class_type`, `str_id4` 1        |
| Weapons     | type 0, `str_id1` = item ID                           |

LOC type 21 has a name and a description for all 47 class types on client 3464, including the unused slots (`Ain (No Use)`, `PYFW5`). The English text matches the inline Korean (class type 0: `Warrior` for `워리어`). The handler shows the LOC name and falls back to the inline Korean, as does the [pcgrowthsimply](pcgrowthsimply_bss.md) handler.

## Suggested UI Layout

### pcgrowth.dbss

| Column          | Type | Notes                                                                 |
| --------------- | ---- | --------------------------------------------------------------------- |
| Class Type      | num  | `class_type`                                                          |
| Class           | text | LOC type 21 name via `class_name()`, else `name_kr`                   |
| Character ID    | num  | `character_key`                                                       |
| Gender          | text | `gender` as Male or Female                                            |
| Playable        | flag | `is_playable` from `pcgrowthsimply.bss`; a dash without that file      |
| Starter Weapons | text | `starter_weapons` with item icons and names                           |
| Class Weapons   | text | Non-zero `class_weapons`, main, sub and awakening                     |
| Selection Video | text | `select_movie`                                                        |
| Description     | text | LOC type 21 `str_id4` 1, else `description_kr`, on one line           |

The `unknown_*` fields, `consume_actions` and `weapon_models` stay on the record but out of the table.

### pcgrowthoffset.dbss

| Column      | Type | Notes                 |
| ----------- | ---- | --------------------- |
| Class Type  | num  | `class_type`          |
| Data Offset | num  | `data_offset`, as hex |
| Data Size   | num  | `data_size`           |

## Notes

- iDevelopThings/bdo-data-extractor `FORMATS.md` lists this record layout. Checked against client 3464: the offset table and the record walk match, and all 47 records end at their recorded size. It reads the presentation block as seven f32 and a u32 at `+0x43`, with four extra u32 only on Shai; this doc reads `+0x3F` as a pair count, which gives the same byte total.
- `starter_weapons` start with the same main and sub weapon as `class_weapons` on every class with class weapons except Wukong and Ninja, which list them in another order (Ninja: Old Shuriken before Old Kunai).
- The ten unplayable class types 37 to 46 (`PYFM`, `PYFW` to `PYFM5`, `PYFW5`) copy the Dosa (male) and Woosa (female) records: same gender, starter weapons, video, models and `unknown_09`, no class weapons.

## Open Questions

### Header Fields unknown_03 to unknown_0d

`unknown_03` equals `100 + character_key` on 24 of 47 records (Warrior `101`, Wizard `129`) but not on the others (Kunoichi `132` for character 26, Woosa `117` for character 31). `unknown_05` (`521` to `536`) and `unknown_07` (`201` to `214`) take few values that many classes share. `unknown_09` follows the character key in its low byte. They could be keys of a customization, skeleton or animation table; no table has been matched yet.

### Setup Block

The 99 bytes are the same on every class except `+0x5E`. The f32 triples have world-coordinate magnitudes, so the block could hold the start positions and directions (`270`, `180`) of a new character, but no table links them yet. `unknown_5e` (`0` to `3`) has no matching class grouping.

### Presentation Values

`unknown_18` takes three values on the 32 playable class types:

| Value | Playable class types |
| ----- | -------------------- |
| `0` | Warrior (0), Wukong (3), Guardian (5), Scholar (6), Drakania (7), Nova (9), Corsair (10), Lahn (11), Berserker (12), Shai (17), Striker (19), Musa (20), Maehwa (21), Mystic (23), Valkyrie (24), Kunoichi (25), Ninja (26), Seraph (32) |
| `1` | Ranger (4), Archer (29), Deadeye (34), Agent (35) |
| `2` | Hashashin (1), Sage (2), Sorceress (8), Maegu (15), Tamer (16), Dark Knight (27), Wizard (28), Woosa (30), Witch (31), Dosa (33) |

Of the unplayable slots, 13, 14, 22 and 36 hold `0`, and 18 and 37 to 46 hold `2`. The split could be the attack type the game gives each class (`0` melee, `1` ranged, `2` magic): Hashashin and Dark Knight fight at close range but would count as magic classes there. No client Lua or table names the field yet. The two f32 groups could be class selection camera and colour settings. The Shai pairs (`0, 31, 4, 31`) could also read as a zero u32 followed by `31, 4, 31, 0`.

### Second Model List

Both model lists hold the same slots and paths on every record of client 3464. A record where they differ would show which one the class selection screen uses.
