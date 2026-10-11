"""Map pins: markers the Map view draws at world positions.

Pins come from the local HTTP API (`bdo_server.py`, docs/map-api.md) and live
in memory while the app runs. Positions are world units (cm): x and z on the
ground plane, y the optional height. The optional heading is the way the pin
faces in degrees clockwise from north (+z), 0 to 360. A singleton pin type,
such as `player`, keeps at most one pin: placing a new one replaces the old
one.
"""

from __future__ import annotations

import math
import threading
from collections.abc import Callable, Mapping
from dataclasses import dataclass


@dataclass(frozen=True)
class PinType:
    name: str
    # At most one pin of this type; a new one replaces the old one.
    singleton: bool


PIN_TYPES: Mapping[str, PinType] = {
    pin_type.name: pin_type
    for pin_type in (
        PinType("player", singleton=True),
        PinType("marker", singleton=False),
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


@dataclass(frozen=True)
class Pin:
    id: str
    type: str
    x: float
    z: float
    y: float | None
    label: str
    heading: float | None = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "type": self.type,
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "label": self.label,
            "heading": self.heading,
        }


def parse_pin_request(data: object) -> PinRequest:
    """A `PinRequest` from a JSON object: {"type", "x", "z", "y"?, "label"?, "heading"?}.

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
    )


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


class PinStore:
    """The pins of this session; thread safe, every change notifies the listeners."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._pins: tuple[Pin, ...] = ()
        self._next_id = 1
        self._listeners: tuple[PinListener, ...] = ()

    def subscribe(self, listener: PinListener) -> None:
        """Call `listener` with every pin after each change."""
        self._listeners = (*self._listeners, listener)

    def pins(self) -> tuple[Pin, ...]:
        return self._pins

    def place(self, request: PinRequest) -> Pin:
        """Add a pin; a singleton type's old pin goes."""
        with self._lock:
            pin = Pin(
                id=str(self._next_id),
                type=request.type,
                x=request.x,
                z=request.z,
                y=request.y,
                label=request.label,
                heading=request.heading,
            )
            self._next_id += 1
            kept = self._pins
            if PIN_TYPES[request.type].singleton:
                kept = tuple(old for old in kept if old.type != request.type)
            self._pins = (*kept, pin)
            pins = self._pins
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
            kept = tuple(pin for pin in self._pins if not matches(pin))
            removed = len(self._pins) - len(kept)
            self._pins = kept
        if removed:
            self._notify(kept)
        return removed

    def _notify(self, pins: tuple[Pin, ...]) -> None:
        for listener in self._listeners:
            listener(pins)
