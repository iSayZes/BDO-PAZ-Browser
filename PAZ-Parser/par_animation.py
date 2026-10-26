"""Keys of the PAR animation files (`.paa`), for the Model view.

The layout is in `docs/file-formats/other/animation_paa.md`. A clip holds
one node per bone, named by the `.pab` `bone_id` hash, with scale, rotation
and translation keys relative to the parent bone. Version 1 (one clip on
client 3483) stores i16 fixed point whose translation scale is not known,
so only version 2 is read.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from par_bytes import KIND_PAA, check_par, expect_end, f32, need, u16, u32

_SUPPORTED_VERSION = 2
_NODE_COUNT = 0x10
_DURATION = 0x12
_KEY_DATA_SIZE = 0x16
_NODES = 0x1A
_TIME = np.dtype("<u2")
# Components per key: scale x, y, z; rotation x, y, z, w; translation x, y, z.
_SCALE_SIZE = 3
_ROTATION_SIZE = 4
_TRANSLATION_SIZE = 3
_COMPONENT_SIZES = (_SCALE_SIZE, _ROTATION_SIZE, _TRANSLATION_SIZE)


@dataclass(frozen=True)
class Track:
    """Keys of one channel: `times` in milliseconds, rising from 0, and one value row per key."""

    times: np.ndarray   # uint16, shape (keys,)
    values: np.ndarray  # float32, shape (keys, components)


@dataclass(frozen=True)
class AnimationNode:
    bone_id: int
    scale: Track
    rotation: Track      # quaternion x, y, z, w
    translation: Track   # centimetres


@dataclass(frozen=True)
class Animation:
    duration: float      # seconds
    nodes: tuple[AnimationNode, ...]


def parse_animation(data: bytes) -> Animation:
    """The nodes and keys of a `.paa` file; ValueError when the bytes do not fit its layout."""
    version = check_par(data, KIND_PAA, "an animation")
    if version != _SUPPORTED_VERSION:
        raise ValueError(f".paa version {version} is not read (only version {_SUPPORTED_VERSION})")
    count = u16(data, _NODE_COUNT)
    duration = f32(data, _DURATION)
    key_data_size = u32(data, _KEY_DATA_SIZE)
    offset = _NODES
    key_bytes = 0
    nodes: list[AnimationNode] = []
    for _ in range(count):
        bone_id = u32(data, offset)
        offset += 4
        tracks: list[Track] = []
        for components in _COMPONENT_SIZES:
            track, offset = _track(data, offset, components)
            key_bytes += len(track.times) * (_TIME.itemsize * (1 + components))
            tracks.append(track)
        nodes.append(AnimationNode(bone_id, *tracks))
    expect_end(data, offset)
    if key_bytes != key_data_size:
        raise ValueError(f"the keys take {key_bytes} bytes, the header says {key_data_size}")
    return Animation(duration, tuple(nodes))


def _track(data: bytes, offset: int, components: int) -> tuple[Track, int]:
    count = u16(data, offset)
    key = np.dtype([("time", _TIME), ("value", "<f2", (components,))])
    need(data, offset + 2, count * key.itemsize)
    keys = np.frombuffer(data, key, count, offset + 2)
    times = keys["time"].copy()
    if count and (times[0] != 0 or np.any(np.diff(times.astype(np.int32)) <= 0)):
        raise ValueError(f"key times at 0x{offset:x} do not rise from 0")
    track = Track(times, keys["value"].astype(np.float32))
    return track, offset + 2 + count * key.itemsize
