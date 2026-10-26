"""Geometry of the PAR mesh files: `.pam` static meshes, `.pcm` simple meshes
and `.pac` character meshes, for the Model view.

The layouts are in `docs/file-formats/other/mesh_pam.md`, `mesh_pcm.md` and
`mesh_pac.md`. Only what a viewer draws is read: positions, UVs, triangles
and the submesh split with each part's texture file name. A `.pac` keeps
LOD 0 of each submesh with its skin (the bone palette and each vertex's bone
indices and weights, for posing it on a `.pab` skeleton) and skips the
matrices of its own bones and the groups after the submeshes.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from par_bytes import (
    KIND_PAC, KIND_PAM, KIND_PCM, PAR_HEADER_SIZE, PAR_MAGIC, cp949_name, expect_end, need, u8, u16, u32,
)

_POSITION = np.dtype("<f4")
_UV = np.dtype("<f2")
_INDEX = np.dtype("<u2")
_INDEX32 = np.dtype("<u4")
_TEXTURE_EXT = ".dds"
_TRIANGLE_CORNERS = 3

# .pam: header, then one material record per submesh, then all vertices, then all indices.
_PAM_HEADER_SIZE = 0x410
_PAM_MATERIAL_COUNT = 0x10
# 1 when the indices are u32: only files with a material of more than 65,535 vertices.
_PAM_U32_INDICES = 0x36
_VERTEX_UV = 0x10
# Per version: material record size, offset of the texture name in it, vertex size.
_PAM_LAYOUTS: dict[int, tuple[int, int, int]] = {
    4: (0x110, 0x10, 28),
    5: (0x114, 0x14, 28),
    6: (0x110, 0x10, 32),
}

# .pcm: vertex count, positions, index count, indices.
_PCM_VERTEX_COUNT = 0x10
_PCM_VERTEX_SIZE = 12

# .pac: a version 1 header puts the bone palette count at 0x10; versions 2 and 3
# have a u32 at 0x10 that is 1 when the mesh carries its own bones.
_PAC_V1_PALETTE = 0x10
_PAC_HAS_BONES = 0x10
_PAC_BONE_COUNT = 0x14
_PAC_BONES = 0x18
_PAC_BONE_SIZE = 306
# A bone record ends in its constraint axis count (0 or 1), then 36 bytes per axis.
_PAC_CONSTRAINT_AXIS_SIZE = 36
_PAC_UNKNOWN_BEFORE_SUBMESHES = 8
_PAC_LOD_COUNT = 3
_PAC_VERTEX_SIZE = 32
# Four u8 bone indices into the palette, then four u8 weights, at the end of a vertex.
_PAC_VERTEX_BONES = 0x18
_PAC_VERTEX_WEIGHTS = 0x1C
_BONES_PER_VERTEX = 4
_BONE_ID = np.dtype("<u4")


@dataclass(frozen=True)
class Submesh:
    """A run of triangles: the texture file name (`.pam`), the mesh name (`.pac`) or "" (`.pcm`).

    `texture` is the file name of its texture, "" when it has none.
    """

    name: str
    first_index: int
    index_count: int
    texture: str


@dataclass(frozen=True)
class Skin:
    """How a `.pac` vertex follows the bones: four palette indices and four weights per vertex.

    `palette` holds the `bone_id` name hashes the indices point at;
    `own_bone_ids` the ids of the bones the mesh carries itself, which a
    skeleton need not hold. The weights add up to about 255.
    """

    palette: tuple[int, ...]
    own_bone_ids: tuple[int, ...]
    bone_indices: np.ndarray  # uint8, shape (vertices, 4)
    bone_weights: np.ndarray  # uint8, shape (vertices, 4)


@dataclass(frozen=True)
class Mesh:
    """Positions (x, y, z per vertex, centimetres), texture coordinates and a triangle list into them."""

    kind: int
    version: int
    positions: np.ndarray    # float32, shape (vertices, 3)
    uvs: np.ndarray | None   # float32, shape (vertices, 2); None for a .pcm
    indices: np.ndarray      # uint32, 3 per triangle
    submeshes: tuple[Submesh, ...]
    skin: Skin | None = None  # a .pac only

    @property
    def vertex_count(self) -> int:
        return len(self.positions)

    @property
    def triangle_count(self) -> int:
        return len(self.indices) // _TRIANGLE_CORNERS


def parse_mesh(data: bytes) -> Mesh:
    """The geometry of a `.pam`, `.pcm` or `.pac` file; ValueError when the bytes do not fit."""
    if data[:4] != PAR_MAGIC or len(data) < PAR_HEADER_SIZE:
        raise ValueError("no PAR magic")
    parser = _PARSERS.get(data[4])
    if parser is None:
        raise ValueError(f"PAR kind 0x{data[4]:02x} is not a mesh")
    return parser(data)


def _positions(data: bytes, offset: int, count: int, stride: int) -> np.ndarray:
    """`count` float32 x, y, z triples, one every `stride` bytes from `offset`."""
    need(data, offset, count * stride)
    view = np.ndarray((count, 3), _POSITION, data, offset, (stride, _POSITION.itemsize))
    return view.astype(np.float32)


def _uvs(data: bytes, offset: int, count: int, stride: int) -> np.ndarray:
    """`count` float16 u, v pairs, one every `stride` bytes from `offset`, as float32."""
    if not count:
        return np.zeros((0, 2), np.float32)
    need(data, offset, (count - 1) * stride + 2 * _UV.itemsize)
    view = np.ndarray((count, 2), _UV, data, offset, (stride, _UV.itemsize))
    return view.astype(np.float32)


def _indices(
    data: bytes, offset: int, count: int, vertex_count: int, index_type: np.dtype = _INDEX
) -> np.ndarray:
    """`count` vertex numbers of `index_type` from `offset`, each below `vertex_count`."""
    if count % _TRIANGLE_CORNERS:
        raise ValueError(f"index count {count} at 0x{offset:x} is not a multiple of 3")
    need(data, offset, count * index_type.itemsize)
    indices = np.frombuffer(data, index_type, count, offset).astype(np.uint32)
    if count and int(indices.max()) >= vertex_count:
        raise ValueError(f"index at 0x{offset:x} points past the {vertex_count} vertices")
    return indices


def _parse_pam(data: bytes) -> Mesh:
    version = data[5]
    layout = _PAM_LAYOUTS.get(version)
    if layout is None:
        raise ValueError(f".pam version {version} is not known")
    record_size, name_offset, vertex_size = layout
    count = u32(data, _PAM_MATERIAL_COUNT)
    records = [_PAM_HEADER_SIZE + i * record_size for i in range(count)]
    need(data, _PAM_HEADER_SIZE, count * record_size)

    vertex_counts = [u32(data, at) for at in records]
    index_counts = [u32(data, at + 4) for at in records]
    total_vertices = sum(vertex_counts)
    index_type = _INDEX32 if data[_PAM_U32_INDICES] else _INDEX
    vertex_start = _PAM_HEADER_SIZE + count * record_size
    index_start = vertex_start + total_vertices * vertex_size

    positions = _positions(data, vertex_start, total_vertices, vertex_size)
    uvs = _uvs(data, vertex_start + _VERTEX_UV, total_vertices, vertex_size)
    parts: list[np.ndarray] = []
    submeshes: list[Submesh] = []
    first_index = 0
    for at, vertex_count, index_count in zip(records, vertex_counts, index_counts):
        base_vertex = u32(data, at + 8)
        base_index = u32(data, at + 12)
        if base_vertex + vertex_count > total_vertices:
            raise ValueError(f"material at 0x{at:x} reaches past the {total_vertices} vertices")
        local_start = index_start + base_index * index_type.itemsize
        local = _indices(data, local_start, index_count, vertex_count, index_type)
        parts.append(local + base_vertex)
        name = cp949_name(data[at + name_offset:at + record_size])
        submeshes.append(Submesh(name, first_index, index_count, name))
        first_index += index_count

    expect_end(data, index_start + sum(index_counts) * index_type.itemsize)
    return Mesh(KIND_PAM, version, positions, uvs, _joined(parts), tuple(submeshes))


def _parse_pcm(data: bytes) -> Mesh:
    vertex_count = u32(data, _PCM_VERTEX_COUNT)
    vertex_start = _PCM_VERTEX_COUNT + 4
    positions = _positions(data, vertex_start, vertex_count, _PCM_VERTEX_SIZE)
    index_count_at = vertex_start + vertex_count * _PCM_VERTEX_SIZE
    index_count = u32(data, index_count_at)
    indices = _indices(data, index_count_at + 4, index_count, vertex_count)
    expect_end(data, index_count_at + 4 + index_count * _INDEX.itemsize)
    return Mesh(KIND_PCM, data[5], positions, None, indices, (Submesh("", 0, index_count, ""),))


def _pac_own_bones(data: bytes) -> tuple[tuple[int, ...], int]:
    """The ids of the mesh's own bones and where the bone palette count sits after them."""
    version = data[5]
    if version == 1:
        return (), _PAC_V1_PALETTE
    if version not in (2, 3):
        raise ValueError(f".pac version {version} is not known")
    has_bones = u32(data, _PAC_HAS_BONES)
    if has_bones == 0:
        return (), _PAC_BONE_COUNT
    if has_bones != 1:
        raise ValueError(f".pac bone flag {has_bones} at 0x10 is not 0 or 1")
    offset = _PAC_BONES
    bone_ids: list[int] = []
    for _ in range(u32(data, _PAC_BONE_COUNT)):
        bone_ids.append(u32(data, offset))
        axis_count = u8(data, offset + _PAC_BONE_SIZE - 1)
        if axis_count > 1:
            raise ValueError(f"bone record at 0x{offset:x} has {axis_count} constraint axes, not 0 or 1")
        offset += _PAC_BONE_SIZE + axis_count * _PAC_CONSTRAINT_AXIS_SIZE
    return tuple(bone_ids), offset


def _vertex_bytes(data: bytes, offset: int, count: int) -> np.ndarray:
    """The 4 bytes at `offset` of each of `count` .pac vertices, one row per vertex."""
    need(data, offset, (count - 1) * _PAC_VERTEX_SIZE + _BONES_PER_VERTEX if count else 0)
    view = np.ndarray((count, _BONES_PER_VERTEX), np.uint8, data, offset, (_PAC_VERTEX_SIZE, 1))
    return view.copy()


def _parse_pac(data: bytes) -> Mesh:
    own_bone_ids, offset = _pac_own_bones(data)
    palette_count = u8(data, offset)
    need(data, offset + 1, palette_count * _BONE_ID.itemsize)
    palette = tuple(int(bone_id) for bone_id in np.frombuffer(data, _BONE_ID, palette_count, offset + 1))
    offset += 1 + palette_count * _BONE_ID.itemsize
    offset += 1 + u8(data, offset)          # a u8-counted byte list
    offset += _PAC_UNKNOWN_BEFORE_SUBMESHES
    submesh_count = u16(data, offset)
    offset += 2

    positions: list[np.ndarray] = []
    uvs: list[np.ndarray] = []
    bone_indices: list[np.ndarray] = []
    bone_weights: list[np.ndarray] = []
    parts: list[np.ndarray] = []
    submeshes: list[Submesh] = []
    vertex_total = 0
    first_index = 0
    for _ in range(submesh_count):
        name_length = u8(data, offset)
        need(data, offset + 1, name_length + 2)
        name = cp949_name(data[offset + 1:offset + 1 + name_length])
        offset += 1 + name_length + 2          # name, then a u16
        for lod in range(_PAC_LOD_COUNT):
            vertex_count = u16(data, offset)
            vertex_start = offset + 2
            index_count_at = vertex_start + vertex_count * _PAC_VERTEX_SIZE
            index_count = u32(data, index_count_at)
            index_start = index_count_at + 4
            if lod == 0:
                positions.append(_positions(data, vertex_start, vertex_count, _PAC_VERTEX_SIZE))
                uvs.append(_uvs(data, vertex_start + _VERTEX_UV, vertex_count, _PAC_VERTEX_SIZE))
                bone_indices.append(_vertex_bytes(data, vertex_start + _PAC_VERTEX_BONES, vertex_count))
                bone_weights.append(_vertex_bytes(data, vertex_start + _PAC_VERTEX_WEIGHTS, vertex_count))
                parts.append(_indices(data, index_start, index_count, vertex_count) + vertex_total)
                texture = name + _TEXTURE_EXT if name else ""
                submeshes.append(Submesh(name, first_index, index_count, texture))
                vertex_total += vertex_count
                first_index += index_count
            else:
                need(data, index_start, index_count * _INDEX.itemsize)
            offset = index_start + index_count * _INDEX.itemsize

    joined = np.concatenate(positions) if positions else np.zeros((0, 3), np.float32)
    joined_uvs = np.concatenate(uvs) if uvs else np.zeros((0, 2), np.float32)
    skin = Skin(palette, own_bone_ids, _joined_bones(bone_indices), _joined_bones(bone_weights))
    return Mesh(KIND_PAC, data[5], joined, joined_uvs, _joined(parts), tuple(submeshes), skin)


def _joined_bones(parts: list[np.ndarray]) -> np.ndarray:
    return np.concatenate(parts) if parts else np.zeros((0, _BONES_PER_VERTEX), np.uint8)


def _joined(parts: list[np.ndarray]) -> np.ndarray:
    return np.concatenate(parts).astype(np.uint32) if parts else np.zeros(0, np.uint32)


_PARSERS = {KIND_PAM: _parse_pam, KIND_PCM: _parse_pcm, KIND_PAC: _parse_pac}
