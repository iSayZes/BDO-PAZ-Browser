"""Checks of the Edania tables in `edania_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

import math

from tests.fixtures import load_binary_fixture

from .edania_tables import EDANIA_TABLES
from .parser import parse_value_table


_TABLES = {value_table.file_name: value_table for value_table in EDANIA_TABLES}
_CASTLE_INFO = "edanacastleinfostaicstatusmanager.bss"
# ui_texture/renewal/etc/wordmap/territorymark_<god>_large.dds.
_MARK_PREFIX = "territorymark_"
_MARK_SUFFIX = "_large"


def _records(name: str) -> list[dict]:
    return parse_value_table(load_binary_fixture(name), _TABLES[name])


def test_every_castle_has_its_own_node() -> None:
    keys = [record["node_key"] for record in _records(_CASTLE_INFO)]
    assert keys and len(keys) == len(set(keys))


def test_every_mark_texture_is_a_large_territory_mark() -> None:
    textures = [record["mark_texture"] for record in _records(_CASTLE_INFO)]
    assert len(textures) == len(set(textures))
    for texture in textures:
        assert texture.startswith(_MARK_PREFIX) and texture.endswith(_MARK_SUFFIX), texture


def test_every_mark_position_is_finite() -> None:
    for record in _records(_CASTLE_INFO):
        assert math.isfinite(record["x"]) and math.isfinite(record["z"]), record
