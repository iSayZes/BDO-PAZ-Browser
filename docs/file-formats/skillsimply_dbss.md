# `skillsimply.dbss` Format

## Purpose

The learning rules of every skill rank: which classes can learn it, the
character level and skill points it needs, the skills that must be learned
first, the rank chain it belongs to, and the skills it cannot be held with.
It has exactly the keys of [`skill.dbss`](skill_dbss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes     | Records                    | Row bytes                  |
| ------ | -------------- | ------- | ------------------------ | --------- | -------------------------- | -------------------------- |
| 1      | 1784 and later | 3474    | `skillsimply.dbss`       | 3,499,846 | 30,487 Skill Simply Record | 114 to 134, 115 on average |
| 1      | 1784 and later | 3474    | `skillsimplyoffset.dbss` | 365,848   | 30,487 Offset Row          | 12                         |

| Layout | File                     | Known               | Unknown             |
| ------ | ------------------------ | ------------------- | ------------------- |
| 1      | `skillsimply.dbss`       | 2,493,775 B (71.3%) | 1,006,071 B (28.7%) |
| 1      | `skillsimplyoffset.dbss` | 365,848 B (100.0%)  | 0 B (0.0%)          |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3474   | Layout 1             |
| 3251   | Layout 1             |
| 3002   | Layout 1             |
| 2519   | Layout 1             |
| 2107   | Layout 1             |
| 1784   | Layout 1             |
| 1485   | No documented layout |
| 1230   | No file              |
| 794    | No file              |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                                  |
| ------------------------ | -------- | ----------------------------------------------------- |
| `skillsimplyoffset.dbss` | Required | `skill_key → (offset, size)` index into this file     |
| `languagedata_en.loc`    | Optional | Skill names (type `10`) and class names (type `21`)   |

The skill key is the one shared by the whole skill cluster; see
[`skill.dbss` Skill Keys](skill_dbss.md#skill-keys). All multi-byte values are
little-endian.

## Layout 1

### File Layout

| Offset              | Type                       | Field        | Notes                                                        |
| ------------------- | -------------------------- | ------------ | ------------------------------------------------------------ |
| `+0x00`             | char[4]                    | magic        | `PABR`                                                       |
| `+0x04`             | u32                        | count        | Number of records; `30424`, the `skill.dbss` key set exactly |
| `+0x08`             | Skill Simply Record[count] | records      | Back to back, no repeated key between them                   |
| `records+0x00`      | String Table               | string_table | Empty string table: `u32 0`                                  |
| `string_table+0x00` | u32                        | table_start  | End of the records                                           |
| `string_table+0x04` | u32                        | zero         | Always `0`                                                   |

The last 12 bytes are the empty string table and its trailer: `u32 0`, `u32` end of the records, `u32 0`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                          |
| ------- | ------------------ | ------------ | ------------------------------ |
| `+0x00` | u32                | string_count | `0`; the table is always empty |
| `+0x04` | pstr[string_count] | strings      | None                           |

### Skill Simply Record (variable: 110 bytes + lists)

`size` bytes from `offset` in `skillsimplyoffset.dbss`. Four lists make the
record variable; offsets after a list count from the end of
`contents_group_hashes`, `next_rank_keys`, `exclusive_skill_nos` or
`related_cool_time_skill_keys`. Record counts in the table are from client 3458, and
fields noted "Always `0`" are `0` on every record of it. The sheet columns
behind the names are in Field Names.

| Offset                     | Type                  | Field               | Notes                                                              |
| -------------------------- | --------------------- | ------------------- | ------------------------------------------------------------------ |
| `+0x00`                    | u32                   | skill_key           | Equals the index key                                               |
| `+0x04`                    | u32                   | level_1_key         | `skill_no << 16 \| 1`, as in `skill.dbss`                           |
| `+0x08`                    | u32                   | kind                | `0` other, `1` active, `2` passive; equals `skilltype.dbss` `kind` on all 30,342 shared keys |
| `+0x0C`                    | u8                    | branch              | `1` Awakening (1,985 records), `2` Succession (1,122), `0` neither; see below |
| `+0x0D`                    | u8                    | unknown_0d          | `0` with `branch` `0`, else the other branch                       |
| `+0x0E`                    | u32                   | contents_group_count | `1` on 29,916 records, up to `4`                                  |
| `+0x12`                    | u32[contents_group_count] | contents_group_hashes | `key_hash()` of each contents group key in decimal; `0x6016CFF7` (key `0`, every region) is the first on 18,784 records; see Field Names |
| `contents_group_hashes+0x00` | u8                  | unknown_h00         | `1` on 4,643 records, all at `0` skill points; see In-Game Checks  |
| `contents_group_hashes+0x01` | u32                 | need_level          | Character level needed to learn it; see below                      |
| `contents_group_hashes+0x05` | u16                 | previous_rank_no    | Skill number of the rank before it, `0` on the first rank          |
| `contents_group_hashes+0x07` | u32                 | next_rank_count     | `0` on 26,056 records, `1` on 4,099, up to `5`                     |
| `contents_group_hashes+0x0B` | u32[next_rank_count] | next_rank_keys     | Skill keys of the ranks after it, see below                        |
| `next_rank_keys+0x00`      | u8                    | require_equip_type  | Item equip type the skill needs (`itemenchant.dbss` `equip_type`); `0` none, `57` Awakening weapon; see below |
| `next_rank_keys+0x01`      | u8                    | uses_main_weapon    | `1` when the skill is used with the main weapon (4,768 records); see below |
| `next_rank_keys+0x02`      | u8                    | uses_sub_weapon     | `1` when the skill is used with the sub-weapon (451 records); see below |
| `next_rank_keys+0x03`      | bytes[2]              | unknown_n03         | Both `1` on every skill with a weapon, else `0`                     |
| `next_rank_keys+0x05`      | u8                    | unknown_n05         | `2` on 25,513 records, else `0` or `1`                             |
| `next_rank_keys+0x06`      | u8                    | unknown_n06         | `1` on one record                                                  |
| `next_rank_keys+0x07`      | u8                    | require_equip_slot  | Slot of `require_equip_type` (`itemenchant.dbss` `equip_slot`): `0` main weapon, `1` sub-weapon, `29` Awakening weapon, `46` none |
| `next_rank_keys+0x08`      | u8                    | unknown_n08         | `2` on every skill without an equip type, else `0`, `1` or `2`      |
| `next_rank_keys+0x09`      | bytes[4]              | unknown_n09         | Always `0`; see Open Questions                                     |
| `next_rank_keys+0x0D`      | u32                   | skill_owner_type    | `0` character skill, `1` guild skill (766 records); see Field Names |
| `next_rank_keys+0x11`      | u8                    | unknown_n11         | `1` on 3,665 records                                               |
| `next_rank_keys+0x12`      | u32                   | first_rank_key      | Level 1 key of the first rank of its chain; its own `level_1_key` on a first rank |
| `next_rank_keys+0x16`      | u8                    | is_fusion           | `1` on the 205 fusion skills, see below                            |
| `next_rank_keys+0x17`      | u8                    | condition           | `1` on 847 records; see Field Names                                |
| `next_rank_keys+0x18`      | u8                    | unknown_n18         | Always `0`                                                         |
| `next_rank_keys+0x19`      | u8                    | can_quick_slot      | `1` when the skill can be put on a quick slot (3,592 records); see below |
| `next_rank_keys+0x1A`      | u16                   | max_level           | Highest level of the skill number; `1` on 30,288 records, else `2`, `3` or `13` |
| `next_rank_keys+0x1C`      | u64                   | class_mask          | Bit `n` set: class `n` (LOC type `21`) can learn it; see below     |
| `next_rank_keys+0x24`      | u16                   | need_skill_level_1  | Level of `need_skill_no_1` that must be learned: `1` when it is set, else `0` |
| `next_rank_keys+0x26`      | u16                   | need_skill_no_1     | Skill number that must be learned first, `0` when none             |
| `next_rank_keys+0x28`      | u16                   | need_skill_level_2  | Level of `need_skill_no_2`: `1` when it is set, else `0`           |
| `next_rank_keys+0x2A`      | u16                   | need_skill_no_2     | A second required skill, `0` when none                             |
| `next_rank_keys+0x2C`      | bytes[8]              | unknown_n2c         | Always `0`                                                         |
| `next_rank_keys+0x34`      | u16                   | need_skill_point    | Skill points it costs; `0` on 9,304 records, `1` on 17,512, up to `999` |
| `next_rank_keys+0x36`      | bytes[4]              | unknown_n36         | Always `0`                                                         |
| `next_rank_keys+0x3A`      | u64                   | exclusive_count     | `0` on 29,716 records, up to `5`                                   |
| `next_rank_keys+0x42`      | u16[exclusive_count]  | exclusive_skill_nos | Skill numbers it cannot be held with, see below                    |
| `exclusive_skill_nos+0x00` | bytes[8]              | unknown_e00         | Always `0`                                                         |
| `exclusive_skill_nos+0x08` | u8                    | is_attack_skill         | Equals `skill.dbss` `is_attack_skill` on every record; see Notes  |
| `exclusive_skill_nos+0x09` | u8                    | is_except_cool_time | `1` on 255 records, all "Black Spirit:" skills; see Field Names    |
| `exclusive_skill_nos+0x0A` | u32                   | related_cool_time_skill_count    | `1` on 155 records, else `0`                                       |
| `exclusive_skill_nos+0x0E` | u32[related_cool_time_skill_count] | related_cool_time_skill_keys     | Equals `skill.dbss` `related_cool_time_skill_keys` on every record |
| `related_cool_time_skill_keys+0x00`     | u8                    | need_buff_module_type | `buff.dbss` `effect_type` that must be active: `179` (`0xB3`) on exactly the 27 "Elvia:" skills, `202` (`0xCA`, none) on the rest; see below |

Every one of the 30,424 records on client 3458 walks to exactly its `size`
with this layout. The shortest record (114 bytes) has one contents group and
empty lists. Earlier versions of this doc called `contents_group_count`
`hash_count`, `contents_group_hashes` `unknown_hashes` (before that
`hashes`), `require_equip_type` `weapon_type`, `require_equip_slot` and
`unknown_n08` together `unknown_n07` (a u16), `skill_owner_type`
`unknown_n0d` and `unknown_n0e`,
`condition` `unknown_n17`, `max_level` `unknown_n1a` and `unknown_n1b`,
`need_skill_level_1` and `need_skill_level_2` `has_need_skill_1` and
`has_need_skill_2`, `is_except_cool_time` `unknown_e09`,
`need_buff_module_type` `unknown_end`, `is_attack_skill` `unknown_e08` and
`related_cool_time_skill_keys` `base_skill_keys`.

### `skillsimplyoffset.dbss`

Unlike `skilloffset.dbss` this index has no magic and no trailer: a u32 count
(`30424` on client 3458) and then 12-byte rows of u32 `skill_key`, u32
`offset`, u32 `size`, ending exactly at end of file. Read it with
`parse_bare_u32_offset_rows()`.

| Offset  | Type              | Field | Notes                  |
| ------- | ----------------- | ----- | ---------------------- |
| `+0x00` | u32               | count | `30424` on client 3458 |
| `+0x04` | Offset Row[count] | rows  | See Offset Row         |

### Offset Row (12 bytes)

| Offset  | Type | Field     | Notes                                            |
| ------- | ---- | --------- | ------------------------------------------------ |
| `+0x00` | u32  | skill_key | Record key                                       |
| `+0x04` | u32  | offset    | Absolute byte offset of the record's `skill_key` |
| `+0x08` | u32  | size      | Record size in bytes                             |

## `need_level` and `need_skill_point`

Checked on bdocodex: "Grave Digging III" (1761) needs level 58 and 33 skill
points and stores `58` and `33`; "Imminent Doom" (1209) needs level 50 and 1
point and stores `50` and `1`. Checked in game (2026-10-01) on Wizard: the
tooltips of "Fireball IV" (level 30), "Lightning V" (46) and "Teleport III"
(51) show those levels and 0 skill points, "Mind Training XX" costs 3 points
and "Unyielding Might" needs level 62 and 10 points, all as stored. Both
values match the learning requirement fields of the skill tooltip Lua
(`_needCharacterLevelForLearning`, `_needSkillPointForLearning`).

`need_level` is `1` on 19,189 records and `0` on 4,760. Real requirements go
up to `60`, plus one `62` ("Unyielding Might"). The 207 records at `99` (192)
and `100` (15, the Berserker "Blood Call" ranks and Ranger "(Not in Use) Wind
Spirit") are far past any real character: the top player is level 70 in
October 2026, and active players sit around 61 to 63. 152 of them also store
`99` skill points, and 39 of the `99` records are named `(Not in Use)`, so
both values lock out skills that are retired or not learned from the skill
window.

## `need_skill_no_1` and `need_skill_no_2`

The skill tooltip Lua reads them as `_needSkillNo1` and `_needSkillNo2`.
"Grave Digging III" needs `1760` "Grave Digging II" and `1712` "Awakening:
Goyen's Greatsword", the two prerequisites bdocodex lists. 6,391 records set
the first and 1,486 the second; every value is a skill number of this table.

Each number follows its `need_skill_level_*`, the level of that skill that
must be learned, `1` wherever a number is set. Read as one u32, the pair is a
skill key (`skill_no << 16 | level`), the 2016 `_needPreSkillKeyForLearning`.

## `previous_rank_no`, `next_rank_keys` and `first_rank_key`

The three fields link the ranks of a skill line ("Grave Digging I" to "IV",
"Hammer Mastery I" to "IV"). On all 30,424 records `next_rank_keys` holds
exactly the keys whose `previous_rank_no` is this skill, and following
`previous_rank_no` back ends at the skill named by `first_rank_key`.

`next_rank_keys` is narrower than `skill.dbss` `next_skill_keys` and equal to
it on 29,014 records: it leaves out what a rank only unlocks ("Sudden
Decapitation IV" lists no next rank here, `skill.dbss` lists "Core: Sudden
Decapitation") and the guild skill chains ("Ample Storage Lv. 26" to "Lv.
27").

## `class_mask`

| Value              | Records | Meaning                                          |
| ------------------ | ------- | ------------------------------------------------ |
| `0x7FFFFFFFFFFF`   | 18,392  | Every class: item, event, guild and life skills  |
| `0`                | 4,295   | No class: ship, wagon and item effect skills     |
| one bit            | 7,043   | One class, e.g. `0x1` Warrior, `0x100` Sorceress |
| several bits       | 694     | Shared skills, e.g. `0x90000000` Wizard and Witch, `0x6000000` Kunoichi and Ninja |

Bit `n` is class type `n`, the value LOC type `21` names (`0` Warrior, `4`
Ranger, `8` Sorceress, `32` Seraph). Every single-bit skill sampled belongs
to the class of its bit. Musa and Maehwa skills share a bit with class `22`
("Temp Maehwa"): `0x500000` and `0x600000`.

## `exclusive_skill_nos`

Set on 708 records, in two patterns. The "Core:" skills of a class list every
other Core of that class ("Core: Soul Shower" lists the five other Woosa
Cores), and the "Absolute:" and "Prime:" versions of a skill list each other
("Absolute: Heavy Strike" and "Prime: Heavy Strike I"). 1,400 of the 1,410
entries are mutual. bdocodex shows the list on "Prime: Fireball I" (4941) as
"Skills you cannot learn after learning this skill: Absolute: Fireball". In
game (Wizard) only one Core can be selected at a time, and only on the
Awakening branch.

## `branch`

`1` on every "Awakening:" and "Core:" skill and on the Awakening weapon
skills ("Water Sphere I" to "III"), `2` on 972 of the 1,051 "Prime:" skills
and on 99 "Succession:" skills, `0` on the rest, which both branches use.
Cores are Awakening-only in game, matching their `1`. The client Lua reads a
skill's branch with `getSkillAwakenBranchType`.

## `is_fusion`

Fusion skills are learned by combining two skills at levels 56, 57 and 58,
cost no skill points, and each class picks three of its six (one per level
row). 192 of the 205 flagged records are exactly 64 per level (32 classes
times two options) with `need_level` `56`, `57` or `58`; on Wizard they are
"Sage's Light", "Sage's Rage", "Trembling Thunder", "Swift Earthquake",
"Lightning Spear" and "Mana Arrows". The two skills a fusion combines are not
stored here (the Lua reads them with `ToClient_getFusionMainSkillNoByClassType`
and `ToClient_getFusionSubSkillNoByClassType`), and neither is the one-per-row
choice: `exclusive_skill_nos` is empty on them.

## `can_quick_slot`

Checked in game (2026-10-01) on 15 Wizard skills: the tooltip line "Can be
added to a Quick Slot" appears exactly where the byte is `1` ("Teleport III",
"Healing Aura V", "Speed Spell III", "Absolute: Fireball", "Absolute: Dagger
Stab", "Prime: Lightning III", "Magma Bomb") and not where it is `0` ("Magic
Arrow V", "Magical Evasion V", "Ultimate: Teleport", "Flow: Magical Evasion",
"Absolute: Lightning Chain", "Absolute: Blizzard", "Elementalization",
"Barrage of Water"). It splits even within a line: "Teleport III" is `1`,
"Ultimate: Teleport" `0`. Every flagged record is an active skill on Wizard;
basic attacks, Flow follow-ups, Cores and passives are `0`.

## `require_equip_type`, `uses_main_weapon` and `uses_sub_weapon`

Checked in game (2026-10-01) on Wizard tooltips. On class skills the four
bytes from `next_rank_keys+0x01` take only four patterns:

| `+0x01` to `+0x04` | Class skills | Wizard example and tooltip                                       |
| -------------- | ------------ | ---------------------------------------------------------------- |
| `01 00 01 01`  | 4,488        | "Fireball IV", a staff skill: "Can be used via a Quick Slot with your sphera" |
| `00 00 01 01`  | 1,966        | "Water Sphere III", a sphera skill: "Can be used via a Quick Slot with your staff" |
| `00 01 01 01`  | 451          | "Absolute: Dagger Stab", a dagger skill                           |
| `00 00 00 00`  | 832          | Passives and fusion skills                                       |

`uses_main_weapon` is `1` on the main weapon skills, including 874 Succession
ones (Prime skills use the main weapon). The second pattern is the Awakening
weapon: 1,945 of its 1,966 class skills have `branch` `1`, and
`require_equip_type` is `57` on all of them. The third is the sub-weapon
(`uses_sub_weapon`).

`require_equip_type` names the weapon: `57` on every Awakening skill, one
value per class on main weapon skills (Wizard `6`, Nova `86`), and on
sub-weapon skills the sub-weapon itself, shared where classes share one:

| `require_equip_type` | Sub-weapon skills                                         |
| -------------------- | --------------------------------------------------------- |
| `8`           | Shield: Warrior "Shield Strike", Valkyrie "Shield Chase", Guardian "Guard" |
| `32`          | Dagger: Wizard and Witch "Dagger Stab"                            |
| `36`          | Horn bow: Musa and Maehwa "Stub Arrow"                            |
| `55`          | Kunai: Kunoichi and Ninja "Kunai Throw"                           |
| `56`          | Shuriken: Kunoichi and Ninja "Shuriken Throw"                     |
| `87`          | Quoratum, Nova's sub-weapon: "Quoratum's Opening" ("Raise your quoratum, then dash forward"), "Command: Passed Pawn" |

The other sub-weapon values belong to one class each (Dosa `110`, Hashashin
`81`, Corsair `90`, Lahn `70`, Deadeye `113`, Woosa `99`).

The nine bytes from `next_rank_keys+0x00` are a copy of an item equip type,
the 2016 `gc::ItemEquipType` (`_value`, `_isWeapon`, `_isSubWeapon`,
`_isExtractable`, `_isUseAvatarMesh`, `_rangeType`, `_isTwoHanded`,
`_equipSlotNo`, `_enchantFailType`): on client 3473, 30,481 of the 30,487
records hold the same nine bytes as the `itemenchant.dbss` header (`+0x07` to
`+0x0F`) of an item with that `equip_type`. The other 6 have equip types `23`
and `95`, which no item has. `uses_main_weapon` and `uses_sub_weapon` are the
`_isWeapon` and `_isSubWeapon` bytes, and `require_equip_slot` is the item's
`equip_slot`. `unknown_n03` to `unknown_n06` and `unknown_n08` sit in the
other places; `itemenchant.dbss` and `buff.dbss` leave the same bytes
unnamed.

## `need_buff_module_type`

`179` (`0xB3`) marks exactly the 27 "Elvia:" skills. Those only work while
an Elvia weapon buff is active: the buff comes from orbs that drop in Elvia,
lasts 10 minutes, and enables the class's Elvia skill. `179` is the
`buff.dbss` `effect_type` of the Elvia weapon blessings. Every other record
stores `202` (`0xCA`) on client 3473, one past the highest `effect_type` in
its `buff.dbss` (`201`); the private server's file on client 1784 stores
`182` there.

## Notes

- `0x6016CFF7`, `key_hash("0")`, also sits in the `skilltype.dbss`
  configuration of 18,744 records (client 3458), close to the 18,784 here, so
  that configuration likely holds the same contents group list.
- The MP and stamina costs a tooltip shows are not here; they are in
  [`skill.dbss`](skill_dbss.md) (`resource_cost`, `stamina_cost`).
- Protection (Super Armor, Frontal Guard, Invincible) is not here either: no
  byte separates "Frigid Fog IV" and "Earthquake IV" (Super Armor in game)
  from "Fireball IV" or "Lightning V". The tooltip's "Effect Details" lines
  are LOC type `46`, keyed by 32-bit IDs that appear in none of the skill
  tables; the class action chart (`.paac`) is the likely source.
- `is_attack_skill` follows the damage line of the tooltip's "Effect Details" on
  7 of 8 Wizard skills checked in game. It is `1` on "Flame's Calling",
  "Magma Bomb" and "Fireball IV", which show damage, and `0` on
  "Archwizardry: Mass Teleport", "Prime: Elemental Palace", "Speed Spell III"
  and "Summon: Keeper Marg", which show none. "Elementalization" is the
  exception: it stores `1` but deals no damage (it moves the character
  backwards for 250 stamina, 5 s cooldown). No sheet column matches it; the
  name comes from `skill.dbss`, see Field Names.

## Field Names

The record joins two sheets of the private server's skill workbooks on
client 1784: `SkillType_Table_New`, one row per skill number, and
`Skill_Table_New`, one row per skill rank. I matched every record field
against every column by value, twice: client 3473's file against the sheets
of the server's `DataSheets.bexcel` (22,829 shared skill numbers and 22,876
shared ranks), and that server's own `skillsimply.dbss` against the `.xlsm`
sheets it was compiled from (27,310 and 27,360). Where the 2016 client's
`gc::SkillTypeStaticStatus` and `gc::SkillStaticStatus` have the member, it is
listed.

| Field | Column | 2016 member | Equal, client 3473 | Equal, client 1784 |
| ----- | ------ | ----------- | ------------------ | ------------------ |
| `kind` | `SkillType` | `_skillType` | 22,540 | 27,309 |
| `branch` | `BranchType` | | 22,768 | 27,308 |
| `contents_group_hashes` | `ContentsGroupKey`, hashed | `_contentsGroupKey` | 22,346 | 27,310 |
| `previous_rank_no` | `UpgradeSkillType` | `_upgradedFrom` | 22,730 | 27,308 |
| `require_equip_type` | `RequireEquipType` | `_requireEquipType` | 22,751 | 27,310 |
| `skill_owner_type` | `SkillOwnerType` | `_skillOwnerType` | 22,829 | 27,310 |
| `condition` | `Condition` | | 22,714 | 27,309 |
| `can_quick_slot` | `IsSettableQuickSlot` | `_isSettableQuickSlot` | 22,701 | 27,307 |
| `class_mask` bits 0 to 31 | `0` to `31` | `_usableClassType` | 21,923 | 27,147 |
| `exclusive_skill_nos` | `ForbidSkillType` | `_forbidSkill` | 22,798 | 27,310 |
| `need_buff_module_type` | `NeedBuffModuleType` | | 23 of 23 set | 24 of 24 set |
| `need_level` | `PcLevel_ForLearning` | `_needCharacterLevelForLearning` | 22,049 | 26,924 |
| `need_skill_point` | `SkillPoint_ForLearning` | `_needSkillPointForLearning` | 19,409 | 27,020 |
| `need_skill_level_1`, `need_skill_no_1` | `NeedSkillLevelNo0_ForLearning`, `NeedSkillNo0_ForLearning` | `_needPreSkillKeyForLearning` | 22,399, 22,695 | 27,038, 27,354 |
| `need_skill_level_2`, `need_skill_no_2` | `NeedSkillLevelNo1_ForLearning`, `NeedSkillNo1_ForLearning` | `_needPreSkillKeyForLearning` | 22,646, 22,795 | 27,326, 27,355 |
| `is_fusion` | `IsFusion` | | 22,876 | 27,348 |
| `is_except_cool_time` | `ExceptCoolTime` | | 22,875 | 27,360 |

The fields named before (`kind`, `branch`, the rank, need, weapon and
quick slot fields, `class_mask`, `exclusive_skill_nos`, `is_fusion`) match
their columns; `weapon_type` takes the column's name `require_equip_type`,
and the `has_need_skill_*` flags turn out to be the required skill's level.

- `contents_group_hashes` stores `key_hash()` (`_common/string_hash.py`, the
  `stringtable.bss` key hash: lookup3 `hashlittle` over UTF-16LE, seed
  `0xC5EDE`) of each `ContentsGroupKey` written in decimal, one entry per key
  of the cell: `key_hash("0")` is `0x6016CFF7`, `key_hash("909")` the
  `0xD6CCB471` of "Water Sphere II". Every hash on client 3473 decodes to a
  key below 32,768; the parser reads them back as `contents_group_keys`. By
  the sheet comment the key lets the service operator turn a content on or
  off, and `0` applies in every service region.
- `kind` follows the 2016 enum `SkillType`: `eItemSkillType` `0`,
  `eActiveSkillType` `1`, `ePassiveSkillType` `2`, `eProductSkillType` `3`
  (no record stores `3`).
- `skill_owner_type` follows the 2016 enum `SkillOwnerType`
  (`eSkillOwnerTypeActor` `0`, `eSkillOwnerTypeGuild` `1`) and the sheet
  comment ("0: normal skill, 1: guild skill"). On client 3473 the 766 guild
  records are 650 passives and 116 actives, all with every class bit set,
  such as "Ample Storage Lv. 26" and "Boost Morale".
- `is_except_cool_time` is the `isExceptCoolTime()` of the skill wrapper in
  the client Lua. When an effect cuts every cooldown, the quick slot and
  cooldown panels (`panel_quickslot.luac`, `panel_skillcooltime.luac`,
  `panel_skillcooltimequickslot.luac`) replay the cooldown effect on each
  slot except the skills with this flag. On client 3473 it is set on 255 of
  the 750 "Black Spirit:" records and on nothing else.
- `max_level` is the highest level of its skill number on all 30,487
  records of client 3473 and all 27,580 of the private server's file. The
  2016 struct calls it `_masterLevel` (a u16) and no sheet column holds it;
  the field and the handler's column use "max level", the client's own term
  ("Max Level", 최대 레벨), since "master level" appears nowhere in the client
  text.
- `condition` is a flag column whose sheet comment reads "all condition
  checks (work in progress)". On client 3473 it is set on 787 records, such
  as the Scholar Cores and "Black Spirit: Soul Shower"; what it gates is
  open.
- `need_buff_module_type`: the sheet comment reads "buff module number to
  check when using the skill", and `buff.dbss` `effect_type` is the 2016
  buff `_moduleType`.
- `require_equip_slot` follows the `itemenchant.dbss` `equip_slot` it copies,
  as `buff.dbss` names its `need_equip_slot`; see the equip type paragraph
  above.
- `is_attack_skill` and `related_cool_time_skill_keys` equal the
  `skill.dbss` fields of those names on every record and take their names
  from there (`skill_dbss.md`, Field Names): the client 1784 server's file
  reader puts the byte in the member the 2016 struct calls `_isAttackSkill`,
  and the list is the `RelatedCoolTimeSkillNo` column.

## Open Questions

### What do the remaining flags hold?

`unknown_0d`, `unknown_h00` and `unknown_n11` match no column of
`SkillType_Table_New` or `Skill_Table_New`. `unknown_h00` sits where the
2016 `gc::SkillStaticStatus` has `_isPromptForLearning`, before the learning
level and points, but it is not `IsPrompt_ForLearning`: on client 3473, 4,715
shared ranks have the column at `1` and the byte at `0`. `skill.dbss` stores
`IsPrompt_ForLearning` in its own byte (equal on 22,857 of 22,876 ranks,
client 3474), so `unknown_h00` is a different flag. `unknown_n03` to
`unknown_n06` and `unknown_n08` are item equip type bytes (see above) with
no column. `unknown_n09` sits where the 2016 struct has `_equippedItemKey`,
right after `_requireEquipType`, but its four bytes are `0` on every record
and the sheet's `EquipedItemID` is empty on every row, so the values cannot
confirm it. The HP cost and learning item the skill tooltip Lua reads are
the `RequireHP` and `NeedItemID_ForLearning` columns, which `skill.dbss`
holds (`require_hp`, `need_item_key_for_learning`); whether the always-zero
blocks here (`unknown_n2c`, `unknown_n36`, `unknown_e00`) copy them, the
values cannot tell.

## In-Game Checks

### Is `unknown_h00` the Auto-Learn Flag?

Needs class: Wizard (a new character below level 8)

On client 3458 the byte is set on 4,643 records and none of them costs skill points. On
Wizard it is set on the base skills, whose tooltips show "Required Skill
Points : 0" ("Fireball IV", "Lightning V", "Teleport III"), and clear on
Awakening and Prime skills. The skill window and skill tooltip Lua
(`panel_window_skill_global.luac`, `panel_tooltip_skillgroup_1.luac`) read
an "auto learn by level" flag (`isAutoLearnSkillByLevel`), which fits, but
4,661 other records also cost 0 points without the flag (fusion and Black
Spirit skills among them, and Wizard's "Access Awakening Requirement", which the awakening quest
grants), so 0 points alone does not prove it.

Level the character from 7 to 10 without opening the skill window, then open
it. "Teleport I" (level 8) and "Magic Arrow II", "Concentrated Magic Arrow I"
and "Healing Aura I" (level 10) all store `1`. If they show as learned with
no Learn button, `unknown_h00` is the auto-learn flag; if they wait for a
click, it is something else.
