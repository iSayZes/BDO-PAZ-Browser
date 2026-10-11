from __future__ import annotations

from pathlib import Path

import pytest

import api.bdo_config as bdo_config
from api.bdo_config import OUTPUT_PATH_KEY, load_config, output_path_setting, save_config


@pytest.fixture
def config_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    path = tmp_path / "paz_config.json"
    monkeypatch.setattr(bdo_config, "config_file", lambda: path)
    return path


def test_the_output_folder_round_trips(config_file: Path) -> None:
    save_config({OUTPUT_PATH_KEY: r"D:\BDO\extract"})

    assert output_path_setting(load_config()) == r"D:\BDO\extract"


@pytest.mark.parametrize("saved", [None, 5, [r"D:\out"], "x" * 40000], ids=["none", "number", "list", "too-long"])
def test_anything_but_a_path_reads_as_none(saved: object) -> None:
    assert output_path_setting({OUTPUT_PATH_KEY: saved}) == ""
