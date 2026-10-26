"""par_animation: the keys of a .paa, on built bytes and on client clips."""
from __future__ import annotations

import struct

import numpy as np
import pytest

from bdo_models import PazEntry
from bdo_preview import ModelHandler
from par_animation import parse_animation
from tests import par_builders as par
from tests.fixtures import FIXTURES_DIR, fetch_missing

_ROOT_ID = 0xE19AE7B8


_IDLE = par.paa_node(
    _ROOT_ID,
    [(0, (1.0, 1.0, 1.0))],
    [(0, (0.0, 0.0, 0.0, 1.0)), (500, (0.0, 0.0, 1.0, 0.0))],
    [(0, (0.0, 35.0, 0.0)), (250, (0.0, 36.0, 0.0)), (500, (0.0, 35.0, 0.0))],
)


def test_keys_come_back_per_channel_as_float32() -> None:
    animation = parse_animation(par.paa(0.5, [_IDLE]))

    assert animation.duration == 0.5
    (node,) = animation.nodes
    assert node.bone_id == _ROOT_ID
    assert node.scale.values.tolist() == [[1.0, 1.0, 1.0]]
    assert node.rotation.times.tolist() == [0, 500]
    assert node.rotation.values.dtype == np.float32
    assert node.translation.values[:, 1].tolist() == [35.0, 36.0, 35.0]


def test_a_clip_with_no_nodes_is_empty() -> None:
    assert parse_animation(par.paa(6.67, [])).nodes == ()


@pytest.mark.parametrize(("data", "message"), [
    (b"PAR " + bytes([0x01, 2]) + par.DESCRIPTOR + bytes(10), "not an animation"),
    (par.paa(0.5, [_IDLE], version=1), "version 1 is not read"),
    (par.paa(0.5, [_IDLE], key_bytes=4), "header says 4"),
    (par.paa(0.5, [par.paa_node(_ROOT_ID, [(5, (1.0, 1.0, 1.0))], [], [])]), "do not rise from 0"),
    (par.paa(0.5, [par.paa_node(_ROOT_ID, [], [(0, (0, 0, 0, 1)), (0, (0, 0, 0, 1))], [])]), "do not rise from 0"),
    (par.paa(0.5, [_IDLE])[:-2], "file ends"),
    (par.paa(0.5, [_IDLE]) + b"\x00", "layout ends"),
])
def test_bytes_that_do_not_fit_raise(data: bytes, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        parse_animation(data)


def test_model_view_of_a_clip_names_its_length() -> None:
    html = ModelHandler().render(par.paa(0.5, [_IDLE]), PazEntry("pad00001.paz", "character/motion/x/idle.paa", 0, 0, 0, 0, 0), {})

    assert 'data-rig="clip"' in html
    assert "0.50 s" in html
    assert "<canvas>" in html


# Client clips with a name no other file has: an object effect with one bone,
# a player riding clip with many.
_FIXTURES = ["cs_calpheon_01_cob0003_effect_0138_004.paa", "pmyf_00_00_rh_riding_run_l_drift_dash_00.paa"]


@pytest.mark.parametrize("name", _FIXTURES)
def test_client_clip_keys_are_well_formed(name: str) -> None:
    fetch_missing([name])
    animation = parse_animation((FIXTURES_DIR / name).read_bytes())

    assert animation.duration > 0
    assert animation.nodes
    for node in animation.nodes:
        for track in (node.scale, node.rotation, node.translation):
            assert np.isfinite(track.values).all()
            if len(track.times):
                assert int(track.times[-1]) <= round(animation.duration * 1000) + 1
        if len(node.rotation.times):
            assert np.allclose(np.linalg.norm(node.rotation.values, axis=1), 1, atol=2e-3)
