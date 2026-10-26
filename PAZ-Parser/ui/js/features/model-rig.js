"use strict";

import { t } from "../core/i18n.js";
import {
  boneLines,
  decodeBase64,
  decodeClip,
  decodeSkeleton,
  jointPositions,
  paletteBones,
  poseWorld,
  skinVertices,
} from "./model-pose.js";
import { vertexNormals } from "./model-renderer.js";

// The rig toolbar of a Model tab (preview_model.py _rig_toolbar): finds the
// skeleton of the open .pac, .pab or .paa (Api.get_model_skeleton), lists
// the clips of its motion folder (Api.list_model_animations), loads the one
// picked (Api.get_model_animation) and plays it on the bones and the
// skinned mesh. A .paa view plays its own clip at once.

const RIG_MESH = "mesh";
const RIG_CLIP = "clip";
const CLOCK_DIGITS = 2;
const MS_PER_SECOND = 1000;

function fileName(path) {
  return path.slice(path.lastIndexOf("/") + 1);
}

export class ModelRig {
  // `view` holds the toolbars and the stage; `mesh` the bind-pose geometry
  // the renderer was built from; `path` the open file.
  constructor(view, renderer, mesh, path) {
    const stage = view.querySelector(".model-stage");
    this._view = view;
    this._renderer = renderer;
    this._path = path;
    this._kind = stage.dataset.rig;
    this._toolbar = view.querySelector(".model-rig");
    this._input = this._toolbar.querySelector(".model-clip");
    this._list = this._toolbar.querySelector("datalist");
    this._playButton = this._toolbar.querySelector('[data-action="model-play"]');
    this._clock = this._toolbar.querySelector(".model-clock");
    this._status = this._toolbar.querySelector(".model-skeleton");
    this._showsBones = this._toolbar.querySelector('[data-action="model-bones"]').getAttribute("aria-pressed") === "true";
    this._skin = this._kind === RIG_MESH ? {
      positions: mesh.positions,
      normals: vertexNormals(mesh.positions, mesh.indices),
      boneIndices: decodeBase64(stage.dataset.bones, Uint8Array),
      boneWeights: decodeBase64(stage.dataset.weights, Uint8Array),
      palette: JSON.parse(stage.dataset.palette),
      bones: null,
    } : null;
    this._skeleton = null;
    this._clip = null;
    this._clipPaths = new Map();
    this._timeMs = 0;
    this._isPlaying = false;
    this._frame = 0;
    this._lastTick = 0;
    this._isDisposed = false;
    this._input.addEventListener("change", () => this._pickClip(this._input.value.trim()));
  }

  async start() {
    const result = await window.pywebview.api.get_model_skeleton(this._path);
    if (this._isDisposed) return;
    this._toolbar.hidden = false;
    if (!result.skeleton) {
      this._setEnabled(false);
      this._status.textContent = result.error;
      return;
    }
    this._skeleton = decodeSkeleton(result.skeleton);
    this._world = new Float32Array(this._skeleton.parents.length * 16);
    if (this._skin) {
      this._skin.bones = paletteBones(this._skeleton, this._skin.palette);
      this._posed = { positions: new Float32Array(this._skin.positions.length), normals: new Float32Array(this._skin.positions.length) };
    }
    this._showSkeletonStatus(0);
    this._pose();
    if (!this._skin) this._renderer.fitPoints(jointPositions(this._world));
    await this._listClips();
    if (this._kind === RIG_CLIP && !this._isDisposed) {
      this._input.value = this._clipName(this._path);
      await this._loadClip(this._path);
    }
  }

  toggleBones(button) {
    this._showsBones = !this._showsBones;
    button.classList.toggle("active", this._showsBones);
    button.setAttribute("aria-pressed", String(this._showsBones));
    this._pose();
  }

  togglePlay() {
    if (!this._clip) return;
    this._isPlaying = !this._isPlaying;
    this._playButton.textContent = t(this._isPlaying ? "preview.pause" : "preview.play");
    if (this._isPlaying) this._run();
  }

  dispose() {
    this._isDisposed = true;
    this._isPlaying = false;
    cancelAnimationFrame(this._frame);
  }

  _setEnabled(isEnabled) {
    this._toolbar.querySelectorAll("button, input").forEach((control) => {
      control.disabled = !isEnabled;
    });
  }

  async _listClips() {
    const { folder, clips } = await window.pywebview.api.list_model_animations(this._skeleton.path);
    if (this._isDisposed) return;
    this._folder = folder;
    this._clipPaths = new Map(clips.map((path) => [this._clipName(path), path]));
    const options = [...this._clipPaths.keys()].map((name) => {
      const option = document.createElement("option");
      option.value = name;
      return option;
    });
    this._list.replaceChildren(...options);
    this._input.disabled = clips.length === 0;
    this._showSkeletonStatus(clips.length);
  }

  // A clip's path inside the motion folder, as the picker lists it.
  _clipName(path) {
    return this._folder && path.toLowerCase().startsWith(this._folder.toLowerCase())
      ? path.slice(this._folder.length)
      : fileName(path);
  }

  _showSkeletonStatus(clipCount) {
    const skeleton = this._skeleton;
    const name = fileName(skeleton.path);
    let text = t("preview.rigSkeleton", { name });
    if (this._skin && !skeleton.isComplete) {
      const held = this._skin.palette.filter((id) => skeleton.indexById.has(id)).length;
      text = t("preview.rigPartial", { name, held, total: this._skin.palette.length });
    }
    const clips = clipCount ? t("preview.clipCount", { count: clipCount.toLocaleString() }) : t("preview.noClips");
    this._status.textContent = `${text} · ${clips}`;
    this._status.title = skeleton.path;
  }

  async _pickClip(name) {
    const path = this._clipPaths.get(name);
    if (!name) {
      this._stopClip();
      return;
    }
    if (path && path !== this._clip?.path) await this._loadClip(path);
  }

  async _loadClip(path) {
    const result = await window.pywebview.api.get_model_animation(path);
    if (this._isDisposed) return;
    if (!result.animation) {
      this._clock.textContent = t("preview.clipError", { message: result.error });
      return;
    }
    this._clip = decodeClip(result.animation, this._skeleton);
    this._timeMs = 0;
    this._playButton.disabled = false;
    if (!this._isPlaying) this.togglePlay();
    else this._pose();
  }

  _stopClip() {
    this._clip = null;
    this._isPlaying = false;
    this._playButton.disabled = true;
    this._playButton.textContent = t("preview.play");
    this._clock.textContent = "";
    this._pose();
  }

  _run() {
    this._lastTick = performance.now();
    const tick = (now) => {
      if (!this._isPlaying || this._isDisposed) return;
      const duration = this._clip.durationMs;
      this._timeMs = duration > 0 ? (this._timeMs + now - this._lastTick) % duration : 0;
      this._lastTick = now;
      this._pose();
      this._frame = requestAnimationFrame(tick);
    };
    this._frame = requestAnimationFrame(tick);
  }

  // Poses the bones (and the mesh) at the clip's current time, or the bind pose.
  _pose() {
    if (!this._skeleton || this._isDisposed) return;
    poseWorld(this._skeleton, this._clip, this._timeMs, this._world);
    if (this._skin) {
      skinVertices(this._skeleton, this._world, this._skin, this._posed);
      this._renderer.setVertices(this._posed.positions, this._posed.normals);
    }
    this._renderer.setBoneLines(this._showsBones ? boneLines(this._skeleton, this._world) : null);
    if (this._clip) {
      const seconds = (value) => (value / MS_PER_SECOND).toFixed(CLOCK_DIGITS);
      this._clock.textContent = `${seconds(this._timeMs)} / ${t("preview.seconds", { value: seconds(this._clip.durationMs) })}`;
    }
  }
}
