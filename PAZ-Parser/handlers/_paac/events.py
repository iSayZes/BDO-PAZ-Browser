"""Frame events of an action chart: a u8 type, a common base, then the type's fields.

The fields per type are the "Fields on client 1784 / 3483" columns of Frame
Event Types in docs/file-formats/other/actionchart_paac.md; each kind below is
one of that doc's `... Fields` structures, written as a list of reads. The
handler shows no event, so `skip_events()` only walks past them.
"""

from __future__ import annotations

from collections.abc import Mapping

from .reader import ChartReader

# One read each: "string" (u32 table index), "u8" / "u16" / "u32", "block" (u64
# size + bytes), "rawN" (N bytes), "effect" (Effect Data), "names" (u8 count +
# string indexes), "bytes" (u8 count + bytes), "lists" (u64 count of U32 Lists).
_ATTACK = ("string", "string", "string", "u32", "block")
_ATTACK_ARROW = (*_ATTACK, *("string",) * 7, "block")
_SWITCH = ("names", "u8", "u8")

KINDS: Mapping[str, tuple[str, ...]] = {
    "base": (),
    "attack": _ATTACK,
    "attack_skill": (*_ATTACK, "block", "u8"),
    "attack_arrow": _ATTACK_ARROW,
    "attack_arrow_skill": (*_ATTACK_ARROW, "block", "u8", "u8"),
    "attack_catch": (*_ATTACK, "string", "string", "u8"),
    "attack_skill_simple": (*_ATTACK, "block", "lists"),
    "attack_arrow_skill_simple": (*_ATTACK_ARROW, "block", "lists"),
    "attack_throw": ("u16",) * 5,
    "effect_1784": ("effect", "u8", "u8"),
    "effect": ("effect", "u8", "u8", "u8"),
    "effect_ground_1784": ("effect", "u8", "u8", "string", "u32"),
    "effect_ground": ("effect", "u8", "u8", "u8", "string", "u32", "u8"),
    "switch": _SWITCH,
    "switch_chain": (*_SWITCH, "string", "string", "string", "block", "u8"),
    "switch_target": (*_SWITCH, "u8"),
    "switch_change": ("string", "string", "u8", "u8"),
    "data": ("block",),
    "camera_motion": ("raw12",),
    "camera_pulse": ("raw84",),
    "name": ("string",),
    "bubble": ("string", "u8"),
    "value": ("u32",),
    "two_values": ("u32", "u32"),
    "name_data": ("string", "block"),
    "sword_trail": ("string", "string", "block", "block"),
    "mesh": ("names", "u32", "u8"),
    "jump": ("u32", "u8"),
    "weapon": ("bytes",),
    "weapon_mesh": ("bytes", "u8"),
    "glitter": ("raw12", "string", "u8"),
    "sound_external": ("block", "string"),
    "camera": ("block", "u8"),
    "byte": ("u8",),
    "additive": ("string", "u32"),
    "two_bytes": ("u8", "u8"),
    "lua_event": ("u32", "u32", "u32", "u8", "u8"),
    "decal": ("string", "block", "u8"),
    "light": ("raw12", "u32", "string", "u8"),
    "weather": ("raw16", "u32"),
    "pose": ("u32",) * 6 + ("u8",),
    "cannon_predict": ("string", "string", "string", "u8", "raw16", "u32", "block"),
    "wave": ("u32",) * 6,
    "model_animation": ("string", "string") + ("u32",) * 5,
    "client_attack": ("u8", "u32", "raw24", "raw8", "u8"),
    "grenade": ("string", "raw12", "u32", "u32", "u32", "raw12", "u32", "u32"),
    "grenade_path": ("string", "u32", "u32", "u32", "raw12", "u8"),
    "battle_fx": ("raw12", "u32"),
    "cutscene": ("u8", "string", "u32"),
    "play_animation": ("u32",) * 5,
    "sound": ("string", "block"),
    "sound_kill": ("u8",),
    "attack_bounds": ("block", "raw33"),
}

# Type id -> kind on client 1784, in id order (0x00 to 0xAB).
_TYPES_1784 = (
    "attack", "attack_skill", "attack_arrow", "attack_arrow_skill", "attack_catch", "attack_throw",
    "effect_1784", "effect_ground_1784", "switch", "switch_chain", "switch_target", "base",
    "switch_change", "base", "data", "data", "data", "data", "camera_motion", "camera_pulse",
    "name", "name", "name", "bubble", "value", "two_values", "two_values", "data", "name_data",
    "sword_trail", "value", "value", "base", "mesh", "mesh", "jump", "weapon", "weapon",
    "weapon_mesh", "weapon_mesh", "data", "data", "data", "data", "data", "data", "glitter",
    "name_data", "data", "data", "data", "data", "sound_external", "data", "data", "data", "data",
    "data", "data", "data", "data", "data", "data", "data", "data", "data", "name_data", "name_data",
    "two_values", "two_values", "base", "base", "base", "base", "name", "data", "data", "value",
    "camera", "value", "camera", "value", "byte", "additive", "byte", "data", "base", "data", "data",
    "data", "data", "base", "data", "data", "data", "base", "base", "base", "base", "value", "value",
    "two_bytes", "base", "base", "base", "base", "base", "base", "value", "base", "base", "lua_event",
    "decal", "base", "base", "value", "byte", "value", "value", "two_values", "light", "weather",
    "base", "light", "byte", "data", "base", "base", "byte", "pose", "data", "base", "base", "base",
    "data", "cannon_predict", "base", "wave", "two_values", "two_values", "model_animation", "base",
    "light", "base", "data", "attack_skill_simple", "attack_arrow_skill_simple", "base", "base",
    "base", "base", "base", "client_attack", "base", "grenade", "attack", "grenade_path", "byte",
    "value", "value", "base", "battle_fx", "two_bytes", "base", "name_data", "data", "data", "data",
    "value", "cutscene", "base", "play_animation",
)
TYPES_1784: Mapping[int, str] = dict(enumerate(_TYPES_1784))

# Client 3483: the 1784 kinds with five changed readers. 0x34 is Sound External.
TYPES_LIVE: Mapping[int, str] = {
    **TYPES_1784,
    0x06: "effect",
    0x07: "effect_ground",
    0x30: "sound_kill",
    **{kind: "sound" for kind in range(0x31, 0x42) if kind != 0x34},
    0x86: "attack_bounds",
}

_BASE_SIZE = 7
_SET_COUNT_INDEX = 6
_EFFECT_COUNT_INDEX = 0x70


def skip_condition_set(reader: ChartReader) -> None:
    """A Condition Set: two u32 flags, then a u16 list and a 16-byte list when they are set."""
    has_list, has_wide_list = reader.u32(), reader.u32()
    if has_list:
        reader.raw(2 * reader.count())
    if has_wide_list:
        reader.raw(16 * reader.count())


def skip_effect_data(reader: ChartReader) -> None:
    """Effect Data: two strings, the parameters, then the attachments byte 0x70 of them counts."""
    reader.raw(8)
    parameters = reader.block()
    attachments = parameters[_EFFECT_COUNT_INDEX] if len(parameters) > _EFFECT_COUNT_INDEX else 0
    reader.raw(56 * attachments)


def _skip_read(reader: ChartReader, read: str) -> None:
    if read in ("string", "u32"):
        reader.raw(4)
    elif read == "u8":
        reader.raw(1)
    elif read == "u16":
        reader.raw(2)
    elif read == "block":
        reader.block()
    elif read.startswith("raw"):
        reader.raw(int(read[3:]))
    elif read == "effect":
        skip_effect_data(reader)
    elif read == "names":
        reader.raw(4 * reader.u8())
    elif read == "bytes":
        reader.raw(reader.u8())
    elif read == "lists":
        for _ in range(reader.count()):
            reader.raw(4 * reader.count())
    else:
        raise ValueError(f"unknown frame event read {read!r}")


def skip_events(reader: ChartReader, types: Mapping[int, str]) -> int:
    """Walk a u32-counted list of frame events; return the count."""
    count = reader.short_count()
    for _ in range(count):
        start = reader.pos
        event_type = reader.u8()
        kind = types.get(event_type)
        if kind is None:
            raise ValueError(f"frame event type 0x{event_type:02X} at 0x{start:X} is unknown")
        reader.raw(4)
        base = reader.block()
        if len(base) != _BASE_SIZE:
            raise ValueError(f"frame event at 0x{start:X} has a {len(base)}-byte base, not {_BASE_SIZE}")
        for _ in range(base[_SET_COUNT_INDEX]):
            skip_condition_set(reader)
        for read in KINDS[kind]:
            _skip_read(reader, read)
    return count
