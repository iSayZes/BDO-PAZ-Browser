"""PAZ paths of the texture paths tables store.

Tables store a texture path relative to `ui_texture/` ("Combine/Icon/...",
"Icon/Quest/...", "UI_Artwork/...") or, for item icons, relative to
`ui_texture/icon/` ("New_Icon/..."), in the client's mixed case. The PAZ index
spells them lowercase under those folders.
"""

from __future__ import annotations


UI_TEXTURE_ROOT = "ui_texture/"
UI_TEXTURE_ICON_ROOT = f"{UI_TEXTURE_ROOT}icon/"


def ui_texture_path(stored: str, root: str = UI_TEXTURE_ROOT) -> str:
    """PAZ path of a stored texture path under `root`, or '' when there is none."""
    return f"{root}{stored.lower()}" if stored else ""
