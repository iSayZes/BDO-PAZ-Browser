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
    ".barrier", # Siege barrier outlines, x/y/z float points (gamecommondata/villagesiegebarrier)
    ".bk2", # Bink 2 video, "KB2j" magic (ui_movie)
    ".bkd", # Region map block data, pairs with .rid (ui_texture/minimap/area/*.bmp.bkd)
    ".bnk", # Wwise SoundBank, "BKHD" magic (sound2022/windows/<language>)
    ".chroma", # RGB lighting effects for keyboard, mouse and mousepad (gamecommondata/ledani)
    ".col", # Collision objects in neighbouring sectors (1 file in mapdata_real)
    ".collisiondata2", # Havok tagfile, "TAG0" + "SDKV20170100", collision per sector
    ".combine", # World data per sector (mapdata_real/sectormapinfo_combine)
    ".data", # Raw floats: terrain heightfield.data and effect/turbulence.data
    ".db", # Windows thumbs.db left in texture/
    ".fcb", # 3 effect files of 4 to 68 bytes (effect/texture)
    ".gnf", # PS4 texture, "GNF " magic (1 file)
    ".hdr", # Radiance HDR environment maps, "#?RADIANCE" magic (texture/)
    ".hlod", # HLOD sector coordinate list (mapdata_real/hloddata)
    ".house", # Every housing slot key, e.g. HH_-101_-1_88_1_0 (1 file)
    ".ipam", # Object mesh paths and placements per sector (object/intergrate)
    ".light", # Event map lights (mapdata_real/event)
    ".lightlist", # Far light list (mapdata_real/farlightlist.lightlist)
    ".lod", # Float point list per town, e.g. hideltown.lod
    ".mapdata", # LOD map data per sector (sectormapinfo_combine/*_lod.mapdata)
    ".namelist", # Far tree model names, .srt paths (mapdata_real)
    ".object", # Event map object placements with .pam paths
    ".paa", # Animations, binary form of the .pa text exports (character/motion)
    ".paac", # Action charts per character (character/binaryactionchart)
    ".paach", # Action chart header shared by the .paac files
    ".paap", # Object bounding box pack (object/aabb_pack.paap)
    ".pab", # Skeleton? (character/model)
    ".pabav", # Action chart version stamp, 20 bytes (1 file)
    ".pac", # Skinned character meshes? (character/model)
    ".pad", # Animation data packs (character/motion/*/animdatapack.pad)
    ".pae", # Effects (effectbin)
    ".paem", # Effect meshes (effectbin/mesh)
    ".pah", # Effect meshes, binary form of the .ph text exports? (effect/mesh)
    ".pam", # Static object meshes, binary form of the .pm text exports? (object/)
    ".pas", # Cutscenes (character/cutscene)
    ".paseqfe", # Sequences, most are 20-byte stubs (sequence/)
    ".pat", # Head data (character/model/*/head/*_mt_*.pat)
    ".pcm", # Small PAR file next to the .pam meshes (object/), not audio
    ".probe", # Probes per sector, almost all empty (mapdata_real/probe)
    ".procedural", # Event map procedural ground decoration
    ".r3m", # Old effect meshes (effect/mesh/oldpah)
    ".rid", # Region map colour table, pairs with .bkd
    ".tome", # Occluders per sector (mapdata_real/occluder)
    ".tree", # Event map tree placements
    ".treelist", # Far tree placements (mapdata_real/fartreelist)
    ".treelist2", # Far tree placements, second version of .treelist
    ".vnl", # Navigation data, pairs with .vnm (gamecommondata/char_navigation)
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
