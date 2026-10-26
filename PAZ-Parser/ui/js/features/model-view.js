"use strict";

import { t } from "../core/i18n.js";
import { ModelRenderer, WebGLUnavailableError } from "./model-renderer.js";

// The Model tab of the PAR meshes (.pam, .pcm, .pac): preview_views.py
// model_view_html puts the geometry on .model-stage as base64 data
// attributes, and one ModelRenderer draws it. Each texture comes from
// Api.get_model_texture once the mesh is drawn. A new view, or a canvas
// taken off the page, disposes the old renderer, so one WebGL context is
// alive.

function decodeBase64(text) {
  const binary = atob(text);
  const bytes = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i += 1) bytes[i] = binary.charCodeAt(i);
  return bytes.buffer;
}

function stageMesh(stage) {
  const uvs = stage.dataset.uvs;
  return {
    positions: new Float32Array(decodeBase64(stage.dataset.positions)),
    uvs: uvs ? new Float32Array(decodeBase64(uvs)) : null,
    indices: new Uint32Array(decodeBase64(stage.dataset.indices)),
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

  _disposeModelView() {
    this._modelRenderer?.dispose();
    this._modelRenderer = null;
  },
};
