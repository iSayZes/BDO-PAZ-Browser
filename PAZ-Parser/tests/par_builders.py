"""Byte builders of the PAR files for the tests: .pac meshes, .pab skeletons and .paa clips.

Each builds the smallest file the layout in docs/file-formats/other/ allows,
so a test states only the fields it is about.
"""
from __future__ import annotations

import struct

import numpy as np

from _common.string_hash import KEY_HASH_SEED, hashlittle
from par_bytes import KIND_PAA, KIND_PAB, KIND_PAC

DESCRIPTOR = bytes(range(10))
TRIANGLE = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 2.0, 0.0)]
IDENTITY = struct.pack("<16f", *np.eye(4, dtype=np.float32).ravel())
_UNIT_LOCAL = struct.pack("<10f", 1, 1, 1, 0, 0, 0, 1, 0, 0, 0)
# Bytes per .paa key: u16 time, then 3, 4 or 3 half floats.
_KEY_BYTES = (8, 10, 8)


def par_header(kind: int, version: int) -> bytes:
    return b"PAR " + bytes([kind, version]) + DESCRIPTOR


def indices(*values: int) -> bytes:
    return struct.pack(f"<{len(values)}H", *values)


def vertex(position: tuple[float, float, float], size: int) -> bytes:
    """A vertex of `size` bytes: the position, then u, v as float16 at 0x10 (x and y of the position)."""
    head = struct.pack("<3f", *position) + b"\x7f" * 4 + struct.pack("<2e", position[0], position[1])
    return head.ljust(size, b"\x7f")


def pac_lod(positions: list[tuple[float, float, float]], corners: list[int]) -> bytes:
    vertices = b"".join(vertex(p, 32) for p in positions)
    return struct.pack("<H", len(positions)) + vertices + struct.pack("<I", len(corners)) + indices(*corners)


def pac_body(
    submeshes: list[tuple[str, list[tuple[float, float, float]], list[int]]],
    palette: tuple[int, ...] = (10, 11),
) -> bytes:
    """The bone palette, a 3-byte list, 8 unknown bytes, then the submeshes with 3 LODs each."""
    body = bytes([len(palette)]) + struct.pack(f"<{len(palette)}I", *palette) + bytes([3, 1, 2, 3]) + bytes(8)
    body += struct.pack("<H", len(submeshes))
    for name, positions, corners in submeshes:
        body += bytes([len(name)]) + name.encode() + struct.pack("<H", 0)
        body += pac_lod(positions, corners) + pac_lod(positions[:3], [0, 1, 2]) + pac_lod([], [])
    return body


def pac(palette: tuple[int, ...]) -> bytes:
    """A version 3 .pac without own bones: one triangle weighted to `palette`."""
    return par_header(KIND_PAC, 3) + struct.pack("<I", 0) + pac_body([("body", TRIANGLE, [0, 1, 2])], palette)


def bone_id(name: str) -> int:
    return hashlittle(name.encode("cp949"), KEY_HASH_SEED)


def pab_bone(name: str, parent: int, shapes: bytes = b"\x00", axes: int = 0) -> bytes:
    raw = name.encode("cp949")
    return (struct.pack("<IB", bone_id(name), len(raw)) + raw + struct.pack("<i", parent)
            + IDENTITY * 4 + _UNIT_LOCAL + shapes + bytes([axes]) + bytes(36 * axes))


def pab(version: int, bones: list[bytes], volumes: bytes = b"\x00\x00") -> bytes:
    return par_header(KIND_PAB, version) + struct.pack("<H", len(bones)) + b"".join(bones) + volumes


def skeleton(*names: str) -> bytes:
    """A version 3 .pab of `names` in a chain, the first the root."""
    return pab(3, [pab_bone(name, index - 1) for index, name in enumerate(names)])


def paa_keys(keys: list[tuple[int, tuple[float, ...]]]) -> bytes:
    return struct.pack("<H", len(keys)) + b"".join(
        struct.pack(f"<H{len(value)}e", time, *value) for time, value in keys
    )


def paa_node(node_bone_id: int, scale: list, rotation: list, translation: list) -> tuple[bytes, int]:
    """The node's bytes and the key bytes it adds to `key_data_size`."""
    data = struct.pack("<I", node_bone_id) + paa_keys(scale) + paa_keys(rotation) + paa_keys(translation)
    key_bytes = sum(size * len(keys) for size, keys in zip(_KEY_BYTES, (scale, rotation, translation)))
    return data, key_bytes


def paa(duration: float, nodes: list[tuple[bytes, int]], version: int = 2, key_bytes: int | None = None) -> bytes:
    total = sum(size for _, size in nodes) if key_bytes is None else key_bytes
    return (par_header(KIND_PAA, version)
            + struct.pack("<HfI", len(nodes), duration, total) + b"".join(data for data, _ in nodes))


def clip(*names: str) -> bytes:
    """A half-second .paa with one rotation key on each bone of `names`."""
    return paa(0.5, [paa_node(bone_id(name), [], [(0, (0.0, 0.0, 0.0, 1.0))], []) for name in names])
