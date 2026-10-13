"""The forgiving XML reader and the state model, on small scripts written like the client's."""
from __future__ import annotations

from _ai.xml_tree import parse_xml
from .records import script_records
from .render import ScriptRenderer
from .script import KIND_HANDLER, PHASE_END, PHASE_START, PHASE_TICK, parse_script

_STRINGS = {
    "hp": "HP",
    "phases": {"start": "start", "tick": "each cycle", "end": "end"},
    "summary": {
        "script": "Script", "states": "states", "handlers": "handlers", "transitions": "transitions",
        "hpGates": "HP gates", "variables": "Variables", "none": "None", "from": "from {names}",
    },
    "handler": "handler",
    "event": "event",
    "missingState": "missing",
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
    states = parse_script(_SCRIPT)

    assert [(s.kind, s.name) for s in states] == [
        ("state", "InitialState"), ("state", "Wait"), ("state", "Attack"), (KIND_HANDLER, "HandleTakeDamage"),
    ]
    assert (states[0].section, states[0].note) == ("", "초기 상태")
    assert (states[1].section, states[1].note) == ("비전투 상태", "대기")
    assert states[2].section == "비전투 상태"
    assert states[1].edges == (("exit", "Wait"), ("TargetLost", "Gone"))
    assert states[2].attrs == (("Rotate", "False"),)


def test_steps_keep_their_phase() -> None:
    wait = parse_script(_SCRIPT)[1]
    assert [(phase, node.name) for phase, node in wait.steps] == [
        (PHASE_START, "compute"), (PHASE_TICK, "findtarget"), (PHASE_END, "changestate"),
    ]


def test_records_mark_hp_conditions_and_link_sources() -> None:
    records = script_records(parse_script(_SCRIPT), _STRINGS)
    wait = records[1]
    find = next(step for step in wait["_steps"] if step["phase"] == PHASE_TICK)

    assert find["to"] == "Attack" and find["tag"] == "findtarget" and find["dice"] == "30"
    assert [c["text"] for c in find["conditions"]] == ["distance ≤ 500", "HP ≤ 70%"]
    assert [c["gate"] for c in find["conditions"]] == [False, True]
    end = next(step for step in wait["_steps"] if step["phase"] == PHASE_END)
    assert end["conditions"][0]["hp"] and not end["conditions"][0]["gate"]
    assert records[2]["_reached_from"] == ["Wait", "HandleTakeDamage"]
    assert "exit → Wait" in records[2]["transitions"]


def test_state_links_carry_the_record_index_and_mark_unknown_states() -> None:
    renderer = ScriptRenderer(script_records(parse_script(_SCRIPT), _STRINGS), _STRINGS)

    assert 'data-record="2"' in renderer.state_link("Attack")
    assert "missing" in renderer.state_link("Gone")
    assert "HP ≤ 70%" in renderer.summary()


def test_state_links_follow_the_order_of_a_sorted_page() -> None:
    records = list(reversed(script_records(parse_script(_SCRIPT), _STRINGS)))

    assert 'data-record="1"' in ScriptRenderer(records, _STRINGS).state_link("Attack")
