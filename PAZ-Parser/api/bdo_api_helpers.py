from __future__ import annotations

_DISK_VIRTUAL_PREFIX = "__disk__"

_ICON_MAP: dict[str, str] = {
    ".dds": "🖼", ".png": "🖼", ".jpg": "🖼", ".jpeg": "🖼", ".bmp": "🖼", ".tga": "🖼",
    ".xml": "📋", ".json": "📋", ".yaml": "📋", ".yml": "📋",
    ".txt": "📄", ".log": "📄", ".csv": "📄", ".ini": "📄", ".cfg": "📄",
    ".htm": "🌐", ".html": "🌐",
    ".lua": "📜",
    ".webm": "🎬",
    ".pac": "📦", ".bss": "🔒", ".dbss": "🔒",
    ".loc": "💬",
}


def _norm(path: str) -> str:
    return path.replace("\\", "/")


def _file_icon(ext: str) -> str:
    return _ICON_MAP.get(ext.lower(), "·")
