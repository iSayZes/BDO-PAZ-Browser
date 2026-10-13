from __future__ import annotations

import os
import random

import pytest

from paz import native_backend
from paz.bdo_ice import BDO_ICE_KEY, NATIVE_CRYPT, Crypt, IceCipher, crypt_blocks_numpy
from paz.bdo_payload_reader import ice_decrypt_bytes, ice_decrypt_many

_BACKENDS = [
    pytest.param(crypt_blocks_numpy, id="numpy"),
    pytest.param(
        NATIVE_CRYPT,
        id="native",
        marks=pytest.mark.skipif(NATIVE_CRYPT is None, reason="_bdo_native is not built"),
    ),
]
_needs_native = pytest.mark.skipif(NATIVE_CRYPT is None, reason="_bdo_native is not built")
_PARITY_SIZES = [8, 64, 4096, 1 << 20]

# Two blocks, 00 01 .. 0F. The expected outputs were taken from the original
# block-at-a-time port of kukdh1/PAZ-Unpacker, before the loop was rewritten.
_BLOCKS = bytes(range(16))
_KEY_16 = bytes(range(0x10, 0x20))


@pytest.mark.parametrize("crypt", _BACKENDS)
def test_ice_decrypt_matches_the_reference_port(crypt: Crypt) -> None:
    assert IceCipher(BDO_ICE_KEY).decrypt(_BLOCKS, crypt).hex() == "544e03c9383e92252d9b5234571c54ab"


@pytest.mark.parametrize("crypt", _BACKENDS)
def test_ice_encrypt_matches_the_reference_port(crypt: Crypt) -> None:
    assert IceCipher(BDO_ICE_KEY).encrypt(_BLOCKS, crypt).hex() == "c3bdf28b3c7dde63bccdf2d6ce3ace8e"


@pytest.mark.parametrize("crypt", _BACKENDS)
def test_ice_16_byte_key_matches_the_reference_port(crypt: Crypt) -> None:
    assert IceCipher(_KEY_16).decrypt(_BLOCKS, crypt).hex() == "38f5d62086d7bc4011c87f1c9c9f0497"


@pytest.mark.parametrize("crypt", _BACKENDS)
@pytest.mark.parametrize("key", [BDO_ICE_KEY, _KEY_16], ids=["bdo-key", "16-byte-key"])
def test_ice_round_trips(key: bytes, crypt: Crypt) -> None:
    data = os.urandom(4096)
    cipher = IceCipher(key)

    assert cipher.decrypt(cipher.encrypt(data, crypt), crypt) == data


@_needs_native
@pytest.mark.parametrize("size", _PARITY_SIZES)
@pytest.mark.parametrize("key", [BDO_ICE_KEY, _KEY_16], ids=["bdo-key", "16-byte-key"])
def test_native_ice_matches_numpy(key: bytes, size: int) -> None:
    assert NATIVE_CRYPT is not None
    data = random.Random(size).randbytes(size)
    cipher = IceCipher(key)

    assert cipher.decrypt(data, NATIVE_CRYPT) == cipher.decrypt(data, crypt_blocks_numpy)
    assert cipher.encrypt(data, NATIVE_CRYPT) == cipher.encrypt(data, crypt_blocks_numpy)


@_needs_native
@pytest.mark.parametrize(
    ("data", "subkeys", "sbox", "message"),
    [
        (bytes(7), ((0, 0, 0),), bytes(16384), "multiple of 8"),
        (bytes(8), ((1 << 20, 0, 0),), bytes(16384), "20-bit"),
        (bytes(8), ((0, 0, 0),), bytes(16383), "S-boxes"),
    ],
    ids=["partial-block", "wide-subkey", "short-sbox"],
)
def test_native_ice_rejects_bad_input(
    data: bytes, subkeys: tuple[tuple[int, int, int], ...], sbox: bytes, message: str
) -> None:
    assert native_backend.ICE_CRYPT is not None
    with pytest.raises(ValueError, match=message):
        native_backend.ICE_CRYPT(data, subkeys, sbox)


def test_ice_decrypts_each_block_on_its_own() -> None:
    data = os.urandom(64 * 1024)
    cipher = IceCipher(BDO_ICE_KEY)
    block_by_block = b"".join(cipher.decrypt(data[i : i + 8]) for i in range(0, len(data), 8))

    assert cipher.decrypt(data) == block_by_block


def test_ice_decrypts_empty_input() -> None:
    assert IceCipher(BDO_ICE_KEY).decrypt(b"") == b""


def test_ice_rejects_a_partial_block() -> None:
    with pytest.raises(ValueError, match="multiple of 8"):
        IceCipher(BDO_ICE_KEY).decrypt(bytes(7))


def test_ice_decrypt_bytes_keeps_the_input_length() -> None:
    data = os.urandom(13)
    padded = data + bytes(3)

    assert ice_decrypt_bytes(data) == IceCipher(BDO_ICE_KEY).decrypt(padded)[:13]


def test_ice_decrypt_many_matches_one_call_per_input() -> None:
    inputs = [os.urandom(size) for size in (13, 0, 8, 4096, 1, 63)]

    assert ice_decrypt_many(inputs) == [ice_decrypt_bytes(data) for data in inputs]
