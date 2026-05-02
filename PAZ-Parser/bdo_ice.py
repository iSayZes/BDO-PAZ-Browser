"""
ICE block cipher — ported from kukdh1/PAZ-Unpacker Crypt.cpp.

Only the decrypt path is needed for PAZ extraction; encrypt is included for
completeness.
"""
from __future__ import annotations

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


_SBOX: list[list[int]] = _build_sbox()


# ── ICE round function ────────────────────────────────────────────────────────

def _ice_f(p: int, sk: list[int]) -> int:
    # Left half expansion
    tl = ((p >> 16) & 0x3FF) | (((p >> 14) | ((p << 18) & 0xFFFFFFFF)) & 0xFFC00)
    # Right half expansion
    tr = (p & 0x3FF) | (((p << 2) & 0xFFFFFFFF) & 0xFFC00)
    # Salt permutation
    al = sk[2] & (tl ^ tr)
    ar = al ^ tr
    al ^= tl
    al ^= sk[0]
    ar ^= sk[1]
    return (
        _SBOX[0][al >> 10]
        | _SBOX[1][al & 0x3FF]
        | _SBOX[2][ar >> 10]
        | _SBOX[3][ar & 0x3FF]
    )


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
        self._key_rounds: int = key_rounds
        self._keysched: list[list[int]] = _build_keysched(key, key_rounds, key_size)

    def decrypt(self, data: bytes) -> bytes:
        if len(data) % 8 != 0:
            raise ValueError(f"ICE input must be a multiple of 8 bytes, got {len(data)}.")
        out = bytearray(len(data))
        for idx in range(len(data) // 8):
            b = data[idx * 8 : idx * 8 + 8]
            l = (b[0] << 24) | (b[1] << 16) | (b[2] << 8) | b[3]
            r = (b[4] << 24) | (b[5] << 16) | (b[6] << 8) | b[7]
            i = self._key_rounds - 1
            while i > 0:
                l ^= _ice_f(r, self._keysched[i])
                r ^= _ice_f(l, self._keysched[i - 1])
                i -= 2
            base = idx * 8
            for j in range(4):
                out[base + 3 - j] = r & 0xFF
                out[base + 7 - j] = l & 0xFF
                r >>= 8
                l >>= 8
        return bytes(out)

    def encrypt(self, data: bytes) -> bytes:
        if len(data) % 8 != 0:
            raise ValueError(f"ICE input must be a multiple of 8 bytes, got {len(data)}.")
        out = bytearray(len(data))
        for idx in range(len(data) // 8):
            b = data[idx * 8 : idx * 8 + 8]
            l = (b[0] << 24) | (b[1] << 16) | (b[2] << 8) | b[3]
            r = (b[4] << 24) | (b[5] << 16) | (b[6] << 8) | b[7]
            for i in range(0, self._key_rounds, 2):
                l ^= _ice_f(r, self._keysched[i])
                r ^= _ice_f(l, self._keysched[i + 1])
            base = idx * 8
            for j in range(4):
                out[base + 3 - j] = r & 0xFF
                out[base + 7 - j] = l & 0xFF
                r >>= 8
                l >>= 8
        return bytes(out)
