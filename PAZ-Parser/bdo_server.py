from __future__ import annotations

import asyncio
import base64
import secrets
import threading
from dataclasses import dataclass
from typing import Protocol

from aiohttp import web

from bdo_models import PazEntry


class StreamReader(Protocol):
    def get_entry(self, internal_path: str) -> PazEntry | None: ...
    def is_streamable(self, internal_path: str) -> bool: ...
    def get_stream_mime_type(self, internal_path: str) -> str: ...
    def read_entry(self, internal_path: str) -> bytes: ...


@dataclass(frozen=True)
class _ByteRange:
    start: int
    end: int


class LocalServer:
    def __init__(self) -> None:
        self.port = 0
        self.token = secrets.token_urlsafe(24)
        self._reader: StreamReader | None = None
        self._loop: asyncio.AbstractEventLoop | None = None
        self._runner: web.AppRunner | None = None
        self._thread: threading.Thread | None = None
        self._started = threading.Event()
        self._stopped = threading.Event()
        self._startup_error: BaseException | None = None

    def set_reader(self, reader: StreamReader) -> None:
        self._reader = reader

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
