from __future__ import annotations

import pytest

from map_pins import LABEL_MAX_LENGTH, WORLD_LIMIT_CM, Pin, PinError, PinRequest, PinStore, parse_pin_request


def _player(x: float = 1.0, z: float = 2.0) -> PinRequest:
    return PinRequest(type="player", x=x, z=z)


def test_a_new_player_pin_replaces_the_old_one() -> None:
    store = PinStore()
    first = store.place(_player(1, 1))
    second = store.place(_player(5, 5))

    assert store.pins() == (second,)
    assert first.id != second.id


def test_markers_add_up_and_keep_the_player() -> None:
    store = PinStore()
    player = store.place(_player())
    markers = [store.place(PinRequest(type="marker", x=i, z=i)) for i in range(3)]

    assert store.pins() == (player, *markers)


def test_remove_and_clear() -> None:
    store = PinStore()
    player = store.place(_player())
    marker = store.place(PinRequest(type="marker", x=0, z=0))

    assert store.remove(marker.id)
    assert not store.remove(marker.id)
    assert store.clear("marker") == 0
    assert store.clear("player") == 1
    assert store.pins() == ()
    assert player not in store.pins()


def test_every_change_notifies_with_the_full_list() -> None:
    store = PinStore()
    seen: list[tuple[Pin, ...]] = []
    store.subscribe(seen.append)

    pin = store.place(_player())
    store.remove(pin.id)
    store.clear()  # nothing left: no call

    assert seen == [(pin,), ()]


def test_parse_pin_request_reads_the_fields() -> None:
    request = parse_pin_request(
        {"type": "player", "x": 13800, "z": -76996.5, "y": -6715, "label": "Me", "heading": 171.5}
    )

    assert request == PinRequest(type="player", x=13800.0, z=-76996.5, y=-6715.0, label="Me", heading=171.5)
    marker = parse_pin_request({"type": "marker", "x": 0, "z": 0})
    assert marker.y is None and marker.heading is None


@pytest.mark.parametrize(("heading", "stored"), [(0, 0.0), (360, 0.0), (-90, 270.0), (725.5, 5.5), (None, None)])
def test_heading_folds_into_0_to_360(heading: object, stored: float | None) -> None:
    pin = PinStore().place(parse_pin_request({"type": "player", "x": 0, "z": 0, "heading": heading}))

    assert pin.heading == stored
    assert pin.to_dict()["heading"] == stored


@pytest.mark.parametrize(
    "data",
    [
        [],
        {"type": "boss", "x": 0, "z": 0},
        {"type": "player", "x": "1", "z": 0},
        {"type": "player", "x": True, "z": 0},
        {"type": "player", "x": 0},
        {"type": "player", "x": float("nan"), "z": 0},
        {"type": "player", "x": WORLD_LIMIT_CM + 1, "z": 0},
        {"type": "player", "x": 0, "z": 0, "label": 5},
        {"type": "player", "x": 0, "z": 0, "label": "x" * (LABEL_MAX_LENGTH + 1)},
        {"type": "player", "x": 0, "z": 0, "heading": "north"},
        {"type": "player", "x": 0, "z": 0, "heading": True},
        {"type": "player", "x": 0, "z": 0, "heading": float("inf")},
    ],
)
def test_parse_pin_request_refuses_bad_data(data: object) -> None:
    with pytest.raises(PinError):
        parse_pin_request(data)
