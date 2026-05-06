"use strict";

export const setupMethods = {
  _setupOutputPathSave() {
    document.getElementById("output-path").addEventListener("change", (e) => {
      localStorage.setItem("outputPath", e.target.value);
    });
  },

  _setupImageZoom() {
    const content = document.getElementById("preview-content");
    content.addEventListener("wheel", (e) => {
      if (!e.ctrlKey) return;
      const img = content.querySelector(".img-view img");
      if (!img) return;
      e.preventDefault();
      const current = parseFloat(img.style.zoom) || 1;
      const delta = e.deltaY < 0 ? 0.1 : -0.1;
      img.style.zoom = Math.max(0.1, Math.round((current + delta) * 10) / 10);
    }, { passive: false });
  },

  _initStreamThumbnails(root) {
    root.querySelectorAll('video[data-stream-thumbnail="first-frame"]').forEach((video) => {
      this._createVideoPoster(video);
    });
  },

  _createVideoPoster(video) {
    if (video.dataset.thumbnailStarted === "1") return;
    video.dataset.thumbnailStarted = "1";

    const cleanup = () => {
      video.removeEventListener("loadedmetadata", onLoadedMetadata);
      video.removeEventListener("seeked", onSeeked);
      video.removeEventListener("error", cleanup);
    };

    const onSeeked = () => {
      try {
        const canvas = document.createElement("canvas");
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const ctx = canvas.getContext("2d");
        if (!ctx || canvas.width === 0 || canvas.height === 0) return;
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        video.poster = canvas.toDataURL("image/jpeg", 0.82);
      } catch (_) {
        // Browser decode/canvas restrictions vary; normal video playback is fallback.
      } finally {
        cleanup();
        video.currentTime = 0;
      }
    };

    const onLoadedMetadata = () => {
      if (!Number.isFinite(video.duration) || video.videoWidth === 0 || video.videoHeight === 0) {
        cleanup();
        return;
      }
      const targetTime = Math.min(0.1, Math.max(0, video.duration / 20));
      try {
        video.currentTime = targetTime;
      } catch (_) {
        cleanup();
      }
    };

    video.addEventListener("loadedmetadata", onLoadedMetadata, { once: true });
    video.addEventListener("seeked", onSeeked);
    video.addEventListener("error", cleanup, { once: true });
  },

  _setupEscapeClear() {
    document.addEventListener("keydown", (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "f") {
        e.preventDefault();
        this.openTabSearch();
        return;
      }
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "r") {
        e.preventDefault();
        window.pywebview.api.reload_plugins();
        return;
      }
      if (e.key === "Escape" && this._extractPaths.size > 0) {
        this._clearExtractSelection();
      }
    });
  },
};
