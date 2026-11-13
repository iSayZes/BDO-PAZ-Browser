from __future__ import annotations

from collections.abc import Iterator

import pytest

from _common.class_type import (
    PLAYABLE_CLASSES_MASK,
    class_types_in_mask,
    classes_label,
    is_all_classes,
    playable_classes_mask,
)
from _common.lookup_index import IndexKind, init_index

_ALL = "All"
_WIZARD = 28
_WITCH = 31
# A placeholder class type on client 1784 that later became a class.
_UNRELEASED = 6
# The class types pcgrowthsimply.bss marks playable on client 1784.
_PLAYABLE_1784 = (0, 1, 2, 4, 5, 8, 9, 10, 11, 12, 16, 17, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 31)
# Client 1784 masks repeat bit 31 into the upper half, as a sign-extended i32 does.
_SIGN_EXTENDED = 0xFFFF_FFFF_0000_0000


@pytest.fixture
def client_1784_classes() -> Iterator[None]:
    init_index(IndexKind.PLAYABLE_CLASSES, {class_type: 1 for class_type in _PLAYABLE_1784})
    yield
    init_index(IndexKind.PLAYABLE_CLASSES, None)


def test_without_the_index_the_client_3458_classes_are_playable() -> None:
    assert playable_classes_mask() == PLAYABLE_CLASSES_MASK


@pytest.mark.usefixtures("client_1784_classes")
def test_the_index_sets_the_playable_classes() -> None:
    assert class_types_in_mask(playable_classes_mask()) == _PLAYABLE_1784


@pytest.mark.usefixtures("client_1784_classes")
def test_a_sign_extended_mask_names_only_the_classes_of_its_client(monkeypatch: pytest.MonkeyPatch) -> None:
    # Without LOC names a class reads as its number, whichever test loaded LOC before.
    monkeypatch.setattr("_common.class_type.loc_text", lambda *_: "")
    mask = _SIGN_EXTENDED | 1 << _WITCH | 1 << _WIZARD | 1 << _UNRELEASED

    assert classes_label(mask, _ALL) == f"{_WIZARD}, {_WITCH}"


@pytest.mark.usefixtures("client_1784_classes")
def test_every_bit_set_is_every_class_of_the_client() -> None:
    assert is_all_classes(0xFFFF_FFFF_FFFF_FFFF)
    assert not is_all_classes(0xFFFF_FFFF_FFFF_FFFF & ~(1 << _WITCH))
