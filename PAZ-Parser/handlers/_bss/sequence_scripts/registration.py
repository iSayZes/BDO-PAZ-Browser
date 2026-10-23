"""Registers every handler of the sequence and cutscene script tables."""

from __future__ import annotations

from bdo_preview import register_handler

from _bss.sequence_skill.handler import SequenceSkillBssHandler
from _bss.sequence_skill.parser import CUTSCENE_FILE_NAME as CUTSCENE_SKILL
from _bss.sequence_skill.parser import SEQUENCE_FILE_NAME as SEQUENCE_SKILL
from _bss.sequencedatatable.handler import SequenceDataTableBssHandler
from _bss.sequencedatatable.parser import FILE_NAME as SEQUENCE_DATA_TABLE
from _bss.tutorial_equipment.handler import TutorialEquipmentBssHandler
from _bss.tutorial_equipment.parser import CUTSCENE_FILE_NAME as CUTSCENE_EQUIPMENT
from _bss.tutorial_equipment.parser import SEQUENCE_FILE_NAME as SEQUENCE_EQUIPMENT


def register_sequence_script_handlers() -> None:
    register_handler(SEQUENCE_DATA_TABLE, SequenceDataTableBssHandler())
    for skill_table in (SEQUENCE_SKILL, CUTSCENE_SKILL):
        register_handler(skill_table, SequenceSkillBssHandler(skill_table))
    for equipment_table in (SEQUENCE_EQUIPMENT, CUTSCENE_EQUIPMENT):
        register_handler(equipment_table, TutorialEquipmentBssHandler(equipment_table))
