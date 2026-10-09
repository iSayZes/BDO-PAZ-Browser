# `skillsimply.dbss` Format

## Purpose

The learning rules of every skill rank: which classes can learn it, the
character level and skill points it needs, the skills that must be learned
first, the rank chain it belongs to, and the skills it cannot be held with.
It has exactly the keys of [`skill.dbss`](skill_dbss.md).

```text
skill 1761 "Grave Digging III"
  classes     Warrior                         (class_mask 0x1)
  need_level  58, need_skill_point 33
  need_skill  1760 "Grave Digging II", 1712 "Awakening: Goyen's Greatsword"
  rank chain  1759 I -> 1760 II -> 1761 III -> 1762 IV
```

## Companion Files

| File                     | Required | Role                                                  |
| ------------------------ | -------- | ----------------------------------------------------- |
| `skillsimplyoffset.dbss` | Required | `skill_key → (offset, size)` index into this file     |
| `languagedata_en.loc`    | Optional | Skill names (type `10`) and class names (type `21`)   |

The skill key is the one shared by the whole skill cluster; see
[`skill.dbss` Skill Keys](skill_dbss.md#skill-keys). All multi-byte values are
little-endian.

## File Layout

### skillsimplyoffset.dbss

Unlike `skilloffset.dbss` this index has no magic and no trailer: a u32 count
(`30424` on client 3458) and then 12-byte rows of u32 `skill_key`, u32
`offset`, u32 `size`, ending exactly at end of file. Read it with
`parse_bare_u32_offset_rows()`.

### skillsimply.dbss

| Offset  | Type     | Field   | Notes                                                           |
| ------- | -------- | ------- | --------------------------------------------------------------- |
| `+0x00` | u8[4]    | magic   | `PABR`                                                          |
| `+0x04` | u32      | count   | Number of records; `30424`, the `skill.dbss` key set exactly    |
| `+0x08` | ...      | records | Back to back, no repeated key between them                      |
| end     | 12 bytes | trailer | Empty string table: `u32 0`, `u32` end of the records, `u32 0`  |

## Record Structure

### Skill Simply Record (variable, `size` bytes from `offset`)

Four lists make the record variable. Offsets marked `H+`, `N+` and `E+` count
from the end of `hashes`, `next_rank_keys` and `exclusive_skill_nos`. Record
counts in the table are from client 3458, and fields called "zero" are `0` on
every record of it.

| Offset  | Type    | Field               | Notes                                                              |
| ------- | ------- | ------------------- | ------------------------------------------------------------------ |
| `+0x00` | u32     | skill_key           | Equals the index key                                               |
| `+0x04` | u32     | level_1_key         | `skill_no << 16 \| 1`, as in `skill.dbss`                           |
| `+0x08` | u32     | kind                | `0` other, `1` active, `2` passive; equals `skilltype.dbss` `kind` on all 30,342 shared keys |
| `+0x0C` | u8      | branch              | `1` Awakening (1,985 records), `2` Succession (1,122), `0` neither; see below |
| `+0x0D` | u8      | unknown_0d          | `0` with `branch` `0`, else the other branch                       |
| `+0x0E` | u32     | hash_count          | `1` on 29,916 records, up to `4`                                   |
| `+0x12` | u32[]   | hashes              | Hash-like values; `0x6016CFF7` is the first on 18,784 records, 444 distinct |
| `H+0`   | u8      | unknown_h00         | `1` on 4,643 records, all at `0` skill points; see In-Game Checks  |
| `H+1`   | u32     | need_level          | Character level needed to learn it; see below                      |
| `H+5`   | u16     | previous_rank_no    | Skill number of the rank before it, `0` on the first rank          |
| `H+7`   | u32     | next_rank_count     | `0` on 26,056 records, `1` on 4,099, up to `5`                     |
| `H+11`  | u32[]   | next_rank_keys      | Skill keys of the ranks after it, see below                        |
| `N+0`   | u8      | weapon_type         | The weapon the skill is used with; `0` none, `57` Awakening weapon; see below |
| `N+1`   | u8      | uses_main_weapon    | `1` when the skill is used with the main weapon (4,768 records); see below |
| `N+2`   | u8      | uses_sub_weapon     | `1` when the skill is used with the sub-weapon (451 records); see below |
| `N+3`   | u8[2]   | unknown_n03         | Both `1` on every skill with a weapon, else `0`                     |
| `N+5`   | u8      | unknown_n05         | `2` on 25,513 records, else `0` or `1`                             |
| `N+6`   | u8      | unknown_n06         | `1` on one record                                                  |
| `N+7`   | u16     | unknown_n07         | 21 values; `558` on 22,285 records                                 |
| `N+9`   | u8[4]   | zero                |                                                                    |
| `N+13`  | u8      | unknown_n0d         | `1` on 766 records                                                 |
| `N+14`  | u8[3]   | zero                |                                                                    |
| `N+17`  | u8      | unknown_n11         | `1` on 3,665 records                                               |
| `N+18`  | u32     | first_rank_key      | Level 1 key of the first rank of its chain; its own `level_1_key` on a first rank |
| `N+22`  | u8      | is_fusion           | `1` on the 205 fusion skills, see below                            |
| `N+23`  | u8      | unknown_n17         | `1` on 847 records                                                 |
| `N+24`  | u8      | zero                |                                                                    |
| `N+25`  | u8      | can_quick_slot      | `1` when the skill can be put on a quick slot (3,592 records); see below |
| `N+26`  | u8      | unknown_n1a         | `1` on 30,288 records, else `2`, `3` or `13`                       |
| `N+27`  | u8      | zero                |                                                                    |
| `N+28`  | u64     | class_mask          | Bit `n` set: class `n` (LOC type `21`) can learn it; see below     |
| `N+36`  | u16     | has_need_skill_1    | `1` when `need_skill_no_1` is set, else `0`                        |
| `N+38`  | u16     | need_skill_no_1     | Skill number that must be learned first, `0` when none             |
| `N+40`  | u16     | has_need_skill_2    | `1` when `need_skill_no_2` is set, else `0`                        |
| `N+42`  | u16     | need_skill_no_2     | A second required skill, `0` when none                             |
| `N+44`  | u8[8]   | zero                |                                                                    |
| `N+52`  | u16     | need_skill_point    | Skill points it costs; `0` on 9,304 records, `1` on 17,512, up to `999` |
| `N+54`  | u8[4]   | zero                |                                                                    |
| `N+58`  | u64     | exclusive_count     | `0` on 29,716 records, up to `5`                                   |
| `N+66`  | u16[]   | exclusive_skill_nos | Skill numbers it cannot be held with, see below                    |
| `E+0`   | u8[8]   | zero                |                                                                    |
| `E+8`   | u8      | unknown_e08         | Equals `skill.dbss` `unknown_08` on every record; see Notes        |
| `E+9`   | u8      | unknown_e09         | `1` on 255 records, all active                                     |
| `E+10`  | u32     | base_skill_count    | `1` on 155 records, else `0`                                       |
| `E+14`  | u32[]   | base_skill_keys     | Equals `skill.dbss` `base_skill_keys` on every record              |
| last    | u8      | unknown_end         | `0xCA` on 30,397 records; `0xB3` on exactly the 27 "Elvia:" skills |

Every one of the 30,424 records on client 3458 walks to exactly its `size`
with this layout. The shortest record (114 bytes) has one hash and empty
lists.

### `need_level` and `need_skill_point`

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

### `need_skill_no_1` and `need_skill_no_2`

The skill tooltip Lua reads them as `_needSkillNo1` and `_needSkillNo2`.
"Grave Digging III" needs `1760` "Grave Digging II" and `1712` "Awakening:
Goyen's Greatsword", the two prerequisites bdocodex lists. 6,391 records set
the first and 1,486 the second; every value is a skill number of this table.

### `previous_rank_no`, `next_rank_keys` and `first_rank_key`

The three fields link the ranks of a skill line ("Grave Digging I" to "IV",
"Hammer Mastery I" to "IV"). On all 30,424 records `next_rank_keys` holds
exactly the keys whose `previous_rank_no` is this skill, and following
`previous_rank_no` back ends at the skill named by `first_rank_key`.

`next_rank_keys` is narrower than `skill.dbss` `next_skill_keys` and equal to
it on 29,014 records: it leaves out what a rank only unlocks ("Sudden
Decapitation IV" lists no next rank here, `skill.dbss` lists "Core: Sudden
Decapitation") and the guild skill chains ("Ample Storage Lv. 26" to "Lv.
27").

### `class_mask`

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

### `exclusive_skill_nos`

Set on 708 records, in two patterns. The "Core:" skills of a class list every
other Core of that class ("Core: Soul Shower" lists the five other Woosa
Cores), and the "Absolute:" and "Prime:" versions of a skill list each other
("Absolute: Heavy Strike" and "Prime: Heavy Strike I"). 1,400 of the 1,410
entries are mutual. bdocodex shows the list on "Prime: Fireball I" (4941) as
"Skills you cannot learn after learning this skill: Absolute: Fireball". In
game (Wizard) only one Core can be selected at a time, and only on the
Awakening branch.

### `branch`

`1` on every "Awakening:" and "Core:" skill and on the Awakening weapon
skills ("Water Sphere I" to "III"), `2` on 972 of the 1,051 "Prime:" skills
and on 99 "Succession:" skills, `0` on the rest, which both branches use.
Cores are Awakening-only in game, matching their `1`. The client Lua reads a
skill's branch with `getSkillAwakenBranchType`.

### `is_fusion`

Fusion skills are learned by combining two skills at levels 56, 57 and 58,
cost no skill points, and each class picks three of its six (one per level
row). 192 of the 205 flagged records are exactly 64 per level (32 classes
times two options) with `need_level` `56`, `57` or `58`; on Wizard they are
"Sage's Light", "Sage's Rage", "Trembling Thunder", "Swift Earthquake",
"Lightning Spear" and "Mana Arrows". The two skills a fusion combines are not
stored here (the Lua reads them with `ToClient_getFusionMainSkillNoByClassType`
and `ToClient_getFusionSubSkillNoByClassType`), and neither is the one-per-row
choice: `exclusive_skill_nos` is empty on them.

### `can_quick_slot`

Checked in game (2026-10-01) on 15 Wizard skills: the tooltip line "Can be
added to a Quick Slot" appears exactly where the byte is `1` ("Teleport III",
"Healing Aura V", "Speed Spell III", "Absolute: Fireball", "Absolute: Dagger
Stab", "Prime: Lightning III", "Magma Bomb") and not where it is `0` ("Magic
Arrow V", "Magical Evasion V", "Ultimate: Teleport", "Flow: Magical Evasion",
"Absolute: Lightning Chain", "Absolute: Blizzard", "Elementalization",
"Barrage of Water"). It splits even within a line: "Teleport III" is `1`,
"Ultimate: Teleport" `0`. Every flagged record is an active skill on Wizard;
basic attacks, Flow follow-ups, Cores and passives are `0`.

### `weapon_type`, `uses_main_weapon` and `uses_sub_weapon`

Checked in game (2026-10-01) on Wizard tooltips. On class skills the four
bytes from `N+1` take only four patterns:

| `N+1` to `N+4` | Class skills | Wizard example and tooltip                                       |
| -------------- | ------------ | ---------------------------------------------------------------- |
| `01 00 01 01`  | 4,488        | "Fireball IV", a staff skill: "Can be used via a Quick Slot with your sphera" |
| `00 00 01 01`  | 1,966        | "Water Sphere III", a sphera skill: "Can be used via a Quick Slot with your staff" |
| `00 01 01 01`  | 451          | "Absolute: Dagger Stab", a dagger skill                           |
| `00 00 00 00`  | 832          | Passives and fusion skills                                       |

`uses_main_weapon` is `1` on the main weapon skills, including 874 Succession
ones (Prime skills use the main weapon). The second pattern is the Awakening
weapon: 1,945 of its 1,966 class skills have `branch` `1`, and `weapon_type`
is `57` on all of them. The third is the sub-weapon (`uses_sub_weapon`).

`weapon_type` names the weapon: `57` on every Awakening skill, one value per
class on main weapon skills (Wizard `6`, Nova `86`), and on sub-weapon
skills the sub-weapon itself, shared where classes share one:

| `weapon_type` | Sub-weapon skills                                                |
| ------------- | ---------------------------------------------------------------- |
| `8`           | Shield: Warrior "Shield Strike", Valkyrie "Shield Chase", Guardian "Guard" |
| `32`          | Dagger: Wizard and Witch "Dagger Stab"                            |
| `36`          | Horn bow: Musa and Maehwa "Stub Arrow"                            |
| `55`          | Kunai: Kunoichi and Ninja "Kunai Throw"                           |
| `56`          | Shuriken: Kunoichi and Ninja "Shuriken Throw"                     |
| `87`          | Quoratum, Nova's sub-weapon: "Quoratum's Opening" ("Raise your quoratum, then dash forward"), "Command: Passed Pawn" |

The other sub-weapon values belong to one class each (Dosa `110`, Hashashin
`81`, Corsair `90`, Lahn `70`, Deadeye `113`, Woosa `99`).

### `unknown_end`

`0xB3` marks exactly the 27 "Elvia:" skills. Those only work
while an Elvia weapon buff is active: the buff comes from orbs that drop in
Elvia, lasts 10 minutes, and enables the class's Elvia skill. Every other
record ends in `0xCA`, so the byte is not a plain end marker.

## Suggested UI Layout

Opens sorted by `skill_key` (Skill No, then Level); the index order is
arbitrary.

| Column           | Type | Notes                                                              |
| ---------------- | ---- | ------------------------------------------------------------------ |
| Skill No         | num  | `skill_key >> 16`                                                  |
| Level            | num  | `skill_key & 0xFFFF`                                               |
| Icon             | icon | `IconKind.SKILL` icon of `skill_no`                                |
| Name             | text | LOC type `10`, `str_id1 = skill_no`, `str_id4 = 0`; else the `skilltype.dbss` Korean name |
| Classes          | text | `class_mask` as LOC type `21` names; "All" for `0x7FFFFFFFFFFF`, empty for `0` |
| Kind             | text | `kind` as Other / Active / Passive                                 |
| Branch           | text | `branch` as Awakening / Succession; empty when `0`                 |
| Weapon           | text | Main (`uses_main_weapon`), Sub (`uses_sub_weapon`) or Awakening (`weapon_type` `57`); empty otherwise |
| Quick Slot       | flag | `can_quick_slot` as a check mark or a cross                        |
| Required Level   | num  | `need_level`; empty when `0`                                       |
| Skill Points     | num  | `need_skill_point`; empty when `0`                                 |
| Required Skills  | list | `need_skill_no_1` and `need_skill_no_2` as skill names             |
| Previous Rank    | text | `previous_rank_no` as skill name                                   |
| Exclusive Skills | list | `exclusive_skill_nos` as skill names                               |

## Notes

- `0x6016CFF7` also sits in the `skilltype.dbss` configuration of 18,744
  records, close to the 18,784 here, so `hashes` likely repeats something
  from that configuration.
- The `need_*` field names follow the skill tooltip Lua
  (`panel_tooltip_skill.luac`); `class_mask`, `branch`, `is_fusion`, `can_quick_slot`, the weapon fields, the rank
  fields and `exclusive_skill_nos` are named from the data and the in-game
  checks above.
- The MP and stamina costs a tooltip shows are not here; they are in
  [`skill.dbss`](skill_dbss.md) (`resource_cost`, `stamina_cost`).
- Protection (Super Armor, Frontal Guard, Invincible) is not here either: no
  byte separates "Frigid Fog IV" and "Earthquake IV" (Super Armor in game)
  from "Fireball IV" or "Lightning V". The tooltip's "Effect Details" lines
  are LOC type `46`, keyed by 32-bit IDs that appear in none of the skill
  tables; the class action chart (`.paac`) is the likely source.
- `unknown_e08` follows the damage line of the tooltip's "Effect Details" on
  7 of 8 Wizard skills checked in game. It is `1` on "Flame's Calling",
  "Magma Bomb" and "Fireball IV", which show damage, and `0` on
  "Archwizardry: Mass Teleport", "Prime: Elemental Palace", "Speed Spell III"
  and "Summon: Keeper Marg", which show none. "Elementalization" is the
  exception: it stores `1` but deals no damage (it moves the character
  backwards for 250 stamina, 5 s cooldown). So the field keeps its offset
  name.

## Open Questions

### What do the remaining flags and `hashes` hold?

The other `unknown_` bytes are small flags and enums (`unknown_n07` is `558`
on most records). `unknown_e08` marks damage skills on Wizard except
"Elementalization" (see Notes); what else it tracks is not known.
`hashes` is up to four hash-like values that also split by weapon on Wizard
(`0x6016CFF7` on the staff skills, `0xD6CCB471` on "Water Sphere II"). The skill
tooltip Lua also reads an HP cost and a learning item, which are candidates;
the MP and stamina costs turned out to live in `skill.dbss`. Matching them
needs skills whose tooltip shows such a value.

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
