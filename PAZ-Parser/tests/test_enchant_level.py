"""`enchant_level_text()`: `+1` to `+15`, then the grade names PRI to DEC."""
from __future__ import annotations

import pytest

from _common.enchant_level import enchant_level_text


@pytest.mark.parametrize(
    ("level", "expected"),
    [(0, ""), (1, "+1"), (15, "+15"), (16, "PRI"), (18, "TRI"), (20, "PEN"), (25, "DEC"), (26, "")],
)
def test_enchant_level_text(level: int, expected: str) -> None:
    assert enchant_level_text(level) == expected
