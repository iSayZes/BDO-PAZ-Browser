"""The compiled `_bdo_native` decoders, None when the module is not installed.

`PAZ-Parser/native/` builds it (`pip install ./PAZ-Parser/native`, needs
Rust). `bdo_decompress.py` and `bdo_ice.py` use these when they are set and
their Python versions otherwise; the Python versions are the reference.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence

try:
    # The stub is PAZ-Parser/native/_bdo_native.pyi; there is no .py source.
    import _bdo_native  # pyright: ignore[reportMissingModuleSource]
except ImportError:
    _bdo_native = None

# (data, input_start, input_end, decompressed_length) -> decompressed bytes.
NativeUnpack = Callable[[bytes, int, int, int], bytes]
# (data, subkeys, sbox bytes) -> data run through the ICE rounds.
NativeIceCrypt = Callable[[bytes, Sequence[tuple[int, int, int]], bytes], bytes]

UNPACK: NativeUnpack | None = _bdo_native.unpack if _bdo_native is not None else None
ICE_CRYPT: NativeIceCrypt | None = _bdo_native.ice_crypt if _bdo_native is not None else None
