from __future__ import annotations

import json
from pathlib import Path

from map_pins import Pin, PinRequest, PinStore, parse_pin_request
from map_pins_file import SavedPinsFile


def _store(path: Path) -> PinStore:
    return PinStore(SavedPinsFile(lambda: path))


def _marker(save: bool = True, label: str = "") -> PinRequest:
    return parse_pin_request({"type": "marker", "x": 100, "z": -200, "label": label, "icon": "tent", "save": save})


def test_saved_pins_come_back_in_a_new_store(tmp_path: Path) -> None:
    path = tmp_path / "map_pins.json"
    saved = _store(path).place(_marker(label="Camp"))

    assert _store(path).pins() == (saved,)


def test_only_saved_pins_are_written(tmp_path: Path) -> None:
    path = tmp_path / "map_pins.json"
    store = _store(path)
    store.place(PinRequest(type="player", x=0, z=0))
    store.place(_marker(save=False))
    kept = store.place(_marker())

    assert _store(path).pins() == (kept,)


def test_removing_a_saved_pin_removes_it_from_the_file(tmp_path: Path) -> None:
    path = tmp_path / "map_pins.json"
    store = _store(path)
    pin = store.place(_marker())

    store.remove(pin.id)

    assert _store(path).pins() == ()


def test_new_ids_count_on_from_the_saved_ones(tmp_path: Path) -> None:
    path = tmp_path / "map_pins.json"
    first = _store(path).place(_marker())

    second = _store(path).place(_marker())

    assert int(second.id) > int(first.id)


def test_changes_to_unsaved_pins_do_not_write(tmp_path: Path) -> None:
    writes: list[tuple[Pin, ...]] = []

    class Recorder:
        def load(self) -> tuple[Pin, ...]:
            return ()

        def write(self, pins: tuple[Pin, ...]) -> None:
            writes.append(pins)

    store = PinStore(Recorder())
    for x in range(3):
        store.place(PinRequest(type="player", x=x, z=0))
    store.clear("player")
    saved = store.place(_marker())

    assert writes == [(saved,)]


def test_bad_saved_pins_are_skipped(tmp_path: Path) -> None:
    path = tmp_path / "map_pins.json"
    good = {"id": "4", "type": "marker", "x": 1, "z": 2}
    entries = [good, {"id": "5", "type": "player", "x": 1, "z": 2}, {"type": "marker", "x": 1, "z": 2}, {**good}]
    path.write_text(json.dumps({"version": 1, "pins": entries}), encoding="utf-8")

    pins = _store(path).pins()

    assert [(pin.id, pin.saved) for pin in pins] == [("4", True)]


def test_a_file_that_is_not_json_is_set_aside(tmp_path: Path) -> None:
    path = tmp_path / "map_pins.json"
    path.write_text("{not json", encoding="utf-8")

    store = _store(path)
    store.place(_marker())

    assert store.pins() != ()
    assert (tmp_path / "map_pins.json.bad").read_text(encoding="utf-8") == "{not json"
