from __future__ import annotations

import argparse
import subprocess
import sys
import threading
from collections.abc import Callable
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from bdo_preview import load_plugins, plugin_failures, use_handlers_dir
from updates.handler_packs import active_pack, mark_running_pack_bad

# The core imports `_common` from the handlers folder, so the pack this run
# uses (updates/handler_packs.py) goes on the path before the imports below.
use_handlers_dir(active_pack().folder)

import webview

from api.bdo_api import Api
from api.bdo_config import LEGACY_CONFIG_FILE
from app_dirs import adopt_legacy_config
from cli.files import run_extract, run_list
from cli.formats import run_formats, run_handlers
from cli.index import run_index
from cli.records import run_records
from cli.render import run_render
from cli.update import run_check_app_update, run_update_app, update_handlers
from cli.stdio import close_stdout_quietly, configure_logging, is_closed_pipe, use_utf8_stdio

# Options that only mean something with one command, checked in _check_options.
_RECORDS_ONLY = ("where", "fields")
_OUTPUT_OPTIONS = ("json", "csv", "limit")


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()
    _check_options(parser, args)
    adopt_legacy_config(LEGACY_CONFIG_FILE)
    _load_handlers()

    command = _command(args)
    if command is None and not args.update_handlers:
        _launch_gui(profile=args.profile, after_update=args.after_update)
        return

    use_utf8_stdio()
    configure_logging()
    try:
        code = _run_command(command, args)
    except OSError as ex:
        if not is_closed_pipe(ex):
            raise
        code = 0
    close_stdout_quietly()
    sys.exit(code)


def _load_handlers() -> None:
    """Register the pack's handlers; an installed pack that fails to load is never picked again."""
    pack = active_pack()
    load_plugins(pack.folder)
    failures = plugin_failures()
    if failures:
        mark_running_pack_bad(pack, "; ".join(f"{name}: {reason}" for name, reason in failures.items()))


def _run_command(command: Callable[[argparse.Namespace], int] | None, args: argparse.Namespace) -> int:
    """`--update-handlers` first, when given, then the command."""
    if not args.update_handlers:
        return command(args) if command is not None else 0
    code, is_installed = update_handlers()
    if code != 0 or command is None:
        return code
    if is_installed:
        # This process runs the old pack; the command runs again with the new one.
        rest = [arg for arg in sys.argv[1:] if arg != "--update-handlers"]
        sys.stdout.flush()
        return subprocess.call([sys.executable, *rest])
    return command(args)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="browser",
        description="BDO PAZ Browser, omit a command to open the GUI.",
    )
    parser.add_argument("--paz-folder", metavar="DIR", help="Path to the PAZ folder (default: last used)")

    commands = parser.add_mutually_exclusive_group()
    commands.add_argument("--file", metavar="PATTERN", help="File name or glob pattern to extract, e.g. title.dbss or *title*.dbss")
    commands.add_argument("--list", metavar="PATTERN", help="List matching file paths without extracting, e.g. title*.dbss")
    commands.add_argument("--formats", action="store_true", help="Show supported file formats and exit")
    commands.add_argument("--handlers", action="store_true", help="List every registered handler key; needs no PAZ folder")
    commands.add_argument("--records", metavar="FILE", help="Print the parsed records of one file, e.g. buffsimply.bss")
    commands.add_argument("--render", metavar="FILE", help="Write one parsed page of FILE as standalone HTML to stdout")
    commands.add_argument(
        "--index", metavar="KIND", nargs="?", const="",
        help="Print a lookup index, e.g. character_item; without KIND, list every kind",
    )
    commands.add_argument("--check-app-update", action="store_true", help="Print this version and the newest release")
    commands.add_argument(
        "--update-app", metavar="ZIP", nargs="?", const="",
        help="Windows exe: install the newest release, or a downloaded release zip, after this command exits",
    )
    parser.add_argument(
        "--update-handlers", action="store_true",
        help="Windows exe: install a newer handler pack first, then run the command; alone, only update",
    )

    parser.add_argument("--output", metavar="DIR", help="Output directory for --file (default: current working directory)")
    parser.add_argument(
        "--where", metavar="EXPR", action="append", default=[],
        help="--records filter: field=value, field=a..b or field*=text; repeat to combine",
    )
    parser.add_argument("--fields", metavar="A,B,C", help="--records: only these fields, in this order")
    parser.add_argument(
        "--sort",
        metavar="FIELD[:desc]",
        help="--records: sort by FIELD as the GUI table does, ascending or with :desc",
    )
    output = parser.add_mutually_exclusive_group()
    output.add_argument("--json", action="store_true", help="--records / --index: JSON with full values")
    output.add_argument("--csv", action="store_true", help="--records / --index: CSV like the app's export")
    parser.add_argument("--limit", metavar="N", type=_positive_int, help="--records / --index: print at most N rows")
    parser.add_argument("--no-loc", action="store_true", help="--records / --render: do not load LOC text")
    parser.add_argument("--page", metavar="N", type=int, default=1, help="--render: page number, from 1 (default: 1)")
    parser.add_argument("--id", metavar="N", help="--index: one ID, decimal or 0x hex")
    parser.add_argument("--profile", action="store_true", help="Enable backend timing and browser-side JS profiling for the GUI")
    # Passed by the update helper (updates/install.py) when it restarts the GUI.
    parser.add_argument("--after-update", action="store_true", help=argparse.SUPPRESS)
    return parser


def _positive_int(text: str) -> int:
    value = int(text)
    if value < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return value


def _command(args: argparse.Namespace) -> Callable[[argparse.Namespace], int] | None:
    if args.file:
        return run_extract
    if args.list:
        return run_list
    if args.formats:
        return run_formats
    if args.handlers:
        return run_handlers
    if args.records:
        return run_records
    if args.render:
        return run_render
    if args.index is not None:
        return run_index
    if args.check_app_update:
        return run_check_app_update
    if args.update_app is not None:
        return run_update_app
    return None


def _check_options(parser: argparse.ArgumentParser, args: argparse.Namespace) -> None:
    """Reject options given without the command they belong to."""
    is_records = bool(args.records)
    is_index = args.index is not None
    if not is_records:
        for name in _RECORDS_ONLY:
            if getattr(args, name):
                parser.error(f"--{name} needs --records")
    if not (is_records or is_index):
        for name in _OUTPUT_OPTIONS:
            if getattr(args, name):
                parser.error(f"--{name} needs --records or --index")
    if args.no_loc and not (is_records or args.render):
        parser.error("--no-loc needs --records or --render")
    if args.page != 1 and not args.render:
        parser.error("--page needs --render")
    if args.id is not None and not is_index:
        parser.error("--id needs --index")
    if args.id is not None and not args.index:
        parser.error("--id needs an index kind, e.g. --index character_item --id 40024")
    if args.output and not args.file:
        parser.error("--output needs --file")

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


# How long the window stays on top after an update restart.
_AFTER_UPDATE_ON_TOP_SECONDS = 1.5


def _bring_to_front(window: webview.Window) -> None:
    """Raise the window above the others for a moment.

    The update helper starts the new version from a hidden console, and
    Windows keeps a window started that way behind the one in front.
    """
    window.on_top = True
    threading.Timer(_AFTER_UPDATE_ON_TOP_SECONDS, setattr, (window, "on_top", False)).start()


def _launch_gui(profile: bool = False, after_update: bool = False) -> None:
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
        background_color="#121316",  # --color-bg in ui/css/00-reset-root.css
    )
    if window is not None:
        api.set_window(window)
        window.events.shown += lambda: _apply_window_icon(window)
        if after_update:
            window.events.shown += lambda: _bring_to_front(window)
    try:
        webview.start(debug=profile)
    finally:
        server.stop()


if __name__ == "__main__":
    main()
