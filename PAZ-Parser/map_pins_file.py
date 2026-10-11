"""Saved map pins: the pins placed with `save`, kept in `map_pins.json` between runs.

The file sits in the Data Folder (`app_dirs.map_pins_file`), next to the
config, and holds {"version": 1, "pins": [pin, ...]} with the fields of the
map API. Each pin is checked like a new request when the app starts; one that
fails is skipped with a warning. A file that is not JSON is renamed to
`map_pins.json.bad` instead of being overwritten by the next save.
"""

from __future__ import annotations

import json
import logging
import os
from collections.abc import Callable
from pathlib import Path

from map_pins import Pin, PinError, parse_pin_request

FILE_VERSION = 1
_SAVED_FIELDS = ("id", "type", "x", "y", "z", "label", "heading", "icon")


class SavedPinsFile:
    """`map_pins.json` at `path()`, looked up on every call so a moved Data Folder takes effect."""

    def __init__(self, path: Callable[[], Path]) -> None:
        self._path = path

    def load(self) -> tuple[Pin, ...]:
        path = self._path()
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            return ()
        except (OSError, ValueError):
            logging.warning("Cannot read the saved map pins in %s", path, exc_info=True)
            _set_aside(path)
            return ()
        entries = data.get("pins") if isinstance(data, dict) else None
        if not isinstance(entries, list):
            logging.warning("%s has no pin list", path)
            _set_aside(path)
            return ()
        return _pins(entries, path)

    def write(self, pins: tuple[Pin, ...]) -> None:
        """Replace the file with `pins`. Not fatal: a pin that cannot be saved stays on the map until the app closes."""
        path = self._path()
        data = {"version": FILE_VERSION, "pins": [_saved_fields(pin) for pin in pins]}
        temp = path.with_name(f"{path.name}.tmp")
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            temp.write_text(json.dumps(data, indent=2), encoding="utf-8")
            os.replace(temp, path)
        except OSError:
            logging.warning("Cannot save the map pins to %s", path, exc_info=True)


def _pins(entries: list, path: Path) -> tuple[Pin, ...]:
    pins: list[Pin] = []
    seen: set[str] = set()
    for entry in entries:
        pin_id = entry.get("id") if isinstance(entry, dict) else None
        if not isinstance(pin_id, str) or not pin_id or pin_id in seen:
            logging.warning("Skipping a saved map pin without a unique id in %s: %r", path, entry)
            continue
        try:
            request = parse_pin_request({**entry, "save": True})
        except PinError as ex:
            logging.warning("Skipping saved map pin %s in %s: %s", pin_id, path, ex)
            continue
        seen.add(pin_id)
        pins.append(Pin.from_request(pin_id, request))
    return tuple(pins)


def _saved_fields(pin: Pin) -> dict:
    fields = pin.to_dict()
    return {name: fields[name] for name in _SAVED_FIELDS}


def _set_aside(path: Path) -> None:
    """Rename an unreadable `path` to `<name>.bad`, so the next save does not overwrite it."""
    try:
        os.replace(path, path.with_name(f"{path.name}.bad"))
    except OSError:
        logging.warning("Cannot rename %s", path, exc_info=True)
