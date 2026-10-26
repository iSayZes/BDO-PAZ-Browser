"use strict";

import { t } from "../core/i18n.js";
import { decodeBase64 } from "./model-pose.js";
import { ModelRenderer, WebGLUnavailableError } from "./model-renderer.js";
import { ModelRig } from "./model-rig.js";

// The Model tab of the PAR meshes (.pam, .pcm, .pac), skeletons (.pab) and
// clips (.paa): preview_model.py model_view_html puts the geometry on
// .model-stage as base64 data attributes, and one ModelRenderer draws it.
// Each texture comes from Api.get_model_texture once the mesh is drawn; a
// stage with a data-rig gets a ModelRig that finds its skeleton and plays
// clips. A new view, or a canvas taken off the page, disposes the old
// renderer, so one WebGL context is alive.

function stageMesh(stage) {
  const uvs = stage.dataset.uvs;
  return {
    positions: decodeBase64(stage.dataset.positions, Float32Array),
    uvs: uvs ? decodeBase64(uvs, Float32Array) : null,
    indices: decodeBase64(stage.dataset.indices, Uint32Array),
    submeshes: JSON.parse(stage.dataset.submeshes),
  };
}

function loadImage(url) {
  return new Promise((resolve, reject) => {
    const image = new Image();
    image.onload = () => resolve(image);
    image.onerror = () => reject(new Error("texture image did not decode"));
    image.src = url;
  });
}

export const modelViewMethods = {
  // Called by _initPreviewView for a view that holds a .model-view.
  _initModelView(view) {
    this._disposeModelView();
    const stage = view.querySelector(".model-stage");
    if (!stage) return; // a mesh with no triangles shows a note instead
    const mesh = stageMesh(stage);
    const shading = view.querySelector('button[data-action="model-shading"].active')?.dataset.value ?? "solid";
    try {
      this._modelRenderer = new ModelRenderer(stage.querySelector("canvas"), mesh, shading);
    } catch (error) {
      if (!(error instanceof WebGLUnavailableError)) throw error;
      const note = document.createElement("div");
      note.className = "model-note";
      note.textContent = t("preview.webglMissing");
      stage.replaceChildren(note);
      return;
    }
    if (mesh.uvs) this._loadModelTextures(view, this._modelRenderer, mesh.submeshes);
    if (stage.dataset.rig) {
      this._modelRig = new ModelRig(view, this._modelRenderer, mesh, this._selectedPath);
      this._modelRig.start();
    }
  },

  // Fetches each texture the parts name, once, and counts the ones found in
  // the toolbar; the names it could not find go in the count's tooltip.
  async _loadModelTextures(view, renderer, submeshes) {
    const names = [...new Set(submeshes.map(([, , name]) => name).filter(Boolean))];
    const status = view.querySelector(".model-textures");
    const path = this._selectedPath;
    const missing = [];
    let loaded = 0;
    const show = () => {
      if (!status) return;
      status.textContent = t("preview.modelTextures", { loaded, total: names.length });
      status.title = missing.join("\n");
    };
    show();
    await Promise.all(
      names.map(async (name) => {
        const result = await window.pywebview.api.get_model_texture(path, name);
        if (renderer !== this._modelRenderer) return;
        try {
          if (!result.url) throw new Error(result.error);
          const image = await loadImage(result.url);
          if (renderer !== this._modelRenderer) return;
          renderer.setTexture(name, image);
          loaded += 1;
        } catch (error) {
          missing.push(error.message || name);
        }
        show();
      }),
    );
  },

  _setModelShading(mode) {
    this._modelRenderer?.setShading(mode);
  },

  _resetModelView() {
    this._modelRenderer?.reset();
  },

  _toggleModelBones(button) {
    this._modelRig?.toggleBones(button);
  },

  _toggleModelPlay() {
    this._modelRig?.togglePlay();
  },

  _disposeModelView() {
    this._modelRig?.dispose();
    this._modelRig = null;
    this._modelRenderer?.dispose();
    this._modelRenderer = null;
  },
};
