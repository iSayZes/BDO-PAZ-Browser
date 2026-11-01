# `*.ai` AI Script Format

## Purpose

State machines that drive NPCs, monsters, bosses, summons and gimmick objects. Each file is XML text: a `<root>` holding `<state>` and `<handler>` elements. On client 3464 there are 7,070 `.ai` files: 7,032 under `character/aiscript/` (`monster` 2,500, `thelandofthemorning` 897, `boss` 588, `summon` 565, `thelandofthemorning_pt2` 461, `npc` 390, ...), 37 under `character/ai_check/` and 1 under `character/pcaiscript/`. Together they hold 238,151 states, 46,981 handlers and 271,686 transitions.

```text
character/aiscript/boss/mutanttreedummer_boss.ai
  InitialState  idle  CallCycleTime 500   exit -> Wait
  Battle_Wait   idle  CallCycleTime 100   -> Attack_SwingL dice 30 (distance <= 450, _HP <= 70)
  HandleTakeDamage                        -> Detect_Target (state == Wait, _isBattleMode == 0)
```

## Companion Files

None to read the script. [characterstatic.dbss](../dbss/characterstatic_dbss.md#ai-script) names the script of each character by file stem, without folder or extension (`9999` for `character/aiscript/9999.ai`); the view lists those characters under Used by, through the `CHARACTER_AI_SCRIPT` lookup index. On client 3464, 5,643 of the 7,070 files have a stem some character names. The stem is not unique: 31 stems exist in two folders, mostly `character/ai_check/before/` copies of `character/aiscript/` files, and both files list the same characters.

Values of attributes and condition tags whose name ends in `characterKey` are character IDs, several joined by `|`: `summonCharacter characterKey`, `summonCharacters CharacterKey`, `target_characterKey`, `checkCharacterKey`, `ownercharacterkey`.

## File Layout

Text, CRLF line endings. On client 3464, 4,855 files read as UTF-8 (216 of them with a BOM), 2,212 as CP949, and 3 as neither (`mountaingoat.ai`, `pcworker.ai`, `pc_bot.ai` hold broken bytes inside comments). There is no `<?xml ?>` declaration.

```xml
<root>
<!-- 초기 상태 -->
	<state name="InitialState" behavior="idle" action="WAIT" CallCycleTime="500" exit="Wait">
		<variable name="_HP"/>
	</state>
	<!-- ■■■ 비전투 상태 ■■■ -->
	<state name="Wait" behavior="idle" action="WAIT" CallCycleTime="1000" exit="Wait">
		<findTarget state="Detect_Target">
			<distance cmp="<=" value="1800"/>
			<target_hp cmp=">" value="0"/>
		</findTarget>
		<changeState state="Move_Random" callCount="20" blendTime="0.3"/>
	</state>
	<handler name="HandleTakeDamage">
		<changeState state="Detect_Target" blendTime="0.3">
			<state cmp="==" value="Wait"/>
		</changeState>
	</handler>
</root>
```

Other elements directly under `<root>` on client 3464: `<macro_value_define>` (81, each naming one expression, `Protected_Check="0 == (...)"`, that states use as `<compute expr="Protected_Check"/>`), `<compute>` (50), `<changeState>` (25), `<end>` (9), `<import filepath="/Summon/Horse.ai"/>` (3), `<start>` (3) and one `<handle>`. The AI Script view shows the macros and imports in its summary; the others are only in the Text tab.

### Not Valid XML

On client 3464, 4,428 of the 7,070 files fail a strict XML parser even after `<` and `>` inside attribute values are escaped:

| Error (Python `xml.etree`) | Files | Cause |
| -------------------------- | ----- | ----- |
| not well-formed            | 3,893 | `--` inside comments (`<!-- 비 전투 상태 ----------- -->`), raw `&&` in values |
| mismatched tag             | 454   | an end tag in other case (`</findTarget>` for `<findtarget>`), a typo (`</change>`), or one `</state>` too many |
| duplicate attribute        | 81    | the same attribute twice on one element (`CallCycleTime="1000" CallCycleTime="1000"`) |

The handler reads them with `handlers/_ai/xml_tree.py`, which never fails: quoted values are read whole, tag names match without case, an end tag closes the nearest open element of its name (and everything inside it), an end tag with no such element is skipped, and a repeated attribute keeps its first value. How the client resolves these cases is not known.

Tag and attribute names vary in case across files: `findTarget` / `findtarget` / `FindTarget`, `State`, `CallCycleTime` / `callcycletime`, `TargetLost` / `Targetlost`. The handler compares both without case.

## Record Structure

### State

| Attribute       | Notes |
| --------------- | ----- |
| `name`          | State name; the target of transitions. On client 3464 every file starts with `InitialState` |
| `behavior`      | `idle`, `walk`, `chase`, `return`, `escape`, `action`, `dead`, `none`, ... |
| `action`        | Animation action key (`BATTLE_WAIT`, `ATTACK_SWING_R`) |
| `CallCycleTime` | Milliseconds between runs of the state's every-cycle children |
| `exit`          | State to go to when the action ends; on every state |
| `complete`, `TargetLost`, `TargetHit`, `FailFindPath`, `FailByCurvedPath`, `FailByRestrict` | State to go to on that event |

Other attributes depend on the behavior: `Rotate`, `isTargetNeeded`, `IgnoreAggro`, `dest`, `min`, `max`, `radius`, `waypoint`, `OffsetX`/`Y`/`Z`, `RandomCycleTime`, ...

On client 3464, 236,995 `exit` values name a state of the same file and 1,161 do not. Misspelled event attributes (`compelet`, `Comeplete`, `compltet`) hold state names too; the handler shows them as plain attributes.

### Children of a State

| Child | Runs |
| ----- | ---- |
| `<start>` | Its children, once on entering the state |
| `<end>` | Its children, once on leaving |
| anything else | Every `CallCycleTime` ms |

A child with a `state` attribute is a transition to that state. On client 3464: `changeState` 242,421 (all spellings of the case), `findTarget` 24,143, `findTargetInAggro` 3,338, `getTargetFromSenderInfo` 854, `sender_info` 470, `findCharacter` 422, and a few others. Its children are conditions that must all hold. Transition attributes besides `state`: `dice`, `blendTime` (animation blend in seconds), `callCount`, `target`.

Conditions compare a subject with `cmp` (`<`, `<=`, `==`, `!=`, `>=`, `>`) and `value`, or give a `min`/`max` range: `distance`, `angle`, `target_hp`, `heightdiff`, `origin`, `level`, `state` (`value="Wait|Move_Random"`), `variable` (`name`), `target_characterKey`, `obstacle` (no attributes), ...

Other children are actions: `compute dest="_HP" expr="getHpRate()"`, `variable name="_X" value="0"` (declares a script variable; all 51,859 on client 3464 are in `InitialState`), `teleport`, `summonCharacter`, `use_skill`, `send_command`, `aggro`, `setTimer`, `InstanceNotifier`, ...

### Handler

`<handler name="Handle...">` runs its children when the event in its name happens (`HandleTakeDamage`, `HandleTargetInMyArea`). It has no `behavior`, `action` or `exit`.

### Comments

Most states have a Korean developer comment on the line above (`<!-- 대기 -->`). Comments with `■` or a run of three `-`, `=`, `*`, `#` or `~` title a section (`<!-- ■■■ 비전투 상태 ■■■ -->`, `<!-- 비 전투 상태 ------ -->`); the handler strips the decoration and shows the title on the first state under it. A comment on the same line after an element belongs to that element and is not used.

## Notes

- 5,420 of 271,686 transitions on client 3464 name a state that is not in the file. The three `<import>` elements pull states from other scripts, which covers some of them.
- `level cmp="<=" value="5"` and `self_combinePoint` are shown as written.

## Open Questions

### `dice`

`dice="30"` on a transition: a percent chance, or a weight among the transitions whose conditions hold. Shown as written.

### `callCount`

`changeState state="Move_Random" callCount="20"` may mean after 20 runs of the state. Shown as written.

### Malformed Files in the Client

Which element an unmatched end tag closes, and which value of a repeated attribute wins, in the client's own reader.

### Scripts the Client Does Not Ship

On client 3464, 327 `characterstatic.dbss` records name one of 274 scripts with no `.ai` file (`Hadum_M0519_Demonland_Gimmick`). Whether the server holds them, or the characters are unused, is not known.
