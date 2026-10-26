"""Textures of the Model view (ModelTexturesMixin).

A mesh names its texture by file name only (`par_mesh.Submesh.texture`):
`wood_66.dds` in a `.pam`, the submesh name plus `.dds` in a `.pac`. The
file sits in the mesh's own folder (the `hloddata` and
`sectormapinfo_combine` LOD meshes), in `object/texture/` or in
`character/texture/`; `texture_thumbnail/` holds small copies, which are
skipped. A sector LOD mesh names a texture the client does not ship
(`52_0_10_LOD.dds` in `52_10_0_lod.pam`), and its texture is the `.dds` of
the mesh's own name.
"""

from __future__ import annotations

from pathlib import PurePosixPath

from ui_text import ui_text

from .bdo_api_helpers import _norm
from .bdo_api_state import ApiState
from .bdo_icon_images import open_image, preview_data_url

_TEXTURE_FOLDERS = ("object/texture", "character/texture")
_TEXTURE_EXT = ".dds"
# Decoded textures kept as data URLs, oldest dropped first: a character
# shares its textures across the meshes of its folder.
_TEXTURE_CACHE_SIZE = 64


def model_texture_paths(model_path: str, texture: str) -> list[str]:
    """The lowercase PAZ paths to try for `texture` of the mesh at `model_path`, best first."""
    name = PurePosixPath(_norm(texture).strip()).name.lower()
    model = PurePosixPath(_norm(model_path).strip().lower())
    if not name or not model.name:
        return []
    folder = str(model.parent)
    # The texture folder of the mesh's own tree first: a .pac also uses object textures.
    folders = sorted(_TEXTURE_FOLDERS, key=lambda candidate: not candidate.startswith(model.parts[0]))
    paths = [f"{folder}/{name}", *(f"{candidate}/{name}" for candidate in folders)]
    paths.append(f"{folder}/{model.stem}{_TEXTURE_EXT}")
    return list(dict.fromkeys(paths))


class ModelTexturesMixin(ApiState):
    def get_model_texture(self, model_path: str, texture: str) -> dict:
        """`{"url", "path"}` of a mesh's texture as a PNG data URL, scaled like the icon
        preview, or `{"error"}` when the client has no such texture."""
        self._mark_activity()
        if not isinstance(model_path, str) or not isinstance(texture, str):
            return {"error": ui_text("errors.textureNotFound", name=str(texture))}
        entry = next(
            (found for path in model_texture_paths(model_path, texture)
             if (found := self._entry_ignoring_case(path)) is not None),
            None,
        )
        if entry is None:
            return {"error": ui_text("errors.textureNotFound", name=texture)}

        path = _norm(entry.internal_path)
        # One decode at a time, as for the icons: a mesh asks for all its
        # textures at once, and each JS call runs in its own thread.
        with self._model_texture_lock:
            cache = self._model_texture_urls
            url = cache.pop(path, None)
            if url is None:
                try:
                    url = preview_data_url(open_image(self.read_entry(path)))
                except Exception as ex:
                    return {"error": str(ex)}
            cache[path] = url
            while len(cache) > _TEXTURE_CACHE_SIZE:
                cache.pop(next(iter(cache)))
        return {"url": url, "path": path}
