"""
ICE block cipher, ported from kukdh1/PAZ-Unpacker Crypt.cpp.

Only the decrypt path is needed for PAZ extraction; encrypt is included for
completeness. The key schedule and S-boxes are built here. The rounds run in
`_bdo_native.ice_crypt` (Rust) when it is installed, else on numpy arrays,
all blocks at once (`crypt_blocks_numpy`, the reference). The two must return
the same bytes (`tests/test_payload_decode.py`).
"""
from __future__ import annotations

from collections.abc import Callable

import numpy as np
import numpy.typing as npt

from . import native_backend

# ── Constants ─────────────────────────────────────────────────────────────────

_ICE_SMOD: list[list[int]] = [
    [333, 313, 505, 369],
    [379, 375, 319, 391],
    [361, 445, 451, 397],
    [397, 425, 395, 505],
]

_ICE_SXOR: list[list[int]] = [
    [0x83, 0x85, 0x9B, 0xCD],
    [0xCC, 0xA7, 0xAD, 0x41],
    [0x4B, 0x2E, 0xD4, 0x33],
    [0xEA, 0xCB, 0x2E, 0x04],
]

_ICE_PBOX: list[int] = [
    0x00000001, 0x00000080, 0x00000400, 0x00002000,
    0x00080000, 0x00200000, 0x01000000, 0x40000000,
    0x00000008, 0x00000020, 0x00000100, 0x00004000,
    0x00010000, 0x00800000, 0x04000000, 0x20000000,
    0x00000004, 0x00000010, 0x00000200, 0x00008000,
    0x00020000, 0x00400000, 0x08000000, 0x10000000,
    0x00000002, 0x00000040, 0x00000800, 0x00001000,
    0x00040000, 0x00100000, 0x02000000, 0x80000000,
]

_ICE_KEYROT: list[int] = [0, 1, 2, 3, 2, 1, 3, 0, 1, 3, 2, 0, 3, 1, 0, 2]

# BDO hardcoded ICE key (from Main.h: ICE_KEY / ICE_KEY_LEN = 8)
BDO_ICE_KEY: bytes = bytes([0x51, 0xF3, 0x0F, 0x11, 0x04, 0x24, 0x6A, 0x00])


# ── GF helpers ────────────────────────────────────────────────────────────────

def _gf_mult(a: int, b: int, m: int) -> int:
    res = 0
    while b:
        if b & 1:
            res ^= a
        a <<= 1
        b >>= 1
        if a >= 256:
            a ^= m
    return res


def _gf_exp7(b: int, m: int) -> int:
    if b == 0:
        return 0
    x = _gf_mult(b, b, m)
    x = _gf_mult(b, x, m)
    x = _gf_mult(x, x, m)
    return _gf_mult(b, x, m)


def _ice_perm32(x: int) -> int:
    res = 0
    for pval in _ICE_PBOX:
        if x & 1:
            res |= pval
        x >>= 1
        if not x:
            break
    return res


# ── S-box (built once at import) ──────────────────────────────────────────────

def _build_sbox() -> list[list[int]]:
    sbox: list[list[int]] = [[0] * 1024 for _ in range(4)]
    for i in range(1024):
        col = (i >> 1) & 0xFF
        row = (i & 0x1) | ((i & 0x200) >> 8)
        sbox[0][i] = _ice_perm32((_gf_exp7(col ^ _ICE_SXOR[0][row], _ICE_SMOD[0][row]) << 24) & 0xFFFFFFFF)
        sbox[1][i] = _ice_perm32((_gf_exp7(col ^ _ICE_SXOR[1][row], _ICE_SMOD[1][row]) << 16) & 0xFFFFFFFF)
        sbox[2][i] = _ice_perm32((_gf_exp7(col ^ _ICE_SXOR[2][row], _ICE_SMOD[2][row]) << 8) & 0xFFFFFFFF)
        sbox[3][i] = _ice_perm32(_gf_exp7(col ^ _ICE_SXOR[3][row], _ICE_SMOD[3][row]) & 0xFFFFFFFF)
    return sbox


Words = npt.NDArray[np.uint32]

_SBOX: list[list[int]] = _build_sbox()
_S0, _S1, _S2, _S3 = (np.array(column, dtype=np.uint32) for column in _SBOX)
# The four S-boxes as `_bdo_native.ice_crypt` takes them: 4096 little-endian u32.
_SBOX_BYTES: bytes = np.concatenate([_S0, _S1, _S2, _S3]).astype("<u4").tobytes()


# ── Block loop ────────────────────────────────────────────────────────────────

# A block is two 32-bit big-endian halves.
_BLOCK_HALF = np.dtype(">u4")

Subkey = tuple[int, int, int]
# (data, subkeys in round order) -> every 8-byte block run through the rounds.
Crypt = Callable[[bytes, tuple[Subkey, ...]], bytes]


def crypt_blocks_numpy(data: bytes, subkeys: tuple[Subkey, ...]) -> bytes:
    """Run the ICE Feistel rounds over every 8-byte block of `data`.

    Encrypt and decrypt differ only in the order of `subkeys`. Blocks do not
    depend on each other (no chaining), so each round runs over all of them
    at once, with one array of left halves and one of right halves. Each
    round sets (l, r) to (r, l ^ F(r)); the round count is even, so the
    halves end where they started. On a 14 MB texture this takes 0.15 s,
    against 1.83 s for a Python loop per block.
    """
    words: Words = np.frombuffer(data, dtype=_BLOCK_HALF).astype(np.uint32)
    left: Words = words[0::2]
    right: Words = words[1::2]

    for k0, k1, k2 in subkeys:
        # F(r): expand r to two 20-bit halves, salt-permute them with k2,
        # key them with k0 and k1, then look up the four S-boxes
        tl = ((right >> 16) & 0x3FF) | (((right >> 14) | (right << 18)) & 0xFFC00)
        tr = (right & 0x3FF) | ((right << 2) & 0xFFC00)
        al = k2 & (tl ^ tr)
        ar = al ^ tr ^ k1
        al ^= tl ^ k0
        left, right = right, left ^ (_S0[al >> 10] | _S1[al & 0x3FF] | _S2[ar >> 10] | _S3[ar & 0x3FF])

    out = np.empty(words.size, dtype=_BLOCK_HALF)
    out[0::2] = right
    out[1::2] = left
    return out.tobytes()


def _crypt_blocks_native(data: bytes, subkeys: tuple[Subkey, ...]) -> bytes:
    assert native_backend.ICE_CRYPT is not None
    return native_backend.ICE_CRYPT(data, subkeys, _SBOX_BYTES)


NATIVE_CRYPT: Crypt | None = _crypt_blocks_native if native_backend.ICE_CRYPT is not None else None
CRYPT: Crypt = NATIVE_CRYPT or crypt_blocks_numpy


# ── Key schedule ──────────────────────────────────────────────────────────────

def _ice_key_sched_build(
    kb: list[int],
    keysched: list[list[int]],
    n: int,
    keyrot: list[int],
) -> None:
    for i in range(8):
        kr = keyrot[i]
        isk = keysched[n + i]
        isk[0] = isk[1] = isk[2] = 0
        for j in range(15):
            curr_sk_idx = j % 3
            for k in range(4):
                curr_kb_idx = (kr + k) & 3
                bit = kb[curr_kb_idx] & 1
                isk[curr_sk_idx] = ((isk[curr_sk_idx] << 1) | bit) & 0xFFFFFFFF
                kb[curr_kb_idx] = ((kb[curr_kb_idx] >> 1) | ((bit ^ 1) << 15)) & 0xFFFF


def _build_keysched(key: bytes, key_rounds: int, key_size: int) -> list[list[int]]:
    keysched: list[list[int]] = [[0, 0, 0] for _ in range(key_rounds)]
    kb: list[int] = [0, 0, 0, 0]

    if key_rounds == 8:
        for i in range(4):
            kb[3 - i] = ((key[i * 2] << 8) | key[i * 2 + 1]) & 0xFFFF
        _ice_key_sched_build(kb, keysched, 0, _ICE_KEYROT)
    else:
        for i in range(key_size):
            for j in range(4):
                kb[3 - j] = ((key[i * 8 + j * 2] << 8) | key[i * 8 + j * 2 + 1]) & 0xFFFF
            _ice_key_sched_build(kb, keysched, i * 8, _ICE_KEYROT)
            _ice_key_sched_build(kb, keysched, key_rounds - 8 - i * 8, _ICE_KEYROT[8:])

    return keysched


# ── Public API ────────────────────────────────────────────────────────────────

class IceCipher:
    """ICE block cipher with an 8-byte key (BDO default) or multiples of 16."""

    def __init__(self, key: bytes) -> None:
        keylen = len(key)
        if keylen == 8:
            key_size = 1
            key_rounds = 8
        elif keylen % 16 == 0:
            key_size = keylen // 16
            key_rounds = keylen
        else:
            raise ValueError(f"Invalid ICE key length: {keylen}. Must be 8 or a multiple of 16.")
        keysched = _build_keysched(key, key_rounds, key_size)
        self._encrypt_subkeys: tuple[Subkey, ...] = tuple((sk[0], sk[1], sk[2]) for sk in keysched)
        self._decrypt_subkeys: tuple[Subkey, ...] = self._encrypt_subkeys[::-1]

    def decrypt(self, data: bytes, crypt: Crypt | None = None) -> bytes:
        """`crypt`: the backend, `CRYPT` when None; the parity tests pass each one."""
        _check_block_size(data)
        return (crypt or CRYPT)(data, self._decrypt_subkeys)

    def encrypt(self, data: bytes, crypt: Crypt | None = None) -> bytes:
        _check_block_size(data)
        return (crypt or CRYPT)(data, self._encrypt_subkeys)


def _check_block_size(data: bytes) -> None:
    if len(data) % 8 != 0:
        raise ValueError(f"ICE input must be a multiple of 8 bytes, got {len(data)}.")
