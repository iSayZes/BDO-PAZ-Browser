"""Shared reader and registration of the sequence and cutscene script tables.

`sequencedatatable.bss`, `sequence_skill.bss`, `cutscene_skill.bss`,
`sequencetutorial_equipment.bss`, `cutscenetutorial_equipment.bss`,
`sequencetriggerdata.bss` and `videotriggerdata.bss` are PABR tables keyed by
a cutscene, sequence or video file: its name in the string table, its hash,
or both. `experiencedata.bss`, `fieldwalkingcameradata.bss` and
`tutorial_startevent.bss` hold the other script-run events. `reader.py` holds
what they share and `display.py` their shared cells; each table has its own
handler package next to this one, registered from `registration.py`.
"""
