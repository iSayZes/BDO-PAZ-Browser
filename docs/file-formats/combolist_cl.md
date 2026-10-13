# `*.cl` Combo List Format

## Purpose

Skill combos of the player classes for the console pad combo mode and the AI auto hunt. Each file is XML text: a `<combolist>` of `<combo>` elements, each a sequence of skills with the pad button that starts it, and a `<skill_command_list>` with the keyboard and mouse input of each skill. On client 3464 there are 48 `.cl` files, all in `character/pcaiscript/`, one per class (`valkyrie_auto.cl`, `ninjaman_auto.cl`) plus reserved slots and tests. Many are byte-identical copies: 17 files (`blackspirit_auto.cl`, `scholar_auto.cl`, the `*reserved*_auto.cl` slots) share one content, and six more groups of two to six files share another.

```text
character/pcaiscript/valkyrie_auto.cl
  combo BT_Skill_Attack_A   start_weapon_type 1 (pre-awakening)   learn_check_skill 349 1440 1027 385
    skill BT_ATTACK_S1_1    skill_no 349 Forward Slash I     console_key LT 0 X
  skill_command BT_ACTION_CHANGE   awakening_type 0   C 0-200 ms
```

## Companion Files

None to read the file. `skill_no`, `learn_check_skill` and `cool_check_skill` hold skill numbers, the `skill_no` of [skill.dbss](skill_dbss.md): LOC type 10 names them (`349` Forward Slash I, `1712` Awakening: Goyen's Greatsword), and `skilltype.dbss` has the Korean name when LOC has none.

## File Layout

Text, CRLF line endings, no `<?xml ?>` declaration. On client 3464, 38 files read as UTF-8 and 10 as CP949. None passes a strict XML parser: 46 hold `--` inside comments (`<!------ 비각성 ------>`), and the 2 others have two root elements.

```xml
<combolist>
	<!-- ---------- 비각성 ---------- -->
	<!-- 방어 태세 -->
	<combo name="BT_skill_Defence" learn_check_skill="1019" cool_check_skill="1019" is_only_console="true" start_weapon_type="1">
		<skill name="BT_skill_Defence" call_cycle_time="1000" skill_no="1019" console_key="LB 0 0"/>
	</combo>
</combolist>
<skill_command_list>
	<skill_command name="STANCE_CHANGE_MAINWEAPON_AT_U" delay_time="500" awakening_type="0" combo_end_time="0">
		<command key="W" starttime="0" endtime="300"/>
		<command key="C" starttime="100" endtime="300"/>
	</skill_command>
</skill_command_list>
```

The reader is the one of the [`.ai` scripts](aiscript_ai.md#not-valid-xml) (`handlers/_ai/xml_tree.py`): quoted values whole, tag and attribute names without case. Comments follow the `.ai` rules too: a comment with `■` or a run of three `-`, `=`, `*`, `#` or `~` titles a section, a plain comment right above a combo is its developer note (the Korean skill name, `방어 태세`).

The first comments of the current-format files describe the attributes; the field notes below quote them.

## Record Structure

### Combo

| Attribute | Notes |
| --------- | ----- |
| `name` | Combo name; often the action name of its first skill, and not unique: on client 3464, 2 to 12 names repeat in most class files (`BT_skill_Defence` three times, once per `console_key`) |
| `start_weapon_type` | `0` common, `1` pre-awakening, `2` awakening, `3` mount (horse), per the comment in `warrior_auto.cl`. On client 3464: `2` on 3,089 combos, `1` on 3,027, `0` on 221, `3` on none |
| `is_only_console` | `true`: used only by the combo pad, not by the AI auto hunt (file comment). `true` on 6,331 combos, `false` on 6 |
| `learn_check_skill` | Skill numbers, space-separated; the combo needs them learned (file comment) |
| `cool_check_skill` | Skill numbers whose cooldown the combo checks (file comment). Usually the same list as `learn_check_skill` |
| `dice_value` | `1` to `6`, on 6 combos of one file |

### Steps of a Combo

`<skill>` children run in file order; `<move>` (667 on client 3464) moves toward the target.

| Attribute | On | Notes |
| --------- | -- | ----- |
| `name` | both | Action name (`BT_ATTACK_S1_1`); also the name of the `<skill_command>` that holds its keys |
| `skill_no` | skill | Skill number |
| `console_key` | skill | Pad input as `<shoulder> <direction> <face>`: shoulder `LB`, `LT`, `RB`, `RT`; direction `FRONT`, `BACK`, `LEFT`, `RIGHT`; face `A`, `B`, `X`, `Y` or a pair (`XY`); `0` for none (`LT 0 X`, `RB FRONT 0`). 43 values on client 3464 |
| `call_cycle_time` | both | Milliseconds; `1000` on 17,556 skills |
| `combo_end_time` | skill | Milliseconds, on 4,637 skills |
| `min_dist`, `max_dist`, `require_dist`, `require_hp`, `require_mp` | both | On 1,435 skills and every move, the AI auto hunt steps. `require_hp` is `0` on all of them |

### Skill Command

`<skill_command_list>` follows `<combolist>` in 46 files.

| Attribute | Notes |
| --------- | ----- |
| `name` | Action name, the `name` of the combo steps it serves |
| `awakening_type` | `0` both, `1` pre-awakening only, `2` awakening only; `0` when both use the same keys (file comment) |
| `delay_time` | Milliseconds; per the file comment, every `endtime` must stay below it |
| `combo_end_time` | Milliseconds; `0` on 1,003 of 1,057. Per the file comment, one-skill actions such as guard, swap and chase get `0` |
| `console_slot_index` | `0` to `10`, on 353 commands |

Each `<command key="Shift" starttime="0" endtime="300"/>` child presses a key from `starttime` to `endtime` ms. Keys on client 3464: `W`, `A`, `S`, `D`, `Q`, `E`, `F`, `C`, `Shift`, `Space` (both in three spellings of case), `M0` and `M1` (mouse buttons).

On client 3464, 22,745 of the 23,464 skill steps have a `<skill_command>` of their name in the same file. A name can repeat: 111 names have two or more commands, 81 of them with different `awakening_type`.

### Older Layout

`warrior_auto.cl` and `prsa_auto.cl` (one content) use capitalized names and no `<skill_command_list>`: `<Combo Name StartWeaponType InitCombo DelayTime>` and `<Skill Name SkillNo="349 350 351 705" Command="1"/>`. Per its comment, `SkillNo` lists the skills to try, the first usable one runs, `Command` is `1` to `4`, `InitCombo="True"` marks the combo used outside a combo (one per weapon type) and `DelayTime` is the key input window.

## Suggested UI Layout

The `.cl` handler (`handlers/_ai/combolist/`) names the Parsed tab Combo List and shows one row per combo under a summary (counts of combos by weapon type, steps and skill commands). It opens in file order and sorts by Combo, Weapon and Pad only. A Text tab shows the XML.

- Combo: section title, name, developer note.
- Weapon: `start_weapon_type` as its label, in the client's words: Common, Main Weapon, Awakening, Mount.
- Pad only: `is_only_console`.
- Checks: the learned and cooldown skills, each as `349 Forward Slash I`; one line when both lists are the same. A skill number opens its first `skill.dbss` row, here and in Steps.
- Steps: per step its action name, skills with their names, `console_key` (or `Command`), timing and distance requirements, and the keys of every `<skill_command>` of its name (`Shift 0-300 + W 100-300`), with its `awakening_type` when the name has more than one.

## Notes

- On client 3464, 1,261 `<skill_command>` names (counted per file) have no combo step of that name. They show in the Text tab only.
- Skill names come from the loaded LOC, then the Korean `skilltype.dbss` name.

## Open Questions

### Which Skill Command a Step Uses

When a name has several `<skill_command>` entries, the one the client takes for a step is not known; `awakening_type` against the combo's `start_weapon_type` is the likely rule. The view lists all of them.

### Use in the Live Client

The comments describe a test setup (`Load PC_AIScript`, `consolePadType` `0` default, `1` E3 mode, `2` combo mode). Whether the released client reads these files, for the pad combo mode or the AI auto hunt, is not known.
