"""Handler packs in the GUI: the update on start, "Check now", the restart, version labels."""

from __future__ import annotations

import json
import logging
import subprocess
import sys
import threading
from pathlib import Path

from app_version import build_info, is_frozen, source_commit, source_commit_of
from bdo_preview import handler_key
from ui_text import ui_text
from updates.handler_packs import PackCheck, active_pack, check_for_update, clean_up_packs
from updates.handler_sets import handler_files
from updates.releases import RELEASES_PAGE, UpdateError

from .bdo_api_state import ApiState
from .bdo_api_updates import release_notes_html
from .bdo_config import load_config, update_handlers_setting


class HandlerUpdateMixin(ApiState):
    def start_handler_update(self) -> None:
        """Remove old packs and install a newer one in the background, once per start.

        Exe only, with "Update handlers on start" on. An installed pack runs
        from the next start, so `app.onHandlersUpdated` offers a restart.
        """
        if build_info() is None or not update_handlers_setting(load_config()):
            return
        threading.Thread(target=self._update_handlers_on_start, name="handler-update", daemon=True).start()

    def _update_handlers_on_start(self) -> None:
        clean_up_packs()
        try:
            check = self._run_handler_check()
        except UpdateError:
            logging.warning("Handler update failed", exc_info=True)
            return
        if check.outcome == "installed":
            self._push_js(f"app.onHandlersUpdated({json.dumps(self._installed_info(check))})")

    def check_handler_update(self) -> dict:
        """The settings' "Check now": what the check found, as the settings show it."""
        if build_info() is None:
            return {"ok": False, "message": ui_text("handlerUpdate.sourceOnly")}
        try:
            check = self._run_handler_check()
        except UpdateError as ex:
            logging.warning("Handler update failed", exc_info=True)
            return {"ok": False, "message": ui_text("handlerUpdate.failed", message=str(ex))}
        # Installed now, or by an earlier check while this run kept the old pack.
        if check.outcome == "installed" or (check.outcome == "up_to_date" and active_pack().version != check.latest.version):
            return {"ok": True, "installed": self._installed_info(check)}
        return {"ok": True, "message": _check_message(check)}

    def _run_handler_check(self) -> PackCheck:
        # The start-up check and "Check now" never install at the same time.
        with self._handler_update_lock:
            return check_for_update()

    @staticmethod
    def _installed_info(check: PackCheck) -> dict:
        return {
            "version": check.latest.version,
            "current": active_pack().version,
            "notes_html": release_notes_html(check.latest.notes),
        }

    def restart_app(self) -> dict:
        """Start the exe again and close this window, so the new handler pack runs."""
        if not is_frozen():
            return {"ok": False, "error": ui_text("handlerUpdate.sourceOnly")}
        try:
            # --after-update brings the new window to the front (bdo_app.py).
            subprocess.Popen([sys.executable, "--after-update"], close_fds=True)
        except OSError as ex:
            return {"ok": False, "error": ui_text("handlerUpdate.restartFailed", message=str(ex))}
        if self._window is not None:
            self._window.destroy()
        return {"ok": True}

    def get_app_version(self) -> dict:
        """The bottom bar's version: the exe's release, or the source commit."""
        info = build_info()
        pack = active_pack()
        if info is not None:
            label = ui_text("footer.app", version=info.version)
            commit = info.commit
        else:
            commit = source_commit() or ""
            label = ui_text("footer.appSource", commit=commit) if commit else ui_text("footer.appSourceNoGit")
        return {"label": label, "commit": commit, "handlers": pack.version}

    def get_handler_version(self, name: str) -> dict:
        """`{key, version}` of the handler that reads file `name`, or {} when none does.

        The version is the running pack's, from its manifest. From source it
        is the commit that last changed the handler's files, with a `+` for
        uncommitted edits (`app_version.source_commit_of`).
        """
        key = handler_key(Path(name).name, Path(name).suffix) if isinstance(name, str) else None
        if key is None:
            return {}
        pack = active_pack()
        if pack.manifest is not None:
            handler = pack.manifest.handlers.get(key)
            return {"key": key, "version": handler.version} if handler is not None else {}
        version = source_commit_of([pack.folder / file for file in handler_files(pack.folder, key)])
        return {"key": key, "version": version} if version is not None else {}


def _check_message(check: PackCheck) -> str:
    version = check.latest.version
    if check.outcome == "needs_app":
        return ui_text("handlerUpdate.needsApp", version=version, url=RELEASES_PAGE)
    if check.outcome == "bad":
        return ui_text("handlerUpdate.bad", version=version)
    return ui_text("handlerUpdate.upToDate", version=version)
