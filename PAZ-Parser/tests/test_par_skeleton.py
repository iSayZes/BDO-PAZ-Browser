"""par_skeleton: the bones of a .pab, each layout branch on built bytes and on client files."""
from __future__ import annotations

import struct

import numpy as np
import pytest

from bdo_models import PazEntry
from bdo_preview import ModelHandler
from par_skeleton import parse_skeleton
from tests import par_builders as par
from tests.fixtures import FIXTURES_DIR, fetch_missing

_BOX, _CYLINDER, _MESH, _SHAPE_4 = 0, 1, 2, 4


def _mesh_body(points: int = 3, indices: tuple[int, ...] = (0, 1, 2)) -> bytes:
    return (struct.pack("<H", points) + bytes(12 * points)
            + struct.pack(f"<H{len(indices)}H", len(indices), *indices))


def test_bones_keep_ids_names_and_parents() -> None:
    skeleton = parse_skeleton(par.pab(3, [par.pab_bone("Bip01", -1), par.pab_bone("Bip01 Spine", 0), par.pab_bone("Bip01 Head", 1)]))

    assert skeleton.names == ("Bip01", "Bip01 Spine", "Bip01 Head")
    assert skeleton.parents == (-1, 0, 1)
    assert skeleton.bone_ids == tuple(par.bone_id(name) for name in skeleton.names)
    assert skeleton.world.shape == skeleton.inverse_world.shape == (3, 16)
    assert skeleton.local[0].tolist() == [1, 1, 1, 0, 0, 0, 1, 0, 0, 0]


def test_version_3_shapes_are_meshes_and_axes_are_skipped() -> None:
    mesh_shape = b"\x01" + _mesh_body()
    skeleton = parse_skeleton(par.pab(3, [par.pab_bone("Root", -1, mesh_shape, axes=1), par.pab_bone("Axle", 0)]))

    assert skeleton.names == ("Root", "Axle")


@pytest.mark.parametrize(("shape", "body"), [
    (_BOX, bytes(12)), (_CYLINDER, bytes(8)), (_MESH, _mesh_body()), (_SHAPE_4, bytes(4)),
])
def test_version_4_shapes_start_with_their_type(shape: int, body: bytes) -> None:
    typed = b"\x01" + struct.pack("<I3f", shape, 0, 0, 0) + body
    skeleton = parse_skeleton(par.pab(4, [par.pab_bone("Root", -1, typed), par.pab_bone("Tip", 0)]))

    assert skeleton.bone_count == 2


@pytest.mark.parametrize(("shape", "body"), [(_BOX, bytes(12)), (_CYLINDER, bytes(8)), (_MESH, _mesh_body())])
def test_bone_volumes_after_the_bones_are_walked(shape: int, body: bytes) -> None:
    volume = struct.pack("<H I", 1, 0) + par.IDENTITY + bytes([2, shape]) + body
    skeleton = parse_skeleton(par.pab(4, [par.pab_bone("Root", -1)], volume))

    assert skeleton.bone_count == 1


@pytest.mark.parametrize(("data", "message"), [
    (b"PABR" + bytes(20), "no PAR magic"),
    (b"PAR " + bytes([0x03, 3]) + par.DESCRIPTOR + bytes(4), "not a skeleton"),
    (par.pab(5, [par.pab_bone("Root", -1)]), "version 5"),
    (par.pab(3, [par.pab_bone("Root", -1), par.pab_bone("Loop", 1)]), "parent 1"),
    (par.pab(3, [par.pab_bone("Root", -1)]) + b"\x00", "layout ends"),
    (par.pab(4, [par.pab_bone("Root", -1, b"\x01" + struct.pack("<I3f", 3, 0, 0, 0))]), "shape 3"),
    (par.pab(3, [par.pab_bone("Root", -1)], struct.pack("<H I", 1, 5) + par.IDENTITY + bytes(2) + bytes(12)), "bone 5"),
])
def test_bytes_that_do_not_fit_raise(data: bytes, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        parse_skeleton(data)


def test_model_view_of_a_skeleton_has_bones_on_and_no_shading() -> None:
    data = par.pab(3, [par.pab_bone("Bip01", -1), par.pab_bone("Bip01 Spine", 0)])
    html = ModelHandler().render(data, PazEntry("pad00001.paz", "character/model/x/x_01.pab", 0, 0, 0, 0, 0), {})

    assert 'data-rig="skeleton"' in html
    assert 'data-action="model-bones" class="active" aria-pressed="true"' in html
    assert "model-shading" not in html
    assert "<canvas>" in html


# Client skeletons with a name no other file has: version 2, version 3, version 4
# with cylinder shapes, with shape 4 and a CP949 bone name, a box volume and a mesh volume.
_FIXTURES = ["m0099_01.pab", "c0008_01.pab", "m0065_01.pab", "pdw_01.pab", "t0002_05.pab", "t0311_01.pab"]


@pytest.mark.parametrize("name", _FIXTURES)
def test_client_skeleton_is_a_bind_pose_chain(name: str) -> None:
    fetch_missing([name])
    data = (FIXTURES_DIR / name).read_bytes()
    skeleton = parse_skeleton(data)

    assert skeleton.parents[0] == -1
    assert all(0 <= parent < bone for bone, parent in enumerate(skeleton.parents) if bone)
    world = skeleton.world.reshape(-1, 4, 4).astype(np.float64)
    inverse = skeleton.inverse_world.reshape(-1, 4, 4).astype(np.float64)
    for bone in range(skeleton.bone_count):
        assert np.allclose(world[bone] @ inverse[bone], np.eye(4), atol=1e-3)
    assert skeleton.bone_ids == tuple(par.bone_id(name) for name in skeleton.names)
