"""The Model view's skeletons and clips (ModelRigsMixin): which .pab a mesh or clip gets, and the clip list."""
from __future__ import annotations

import base64

import numpy as np

from api.bdo_api import Api
from api.bdo_api_helpers import fold_entry_map
from api.bdo_api_model_rigs import mirror_key
from bdo_models import PazEntry
from tests import par_builders as par

_PC = "character/model/1_pc/17_psw"
_MOTION = "character/motion/1_pc/17_psw"
_CLASS_SKELETON = f"{_PC}/psw_01.pab"
_CLASS_BONES = ("Bip01", "Bip01 Spine", "Bip01 Head")


def _api(files: dict[str, bytes]) -> Api:
    api = Api()
    api._entry_map = {path: PazEntry("PAD00001.PAZ", path, 0, 1, 1, 0, 0) for path in files}
    api._entry_map_folded = fold_entry_map(api._entry_map)
    api.read_entry = lambda path: files[path]  # type: ignore[method-assign]
    return api


def _ids(*names: str) -> tuple[int, ...]:
    return tuple(par.bone_id(name) for name in names)


def test_a_mesh_takes_the_nearest_skeleton_up_its_folders_that_holds_its_palette() -> None:
    api = _api({
        _CLASS_SKELETON: par.skeleton(*_CLASS_BONES),
        f"{_PC}/armor/old.pab": par.skeleton("Bip01"),
        f"{_PC}/armor/9_upperbody/psw_09_ub_0001.pac": par.pac(_ids("Bip01", "Bip01 Head")),
    })

    result = api.get_model_skeleton(f"{_PC}/armor/9_upperbody/psw_09_ub_0001.pac")

    assert result["skeleton"]["path"] == _CLASS_SKELETON
    assert result["skeleton"]["isComplete"] is True
    assert result["skeleton"]["names"] == list(_CLASS_BONES)


def test_without_a_whole_match_the_skeleton_holding_most_ids_is_partial() -> None:
    api = _api({
        _CLASS_SKELETON: par.skeleton(*_CLASS_BONES),
        f"{_PC}/hair.pac": par.pac(_ids("Bip01", "Bip01 Head", "B_Hair_00")),
    })

    skeleton = api.get_model_skeleton(f"{_PC}/hair.pac")["skeleton"]

    assert (skeleton["path"], skeleton["isComplete"]) == (_CLASS_SKELETON, False)


def test_a_mesh_whose_ids_no_skeleton_holds_gets_an_error() -> None:
    api = _api({_CLASS_SKELETON: par.skeleton(*_CLASS_BONES), f"{_PC}/prop.pac": par.pac(_ids("B_Prop"))})

    assert "error" in api.get_model_skeleton(f"{_PC}/prop.pac")


def test_a_skeleton_is_its_own_skeleton() -> None:
    api = _api({_CLASS_SKELETON: par.skeleton(*_CLASS_BONES)})

    assert api.get_model_skeleton(_CLASS_SKELETON)["skeleton"]["path"] == _CLASS_SKELETON


def test_a_clip_takes_the_skeleton_under_its_mirrored_model_folder_that_fits_best() -> None:
    api = _api({
        _CLASS_SKELETON: par.skeleton(*_CLASS_BONES),
        f"{_PC}/pet/pet_01.pab": par.skeleton("B_Pet"),
        f"{_MOTION}/psw_00_00_stand_idle_00.paa": par.clip("Bip01", "Bip01 Spine"),
    })

    skeleton = api.get_model_skeleton(f"{_MOTION}/psw_00_00_stand_idle_00.paa")["skeleton"]

    assert skeleton["path"] == _CLASS_SKELETON


def test_the_clips_of_a_skeleton_are_the_paa_files_of_its_mirrored_motion_folder() -> None:
    api = _api({
        _CLASS_SKELETON: par.skeleton(*_CLASS_BONES),
        f"{_MOTION}/b_run.paa": par.clip("Bip01"),
        f"{_MOTION}/armor/a_idle.paa": par.clip("Bip01"),
        "character/motion/1_pc/18_pam/pam_idle.paa": par.clip("Bip01"),
    })

    result = api.list_model_animations(_CLASS_SKELETON)

    assert result == {"folder": f"{_MOTION}/", "clips": [f"{_MOTION}/armor/a_idle.paa", f"{_MOTION}/b_run.paa"]}


def test_a_skeleton_outside_the_model_folders_has_no_clips() -> None:
    assert _api({}).list_model_animations("object/thing.pab") == {"folder": "", "clips": []}


def test_a_clip_payload_packs_times_and_values_node_by_node() -> None:
    api = _api({f"{_MOTION}/idle.paa": par.clip("Bip01", "Bip01 Head")})

    animation = api.get_model_animation(f"{_MOTION}/idle.paa")["animation"]

    assert animation["duration"] == 0.5
    assert animation["nodes"] == [[par.bone_id("Bip01"), 0, 1, 0], [par.bone_id("Bip01 Head"), 0, 1, 0]]
    assert np.frombuffer(base64.b64decode(animation["times"]), "<u2").tolist() == [0, 0]
    assert np.frombuffer(base64.b64decode(animation["values"]), "<f4").tolist() == [0, 0, 0, 1, 0, 0, 0, 1]


def test_a_missing_clip_gets_an_error() -> None:
    assert "error" in _api({}).get_model_animation(f"{_MOTION}/gone.paa")


def test_mirror_keys_pair_model_and_motion_folders() -> None:
    assert mirror_key("character/model/1_pc/17_psw/psw_01.pab") == "1_pc/17_psw"
    assert mirror_key("character/motion/1_pc/17_psw/armor/x.paa") == "1_pc/17_psw"
    assert mirror_key("character/model/1_pc/top.pab") is None
    assert mirror_key("object/1_pc/17_psw/x.pab") is None
