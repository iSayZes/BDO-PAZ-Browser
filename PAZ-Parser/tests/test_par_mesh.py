"""The PAR meshes (.pam, .pcm, .pac): geometry read by par_mesh.py and the Model view."""
from __future__ import annotations

import base64
import html as _html
import json
import re
import struct

import numpy as np
import pytest

from bdo_models import PazEntry
from bdo_preview import ModelHandler, get_handler, has_parsed_view
from par_mesh import KIND_PAC, KIND_PAM, KIND_PCM, Mesh, parse_mesh
from tests.fixtures import FIXTURES_DIR, fetch_missing

_DESCRIPTOR = bytes(range(10))
_TRIANGLE = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 2.0, 0.0)]
_PAM_U32_INDICES = 0x36


def _vertex(position: tuple[float, float, float], size: int) -> bytes:
    """A vertex of `size` bytes: the position, then u, v as float16 at 0x10 (x and y of the position)."""
    head = struct.pack("<3f", *position) + b"\x7f" * 4 + struct.pack("<2e", position[0], position[1])
    return head.ljust(size, b"\x7f")


def _par_header(kind: int, version: int) -> bytes:
    return b"PAR " + bytes([kind, version]) + _DESCRIPTOR


def _indices(*values: int) -> bytes:
    return struct.pack(f"<{len(values)}H", *values)


def _pam(
    version: int,
    materials: list[tuple[list[tuple[float, float, float]], list[int], str]],
    wide_indices: bool = False,
) -> bytes:
    """A .pam: each material is (positions, local indices, texture name)."""
    record_size, name_offset, vertex_size = {4: (0x110, 0x10, 28), 5: (0x114, 0x14, 28), 6: (0x110, 0x10, 32)}[version]
    header = bytearray(0x410)
    header[:4] = b"PAR "
    header[4:6] = bytes([KIND_PAM, version])
    struct.pack_into("<I", header, 0x10, len(materials))
    header[_PAM_U32_INDICES] = int(wide_indices)
    records = b""
    vertices = b""
    indices = b""
    base_vertex = base_index = 0
    for positions, local, name in materials:
        record = bytearray(record_size)
        struct.pack_into("<IIII", record, 0, len(positions), len(local), base_vertex, base_index)
        record[name_offset:name_offset + len(name)] = name.encode()
        records += record
        vertices += b"".join(_vertex(position, vertex_size) for position in positions)
        indices += struct.pack(f"<{len(local)}I", *local) if wide_indices else _indices(*local)
        base_vertex += len(positions)
        base_index += len(local)
    return bytes(header) + records + vertices + indices


def _pcm(positions: list[tuple[float, float, float]], indices: list[int]) -> bytes:
    body = struct.pack("<I", len(positions)) + b"".join(struct.pack("<3f", *p) for p in positions)
    return _par_header(KIND_PCM, 2) + body + struct.pack("<I", len(indices)) + _indices(*indices)


def _pac_lod(positions: list[tuple[float, float, float]], indices: list[int]) -> bytes:
    vertices = b"".join(_vertex(p, 32) for p in positions)
    return struct.pack("<H", len(positions)) + vertices + struct.pack("<I", len(indices)) + _indices(*indices)


def _pac_body(submeshes: list[tuple[str, list[tuple[float, float, float]], list[int]]]) -> bytes:
    """Bone palette of 2 ids, a 3-byte list, 8 unknown bytes, then the submeshes with 3 LODs each."""
    body = bytes([2]) + struct.pack("<II", 10, 11) + bytes([3, 1, 2, 3]) + bytes(8)
    body += struct.pack("<H", len(submeshes))
    for name, positions, indices in submeshes:
        body += bytes([len(name)]) + name.encode() + struct.pack("<H", 0)
        body += _pac_lod(positions, indices) + _pac_lod(positions[:3], [0, 1, 2]) + _pac_lod([], [])
    return body


def _bone(has_extra: bool) -> bytes:
    """A 306-byte bone record: id, parent, matrices and SRT, then the extra flag."""
    record = bytearray(306)
    struct.pack_into("<Ii", record, 0, 7, -1)
    record[305] = int(has_extra)
    return bytes(record) + (bytes(36) if has_extra else b"")


def test_pam_joins_materials_and_offsets_their_indices() -> None:
    square = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (1.0, 1.0, 0.0), (0.0, 1.0, 0.0)]
    mesh = parse_mesh(_pam(5, [(_TRIANGLE, [0, 1, 2], "rock.dds"), (square, [0, 1, 2, 0, 2, 3], "moss.dds")]))

    assert (mesh.kind, mesh.version, mesh.vertex_count, mesh.triangle_count) == (KIND_PAM, 5, 7, 3)
    assert mesh.indices.tolist() == [0, 1, 2, 3, 4, 5, 3, 5, 6]
    assert mesh.positions[4].tolist() == [1.0, 0.0, 0.0]
    assert [(s.name, s.first_index, s.index_count, s.texture) for s in mesh.submeshes] == [
        ("rock.dds", 0, 3, "rock.dds"),
        ("moss.dds", 3, 6, "moss.dds"),
    ]


@pytest.mark.parametrize("version", [4, 5, 6])
def test_pam_reads_each_version_stride(version: int) -> None:
    mesh = parse_mesh(_pam(version, [(_TRIANGLE, [0, 1, 2], "a.dds")]))

    assert mesh.positions.tolist() == [list(p) for p in _TRIANGLE]
    assert mesh.uvs is not None
    assert mesh.uvs.tolist() == [[x, y] for x, y, _ in _TRIANGLE]
    assert mesh.submeshes[0].name == "a.dds"


def test_pam_reads_u32_indices_when_flagged_at_0x36() -> None:
    mesh = parse_mesh(_pam(5, [(_TRIANGLE, [0, 2, 1], "a.dds")], wide_indices=True))

    assert mesh.indices.tolist() == [0, 2, 1]


def test_pam_with_u16_indices_does_not_fit_a_u32_flag() -> None:
    data = bytearray(_pam(5, [(_TRIANGLE, [0, 2, 1], "a.dds")]))
    data[_PAM_U32_INDICES] = 1
    with pytest.raises(ValueError):
        parse_mesh(bytes(data))


def test_pam_rejects_bytes_past_the_layout() -> None:
    with pytest.raises(ValueError, match="layout ends"):
        parse_mesh(_pam(6, [(_TRIANGLE, [0, 1, 2], "a.dds")]) + b"\0")


def test_pam_rejects_an_index_past_its_material() -> None:
    with pytest.raises(ValueError, match="points past"):
        parse_mesh(_pam(4, [(_TRIANGLE, [0, 1, 3], "a.dds")]))


def test_pcm_is_one_untextured_submesh() -> None:
    mesh = parse_mesh(_pcm(_TRIANGLE, [0, 2, 1]))

    assert (mesh.kind, mesh.triangle_count, mesh.uvs) == (KIND_PCM, 1, None)
    assert mesh.indices.tolist() == [0, 2, 1]
    assert [(s.name, s.first_index, s.index_count, s.texture) for s in mesh.submeshes] == [("", 0, 3, "")]


def test_pcm_rejects_a_partial_triangle() -> None:
    with pytest.raises(ValueError, match="multiple of 3"):
        parse_mesh(_pcm(_TRIANGLE, [0, 1]))


def test_pac_keeps_lod_0_of_each_submesh() -> None:
    quad = [*_TRIANGLE, (1.0, 2.0, 0.0)]
    data = _par_header(KIND_PAC, 3) + struct.pack("<I", 0) + _pac_body(
        [("body", quad, [0, 1, 2, 1, 3, 2]), ("", _TRIANGLE, [0, 1, 2])]
    )
    mesh = parse_mesh(data)

    assert (mesh.kind, mesh.version, mesh.vertex_count, mesh.triangle_count) == (KIND_PAC, 3, 7, 3)
    assert mesh.indices.tolist() == [0, 1, 2, 1, 3, 2, 4, 5, 6]
    assert mesh.uvs is not None
    assert mesh.uvs[3].tolist() == [1.0, 2.0]
    assert [(s.name, s.first_index, s.index_count, s.texture) for s in mesh.submeshes] == [
        ("body", 0, 6, "body.dds"),
        ("", 6, 3, ""),
    ]


def test_pac_version_1_has_the_palette_at_0x10() -> None:
    mesh = parse_mesh(_par_header(KIND_PAC, 1) + _pac_body([("hair", _TRIANGLE, [0, 1, 2])]))

    assert mesh.positions.tolist() == [list(p) for p in _TRIANGLE]


def test_pac_skips_the_mesh_own_bones() -> None:
    bones = struct.pack("<II", 1, 2) + _bone(has_extra=False) + _bone(has_extra=True)
    mesh = parse_mesh(_par_header(KIND_PAC, 2) + bones + _pac_body([("blade", _TRIANGLE, [0, 1, 2])]))

    assert [s.name for s in mesh.submeshes] == ["blade"]
    assert mesh.triangle_count == 1


def test_pac_with_no_submeshes_is_an_empty_mesh() -> None:
    mesh = parse_mesh(_par_header(KIND_PAC, 3) + struct.pack("<I", 0) + _pac_body([]))

    assert (mesh.vertex_count, mesh.triangle_count, mesh.submeshes) == (0, 0, ())


def test_pac_rejects_a_bone_flag_other_than_0_or_1() -> None:
    with pytest.raises(ValueError, match="bone flag"):
        parse_mesh(_par_header(KIND_PAC, 3) + struct.pack("<I", 2) + _pac_body([]))


@pytest.mark.parametrize(
    ("data", "message"),
    [(b"PABR" + bytes(20), "no PAR magic"), (_par_header(0x01, 3) + bytes(8), "not a mesh")],
)
def test_parse_rejects_files_that_are_not_meshes(data: bytes, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        parse_mesh(data)


# Small client files with a name no other file has, one per PAR kind and
# version branch of the parser; pem_00_gtb_0033_01.pac carries its own bones.
_FIXTURES = {
    "barricade_metal_01_hh_nr.pam": KIND_PAM,
    "sectorhlod_-19_-1_-6_2_9.pam": KIND_PAM,
    "devildom_lava_08a.pam": KIND_PAM,
    "ex_ogremine_01.pcm": KIND_PCM,
    "pvw_00_customizing_body_rfinger4_pick.pac": KIND_PAC,
    "psw_00_customizing_eye_right_down_pick.pac": KIND_PAC,
    "pem_00_gtb_0033_01.pac": KIND_PAC,
}


def _assert_well_formed(mesh: Mesh) -> None:
    assert mesh.triangle_count > 0
    assert int(mesh.indices.max()) < mesh.vertex_count
    assert np.isfinite(mesh.positions).all()
    assert mesh.uvs is None or (mesh.uvs.shape == (mesh.vertex_count, 2) and np.isfinite(mesh.uvs).all())
    first = 0
    for part in mesh.submeshes:
        assert part.first_index == first
        first += part.index_count
    assert first == len(mesh.indices)


@pytest.mark.parametrize(("name", "kind"), _FIXTURES.items())
def test_client_mesh_parses(name: str, kind: int) -> None:
    fetch_missing([name])
    mesh = parse_mesh((FIXTURES_DIR / name).read_bytes())

    assert mesh.kind == kind
    _assert_well_formed(mesh)


def _entry(path: str) -> PazEntry:
    return PazEntry("pad00001.paz", path, 0, 0, 0, 0, 0)


@pytest.mark.parametrize("name", ["rock.pam", "rock.pcm", "body.pac"])
def test_meshes_open_in_the_model_view(name: str) -> None:
    handler = get_handler(name, name[name.rfind("."):])

    assert isinstance(handler, ModelHandler)
    assert not has_parsed_view(handler)


def _stage(html: str) -> dict[str, str]:
    return {key: _html.unescape(value) for key, value in re.findall(r'data-(\w+)="([^"]*)"', html)}


def _shading_modes(html: str) -> list[str]:
    return re.findall(r'data-action="model-shading" data-value="(\w+)"', html)


def test_model_view_carries_the_geometry() -> None:
    html = ModelHandler().render(_pcm(_TRIANGLE, [0, 1, 2]), _entry("object/rock.pcm"), {})
    stage = _stage(html)

    positions = np.frombuffer(base64.b64decode(stage["positions"]), "<f4").reshape(-1, 3)
    assert positions.tolist() == [list(p) for p in _TRIANGLE]
    assert np.frombuffer(base64.b64decode(stage["indices"]), "<u4").tolist() == [0, 1, 2]
    assert json.loads(stage["submeshes"]) == [[0, 3, ""]]
    assert stage["uvs"] == ""
    assert _shading_modes(html) == ["solid", "wire"]
    assert "<canvas>" in html


def test_model_view_of_a_textured_mesh_opens_textured() -> None:
    html = ModelHandler().render(_pam(6, [(_TRIANGLE, [0, 1, 2], "rock.dds")]), _entry("object/rock.pam"), {})
    stage = _stage(html)

    uvs = np.frombuffer(base64.b64decode(stage["uvs"]), "<f4").reshape(-1, 2)
    assert uvs.tolist() == [[x, y] for x, y, _ in _TRIANGLE]
    assert json.loads(stage["submeshes"]) == [[0, 3, "rock.dds"]]
    assert _shading_modes(html) == ["textured", "solid", "wire"]
    assert 'class="view-meta model-textures"' in html


def test_model_view_of_an_empty_mesh_has_no_canvas() -> None:
    html = ModelHandler().render(
        _par_header(KIND_PAC, 3) + struct.pack("<I", 0) + _pac_body([]), _entry("character/hide.pac"), {}
    )

    assert "model-note" in html
    assert "<canvas>" not in html
