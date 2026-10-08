"""`browser.py --formats` and `--handlers`: which file formats have a handler."""
from __future__ import annotations

import argparse

from bdo_preview import _BUILTIN_KEYS, _REGISTRY, get_binary_handlers, plugin_failures, unique_format_keys

from .errors import CliError
from .session import open_session
from .stdio import error

_FORMATS_IGNORE: frozenset[str] = frozenset({
    # Add extensions or filenames to hide from --formats output
    # e.g. ".pac", "x_y.bss"
    ".zip",
    ".temp",
    ".exe",
    ".wr",
    ".woff", # Font
    ".wem",
    ".volumefog",
    ".volumedecal",
    ".vnm",
    ".ttf", # Font
    ".otf", # Font
    ".ani", # Cursor/animation, not a game format
    ".bin", # Generic binary, too common to be useful without more context
    ".luac", # Compiled Lua, not sure i cba
    ".lnk", # Windows shortcut, not a game format
    ".fxo", # Shader cache, not a game format
    ".dxil", # Compiled DirectX shader, not a game format
    ".fxo10", # Compiled DirectX Shader, not a game format
    ".fxo11", # Compiled DirectX Shader, not a game format
    # skip for now/I have not checked these:
    ".barrier",
    ".bk2",
    ".bkd",
    ".bnk", # Wwise SoundBank?
    ".chroma",
    ".cl",
    ".col", # Computational boundary data?
    ".collisiondata2", # Computational boundary data?
    ".combine",
    ".data",
    ".db", # Database File?
    ".fcb",
    ".gnf",
    ".hdr", # Radiance HDR Image?
    ".hlod", # Level of Detail?
    ".house",
    ".ifl",
    ".ipam",
    ".light",
    ".lightlist",
    ".lod", # Level of Detail?
    ".mapdata",
    ".namelist",
    ".object",
    ".pa",
    ".paa", # Animation?
    ".paac",
    ".paach",
    ".paap",
    ".pab", # Skeleton?
    ".pabav",
    ".pac", # Skinned Mesh / Character Models?
    ".pad",
    ".pae",
    ".paem",
    ".pah",
    ".pam", # Static Object Mesh?
    ".pami",
    ".pas",
    ".paseqfe",
    ".pat",
    ".pc",
    ".pcm", # Pulse-Code Modulation?
    ".ph",
    ".pm",
    ".probe",
    ".procedural",
    ".r3m",
    ".rid",
    ".tome",
    ".tree",
    ".treelist",
    ".treelist2",
    ".vnl",
})


def run_handlers(args: argparse.Namespace) -> int:
    """Every registered handler key, one per line; needs no PAZ folder.

    Exits with 1 when a handler file failed to import. build.py compares the
    exe's list with the source's, so such a handler stops the release; the
    app update and a handler pack install check a new version with it too.
    """
    for key in get_binary_handlers():
        print(key)
    for name, reason in plugin_failures().items():
        error(f"{name} failed to load: {reason}")
    return 1 if plugin_failures() else 0


def run_formats(args: argparse.Namespace) -> int:
    try:
        api = open_session(args.paz_folder, load_loc=False, load_indexes=False)
    except CliError as ex:
        error(str(ex))
        return 1

    all_keys = [k for k in unique_format_keys(api.entries) if k not in _FORMATS_IGNORE]
    generic  = [k for k in all_keys if k in _BUILTIN_KEYS]
    binary   = [k for k in all_keys if k not in _BUILTIN_KEYS]

    registered_handlers = {k for k in _REGISTRY if k not in _BUILTIN_KEYS and k not in _FORMATS_IGNORE}
    supported_binary   = sorted({k for k in binary if k in _REGISTRY} | registered_handlers)
    unsupported_binary = [k for k in binary if k not in _REGISTRY and k not in registered_handlers]

    supported   = sorted(generic + supported_binary)
    unsupported = sorted(unsupported_binary)
    n_supported = len(supported)
    n_total     = n_supported + len(unsupported)

    print(f"File formats: {n_supported}/{n_total} supported")
    print()
    print(f"Supported ({n_supported}):")
    for k in supported:
        print(f"  {k}")
    print()
    print(f"Unsupported ({len(unsupported)}):")
    for k in unsupported:
        print(f"  {k}")
    return 0
