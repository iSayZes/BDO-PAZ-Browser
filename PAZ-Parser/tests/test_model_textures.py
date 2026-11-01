"""The Model view's textures: where a mesh's texture is looked up, and the data URL it comes back as."""
from __future__ import annotations

import io

import pytest

from api.bdo_api import Api
from api.bdo_api_helpers import fold_entry_map
from api.bdo_api_model_textures import model_texture_paths
from bdo_models import PazEntry

PIL_Image = pytest.importorskip("PIL.Image")


def _png() -> bytes:
    buf = io.BytesIO()
    PIL_Image.new("RGBA", (4, 2), (200, 100, 50, 255)).save(buf, format="PNG")
    return buf.getvalue()


def _api(paths: list[str]) -> Api:
    api = Api()
    api._entry_map = {path: PazEntry("PAD00001.PAZ", path, 0, 1, 1, 0, 0) for path in paths}
    api._entry_map_folded = fold_entry_map(api._entry_map)
    reads: list[str] = []

    def read_entry(path: str) -> bytes:
        reads.append(path)
        return _png()

    api.read_entry = read_entry  # type: ignore[method-assign]
    api.reads = reads  # type: ignore[attr-defined]
    return api


def test_an_object_mesh_tries_its_folder_then_object_textures() -> None:
    assert model_texture_paths("object/04_calpheon/house_001.pam", "Wood_66.dds") == [
        "object/04_calpheon/wood_66.dds",
        "object/texture/wood_66.dds",
        "character/texture/wood_66.dds",
        "object/04_calpheon/house_001.dds",
    ]


def test_a_character_mesh_tries_character_textures_first() -> None:
    assert model_texture_paths("character/model/2_mon/m0310/m0310_0001.pac", "M0310_0001.dds")[1:3] == [
        "character/texture/m0310_0001.dds",
        "object/texture/m0310_0001.dds",
    ]


def test_only_the_file_name_of_a_texture_counts() -> None:
    paths = model_texture_paths("object/rock.pam", "../../ui_texture/secret.dds")

    assert paths == [
        "object/secret.dds",
        "object/texture/secret.dds",
        "character/texture/secret.dds",
        "object/rock.dds",
    ]


def test_a_blank_texture_has_no_paths() -> None:
    assert model_texture_paths("object/rock.pam", "  ") == []


def test_the_texture_comes_back_as_a_png_data_url() -> None:
    api = _api(["object/texture/wood_66.dds", "object/texture_thumbnail/wood_66.dds"])

    result = api.get_model_texture("object/04_calpheon/house_001.pam", "Wood_66.dds")

    assert result["path"] == "object/texture/wood_66.dds"
    assert result["url"].startswith("data:image/png;base64,")


def test_a_sector_lod_mesh_falls_back_to_its_own_name() -> None:
    api = _api(["mapdata_real/sectormapinfo_combine/52_10_0_lod.dds"])

    result = api.get_model_texture("mapdata_real/sectormapinfo_combine/52_10_0_lod.pam", "52_0_10_LOD.dds")

    assert result["path"] == "mapdata_real/sectormapinfo_combine/52_10_0_lod.dds"


def test_a_texture_is_decoded_once() -> None:
    api = _api(["character/texture/body.dds"])

    first = api.get_model_texture("character/model/body.pac", "body.dds")
    second = api.get_model_texture("character/model/hands.pac", "BODY.dds")

    assert first["url"] == second["url"]
    assert api.reads == ["character/texture/body.dds"]  # type: ignore[attr-defined]


def test_a_missing_texture_is_an_error() -> None:
    result = _api([]).get_model_texture("object/rock.pam", "rock.dds")

    assert set(result) == {"error"}
    assert "rock.dds" in result["error"]
