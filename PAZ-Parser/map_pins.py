"""Map pins: markers the Map view draws at world positions.

Pins come from the local HTTP API (`bdo_server.py`, docs/map-api.md) and live
in memory while the app runs; a pin placed with `save` is also kept in
`map_pins.json` (`map_pins_file.py`) and comes back on the next start.
Positions are world units (cm): x and z on the ground plane, y the optional
height. The optional heading is the way the pin faces in degrees clockwise
from north (+z), 0 to 360. The optional icon names one of the game's world map
icons (`map_icons.py`); a pin type can bring its own. A singleton pin type,
such as `player`, keeps at most one pin: placing a new one replaces the old
one.
"""

from __future__ import annotations

import math
import threading
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Protocol

from map_icons import ICON_NAMES, PLAYER_ICON


@dataclass(frozen=True)
class PinType:
    name: str
    # At most one pin of this type; a new one replaces the old one.
    singleton: bool
    # Can be placed with `save`. A player pin follows a live position, so a
    # saved one would be stale on the next start.
    can_save: bool
    # The icon of a pin placed without one; None draws a dot.
    default_icon: str | None = None


PIN_TYPES: Mapping[str, PinType] = {
    pin_type.name: pin_type
    for pin_type in (
        PinType("player", singleton=True, can_save=False, default_icon=PLAYER_ICON),
        PinType("marker", singleton=False, can_save=True),
    )
}
LABEL_MAX_LENGTH = 100
# Far past the world's edge (about 1.8 million cm on client 3464), so only
# nonsense such as a unit mix-up is refused.
WORLD_LIMIT_CM = 100_000_000


class PinError(ValueError):
    """A pin request that cannot be placed; the message says why."""


@dataclass(frozen=True)
class PinRequest:
    """A validated pin to place."""

    type: str
    x: float
    z: float
    y: float | None = None
    label: str = ""
    heading: float | None = None
    icon: str | None = None
    save: bool = False


@dataclass(frozen=True)
class Pin:
    id: str
    type: str
    x: float
    z: float
    y: float | None
    label: str
    heading: float | None = None
    icon: str | None = None
    saved: bool = False

    @classmethod
    def from_request(cls, pin_id: str, request: PinRequest) -> Pin:
        """The pin `request` asks for, with its type's icon when it names none."""
        return cls(
            id=pin_id,
            type=request.type,
            x=request.x,
            z=request.z,
            y=request.y,
            label=request.label,
            heading=request.heading,
            icon=request.icon or PIN_TYPES[request.type].default_icon,
            saved=request.save,
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "type": self.type,
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "label": self.label,
            "heading": self.heading,
            "icon": self.icon,
            "saved": self.saved,
        }


def parse_pin_request(data: object) -> PinRequest:
    """A `PinRequest` from a JSON object: {"type", "x", "z", "y"?, "label"?, "heading"?, "icon"?, "save"?}.

    Raises PinError on a missing or wrong field.
    """
    if not isinstance(data, dict):
        raise PinError("the body must be a JSON object")
    pin_type = data.get("type")
    if not isinstance(pin_type, str) or pin_type not in PIN_TYPES:
        raise PinError(f"type must be one of {', '.join(PIN_TYPES)}, got {pin_type!r}")
    label = data.get("label", "")
    if not isinstance(label, str):
        raise PinError("label must be a string")
    if len(label) > LABEL_MAX_LENGTH:
        raise PinError(f"label is longer than {LABEL_MAX_LENGTH} characters")
    height = data.get("y")
    return PinRequest(
        type=pin_type,
        x=_coordinate(data, "x"),
        z=_coordinate(data, "z"),
        y=None if height is None else _coordinate(data, "y"),
        label=label,
        heading=_heading(data.get("heading")),
        icon=_icon(data.get("icon")),
        save=_save(data.get("save", False), PIN_TYPES[pin_type]),
    )


def _icon(value: object) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or value not in ICON_NAMES:
        raise PinError(f"icon must be one of {', '.join(sorted(ICON_NAMES))}, got {value!r}")
    return value


def _save(value: object, pin_type: PinType) -> bool:
    if not isinstance(value, bool):
        raise PinError(f"save must be true or false, got {value!r}")
    if value and not pin_type.can_save:
        raise PinError(f"{pin_type.name} pins cannot be saved")
    return value


def _heading(value: object) -> float | None:
    """Degrees clockwise from north, folded into 0 to 360; None when absent."""
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise PinError(f"heading must be a number of degrees, got {value!r}")
    return float(value) % 360.0


def _coordinate(data: dict, name: str) -> float:
    value = data.get(name)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise PinError(f"{name} must be a number, got {value!r}")
    if not math.isfinite(value) or abs(value) > WORLD_LIMIT_CM:
        raise PinError(f"{name} must be a world position in cm within {WORLD_LIMIT_CM:,}, got {value!r}")
    return float(value)


PinListener = Callable[[tuple[Pin, ...]], None]


class SavedPins(Protocol):
    """Where saved pins live between runs (`map_pins_file.SavedPinsFile`)."""

    def load(self) -> tuple[Pin, ...]: ...
    def write(self, pins: tuple[Pin, ...]) -> None: ...


class PinStore:
    """The pins of this session; thread safe, every change notifies the listeners.

    With `saved`, the store starts with the saved pins and writes them again
    after every change that adds or removes one.
    """

    def __init__(self, saved: SavedPins | None = None) -> None:
        self._lock = threading.Lock()
        self._saved = saved
        self._pins: tuple[Pin, ...] = saved.load() if saved is not None else ()
        # Saved pins keep their ids, so new ones count on from the highest.
        self._next_id = 1 + max((int(pin.id) for pin in self._pins if pin.id.isdigit()), default=0)
        self._listeners: tuple[PinListener, ...] = ()

    def subscribe(self, listener: PinListener) -> None:
        """Call `listener` with every pin after each change."""
        self._listeners = (*self._listeners, listener)

    def pins(self) -> tuple[Pin, ...]:
        return self._pins

    def place(self, request: PinRequest) -> Pin:
        """Add a pin; a singleton type's old pin goes."""
        with self._lock:
            pin = Pin.from_request(str(self._next_id), request)
            self._next_id += 1
            old = self._pins
            kept = old
            if PIN_TYPES[request.type].singleton:
                kept = tuple(other for other in old if other.type != request.type)
            pins = (*kept, pin)
            self._update(old, pins)
        self._notify(pins)
        return pin

    def remove(self, pin_id: str) -> bool:
        """Remove one pin; False when there is no pin with that id."""
        return self._remove_where(lambda pin: pin.id == pin_id) > 0

    def clear(self, pin_type: str | None = None) -> int:
        """Remove every pin, or every pin of `pin_type`; returns how many went."""
        return self._remove_where(lambda pin: pin_type is None or pin.type == pin_type)

    def _remove_where(self, matches: Callable[[Pin], bool]) -> int:
        with self._lock:
            old = self._pins
            kept = tuple(pin for pin in old if not matches(pin))
            self._update(old, kept)
        removed = len(old) - len(kept)
        if removed:
            self._notify(kept)
        return removed

    def _update(self, old: tuple[Pin, ...], pins: tuple[Pin, ...]) -> None:
        """Make `pins` the store's pins, writing the saved ones when they changed; call with the lock held."""
        self._pins = pins
        if self._saved is None:
            return
        saved = tuple(pin for pin in pins if pin.saved)
        if saved != tuple(pin for pin in old if pin.saved):
            self._saved.write(saved)

    def _notify(self, pins: tuple[Pin, ...]) -> None:
        for listener in self._listeners:
            listener(pins)
