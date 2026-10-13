"""The preview tab remembered per file type in paz_config.json (bdo_config.py)."""
from __future__ import annotations

from pathlib import Path

import pytest

import api.bdo_config as bdo_config
from api.bdo_config import (
    PREVIEW_TABS_KEY,
    load_config,
    preview_tab_setting,
    preview_tab_type,
    save_preview_tab_setting,
)


@pytest.fixture
def config_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    path = tmp_path / "paz_config.json"
    monkeypatch.setattr(bdo_config, "config_file", lambda: path)
    return path


@pytest.mark.parametrize(
    ("path", "kind"),
    [
        ("gamecommondata/binary/buff.dbss", ".dbss"),
        ("gamecommondata/binary/buffsimply.bss", ".dbss"),
        ("ui_texture/icon/a.DDS", ".dds"),
        ("ui_texture/icon/a.dds11", ".dds"),
        ("character/aiscript/boss/x.ai", ".ai"),
        ("character\\no_extension", ""),
        (".hidden", ""),
    ],
)
def test_file_type_is_the_extension_with_shared_ones_folded(path: str, kind: str) -> None:
    assert preview_tab_type(path) == kind


def test_a_saved_tab_applies_to_every_file_of_the_type(config_file: Path) -> None:
    save_preview_tab_setting("gamecommondata/binary/buff.dbss", "parsed")

    cfg = load_config()
    assert preview_tab_setting(cfg, "gamecommondata/binary/title.dbss") == "parsed"
    assert preview_tab_setting(cfg, "gamecommondata/binary/buffsimply.bss") == "parsed"
    assert preview_tab_setting(cfg, "ui/a.xml") is None


def test_types_keep_their_own_tab(config_file: Path) -> None:
    save_preview_tab_setting("a.dbss", "parsed")
    save_preview_tab_setting("b.xml", "hex")
    save_preview_tab_setting("c.dbss", "hex")

    assert load_config()[PREVIEW_TABS_KEY] == {".dbss": "hex", ".xml": "hex"}


def test_an_unknown_tab_is_not_saved(config_file: Path) -> None:
    save_preview_tab_setting("a.dbss", "rendered")

    assert not config_file.exists()


@pytest.mark.parametrize("saved", ["parsed", [".dbss"], {".dbss": "table"}, {".dbss": 1}])
def test_anything_of_another_shape_reads_as_no_tab(saved: object) -> None:
    assert preview_tab_setting({PREVIEW_TABS_KEY: saved}, "a.dbss") is None
