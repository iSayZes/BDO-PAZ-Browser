"""HTML of the Model tab: a toolbar, the rig toolbar and the WebGL stage.

ModelHandler (bdo_preview.py) calls these for the PAR meshes (`.pam`,
`.pcm`, `.pac`), skeletons (`.pab`) and animation clips (`.paa`).
ui/js/features/model-view.js draws the stage; the rig toolbar (bones,
animation picker, play) fills in once Api.get_model_skeleton has found a
skeleton (model-rig.js).
"""
from __future__ import annotations

import base64
import html as _html
import json
from dataclasses import dataclass

from preview_views import count_text, segmented_control
from ui_text import ui_text

# What the stage poses: a skinned .pac mesh, a .pab skeleton or a .paa clip.
RIG_MESH = "mesh"
RIG_SKELETON = "skeleton"
RIG_CLIP = "clip"


@dataclass(frozen=True)
class RigView:
    """The skin of a `.pac` (`RIG_MESH`) or what a mesh-less view shows (`RIG_SKELETON`, `RIG_CLIP`).

    `bone_indices` and `bone_weights` hold 4 bytes per vertex: indices into
    `palette`, the `bone_id` of each palette slot, and weights that add up
    to about 255.
    """

    kind: str
    palette: tuple[int, ...] = ()
    bone_indices: bytes = b""
    bone_weights: bytes = b""


def model_meta(vertex_count: int, triangle_count: int, submesh_count: int) -> str:
    """`1,234 vertices · 2,000 triangles · 3 submeshes`."""
    return " · ".join((
        count_text("preview.vertex", vertex_count),
        count_text("preview.triangle", triangle_count),
        count_text("preview.submesh", submesh_count),
    ))


def skeleton_meta(bone_count: int) -> str:
    """`255 bones`."""
    return count_text("preview.bone", bone_count)


def clip_meta(bone_count: int, duration: float) -> str:
    """`69 bones · 3.33 s`."""
    return " · ".join((count_text("preview.bone", bone_count), ui_text("preview.seconds", value=f"{duration:.2f}")))


def _base64(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii")


def _rig_toolbar(rig: RigView) -> str:
    """Bones toggle, clip picker, play and clock; hidden until a skeleton is found."""
    shows_bones = rig.kind != RIG_MESH
    bones_state = 'class="active" aria-pressed="true"' if shows_bones else 'aria-pressed="false"'
    animation = _html.escape(ui_text("preview.animation"))
    return (
        '<div class="view-toolbar model-rig" hidden>'
        f'<button type="button" data-action="model-bones" {bones_state}>{_html.escape(ui_text("preview.bones"))}</button>'
        f'<label class="input-box model-clip-box"><span class="input-box-label">{animation}</span>'
        f'<input type="search" class="model-clip" list="model-clip-list" spellcheck="false" '
        f'placeholder="{_html.escape(ui_text("preview.animationSearch"), quote=True)}"></label>'
        '<datalist id="model-clip-list"></datalist>'
        f'<button type="button" data-action="model-play" disabled>{_html.escape(ui_text("preview.play"))}</button>'
        '<span class="view-meta model-clock"></span>'
        '<span class="view-toolbar-gap"></span>'
        '<span class="view-meta model-skeleton" aria-live="polite"></span>'
        '</div>'
    )


def _rig_data(rig: RigView | None) -> str:
    if rig is None:
        return ""
    palette = _html.escape(json.dumps(list(rig.palette)), quote=True)
    return (f' data-rig="{rig.kind}" data-palette="{palette}" '
            f'data-bones="{_base64(rig.bone_indices)}" data-weights="{_base64(rig.bone_weights)}"')


def model_view_html(
    positions: bytes,
    uvs: bytes,
    indices: bytes,
    submeshes: list[tuple[int, int, str]],
    meta: str,
    rig: RigView | None = None,
) -> str:
    """The model canvas with shading, a texture count, a reset button and, for a `rig`, the rig toolbar.

    `positions` holds float32 x, y, z per vertex, `uvs` float32 u, v per
    vertex (empty for a mesh without them) and `indices` uint32 triangle
    corners, all little-endian; `submeshes` the (first index, index count,
    texture file name) of each part. The view tints the parts apart and
    fetches their textures (Api.get_model_texture). A view with neither
    triangles nor a rig gets a note in place of the canvas.
    """
    toolbar = f'<span class="view-meta">{_html.escape(meta)}</span>'
    if not indices and rig is None:
        return (
            f'<div class="model-view"><div class="view-toolbar">{toolbar}</div>'
            f'<div class="model-note">{_html.escape(ui_text("preview.modelEmpty"))}</div></div>'
        )
    has_textures = bool(uvs) and any(texture for _, _, texture in submeshes)
    shading = ""
    if indices:
        modes = [("solid", ui_text("preview.shadingSolid")), ("wire", ui_text("preview.shadingWire"))]
        if has_textures:
            modes.insert(0, ("textured", ui_text("preview.shadingTextured")))
        shading = segmented_control("model-shading", "preview.shading", modes, modes[0][0])
    reset = (f'<button type="button" data-action="model-reset">'
             f'{_html.escape(ui_text("preview.resetView"))}</button>')
    parts = _html.escape(json.dumps(submeshes, separators=(",", ":")), quote=True)
    textures = '<span class="view-meta model-textures" aria-live="polite"></span>' if has_textures else ""
    return (
        '<div class="model-view">'
        f'<div class="view-toolbar">{toolbar}{textures}<span class="view-toolbar-gap"></span>{shading}{reset}</div>'
        f'{_rig_toolbar(rig) if rig else ""}'
        f'<div class="model-stage" data-positions="{_base64(positions)}" data-uvs="{_base64(uvs)}" '
        f'data-indices="{_base64(indices)}" data-submeshes="{parts}"{_rig_data(rig)}>'
        '<canvas></canvas>'
        f'<div class="model-note model-hint">{_html.escape(ui_text("preview.modelHint"))}</div>'
        '</div>'
        '</div>'
    )
