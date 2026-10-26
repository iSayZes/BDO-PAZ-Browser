"""Skeletons and animation clips of the Model view (ModelRigsMixin).

A `.pac` mesh names its bones by `bone_id` in its palette but not the
`.pab` that holds them: the skeleton is the nearest `.pab` up the folder
tree that holds every palette id the mesh does not carry itself (96,352 of
97,151 meshes with a palette on client 3483, `skeleton_pab.md`). Clips
mirror the skeleton folders: the clips of a skeleton under
`character/model/<group>/<model>/` are the `.paa` files under
`character/motion/<group>/<model>/`, and a clip's skeleton is the `.pab`
under the mirrored model folder that holds the most of its bone ids.

Arrays go to the page as base64 of little-endian float32 / uint16, as the
mesh geometry does (`preview_views.model_view_html`).
"""

from __future__ import annotations

import base64
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import PurePosixPath

import numpy as np

from par_animation import Animation, parse_animation
from par_mesh import parse_mesh
from par_skeleton import Skeleton, parse_skeleton
from ui_text import ui_text

from .bdo_api_helpers import _norm
from .bdo_api_state import ApiState

_SKELETON_EXT = ".pab"
_CLIP_EXT = ".paa"
_MESH_EXT = ".pac"
_MODEL_ROOT = ("character", "model")
_MOTION_ROOT = ("character", "motion")
# character/model/<group>/<model>: the folders that mirror between models and motions.
_MIRROR_DEPTH = 4
# Parsed skeletons kept, oldest dropped first: a mesh folder walk reads a few.
_SKELETON_CACHE_SIZE = 16


@dataclass
class RigIndex:
    """The loaded folder's `.pab` files by folder and its `.paa` files by mirrored folder."""

    skeletons_by_folder: dict[str, list[str]] = field(default_factory=dict)
    clips_by_mirror: dict[str, list[str]] = field(default_factory=dict)

    @classmethod
    def build(cls, paths: Iterable[str]) -> RigIndex:
        index = cls()
        for path in paths:
            lower = path.lower()
            if lower.endswith(_SKELETON_EXT):
                index.skeletons_by_folder.setdefault(str(PurePosixPath(lower).parent), []).append(path)
            elif lower.endswith(_CLIP_EXT):
                mirror = mirror_key(lower)
                if mirror is not None:
                    index.clips_by_mirror.setdefault(mirror, []).append(path)
        for paths_in in (*index.skeletons_by_folder.values(), *index.clips_by_mirror.values()):
            paths_in.sort(key=str.lower)
        return index

    def skeletons_under(self, mirror: str) -> list[str]:
        """Every `.pab` in the model folder of `mirror` and below it."""
        root = "/".join((*_MODEL_ROOT, mirror))
        return sorted(
            (path for folder, paths in self.skeletons_by_folder.items()
             if folder == root or folder.startswith(root + "/") for path in paths),
            key=lambda path: (path.count("/"), path.lower()),
        )


def mirror_key(path: str) -> str | None:
    """`<group>/<model>` of a lowercase path under character/model or character/motion, else None."""
    parts = PurePosixPath(path).parts
    if len(parts) <= _MIRROR_DEPTH or parts[:2] not in (_MODEL_ROOT, _MOTION_ROOT):
        return None
    return "/".join(parts[2:_MIRROR_DEPTH])


def _base64(array: np.ndarray) -> str:
    return base64.b64encode(np.ascontiguousarray(array).tobytes()).decode("ascii")


def skeleton_payload(path: str, skeleton: Skeleton, is_complete: bool) -> dict:
    """The bones for model-skeleton.js: names, parents, ids and three float32 arrays."""
    return {
        "path": path,
        "isComplete": is_complete,
        "ids": list(skeleton.bone_ids),
        "names": list(skeleton.names),
        "parents": list(skeleton.parents),
        "world": _base64(skeleton.world.astype("<f4")),
        "inverseWorld": _base64(skeleton.inverse_world.astype("<f4")),
        "local": _base64(skeleton.local.astype("<f4")),
    }


def animation_payload(path: str, animation: Animation) -> dict:
    """The keys for model-skeleton.js: per node `[bone id, scale, rotation, translation key counts]`,
    then every key time (uint16) and value (float32) in that order, node by node."""
    tracks = [track for node in animation.nodes for track in (node.scale, node.rotation, node.translation)]
    times = np.concatenate([track.times for track in tracks]) if tracks else np.zeros(0, np.uint16)
    values = (np.concatenate([track.values.ravel() for track in tracks]) if tracks
              else np.zeros(0, np.float32))
    return {
        "path": path,
        "duration": animation.duration,
        "nodes": [[node.bone_id, len(node.scale.times), len(node.rotation.times), len(node.translation.times)]
                  for node in animation.nodes],
        "times": _base64(times.astype("<u2")),
        "values": _base64(values.astype("<f4")),
    }


class ModelRigsMixin(ApiState):
    def get_model_skeleton(self, model_path: str) -> dict:
        """`{"skeleton": ...}` for a `.pac`, `.pab` or `.paa` at `model_path`, or `{"error"}`.

        A mesh gets the skeleton its palette points at (`isComplete` false
        when the best one misses some ids), a skeleton itself, and a clip the
        skeleton its bones fit best.
        """
        self._mark_activity()
        if not isinstance(model_path, str):
            return {"error": ui_text("errors.skeletonNotFound")}
        path = _norm(model_path)
        try:
            with self._model_rig_lock:
                found = self._find_skeleton(path)
                if found is None:
                    return {"error": ui_text("errors.skeletonNotFound")}
                skeleton_path, is_complete = found
                skeleton = self._skeleton(skeleton_path)
            return {"skeleton": skeleton_payload(skeleton_path, skeleton, is_complete)}
        except (OSError, ValueError) as ex:
            return {"error": str(ex)}

    def list_model_animations(self, skeleton_path: str) -> dict:
        """`{"folder", "clips"}`: the `.paa` paths under the motion folder that mirrors the skeleton's."""
        self._mark_activity()
        mirror = mirror_key(_norm(str(skeleton_path)).lower())
        if mirror is None:
            return {"folder": "", "clips": []}
        with self._model_rig_lock:
            clips = list(self._rig_index().clips_by_mirror.get(mirror, []))
        return {"folder": "/".join((*_MOTION_ROOT, mirror)) + "/", "clips": clips}

    def get_model_animation(self, clip_path: str) -> dict:
        """`{"animation": ...}` with the keys of the `.paa` at `clip_path`, or `{"error"}`."""
        self._mark_activity()
        entry = self._entry_ignoring_case(_norm(str(clip_path)))
        if entry is None:
            return {"error": ui_text("errors.entryNotFound")}
        path = _norm(entry.internal_path)
        try:
            return {"animation": animation_payload(path, parse_animation(self.read_entry(path)))}
        except (OSError, ValueError) as ex:
            return {"error": str(ex)}

    def _find_skeleton(self, path: str) -> tuple[str, bool] | None:
        lower = path.lower()
        if lower.endswith(_SKELETON_EXT):
            entry = self._entry_ignoring_case(path)
            return None if entry is None else (_norm(entry.internal_path), True)
        if lower.endswith(_MESH_EXT):
            skin = parse_mesh(self._read_or_raise(path)).skin
            if skin is None:
                return None
            return self._skeleton_for_ids(set(skin.palette) - set(skin.own_bone_ids), self._folders_up(lower))
        if lower.endswith(_CLIP_EXT):
            mirror = mirror_key(lower)
            if mirror is None:
                return None
            animation = parse_animation(self._read_or_raise(path))
            found = self._skeleton_for_ids(
                {node.bone_id for node in animation.nodes}, [self._rig_index().skeletons_under(mirror)],
            )
            # A clip plays on the skeleton that fits it best, whole or not.
            return None if found is None else (found[0], True)
        return None

    def _folders_up(self, lower_path: str) -> list[list[str]]:
        """The `.pab` paths of each folder from the file's own up to the top, nearest first."""
        index = self._rig_index()
        return [index.skeletons_by_folder.get(str(folder), []) for folder in PurePosixPath(lower_path).parents]

    def _skeleton_for_ids(self, wanted: set[int], groups: list[list[str]]) -> tuple[str, bool] | None:
        """The first skeleton, group by group, that holds every id of `wanted`; else the one holding most."""
        if not wanted:
            return None
        best: tuple[int, str] | None = None
        for group in groups:
            for path in group:
                ids = set(self._skeleton(path).bone_ids)
                if wanted <= ids:
                    return path, True
                held = len(wanted & ids)
                if held and (best is None or held > best[0]):
                    best = (held, path)
        return None if best is None else (best[1], False)

    def _skeleton(self, path: str) -> Skeleton:
        cache = self._model_skeletons
        skeleton = cache.pop(path, None)
        if skeleton is None:
            skeleton = parse_skeleton(self._read_or_raise(path))
        cache[path] = skeleton
        while len(cache) > _SKELETON_CACHE_SIZE:
            cache.pop(next(iter(cache)))
        return skeleton

    def _read_or_raise(self, path: str) -> bytes:
        data = self._read_any_case(path)
        if data is None:
            raise ValueError(ui_text("errors.entryNotFound"))
        return data

    def _rig_index(self) -> RigIndex:
        if self._model_rig_index is None:
            self._model_rig_index = RigIndex.build(self._entry_map)
        return self._model_rig_index
