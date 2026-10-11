"""The Map view's pins (MapPinsMixin).

Pins come from the local server's map API (`map_api.py`) into the store
`ApiState` makes; the page gets every change through `app.onMapPinsChanged`
and can remove a pin itself. Their icons are built with the map
(`WorldMapMixin.get_map_icons`).
"""

from __future__ import annotations

from map_pins import PinStore

from .bdo_api_state import ApiState


class MapPinsMixin(ApiState):
    @property
    def map_pins(self) -> PinStore:
        """The pins the local server's map API changes (`map_api.py`)."""
        return self._map_pins

    def get_map_pins(self) -> list[dict]:
        """Every pin, for the Map view when it opens; changes arrive by `app.onMapPinsChanged`."""
        return [pin.to_dict() for pin in self._map_pins.pins()]

    def remove_map_pin(self, pin_id: str) -> bool:
        """The pin popup's Remove; False when the pin is gone already."""
        self._mark_activity()
        return isinstance(pin_id, str) and self._map_pins.remove(pin_id)
