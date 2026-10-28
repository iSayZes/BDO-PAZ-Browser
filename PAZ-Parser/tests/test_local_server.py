from __future__ import annotations

import json
import urllib.error
import urllib.request
from collections.abc import Iterator
from pathlib import Path

import pytest

from bdo_server import LocalServer
from map_icons_build import build_icons
from map_pins import PinStore
from tests.map_icon_samples import sample_files
from world_map import sea_variant
from world_map_build import sea_path, tile_path

_KEY = "3464-0123456789abcdef"
# The same client before a repack, so only the digest differs.
_OLD_KEY = "3464-fedcba9876543210"


@pytest.fixture
def server() -> Iterator[LocalServer]:
    srv = LocalServer()
    srv.start()
    try:
        yield srv
    finally:
        srv.stop()


def _get(url: str) -> tuple[bytes, str]:
    with urllib.request.urlopen(url, timeout=5) as response:
        return response.read(), response.headers["Content-Type"]


def _status(url: str) -> int:
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            return response.status
    except urllib.error.HTTPError as ex:
        return ex.code


def _tile_url(template: str, zoom: int, x: int, y: int) -> str:
    return template.replace("{z}", str(zoom)).replace("{x}", str(x)).replace("{y}", str(y))


def _write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def test_a_map_tile_is_served_as_jpeg(server: LocalServer, tmp_path: Path) -> None:
    _write(tile_path(tmp_path, 7, (-3, 5)), b"tile")
    template = server.serve_map(tmp_path, _KEY)

    assert _get(_tile_url(template, 7, -3, 5)) == (b"tile", "image/jpeg")


def test_a_tile_not_on_disk_gets_the_sea_tile_of_its_zoom(server: LocalServer, tmp_path: Path) -> None:
    _write(sea_path(tmp_path, 4, sea_variant(4, (2, 2))), b"sea")
    template = server.serve_map(tmp_path, _KEY)

    assert _get(_tile_url(template, 4, 2, 2))[0] == b"sea"


def test_a_tile_without_any_file_is_not_found(server: LocalServer, tmp_path: Path) -> None:
    template = server.serve_map(tmp_path, _KEY)

    assert _status(_tile_url(template, 4, 2, 2)) == 404


def test_a_tile_url_of_another_content_key_is_not_found(server: LocalServer, tmp_path: Path) -> None:
    _write(tile_path(tmp_path, 7, (0, 0)), b"tile")
    old = server.serve_map(tmp_path, _OLD_KEY)
    server.serve_map(tmp_path, _KEY)

    assert _status(_tile_url(old, 7, 0, 0)) == 404


def test_no_map_served_after_serve_map_none(server: LocalServer, tmp_path: Path) -> None:
    _write(tile_path(tmp_path, 7, (0, 0)), b"tile")
    template = server.serve_map(tmp_path, _KEY)
    server.serve_map(None, "")

    assert _status(_tile_url(template, 7, 0, 0)) == 404


def test_a_tile_url_without_the_token_is_forbidden(server: LocalServer, tmp_path: Path) -> None:
    _write(tile_path(tmp_path, 7, (0, 0)), b"tile")
    template = server.serve_map(tmp_path, _KEY)

    assert _status(_tile_url(template, 7, 0, 0).split("?")[0]) == 403


def test_a_built_map_icon_is_served_as_png(server: LocalServer, tmp_path: Path) -> None:
    build_icons(sample_files().get, tmp_path)
    server.serve_map(tmp_path, _KEY)
    template = server.map_icon_url(_KEY)

    body, content_type = _get(template.replace("{name}", "village"))

    assert content_type == "image/png" and body.startswith(b"\x89PNG")
    assert _status(template.replace("{name}", "tent")) == 404  # not built: the sample client lacks it
    assert _status(server.map_icon_url(_OLD_KEY).replace("{name}", "village")) == 404
    assert _status(template.replace("{name}", "village").split("?")[0]) == 403


# ── Map API ──────────────────────────────────────────────────────────────────


def _api(server: LocalServer, method: str, path: str, body: object = None, token: str | None = None) -> tuple[int, object]:
    data = None if body is None else json.dumps(body).encode("utf-8")
    request = urllib.request.Request(f"http://127.0.0.1:{server.port}/api/map{path}", data=data, method=method)
    request.add_header("Authorization", f"Bearer {server.token if token is None else token}")
    if data is not None:
        request.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            text = response.read()
            return response.status, json.loads(text) if text else None
    except urllib.error.HTTPError as ex:
        return ex.code, json.loads(ex.read() or b"null")


@pytest.fixture
def pins(server: LocalServer) -> PinStore:
    store = PinStore()
    server.set_pin_store(store)
    return store


def test_placing_a_player_pin_replaces_the_old_one(server: LocalServer, pins: PinStore) -> None:
    _api(server, "POST", "/pins", {"type": "player", "x": 1, "z": 2})
    status, body = _api(server, "POST", "/pins", {"type": "player", "x": 13800, "z": 76996, "label": "Me"})

    assert status == 201
    assert isinstance(body, dict)
    assert _api(server, "GET", "/pins") == (200, {"pins": [body["pin"]]})
    assert [pin.label for pin in pins.pins()] == ["Me"]


def test_a_pin_can_be_removed_by_id_and_by_type(server: LocalServer, pins: PinStore) -> None:
    _, body = _api(server, "POST", "/pins", {"type": "marker", "x": 0, "z": 0})
    _api(server, "POST", "/pins", {"type": "player", "x": 0, "z": 0})
    assert isinstance(body, dict)

    assert _api(server, "DELETE", f"/pins/{body['pin']['id']}") == (204, None)
    assert _api(server, "DELETE", f"/pins/{body['pin']['id']}")[0] == 404
    assert _api(server, "DELETE", "/pins?type=player") == (200, {"removed": 1})
    assert pins.pins() == ()


def test_a_bad_pin_is_refused_with_the_reason(server: LocalServer, pins: PinStore) -> None:
    status, body = _api(server, "POST", "/pins", {"type": "boss", "x": 0, "z": 0})

    assert status == 400
    assert isinstance(body, dict) and "type" in body["error"]
    assert pins.pins() == ()


def test_a_pin_takes_an_icon_and_save(server: LocalServer, pins: PinStore) -> None:
    status, body = _api(server, "POST", "/pins", {"type": "marker", "x": 0, "z": 0, "icon": "tent", "save": True})

    assert status == 201
    assert isinstance(body, dict)
    assert (body["pin"]["icon"], body["pin"]["saved"]) == ("tent", True)
    status, body = _api(server, "POST", "/pins", {"type": "player", "x": 0, "z": 0, "save": True})
    assert status == 400
    assert isinstance(body, dict) and "saved" in body["error"]


def test_the_map_api_needs_the_token(server: LocalServer, pins: PinStore) -> None:
    assert _api(server, "GET", "/pins", token="wrong")[0] == 401
    assert _api(server, "POST", "/pins", {"type": "player", "x": 0, "z": 0}, token="wrong")[0] == 401
    assert pins.pins() == ()


def test_server_info_file_is_written_and_removed_only_by_its_server(server: LocalServer, tmp_path: Path) -> None:
    path = tmp_path / "local_server.json"
    server.write_info(path)
    info = json.loads(path.read_text(encoding="utf-8"))

    assert (info["port"], info["token"]) == (server.port, server.token)
    path.write_text(json.dumps({**info, "token": "another app"}), encoding="utf-8")
    server.remove_info(path)
    assert path.exists()
    server.write_info(path)
    server.remove_info(path)
    assert not path.exists()
