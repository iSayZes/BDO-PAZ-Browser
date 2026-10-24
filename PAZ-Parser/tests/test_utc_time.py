from __future__ import annotations

import pytest

from _common.utc_time import utc_text


@pytest.mark.parametrize(("seconds", "text"), [
    (0, "1970-01-01 00:00"),
    (951_782_400, "2000-02-29 00:00"),
    (1_612_342_740, "2021-02-03 08:59"),
    (1_709_251_199, "2024-02-29 23:59"),
    (4_092_530_400, "2099-09-08 06:00"),
    (4_102_444_800, "2100-01-01 00:00"),
])
def test_utc_text(seconds: int, text: str) -> None:
    assert utc_text(seconds) == text


def test_utc_text_before_1970() -> None:
    assert utc_text(-1) == "1969-12-31 23:59"
