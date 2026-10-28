from __future__ import annotations

import asyncio
import base64
import json
import os
import secrets
import threading
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from aiohttp import web

from bdo_models import PazEntry
from map_api import add_map_api
from map_icons_build import icon_file
from map_pins import PinStore
from world_map_build import tile_file


class StreamReader(Protocol):
    def get_entry(self, internal_path: str) -> PazEntry | None: ...
    def is_streamable(self, internal_path: str) -> bool: ...
    def get_stream_mime_type(self, internal_path: str) -> str: ...
    def read_entry(self, internal_path: str) -> bytes: ...


@dataclass(frozen=True)
class _MapTiles:
    folder: Path
    content_key: str


# Map tile URLs carry the client's content key (version and archive row digest),
# so a tile never changes under its URL, not even after a repack.
_TILE_CACHE_CONTROL = "max-age=31536000, immutable"


@dataclass(frozen=True)
class _ByteRange:
    start: int
    end: int


class LocalServer:
    def __init__(self) -> None:
        self.port = 0
        self.token = secrets.token_urlsafe(24)
        self._reader: StreamReader | None = None
        # The built world map the Map view shows (`serve_map`), or None.
        self._map_tiles: _MapTiles | None = None
        # The pins of the map API (`map_api.py`), set by the app.
        self._pins: PinStore | None = None
        self._loop: asyncio.AbstractEventLoop | None = None
        self._runner: web.AppRunner | None = None
        self._thread: threading.Thread | None = None
        self._started = threading.Event()
        self._stopped = threading.Event()
        self._startup_error: BaseException | None = None

    def set_reader(self, reader: StreamReader) -> None:
        self._reader = reader

    def set_pin_store(self, pins: PinStore) -> None:
        self._pins = pins

    def write_info(self, path: Path) -> None:
        """Write the port and token to `path` (`app_dirs.server_info_file`) for other programs."""
        info = {"base_url": f"http://127.0.0.1:{self.port}", "port": self.port, "token": self.token, "pid": os.getpid()}
        path.parent.mkdir(parents=True, exist_ok=True)
        temp = path.with_name(f"{path.name}.tmp")
        temp.write_text(json.dumps(info, indent=2), encoding="utf-8")
        os.replace(temp, path)

    def remove_info(self, path: Path) -> None:
        """Delete `path` if this server wrote it; a newer app instance may own it by now."""
        try:
            info = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return
        if isinstance(info, dict) and info.get("token") == self.token:
            path.unlink(missing_ok=True)

    def start(self) -> None:
        if self._thread is not None:
            return
        self._thread = threading.Thread(target=self._run, name="bdo-local-server", daemon=True)
        self._thread.start()
        self._started.wait(timeout=5)
        if self._startup_error is not None:
            raise RuntimeError("Local server failed to start") from self._startup_error
        if self.port == 0:
            raise RuntimeError("Local server did not report a port")

    def stop(self) -> None:
        loop = self._loop
        if loop is None:
            return
        asyncio.run_coroutine_threadsafe(self._shutdown(), loop).result(timeout=5)
        loop.call_soon_threadsafe(loop.stop)
        self._stopped.wait(timeout=5)

    def stream_url(self, internal_path: str) -> str:
        encoded = base64.urlsafe_b64encode(internal_path.encode("utf-8")).decode("ascii")
        return f"http://127.0.0.1:{self.port}/stream?path={encoded}&t={self.token}"

    def serve_map(self, folder: Path | None, content_key: str) -> str:
        """Serve the map tiles in `folder` (`<zoom>/<x>/<y>.jpg`), or none when None.

        Returns the Leaflet tile URL template; the content key in it
        (`paz/bdo_content_key.py`) keeps the page from showing a tile of
        another client or of the same client before a repack.
        """
        self._map_tiles = None if folder is None else _MapTiles(folder=folder, content_key=content_key)
        return f"http://127.0.0.1:{self.port}/map/{content_key}/{{z}}/{{x}}/{{y}}.jpg?t={self.token}"

    def map_icon_url(self, content_key: str) -> str:
        """The URL template of the served map's icons (`map_icons_build.py`), `{name}` for the icon name."""
        return f"http://127.0.0.1:{self.port}/map/{content_key}/icons/{{name}}.png?t={self.token}"

    def _run(self) -> None:
        loop = asyncio.new_event_loop()
        self._loop = loop
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(self._startup())
            self._started.set()
            loop.run_forever()
        except BaseException as ex:
            self._startup_error = ex
            self._started.set()
        finally:
            loop.run_until_complete(loop.shutdown_asyncgens())
            loop.close()
            self._stopped.set()

    async def _startup(self) -> None:
        app = web.Application()
        app.router.add_get("/stream", self._handle_stream)
        app.router.add_get(r"/map/{key:[0-9a-f-]+}/{zoom:\d+}/{x:-?\d+}/{y:-?\d+}.jpg", self._handle_map_tile)
        app.router.add_get(r"/map/{key:[0-9a-f-]+}/icons/{name:[a-z_]+}.png", self._handle_map_icon)
        add_map_api(app, self.token, lambda: self._pins)
        self._runner = web.AppRunner(app)
        await self._runner.setup()
        site = web.TCPSite(self._runner, "127.0.0.1", 0)
        await site.start()
        sockets = getattr(site, "_server").sockets
        self.port = sockets[0].getsockname()[1]

    async def _shutdown(self) -> None:
        if self._runner is not None:
            await self._runner.cleanup()
            self._runner = None

    async def _handle_stream(self, request: web.Request) -> web.Response:
        if request.query.get("t") != self.token:
            raise web.HTTPForbidden(text="Invalid stream token")
        reader = self._reader
        if reader is None:
            raise web.HTTPServiceUnavailable(text="No stream reader")

        internal_path = self._decode_path(request.query.get("path", ""))
        entry = reader.get_entry(internal_path)
        if entry is None:
            raise web.HTTPNotFound(text="Entry not found")
        if not reader.is_streamable(internal_path):
            raise web.HTTPForbidden(text="Entry is not streamable")

        data = await asyncio.to_thread(reader.read_entry, internal_path)
        mime_type = reader.get_stream_mime_type(internal_path)
        byte_range = self._parse_range(request.headers.get("Range"), len(data))
        headers = {
            "Accept-Ranges": "bytes",
            "Access-Control-Allow-Origin": "*",
            "Content-Type": mime_type,
        }

        if byte_range is None:
            headers["Content-Length"] = str(len(data))
            return web.Response(body=data, headers=headers)

        chunk = data[byte_range.start:byte_range.end + 1]
        headers["Content-Range"] = f"bytes {byte_range.start}-{byte_range.end}/{len(data)}"
        headers["Content-Length"] = str(len(chunk))
        return web.Response(status=206, body=chunk, headers=headers)

    async def _handle_map_tile(self, request: web.Request) -> web.StreamResponse:
        if request.query.get("t") != self.token:
            raise web.HTTPForbidden(text="Invalid stream token")
        tiles = self._map_tiles
        match = request.match_info
        if tiles is None or match["key"] != tiles.content_key:
            raise web.HTTPNotFound(text="No map for this client")
        # The route only matches whole numbers, so the path stays inside the folder.
        # A tile without radar images under it gets one of its zoom's sea tiles.
        path = tile_file(tiles.folder, int(match["zoom"]), (int(match["x"]), int(match["y"])))
        if path is None:
            raise web.HTTPNotFound(text="No tile")
        return web.FileResponse(path, headers={"Cache-Control": _TILE_CACHE_CONTROL})

    async def _handle_map_icon(self, request: web.Request) -> web.StreamResponse:
        if request.query.get("t") != self.token:
            raise web.HTTPForbidden(text="Invalid stream token")
        tiles = self._map_tiles
        if tiles is None or request.match_info["key"] != tiles.content_key:
            raise web.HTTPNotFound(text="No map for this client")
        # Only the catalog's names: the path stays inside the icons folder.
        path = icon_file(tiles.folder, request.match_info["name"])
        if path is None:
            raise web.HTTPNotFound(text="No such icon")
        return web.FileResponse(path)

    @staticmethod
    def _decode_path(value: str) -> str:
        try:
            return base64.urlsafe_b64decode(value.encode("ascii")).decode("utf-8")
        except Exception as ex:
            raise web.HTTPBadRequest(text="Invalid stream path") from ex

    @staticmethod
    def _parse_range(header: str | None, size: int) -> _ByteRange | None:
        if not header:
            return None
        if not header.startswith("bytes="):
            raise web.HTTPRequestRangeNotSatisfiable(headers={"Content-Range": f"bytes */{size}"})

        spec = header[6:].split(",", 1)[0].strip()
        if "-" not in spec:
            raise web.HTTPRequestRangeNotSatisfiable(headers={"Content-Range": f"bytes */{size}"})
        start_text, end_text = spec.split("-", 1)

        try:
            if start_text == "":
                suffix_len = int(end_text)
                if suffix_len <= 0:
                    raise ValueError
                start = max(0, size - suffix_len)
                end = size - 1
            else:
                start = int(start_text)
                end = int(end_text) if end_text else size - 1
        except ValueError as ex:
            raise web.HTTPRequestRangeNotSatisfiable(headers={"Content-Range": f"bytes */{size}"}) from ex

        if start < 0 or start >= size or end < start:
            raise web.HTTPRequestRangeNotSatisfiable(headers={"Content-Range": f"bytes */{size}"})
        return _ByteRange(start=start, end=min(end, size - 1))
