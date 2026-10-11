from __future__ import annotations

from pathlib import Path

import pytest

import api.bdo_config as bdo_config
from api.bdo_config import MAP_FILTERS_KEY, load_config, map_filters_setting, save_config

_DEFAULT = {"choices": {}, "collapsed": [], "open": True}


@pytest.fixture
def config_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    path = tmp_path / "paz_config.json"
    monkeypatch.setattr(bdo_config, "config_file", lambda: path)
    return path


def test_no_saved_filters_read_as_the_defaults() -> None:
    assert map_filters_setting({}) == _DEFAULT


def test_saved_filters_round_trip(config_file: Path) -> None:
    filters = {"choices": {"nodes": {"quarry": False, "links": True}, "layers": {"player": True}}, "collapsed": ["nodes"], "open": False}

    save_config({MAP_FILTERS_KEY: filters})

    assert map_filters_setting(load_config()) == filters


@pytest.mark.parametrize(
    ("saved", "read"),
    [
        ("all", _DEFAULT),
        ({"choices": {"nodes": {"quarry": "no", "farm": False}}}, {**_DEFAULT, "choices": {"nodes": {"farm": False}}}),
        ({"choices": {"nodes": ["quarry"]}}, _DEFAULT),
        ({"collapsed": ["nodes", 5]}, {**_DEFAULT, "collapsed": ["nodes"]}),
        ({"open": "yes"}, _DEFAULT),
    ],
)
def test_anything_of_another_shape_is_dropped(saved: object, read: dict) -> None:
    assert map_filters_setting({MAP_FILTERS_KEY: saved}) == read
