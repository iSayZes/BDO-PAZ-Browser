"""Joins from other pet tables into `pet.dbss` and the talent catalog.

`pet.dbss` (with `petoffset.dbss`) keys every pet by `pet_id` and stores the
fusion key (`variant`, `species`, `unknown_04`, `tier`) and the
`change_look_key` that `petoldfusion.dbss`, `possiblefusionpet.bss` and
`petchangelook.dbss` key their rows by. Section 2 of `petequipskill.bss`
names the talents (`base_skill_id`).
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable, Hashable, Iterable
from typing import TypeVar

from _bss.petequipskill.parser import parse_petequipskill_records
from _common.character import character_name
from _common.equipskill_roll import equip_skill_name
from .parser import parse_pet_records


PET_FILE = "pet.dbss"
PET_OFFSET_FILE = "petoffset.dbss"
SKILL_CATALOG_FILE = "petequipskill.bss"
# base_skill_id keys Section 2 of the catalog (Pet_BaseSkill_Table).
_BASE_SKILL_SECTION = "S2"
_NAME_SEPARATOR = ", "

# The four fusion key bytes, low byte first: the u32 a fusion table keys by.
_FUSION_KEY_SHIFTS = (0, 8, 16, 24)

K = TypeVar("K", bound=Hashable)


def pet_companion_paths(folder: str) -> list[str]:
    """`pet.dbss` and its offset index in the PAZ `folder`."""
    return [f"{folder}/{PET_FILE}", f"{folder}/{PET_OFFSET_FILE}"]


def fusion_key(variant: int, species: int, zero: int, tier: int) -> int:
    """The u32 fusion key of the four key bytes, as the fusion tables store it."""
    return sum(value << shift for value, shift in zip((variant, species, zero, tier), _FUSION_KEY_SHIFTS))


def fusion_key_text(value: int) -> str:
    """A fusion key as `0x03012801`: tier, zero byte, species, variant from the left."""
    return f"0x{value:08X}"


def pet_fusion_key(pet: dict) -> int:
    """The fusion key of a `pet.dbss` record."""
    return fusion_key(pet["variant"], pet["species"], pet["unknown_04"], pet["tier"])


def pet_ids_by(companions: dict[str, bytes], key: Callable[[dict], K]) -> dict[K, list[int]]:
    """`key(pet) -> pet_ids` over every `pet.dbss` record, in file order; empty without the two files.

    Raises ValueError when `pet.dbss` cannot be parsed.
    """
    pet_raw = companions.get(PET_FILE)
    offset_raw = companions.get(PET_OFFSET_FILE)
    if pet_raw is None or offset_raw is None:
        return {}

    grouped: dict[K, list[int]] = defaultdict(list)
    for pet in parse_pet_records(pet_raw, offset_raw):
        grouped[key(pet)].append(pet["pet_id"])
    return dict(grouped)


def pet_names_text(pet_ids: Iterable[int]) -> str:
    """The distinct names of the pets (LOC, else Korean), in order, comma-separated."""
    names = dict.fromkeys(name for name in map(character_name, pet_ids) if name)
    return _NAME_SEPARATOR.join(names)


def base_skill_names(catalog: bytes | None) -> dict[int, str]:
    """`base_skill_id -> talent name` from Section 2 of `petequipskill.bss`; empty without it."""
    if catalog is None:
        return {}

    return {
        record["equip_skill_id"]: equip_skill_name(record["skill_no"])
        for record in parse_petequipskill_records(catalog)
        if record["section"] == _BASE_SKILL_SECTION
    }
