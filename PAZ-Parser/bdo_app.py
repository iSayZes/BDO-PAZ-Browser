from __future__ import annotations

import argparse
import fnmatch
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import webview

from bdo_api import Api, _load_config, _norm
from bdo_cache import load_cache, read_meta_version, save_cache
from bdo_models import PazEntry
from bdo_paz_extract import extract_entry, find_single_meta_file, parse_meta_file


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="browser",
        description="BDO PAZ Browser — omit --file/--list to open the GUI.",
    )
    parser.add_argument("--paz-folder", metavar="DIR", help="Path to the PAZ folder (default: last used)")
    parser.add_argument("--file", metavar="PATTERN", help="File name or glob pattern to extract, e.g. title.dbss or *title*.dbss")
    parser.add_argument("--list", metavar="PATTERN", help="List matching file paths without extracting, e.g. title*.dbss")
    parser.add_argument("--output", metavar="DIR", help="Output directory for --file (default: current working directory)")
    parser.add_argument("--formats", action="store_true", help="Show supported file formats and exit")
    parser.add_argument("--profile", action="store_true", help="Enable backend timing and browser-side JS profiling for the GUI")
    args = parser.parse_args()

    if args.file:
        sys.exit(_cli_extract(args))
    elif args.list:
        sys.exit(_cli_list(args))
    elif args.formats:
        sys.exit(_cli_formats(args))
    else:
        _launch_gui(profile=args.profile)

def _set_app_user_model_id() -> None:
    import ctypes
    app_id = "bdo.paz.browser"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

def _apply_window_icon(window) -> None:
    try:
        import ctypes
        icon_path = str(Path(__file__).parent / "ui" / "favicon.ico")
        LR_LOADFROMFILE = 0x0010
        LR_DEFAULTSIZE  = 0x0040
        IMAGE_ICON      = 1
        WM_SETICON      = 0x0080
        hicon = ctypes.windll.user32.LoadImageW(
            None, icon_path, IMAGE_ICON, 0, 0, LR_LOADFROMFILE | LR_DEFAULTSIZE
        )
        if not hicon:
            return
        hwnd = getattr(window, "native_handle", None) or \
               ctypes.windll.user32.FindWindowW(None, "BDO PAZ Browser")
        if hwnd:
            ctypes.windll.user32.SendMessageW(hwnd, WM_SETICON, 1, hicon)  # ICON_BIG
            ctypes.windll.user32.SendMessageW(hwnd, WM_SETICON, 0, hicon)  # ICON_SMALL
    except Exception:
        pass


def _launch_gui(profile: bool = False) -> None:
    from bdo_server import LocalServer

    _set_app_user_model_id()
    url = str(Path(__file__).parent / "ui" / "index.html")
    if profile:
        url += "?profile=1"

    server = LocalServer()
    server.start()
    api = Api(profile=profile, server=server)
    server.set_reader(api)
    window = webview.create_window(
        title="BDO PAZ Browser",
        url=url,
        js_api=api,
        width=1280,
        height=800,
        min_size=(900, 560),
        background_color="#1a1a1a",
    )
    if window is not None:
        api.set_window(window)
        window.events.shown += lambda: _apply_window_icon(window)
    try:
        webview.start(debug=profile)
    finally:
        server.stop()


def _resolve_paz_root(paz_folder: str | None) -> Path | None:
    folder = paz_folder or _load_config().get("last_folder")
    if not folder:
        print("Error: use --paz-folder or open a folder in the GUI first.", file=sys.stderr)
        return None
    p = Path(folder)
    if not p.is_dir():
        print(f"Error: PAZ folder not found: {p}", file=sys.stderr)
        return None
    return p


def _load_all_entries(paz_root: Path) -> list[PazEntry] | None:
    print("Loading PAZ entries…")
    try:
        meta_path = find_single_meta_file(paz_root)
        current_version = read_meta_version(meta_path)
        cached = load_cache(paz_root)

        if cached and cached[0] == current_version:
            _, entries = cached
            print(f"Loaded {len(entries):,} entries from cache.")
        else:
            print("Parsing PAZ files (first run, this may take a while)…")
            entries = parse_meta_file(meta_path)
            save_cache(paz_root, current_version, entries)
            print(f"Parsed and cached {len(entries):,} entries.")
        return entries
    except Exception as ex:
        print(f"Error loading PAZ folder: {ex}", file=sys.stderr)
        return None


def _match_entries(entries: list[PazEntry], pattern: str) -> list[PazEntry]:
    q = pattern.replace("\\", "/").lower()
    is_glob = any(c in q for c in ("*", "?", "["))

    matches = []
    for entry in entries:
        path = _norm(entry.internal_path)
        name = path.rsplit("/", 1)[-1]
        if is_glob:
            hit = fnmatch.fnmatch(path.lower(), q) or fnmatch.fnmatch(name.lower(), q)
        else:
            hit = q in path.lower()
        if hit:
            matches.append(entry)
    return matches


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
    ".link", # Shortcut/link file, not a game format
})


def _cli_formats(args: argparse.Namespace) -> int:
    from bdo_preview import _BUILTIN_KEYS, _REGISTRY, unique_format_keys

    paz_root = _resolve_paz_root(args.paz_folder)
    if paz_root is None:
        return 1

    entries = _load_all_entries(paz_root)
    if entries is None:
        return 1

    all_keys = [k for k in unique_format_keys(entries) if k not in _FORMATS_IGNORE]
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


def _cli_list(args: argparse.Namespace) -> int:
    paz_root = _resolve_paz_root(args.paz_folder)
    if paz_root is None:
        return 1

    entries = _load_all_entries(paz_root)
    if entries is None:
        return 1

    matches = _match_entries(entries, args.list)
    if not matches:
        print(f"No files found matching '{args.list}'.", file=sys.stderr)
        return 1

    print(f"\n{len(matches):,} file(s) matching '{args.list}':\n")
    for entry in matches:
        size_kb = entry.uncompressed_size / 1024
        print(f"  {entry.internal_path}  ({size_kb:,.1f} KB)")
    return 0


def _cli_extract(args: argparse.Namespace) -> int:
    paz_root = _resolve_paz_root(args.paz_folder)
    if paz_root is None:
        return 1

    entries = _load_all_entries(paz_root)
    if entries is None:
        return 1

    output_root = Path(args.output) if args.output else Path.cwd()

    matches = _match_entries(entries, args.file)
    if not matches:
        print(f"No files found matching '{args.file}'.", file=sys.stderr)
        return 1

    print(f"Found {len(matches):,} file(s). Extracting to {output_root} …\n")

    extracted = skipped = failed = 0
    for i, entry in enumerate(matches, 1):
        label = f"[{i}/{len(matches)}]"
        try:
            result = extract_entry(paz_root=paz_root, output_root=output_root, entry=entry, overwrite=False, flat=True)
            if result == "skipped":
                skipped += 1
                print(f"  {label} SKIP  {entry.internal_path}")
            else:
                extracted += 1
                print(f"  {label} OK    {entry.internal_path}")
        except Exception as ex:
            failed += 1
            print(f"  {label} FAIL  {entry.internal_path}: {ex}", file=sys.stderr)

    print(f"\nDone — {extracted} extracted, {skipped} skipped, {failed} failed.")
    return 1 if failed else 0


if __name__ == "__main__":
    main()
