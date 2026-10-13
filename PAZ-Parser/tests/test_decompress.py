"""`bdo_decompress` on both backends, and the compiled one against the reference.

The native tests skip when `_bdo_native` is not built
(`pip install ./PAZ-Parser/native`); the client tests skip without a client.
"""

from __future__ import annotations

import random
import struct
from collections.abc import Iterator
from pathlib import Path

import pytest

from bdo_models import PazEntry
from paz.bdo_decompress import NATIVE_UNPACK, Unpack, bdo_decompress, unpack_python
from paz.bdo_paz_reader import parse_paz_file
from paz.bdo_payload_reader import ice_decrypt_bytes, is_encrypted, needs_decompress, read_raw_payload

from .decompress_streams import encode, sample_data
from .fixtures import installed_paz_folder

_BACKENDS = [
    pytest.param(unpack_python, id="python"),
    pytest.param(
        NATIVE_UNPACK,
        id="native",
        marks=pytest.mark.skipif(NATIVE_UNPACK is None, reason="_bdo_native is not built"),
    ),
]
_needs_native = pytest.mark.skipif(NATIVE_UNPACK is None, reason="_bdo_native is not built")

# A hand-built short-mode stream: 8 literals, a back-reference that copies
# them, one whose source overlaps its output (repeat 3, length 10), then the
# byte-at-a-time tail.
_GROUP_HEADER = 0x80000000 | 0b011 << 8  # bits 0-7 literal, 8-9 back-reference
_COPY_8_FROM_8 = (8 << 6) | ((8 - 3) << 2) | 0x02
_COPY_10_FROM_3 = (3 << 6) | ((10 - 3) << 2) | 0x02
_DECOMPRESSED = b"ABCDEFGH" + b"ABCDEFGH" + b"FGHFGHFGHF" + b"WXYZ"

_SIZES = [0, 1, 8, 64, 4096, 1 << 20]
_FUZZ_SEED = 3464
_FUZZ_MUTATIONS = 300
# Client payloads for the parity test: the compressed entry closest to each
# size, from the first archives, read through the Python decoder too.
_CLIENT_TARGET_SIZES = [64, 4096, 64 * 1024, 1 << 20, 4 << 20]
_CLIENT_ARCHIVES = 5


def _short_stream(decompressed_length: int) -> bytes:
    body = (
        struct.pack("<I", _GROUP_HEADER)
        + b"ABCDEFGH"
        + struct.pack("<HH", _COPY_8_FROM_8, _COPY_10_FROM_3)
        + b"WXYZ"
    )
    return bytes([0x01, 3 + len(body), decompressed_length]) + body


def _native() -> Unpack:
    assert NATIVE_UNPACK is not None
    return NATIVE_UNPACK


def _outcome(payload: bytes, expected_size: int, unpack: Unpack) -> bytes | str:
    """The bytes, or the ValueError message. Any other exception fails the test."""
    try:
        return bdo_decompress(payload, expected_size, unpack=unpack)
    except ValueError as ex:
        return str(ex)


def _assert_same_outcome(payload: bytes, expected_size: int) -> None:
    assert _outcome(payload, expected_size, _native()) == _outcome(payload, expected_size, unpack_python)


@pytest.mark.parametrize("unpack", _BACKENDS)
def test_decompress_literals_and_back_references(unpack: Unpack) -> None:
    assert bdo_decompress(_short_stream(len(_DECOMPRESSED)), unpack=unpack) == _DECOMPRESSED


@pytest.mark.parametrize("unpack", _BACKENDS)
def test_decompress_rejects_a_back_reference_past_the_end(unpack: Unpack) -> None:
    with pytest.raises(ValueError, match="error code -3"):
        bdo_decompress(_short_stream(18), unpack=unpack)


@pytest.mark.parametrize("unpack", _BACKENDS)
@pytest.mark.parametrize("size", _SIZES)
def test_decompress_returns_the_encoded_bytes(unpack: Unpack, size: int) -> None:
    source = sample_data(size, seed=size)

    assert bdo_decompress(encode(source), unpack=unpack) == source


@pytest.mark.parametrize("unpack", _BACKENDS)
def test_decompress_rejects_a_truncated_stream(unpack: Unpack) -> None:
    payload = encode(sample_data(4096, seed=1))

    with pytest.raises(ValueError, match="error code"):
        bdo_decompress(payload[: len(payload) // 2], 4096, unpack=unpack)


def test_decompress_returns_a_stored_payload_as_is() -> None:
    stored = bytes([0x00, 3 + 5, 5]) + b"plain"

    assert bdo_decompress(stored) == b"plain"


@pytest.mark.parametrize("payload", [b"", b"\x03\x00\x00\x00"], ids=["empty", "short-long-header"])
def test_decompress_rejects_a_missing_header(payload: bytes) -> None:
    with pytest.raises(ValueError, match="BDO payload"):
        bdo_decompress(payload)


@_needs_native
@pytest.mark.parametrize("size", [64, 4096])
def test_native_matches_python_on_every_truncation(size: int) -> None:
    payload = encode(sample_data(size, seed=size))

    for length in range(len(payload) + 1):
        _assert_same_outcome(payload[:length], size)


@_needs_native
@pytest.mark.parametrize("size", [64, 4096, 1 << 16])
def test_native_matches_python_on_corrupted_bytes(size: int) -> None:
    payload = encode(sample_data(size, seed=size))
    rng = random.Random(_FUZZ_SEED + size)

    for _ in range(_FUZZ_MUTATIONS):
        corrupted = bytearray(payload)
        for _ in range(rng.randint(1, 4)):
            corrupted[rng.randrange(len(corrupted))] = rng.randrange(256)
        _assert_same_outcome(bytes(corrupted), size)


@_needs_native
def test_native_raises_memory_error_for_an_impossible_size() -> None:
    with pytest.raises(MemoryError):
        _native()(encode(b"abc"), 9, 30, 1 << 62)


@_needs_native
def test_native_matches_python_on_client_payloads() -> None:
    paz_folder = installed_paz_folder()
    if paz_folder is None:
        pytest.skip("no client installed")
    payloads = _client_payloads(paz_folder)
    if not payloads:
        pytest.fail(f"no compressed entries in the first {_CLIENT_ARCHIVES} archives of {paz_folder}")

    for name, (payload, size) in payloads.items():
        native = bdo_decompress(payload, size, unpack=_native())
        assert native == bdo_decompress(payload, size, unpack=unpack_python), name
        _assert_same_outcome(payload[: len(payload) // 2], size)


def _client_payloads(paz_folder: Path) -> dict[str, tuple[bytes, int]]:
    """Decrypted compressed payloads by internal path, with their sizes."""
    candidates = list(_compressed_entries(paz_folder))
    payloads: dict[str, tuple[bytes, int]] = {}
    for target in _CLIENT_TARGET_SIZES:
        if not candidates:
            break
        archive, entry = min(candidates, key=lambda candidate: abs(candidate[1].uncompressed_size - target))
        raw = read_raw_payload(archive, entry)
        decrypted = ice_decrypt_bytes(raw) if is_encrypted(entry) else raw
        if needs_decompress(entry, decrypted):
            payloads[entry.internal_path] = (decrypted, entry.uncompressed_size)
    return payloads


def _compressed_entries(paz_folder: Path) -> Iterator[tuple[Path, PazEntry]]:
    for archive in sorted(paz_folder.glob("pad*.paz"))[:_CLIENT_ARCHIVES]:
        for entry in parse_paz_file(archive):
            if entry.uncompressed_size > entry.compressed_size:
                yield archive, entry
