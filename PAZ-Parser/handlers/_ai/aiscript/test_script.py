"""The forgiving XML reader and the state model, on small scripts written like the client's."""
from __future__ import annotations

from collections.abc import Iterator

import pytest

import _common.loc as loc
from _ai.xml_tree import parse_xml
from _common.lookup_index import IndexKind, init_index
from tests.loc_counter import reset_loc
from tests.loc_data import loc_bytes
from .records import script_records
from .render import ScriptRenderer
from .script import KIND_HANDLER, PHASE_END, PHASE_START, PHASE_TICK, parse_script
from .steps import condition_dicts
from .summary import summary_html
from .users import script_users

_STRINGS = {
    "hp": "HP",
    "phases": {"start": "start", "tick": "each cycle", "end": "end"},
    "summary": {
        "script": "Script", "states": "states", "handlers": "handlers", "transitions": "transitions",
        "hpGates": "HP gates", "variables": "Variables", "none": "None", "from": "from {names}",
        "usedBy": "Used by", "macros": "Macros", "imports": "Imports",
    },
    "handler": "handler",
    "event": "event",
    "missingState": "missing",
    "filter": {"label": "Behavior", "shown": "{shown} of {total}"},
}

_SCRIPT = """<root>
<!-- 초기 상태 -->
	<state name="InitialState" behavior="idle" action="WAIT" CallCycleTime="500" exit="Wait">
		<variable name="_HP"/>
	</state>
	<!-- ■■■ 비전투 상태 ■■■ -->
	<!-- 대기 -->
	<state name="Wait" behavior="idle" CallCycleTime="1000" exit="Wait" TargetLost="Gone">
		<start>
			<compute dest="_HP" expr="getHpRate()"/>
		</start>
		<findtarget state="Attack" dice="30" blendTime="0.3">
			<distance cmp="<=" value="500"/>
			<variable name="_HP" cmp="<=" value="70"/>
		</findTarget>
		<end>
			<changeState state="Wait"><variable name="_HP" cmp="<=" value="100"/></change>
		</end>
	</state>
	<State name="Attack" behavior="action" Rotate="False" exit="Wait"/>
	<handler name="HandleTakeDamage">
		<changeState state="Attack"/>
	</handler>
</root>
"""

# A summoned character and a condition on the target's character, as the
# client's boss scripts write them.
_WOLF = 32001
_SUMMONER = 28494


@pytest.fixture
def _loaded_loc() -> Iterator[None]:
    reset_loc()
    loc.init_loc(loc_bytes([(6, _WOLF, 0, 0, 0, "Wolf"), (6, _SUMMONER, 0, 0, 0, "Summoner")]))
    yield
    reset_loc()


def _conditions(xml: str) -> list[str]:
    return [c["text"] for c in condition_dicts(parse_xml(xml).children, frozenset({"_HP"}), "HP")]


def _records(script: str = _SCRIPT, users: list[tuple[int, str]] | None = None) -> list[dict]:
    return script_records(parse_script(script), _STRINGS, users or [])


def test_reader_keeps_raw_lt_in_attribute_values() -> None:
    node = parse_xml('<a cmp="<=" expr="x>0&&y"/>').children[0]
    assert node.attrs == {"cmp": "<=", "expr": "x>0&&y"}


def test_reader_matches_end_tags_without_case_and_skips_unknown_ones() -> None:
    root = parse_xml("<root><findtarget><a/></findTarget><b></change></b><c/></root>").children[0]
    assert [child.tag for child in root.children] == ["findtarget", "b", "c"]


def test_reader_closes_inner_elements_with_their_parent() -> None:
    root = parse_xml("<root><state><end><x/></state><next/></root>").children[0]
    assert [child.tag for child in root.children] == ["state", "next"]
    assert root.children[0].children[0].tag == "end"


def test_reader_keeps_the_first_of_a_repeated_attribute() -> None:
    assert parse_xml('<a x="1" X="2" x="3"/>').children[0].attrs == {"x": "1", "X": "2"}
    assert parse_xml('<a x="1" X="2"/>').children[0].attr("X") == "1"


def test_comments_above_an_element_belong_to_it_and_trailing_ones_do_not() -> None:
    root = parse_xml("<root>\n<!-- a -- b -->\n<x/><!-- trailing -->\n<y/>\n</root>").children[0]
    assert root.children[0].comments == ("a -- b",)
    assert root.children[1].comments == ()


def test_script_reads_states_handlers_sections_and_notes() -> None:
    states = parse_script(_SCRIPT).states

    assert [(s.kind, s.name) for s in states] == [
        ("state", "InitialState"), ("state", "Wait"), ("state", "Attack"), (KIND_HANDLER, "HandleTakeDamage"),
    ]
    assert (states[0].section, states[0].note) == ("", "초기 상태")
    assert (states[1].section, states[1].note) == ("비전투 상태", "대기")
    assert states[2].section == "비전투 상태"
    assert states[1].edges == (("exit", "Wait"), ("TargetLost", "Gone"))
    assert states[2].attrs == (("Rotate", "False"),)


def test_script_reads_macros_and_imports_under_root() -> None:
    script = parse_script(
        '<root>\n<macro_value_define\n\tProtected_Check="0 == (a>0&&b)"/>\n'
        '<import filepath="/Summon/Horse.ai"/>\n<state name="InitialState" exit="InitialState"/>\n</root>'
    )
    assert script.macros == (("Protected_Check", "0 == (a>0&&b)"),)
    assert script.imports == ("/Summon/Horse.ai",)
    assert [state.name for state in script.states] == ["InitialState"]


def test_steps_keep_their_phase() -> None:
    wait = parse_script(_SCRIPT).states[1]
    assert [(phase, node.name) for phase, node in wait.steps] == [
        (PHASE_START, "compute"), (PHASE_TICK, "findtarget"), (PHASE_END, "changestate"),
    ]


def test_records_mark_hp_conditions_and_link_sources() -> None:
    records = _records()
    wait = records[1]
    find = next(step for step in wait["_steps"] if step["phase"] == PHASE_TICK)

    assert find["to"] == "Attack" and find["tag"] == "findtarget" and find["dice"] == "30"
    assert [c["text"] for c in find["conditions"]] == ["distance ≤ 500", "HP ≤ 70%"]
    assert [c["gate"] for c in find["conditions"]] == [False, True]
    end = next(step for step in wait["_steps"] if step["phase"] == PHASE_END)
    assert end["conditions"][0]["hp"] and not end["conditions"][0]["gate"]
    assert records[2]["_reached_from"] == ["Wait", "HandleTakeDamage"]
    assert "exit → Wait" in records[2]["transitions"]


def test_a_lower_and_an_upper_bound_read_as_one_range() -> None:
    assert _conditions(
        '<distance cmp=">" value="300"/><angle cmp="<" value="30"/><Distance cmp="<=" value="500"/>'
    ) == ["300 < distance ≤ 500", "angle < 30"]
    assert _conditions('<variable name="_HP" cmp="<" value="80"/><variable name="_HP" cmp=">=" value="40"/>') == [
        "40% ≤ HP < 80%",
    ]


def test_bounds_stay_apart_when_a_range_would_drop_something() -> None:
    # Two upper bounds, a third condition on the subject, an attribute besides cmp and value.
    assert _conditions('<angle cmp="<=" value="60"/><angle cmp="<" value="90"/>') == ["angle ≤ 60", "angle < 90"]
    assert len(_conditions('<a cmp=">" value="1"/><a cmp="<" value="9"/><a cmp="!=" value="5"/>')) == 3
    assert len(_conditions('<a cmp=">" value="1" target="self"/><a cmp="<" value="9"/>')) == 2


def test_an_hp_range_is_a_gate() -> None:
    conditions = condition_dicts(
        parse_xml('<variable name="_HP" cmp=">" value="50"/><variable name="_HP" cmp="<=" value="100"/>').children,
        frozenset({"_HP"}),
        "HP",
    )
    assert [(c["text"], c["gate"]) for c in conditions] == [("50% < HP ≤ 100%", True)]


@pytest.mark.usefixtures("_loaded_loc")
def test_character_keys_show_the_character_name() -> None:
    assert _conditions(f'<target_characterKey cmp="==" value="{_WOLF}|99999"/>') == [
        f"target_characterKey = {_WOLF} (Wolf) | 99999",
    ]
    script = parse_script(
        f'<root><state name="InitialState" exit="InitialState">'
        f'<summonCharacter CharacterKey="{_SUMMONER}" isChild="true"/></state></root>'
    )
    action = script_records(script, _STRINGS, [])[0]["_steps"][0]
    assert action["text"] == f"summonCharacter CharacterKey={_SUMMONER} (Summoner) isChild=true"


def test_a_list_value_may_wrap() -> None:
    conditions = condition_dicts(parse_xml('<state cmp="==" value="Wait|Move_Random"/>').children, frozenset(), "HP")
    assert conditions[0]["wrap"]


@pytest.mark.usefixtures("_loaded_loc")
def test_script_users_match_the_file_stem_without_case() -> None:
    init_index(IndexKind.CHARACTER_AI_SCRIPT, {_SUMMONER: "Monsters_Main", _WOLF: "Pet_Dog", 7: "monsters_main"})
    try:
        assert script_users("character/aiscript/monster_main/monsters_main.ai") == [(7, ""), (_SUMMONER, "Summoner")]
        assert script_users("character/aiscript/boss/unused.ai") == []
    finally:
        init_index(IndexKind.CHARACTER_AI_SCRIPT, None)


def test_summary_shows_users_macros_and_imports_only_when_the_script_has_them() -> None:
    plain = summary_html(ScriptRenderer(_records(), _STRINGS))
    assert "HP ≤ 70%" in plain
    assert "Used by" not in plain and "Macros" not in plain and "Imports" not in plain

    script = '<root><macro_value_define M="1"/><import filepath="/A.ai"/><state name="InitialState"/></root>'
    full = summary_html(ScriptRenderer(_records(script, [(_SUMMONER, "Summoner")]), _STRINGS))
    assert f"Summoner ({_SUMMONER})" in full and "Macros" in full and "/A.ai" in full
    # Each character links to its characterstatic.dbss row.
    link = (
        'data-action="open-record" data-path="gamecommondata/binary/characterstatic.dbss" '
        f'data-field="character_id" data-value="{_SUMMONER}"'
    )
    assert link in full


def test_state_links_carry_the_record_index_and_mark_unknown_states() -> None:
    renderer = ScriptRenderer(_records(), _STRINGS)

    assert 'data-record="2"' in renderer.state_link("Attack")
    assert "missing" in renderer.state_link("Gone")


def test_state_links_follow_the_order_of_a_sorted_page() -> None:
    records = list(reversed(_records()))

    assert 'data-record="1"' in ScriptRenderer(records, _STRINGS).state_link("Attack")


def test_filter_chips_count_rows_per_behavior_and_rows_carry_theirs() -> None:
    records = _records()
    renderer = ScriptRenderer(records, _STRINGS)
    bar = renderer.filter_bar()

    assert 'data-value="idle"' in bar and 'data-value="action"' in bar and 'data-value="handler"' in bar
    assert '>idle<span class="ai-chip-count">2</span>' in bar
    assert 'data-behavior="handler"' in renderer.id_cell(records[3], "")


def test_no_filter_for_a_script_of_one_behavior() -> None:
    script = '<root><state name="InitialState" behavior="idle"/><state name="B" behavior="Idle"/></root>'
    assert ScriptRenderer(_records(script), _STRINGS).filter_bar() == ""


def test_an_hp_bound_held_in_a_variable_gets_no_percent_sign() -> None:
    assert _conditions('<variable name="_HP" cmp="<=" value="AI_Warp_HP"/>') == ["HP ≤ AI_Warp_HP"]
