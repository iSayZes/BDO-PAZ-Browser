from __future__ import annotations

import json
from pathlib import Path

from PIL import Image

from map_icons_build import ICON_FORMAT, INDEX_NAME, build_icons, icon_file, icons_folder, read_icon_index
from tests.map_icon_samples import sample_files


def test_built_icons_are_files_with_an_index(tmp_path: Path) -> None:
    index = build_icons(sample_files().get, tmp_path)

    assert set(index) == {"village"}
    assert read_icon_index(tmp_path) == index
    path = icon_file(tmp_path, "village")
    assert path is not None
    with Image.open(path) as image:
        assert image.format == "PNG"
    assert index["village"]["size"][1] == image.height / 2


def test_a_new_build_replaces_the_old_icons(tmp_path: Path) -> None:
    build_icons(sample_files().get, tmp_path)

    build_icons({}.get, tmp_path)

    assert read_icon_index(tmp_path) == {}
    assert icon_file(tmp_path, "village") is None


def test_icons_of_another_format_read_as_not_built(tmp_path: Path) -> None:
    build_icons(sample_files().get, tmp_path)
    path = icons_folder(tmp_path) / INDEX_NAME
    data = json.loads(path.read_text(encoding="utf-8"))
    path.write_text(json.dumps({**data, "format": ICON_FORMAT + 1}), encoding="utf-8")

    assert read_icon_index(tmp_path) is None


def test_only_catalog_names_are_icon_files(tmp_path: Path) -> None:
    build_icons(sample_files().get, tmp_path)
    (icons_folder(tmp_path) / "secret.png").write_bytes(b"")

    assert icon_file(tmp_path, "secret") is None
    assert icon_file(tmp_path, "../icons/village") is None
