"""Registers every handler of the sequence and cutscene script tables."""

from __future__ import annotations

from bdo_preview import register_handler

from _bss.experiencedata.handler import ExperienceDataBssHandler
from _bss.experiencedata.parser import FILE_NAME as EXPERIENCE_DATA
from _bss.fieldwalkingcameradata.handler import FieldWalkingCameraDataBssHandler
from _bss.fieldwalkingcameradata.parser import FILE_NAME as FIELD_WALKING_CAMERA_DATA
from _bss.sequence_skill.handler import SequenceSkillBssHandler
from _bss.sequence_skill.parser import CUTSCENE_FILE_NAME as CUTSCENE_SKILL
from _bss.sequence_skill.parser import SEQUENCE_FILE_NAME as SEQUENCE_SKILL
from _bss.sequencedatatable.handler import SequenceDataTableBssHandler
from _bss.sequencedatatable.parser import FILE_NAME as SEQUENCE_DATA_TABLE
from _bss.sequencetriggerdata.handler import SequenceTriggerDataBssHandler
from _bss.sequencetriggerdata.parser import FILE_NAME as SEQUENCE_TRIGGER_DATA
from _bss.tutorial_equipment.handler import TutorialEquipmentBssHandler
from _bss.tutorial_equipment.parser import CUTSCENE_FILE_NAME as CUTSCENE_EQUIPMENT
from _bss.tutorial_equipment.parser import SEQUENCE_FILE_NAME as SEQUENCE_EQUIPMENT
from _bss.tutorial_startevent.handler import TutorialStartEventBssHandler
from _bss.tutorial_startevent.parser import FILE_NAME as TUTORIAL_START_EVENT
from _bss.videotriggerdata.handler import VideoTriggerDataBssHandler
from _bss.videotriggerdata.parser import FILE_NAME as VIDEO_TRIGGER_DATA


def register_sequence_script_handlers() -> None:
    register_handler(SEQUENCE_DATA_TABLE, SequenceDataTableBssHandler())
    for skill_table in (SEQUENCE_SKILL, CUTSCENE_SKILL):
        register_handler(skill_table, SequenceSkillBssHandler(skill_table))
    for equipment_table in (SEQUENCE_EQUIPMENT, CUTSCENE_EQUIPMENT):
        register_handler(equipment_table, TutorialEquipmentBssHandler(equipment_table))
    register_handler(VIDEO_TRIGGER_DATA, VideoTriggerDataBssHandler())
    register_handler(SEQUENCE_TRIGGER_DATA, SequenceTriggerDataBssHandler())
    register_handler(FIELD_WALKING_CAMERA_DATA, FieldWalkingCameraDataBssHandler())
    register_handler(EXPERIENCE_DATA, ExperienceDataBssHandler())
    register_handler(TUTORIAL_START_EVENT, TutorialStartEventBssHandler())
