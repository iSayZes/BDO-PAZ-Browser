"""Shared reader and registration of the sequence and cutscene script tables.

`sequencedatatable.bss`, `sequence_skill.bss`, `cutscene_skill.bss`,
`sequencetutorial_equipment.bss` and `cutscenetutorial_equipment.bss` are PABR
tables keyed by a cutscene or sequence file: its name in the string table,
its hash, or both. `reader.py` holds what they share; each table has its own
handler package next to this one, registered from `registration.py`.
"""
