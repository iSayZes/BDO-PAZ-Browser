"""The combo list model and cells, on small lists written like the client's."""
from __future__ import annotations

from collections.abc import Iterator

import pytest

import _common.loc as loc
from tests.loc_counter import reset_loc
from tests.loc_data import loc_bytes
from .combolist import parse_combo_list
from .records import combo_records
from .render import ComboRenderer

_STRINGS = {
    "checks": {"learned": "learned", "cooldown": "cooldown", "both": "learned + cooldown"},
    "weapons": {"0": "Common", "1": "Main Weapon", "2": "Awakening", "3": "Mount"},
    "awakening": {"0": "Both", "1": "Main Weapon only", "2": "Awakening only"},
    "summary": {"list": "List", "combos": "combos", "steps": "steps", "commands": "commands", "weapons": "Weapons"},
}

_LIST = """<combolist>
	<!-- ---------- 비각성 ---------- -->
	<!-- 방어 태세 -->
	<combo name="BT_skill_Defence" learn_check_skill="1019" cool_check_skill="1019" is_only_console="true" start_weapon_type="1">
		<skill name="BT_skill_Defence" call_cycle_time="1000" skill_no="1019" console_key="LB 0 0"/>
		<move name="Move" call_cycle_time="800" min_dist="0" max_dist="3000"/>
	</combo>
	<combo name="BT_Dash" learn_check_skill="349 1440" cool_check_skill="349" start_weapon_type="2">
		<skill name="BT_Dash" skill_no="349" console_key="LT 0 X"/>
	</combo>
</combolist>
<skill_command_list>
	<skill_command name="bt_skill_defence" delay_time="500" awakening_type="0">
		<command key="Q" starttime="0" endtime="300"/>
	</skill_command>
	<skill_command name="BT_Dash" awakening_type="1"><command key="Shift" starttime="0" endtime="300"/><command key="W" starttime="100" endtime="300"/></skill_command>
	<skill_command name="BT_Dash" awakening_type="2"><command key="M0" starttime="0" endtime="200"/></skill_command>
</skill_command_list>
"""

_OLDER = """<combolist>
	<Combo Name="InitCombo" StartWeaponType="1" InitCombo="True" DelayTime="1000">
		<Skill Name="BT_ATTACK_S1_1" SkillNo="349 350" Command="1"/>
	</Combo>
</combolist>
"""


@pytest.fixture(autouse=True)
def _no_loc() -> Iterator[None]:
    # Another test may leave a LOC loaded; these expect bare skill numbers.
    reset_loc()
    yield
    reset_loc()


@pytest.fixture
def _loaded_loc() -> None:
    loc.init_loc(loc_bytes([(10, 1019, 0, 0, 0, "Guard"), (10, 349, 0, 0, 0, "Forward Slash I")]))


def _records(text: str = _LIST) -> list[dict]:
    return combo_records(parse_combo_list(text), _STRINGS)


def test_combos_keep_section_note_and_steps() -> None:
    combo_list = parse_combo_list(_LIST)
    defence = combo_list.combos[0]

    assert (defence.section, defence.note) == ("비각성", "방어 태세")
    assert [(step.kind, step.name) for step in defence.steps] == [("skill", "BT_skill_Defence"), ("move", "Move")]
    assert defence.steps[0].pad_key == "LB 0 0"
    assert defence.steps[1].attrs == (("call_cycle_time", "800"), ("min_dist", "0"), ("max_dist", "3000"))
    assert [command.name for command in combo_list.commands] == ["bt_skill_defence", "BT_Dash", "BT_Dash"]


def test_records_read_weapon_console_flag_and_checks() -> None:
    defence, dash = _records()

    assert (defence["weapon"], defence["weapon_text"], defence["console_only"]) == (1, "Main Weapon", True)
    assert (dash["weapon_text"], dash["console_only"]) == ("Awakening", None)
    assert dash["learn_check"] == "349, 1440" and dash["cool_check"] == "349"


@pytest.mark.usefixtures("_loaded_loc")
def test_skill_numbers_carry_their_names() -> None:
    defence = _records()[0]
    assert defence["learn_check"] == "1019 Guard"
    assert defence["_steps"][0]["skills"] == [["1019", "Guard"]]


def test_a_step_lists_every_skill_command_of_its_name_without_case() -> None:
    defence, dash = _records()

    assert [c["keys"] for c in defence["_steps"][0]["commands"]] == ["Q 0-300"]
    assert [(c["awakening_text"], c["keys"]) for c in dash["_steps"][0]["commands"]] == [
        ("Main Weapon only", "Shift 0-300 + W 100-300"), ("Awakening only", "M0 0-200"),
    ]
    assert "[Q 0-300]" in defence["steps"]


def test_the_older_layout_reads_the_same_fields() -> None:
    (combo,) = _records(_OLDER)

    assert (combo["combo"], combo["weapon"]) == ("InitCombo", 1)
    assert combo["attributes"] == "InitCombo=True DelayTime=1000"
    step = combo["_steps"][0]
    assert ([number for number, _ in step["skills"]], step["pad_key"]) == (["349", "350"], "1")


def test_checks_show_one_line_when_both_lists_match() -> None:
    defence, dash = _records()
    renderer = ComboRenderer(_records(), _STRINGS)

    assert "learned + cooldown" in renderer.checks_cell(defence)
    assert "learned + cooldown" not in renderer.checks_cell(dash)
    assert "Main Weapon only" in renderer.steps_cell(dash)
    assert "Both" not in renderer.steps_cell(defence)


def test_skill_numbers_link_to_their_skill_dbss_rows() -> None:
    cell = ComboRenderer(_records(), _STRINGS).checks_cell(_records()[0])
    assert (
        'data-action="open-record" data-path="gamecommondata/binary/skill.dbss" '
        'data-field="skill_no" data-value="1019"'
    ) in cell
