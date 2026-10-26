"""Geometry of the PAR mesh files: `.pam` static meshes, `.pcm` simple meshes
and `.pac` character meshes, for the Model view.

The layouts are in `docs/file-formats/other/mesh_pam.md`, `mesh_pcm.md` and
`mesh_pac.md`. Only what a viewer draws is read: positions, UVs, triangles
and the submesh split with each part's texture file name. A `.pac` keeps
LOD 0 of each submesh and skips its bones, palette, weights and the groups
after the submeshes.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass

import numpy as np

PAR_MAGIC = b"PAR "
# Byte 4 of a PAR header: what the file holds.
KIND_PAC = 0x03
KIND_PAM = 0x06
KIND_PCM = 0x11

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
_PAC_BONE_EXTRA_SIZE = 36
_PAC_UNKNOWN_BEFORE_SUBMESHES = 8
_PAC_LOD_COUNT = 3
_PAC_VERTEX_SIZE = 32


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
class Mesh:
    """Positions (x, y, z per vertex, centimetres), texture coordinates and a triangle list into them."""

    kind: int
    version: int
    positions: np.ndarray    # float32, shape (vertices, 3)
    uvs: np.ndarray | None   # float32, shape (vertices, 2); None for a .pcm
    indices: np.ndarray      # uint32, 3 per triangle
    submeshes: tuple[Submesh, ...]

    @property
    def vertex_count(self) -> int:
        return len(self.positions)

    @property
    def triangle_count(self) -> int:
        return len(self.indices) // _TRIANGLE_CORNERS


def parse_mesh(data: bytes) -> Mesh:
    """The geometry of a `.pam`, `.pcm` or `.pac` file; ValueError when the bytes do not fit."""
    if data[:4] != PAR_MAGIC or len(data) < 0x10:
        raise ValueError("no PAR magic")
    parser = _PARSERS.get(data[4])
    if parser is None:
        raise ValueError(f"PAR kind 0x{data[4]:02x} is not a mesh")
    return parser(data)


def _u8(data: bytes, offset: int) -> int:
    _need(data, offset, 1)
    return data[offset]


def _u16(data: bytes, offset: int) -> int:
    _need(data, offset, 2)
    return struct.unpack_from("<H", data, offset)[0]


def _u32(data: bytes, offset: int) -> int:
    _need(data, offset, 4)
    return struct.unpack_from("<I", data, offset)[0]


def _need(data: bytes, offset: int, size: int) -> None:
    if offset + size > len(data):
        raise ValueError(f"file ends at 0x{len(data):x}, needs 0x{offset + size:x}")


def _positions(data: bytes, offset: int, count: int, stride: int) -> np.ndarray:
    """`count` float32 x, y, z triples, one every `stride` bytes from `offset`."""
    _need(data, offset, count * stride)
    view = np.ndarray((count, 3), _POSITION, data, offset, (stride, _POSITION.itemsize))
    return view.astype(np.float32)


def _uvs(data: bytes, offset: int, count: int, stride: int) -> np.ndarray:
    """`count` float16 u, v pairs, one every `stride` bytes from `offset`, as float32."""
    if not count:
        return np.zeros((0, 2), np.float32)
    _need(data, offset, (count - 1) * stride + 2 * _UV.itemsize)
    view = np.ndarray((count, 2), _UV, data, offset, (stride, _UV.itemsize))
    return view.astype(np.float32)


def _indices(
    data: bytes, offset: int, count: int, vertex_count: int, index_type: np.dtype = _INDEX
) -> np.ndarray:
    """`count` vertex numbers of `index_type` from `offset`, each below `vertex_count`."""
    if count % _TRIANGLE_CORNERS:
        raise ValueError(f"index count {count} at 0x{offset:x} is not a multiple of 3")
    _need(data, offset, count * index_type.itemsize)
    indices = np.frombuffer(data, index_type, count, offset).astype(np.uint32)
    if count and int(indices.max()) >= vertex_count:
        raise ValueError(f"index at 0x{offset:x} points past the {vertex_count} vertices")
    return indices


def _name(raw: bytes) -> str:
    return raw.split(b"\0", 1)[0].decode("cp949", errors="replace")


def _expect_end(data: bytes, offset: int) -> None:
    if offset != len(data):
        raise ValueError(f"layout ends at 0x{offset:x}, file at 0x{len(data):x}")


def _parse_pam(data: bytes) -> Mesh:
    version = data[5]
    layout = _PAM_LAYOUTS.get(version)
    if layout is None:
        raise ValueError(f".pam version {version} is not known")
    record_size, name_offset, vertex_size = layout
    count = _u32(data, _PAM_MATERIAL_COUNT)
    records = [_PAM_HEADER_SIZE + i * record_size for i in range(count)]
    _need(data, _PAM_HEADER_SIZE, count * record_size)

    vertex_counts = [_u32(data, at) for at in records]
    index_counts = [_u32(data, at + 4) for at in records]
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
        base_vertex = _u32(data, at + 8)
        base_index = _u32(data, at + 12)
        if base_vertex + vertex_count > total_vertices:
            raise ValueError(f"material at 0x{at:x} reaches past the {total_vertices} vertices")
        local_start = index_start + base_index * index_type.itemsize
        local = _indices(data, local_start, index_count, vertex_count, index_type)
        parts.append(local + base_vertex)
        name = _name(data[at + name_offset:at + record_size])
        submeshes.append(Submesh(name, first_index, index_count, name))
        first_index += index_count

    _expect_end(data, index_start + sum(index_counts) * index_type.itemsize)
    return Mesh(KIND_PAM, version, positions, uvs, _joined(parts), tuple(submeshes))


def _parse_pcm(data: bytes) -> Mesh:
    vertex_count = _u32(data, _PCM_VERTEX_COUNT)
    vertex_start = _PCM_VERTEX_COUNT + 4
    positions = _positions(data, vertex_start, vertex_count, _PCM_VERTEX_SIZE)
    index_count_at = vertex_start + vertex_count * _PCM_VERTEX_SIZE
    index_count = _u32(data, index_count_at)
    indices = _indices(data, index_count_at + 4, index_count, vertex_count)
    _expect_end(data, index_count_at + 4 + index_count * _INDEX.itemsize)
    return Mesh(KIND_PCM, data[5], positions, None, indices, (Submesh("", 0, index_count, ""),))


def _pac_palette_offset(data: bytes) -> int:
    """Where the bone palette count sits, past the mesh's own bones when it has them."""
    version = data[5]
    if version == 1:
        return _PAC_V1_PALETTE
    if version not in (2, 3):
        raise ValueError(f".pac version {version} is not known")
    has_bones = _u32(data, _PAC_HAS_BONES)
    if has_bones == 0:
        return _PAC_BONE_COUNT
    if has_bones != 1:
        raise ValueError(f".pac bone flag {has_bones} at 0x10 is not 0 or 1")
    offset = _PAC_BONES
    for _ in range(_u32(data, _PAC_BONE_COUNT)):
        has_extra = _u8(data, offset + _PAC_BONE_SIZE - 1)
        if has_extra > 1:
            raise ValueError(f"bone record at 0x{offset:x} ends in {has_extra}, not 0 or 1")
        offset += _PAC_BONE_SIZE + has_extra * _PAC_BONE_EXTRA_SIZE
    return offset


def _parse_pac(data: bytes) -> Mesh:
    offset = _pac_palette_offset(data)
    offset += 1 + _u8(data, offset) * 4      # bone palette: u8 count, u32 bone ids
    offset += 1 + _u8(data, offset)          # a u8-counted byte list
    offset += _PAC_UNKNOWN_BEFORE_SUBMESHES
    submesh_count = _u16(data, offset)
    offset += 2

    positions: list[np.ndarray] = []
    uvs: list[np.ndarray] = []
    parts: list[np.ndarray] = []
    submeshes: list[Submesh] = []
    vertex_total = 0
    first_index = 0
    for _ in range(submesh_count):
        name_length = _u8(data, offset)
        _need(data, offset + 1, name_length + 2)
        name = _name(data[offset + 1:offset + 1 + name_length])
        offset += 1 + name_length + 2          # name, then a u16
        for lod in range(_PAC_LOD_COUNT):
            vertex_count = _u16(data, offset)
            vertex_start = offset + 2
            index_count_at = vertex_start + vertex_count * _PAC_VERTEX_SIZE
            index_count = _u32(data, index_count_at)
            index_start = index_count_at + 4
            if lod == 0:
                positions.append(_positions(data, vertex_start, vertex_count, _PAC_VERTEX_SIZE))
                uvs.append(_uvs(data, vertex_start + _VERTEX_UV, vertex_count, _PAC_VERTEX_SIZE))
                parts.append(_indices(data, index_start, index_count, vertex_count) + vertex_total)
                texture = name + _TEXTURE_EXT if name else ""
                submeshes.append(Submesh(name, first_index, index_count, texture))
                vertex_total += vertex_count
                first_index += index_count
            else:
                _need(data, index_start, index_count * _INDEX.itemsize)
            offset = index_start + index_count * _INDEX.itemsize

    joined = np.concatenate(positions) if positions else np.zeros((0, 3), np.float32)
    joined_uvs = np.concatenate(uvs) if uvs else np.zeros((0, 2), np.float32)
    return Mesh(KIND_PAC, data[5], joined, joined_uvs, _joined(parts), tuple(submeshes))


def _joined(parts: list[np.ndarray]) -> np.ndarray:
    return np.concatenate(parts).astype(np.uint32) if parts else np.zeros(0, np.uint32)


_PARSERS = {KIND_PAM: _parse_pam, KIND_PCM: _parse_pcm, KIND_PAC: _parse_pac}
