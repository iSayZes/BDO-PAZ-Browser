"""Bones of the PAR skeleton files (`.pab`), for the Model view.

The layout is in `docs/file-formats/other/skeleton_pab.md`. Only what posing
needs is kept: per bone its `bone_id` name hash, name, parent, the bind
pose `world_matrix` and its inverse, and the local scale, rotation and
translation. The collision shapes, constraint axes and bone volumes are
walked over so that a file that does not fit raises.

Matrices are row-major and act on row vectors (`v · M`): the translation
is the last row, and a bone's world matrix is its local matrix times its
parent's world matrix.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from par_bytes import KIND_PAB, check_par, cp949_name, expect_end, i32, need, u8, u16, u32

_SUPPORTED_VERSIONS = (2, 3, 4)
# Version 4 starts each dynamic shape with a u32 shape type and a position.
_TYPED_SHAPES_FROM = 4
_BONE_COUNT = 0x10
_BONES = 0x12
_MATRIX_SIZE = 64
# world, inverse world, local, inverse local
_MATRIX_COUNT = 4
# scale (3), rotation (4), translation (3) as f32
_LOCAL_SIZE = 40
_LOCAL = np.dtype("<f4")
_CONSTRAINT_AXIS_SIZE = 36
_TYPED_SHAPE_HEAD = 16
_VOLUME_HEAD = 4 + _MATRIX_SIZE + 2
# Shape values and the size of their body; a mesh body (2) holds its own counts.
_SHAPE_BOX = 0
_SHAPE_CYLINDER = 1
_SHAPE_MESH = 2
_SHAPE_4 = 4
_FIXED_BODIES = {_SHAPE_BOX: 12, _SHAPE_CYLINDER: 8, _SHAPE_4: 4}
_VERTEX_SIZE = 12
_INDEX_SIZE = 2


@dataclass(frozen=True)
class Skeleton:
    """The bones of a `.pab`, in file order: a parent always comes before its children.

    `world` and `inverse_world` hold one row-major 4 x 4 matrix (16 floats)
    per bone; `local` the bone's scale x, y, z, rotation x, y, z, w and
    translation x, y, z (centimetres) relative to its parent.
    """

    version: int
    bone_ids: tuple[int, ...]
    names: tuple[str, ...]
    parents: tuple[int, ...]
    world: np.ndarray          # float32, shape (bones, 16)
    inverse_world: np.ndarray  # float32, shape (bones, 16)
    local: np.ndarray          # float32, shape (bones, 10)

    @property
    def bone_count(self) -> int:
        return len(self.bone_ids)


def parse_skeleton(data: bytes) -> Skeleton:
    """The bones of a `.pab` file; ValueError when the bytes do not fit its layout."""
    version = check_par(data, KIND_PAB, "a skeleton")
    if version not in _SUPPORTED_VERSIONS:
        raise ValueError(f".pab version {version} is not known")
    count = u16(data, _BONE_COUNT)
    bone_ids: list[int] = []
    names: list[str] = []
    parents: list[int] = []
    matrices = np.zeros((count, _MATRIX_COUNT, 16), np.float32)
    local = np.zeros((count, 10), np.float32)
    offset = _BONES
    for bone in range(count):
        bone_ids.append(u32(data, offset))
        name_length = u8(data, offset + 4)
        need(data, offset + 5, name_length)
        names.append(cp949_name(data[offset + 5:offset + 5 + name_length]))
        offset += 5 + name_length
        parent = i32(data, offset)
        if not -1 <= parent < bone or (parent == -1) != (bone == 0):
            raise ValueError(f"bone {bone} at 0x{offset:x} has parent {parent}")
        parents.append(parent)
        offset += 4
        need(data, offset, _MATRIX_COUNT * _MATRIX_SIZE + _LOCAL_SIZE)
        matrices[bone] = np.frombuffer(data, _LOCAL, _MATRIX_COUNT * 16, offset).reshape(_MATRIX_COUNT, 16)
        offset += _MATRIX_COUNT * _MATRIX_SIZE
        local[bone] = np.frombuffer(data, _LOCAL, 10, offset)
        offset += _LOCAL_SIZE
        offset = _skip_dynamic_shapes(data, offset, version)
        axis_count = u8(data, offset)
        need(data, offset + 1, axis_count * _CONSTRAINT_AXIS_SIZE)
        offset += 1 + axis_count * _CONSTRAINT_AXIS_SIZE
    offset = _skip_volumes(data, offset, count)
    expect_end(data, offset)
    return Skeleton(
        version, tuple(bone_ids), tuple(names), tuple(parents),
        matrices[:, 0].copy(), matrices[:, 1].copy(), local,
    )


def _skip_dynamic_shapes(data: bytes, offset: int, version: int) -> int:
    count = u8(data, offset)
    offset += 1
    for _ in range(count):
        if version < _TYPED_SHAPES_FROM:
            offset = _skip_shape_body(data, offset, _SHAPE_MESH)
            continue
        shape = u32(data, offset)
        offset = _skip_shape_body(data, offset + _TYPED_SHAPE_HEAD, shape)
    return offset


def _skip_volumes(data: bytes, offset: int, bone_count: int) -> int:
    count = u16(data, offset)
    offset += 2
    for _ in range(count):
        parent = u32(data, offset)
        if parent >= bone_count:
            raise ValueError(f"bone volume at 0x{offset:x} names bone {parent} of {bone_count}")
        shape = u8(data, offset + _VOLUME_HEAD - 1)
        offset = _skip_shape_body(data, offset + _VOLUME_HEAD, shape)
    return offset


def _skip_shape_body(data: bytes, offset: int, shape: int) -> int:
    if shape in _FIXED_BODIES:
        need(data, offset, _FIXED_BODIES[shape])
        return offset + _FIXED_BODIES[shape]
    if shape != _SHAPE_MESH:
        raise ValueError(f"shape {shape} at 0x{offset:x} is not known")
    vertex_count = u16(data, offset)
    offset += 2 + vertex_count * _VERTEX_SIZE
    index_count = u16(data, offset)
    offset += 2 + index_count * _INDEX_SIZE
    need(data, offset, 0)
    return offset
