"use strict";

import { clamp, cross, lookAt, multiply, normalize, perspective } from "./model-math.js";

// A WebGL 2 view of one triangle mesh: orbit, pan and zoom around its
// bounding box, lit from the camera with its textures or a tint per part, or
// a wireframe, with the bones of a skeleton drawn over it as lines. Draws
// only when something changed. model-view.js makes one per Model tab and
// hands it the textures as they arrive; model-rig.js poses it.

const FIELD_OF_VIEW = Math.PI / 4;
const START_YAW = Math.PI / 4;
const START_PITCH = 0.35;
const MAX_PITCH = Math.PI / 2 - 0.01;
const ORBIT_RADIANS_PER_PIXEL = 0.008;
const ZOOM_STEP = 1.15;
// The fitted camera leaves this much room around the bounding sphere.
const FIT_MARGIN = 1.1;
const MIN_DISTANCE_FACTOR = 0.01;
const MAX_DISTANCE_FACTOR = 100;
const NEAR_FACTOR = 0.005;
const MOUSE_PRIMARY = 0;
const MOUSE_MIDDLE = 1;
const MOUSE_SECONDARY = 2;
const BYTES_PER_INDEX = 4;
// Muted tints that set the submeshes apart, used in turn.
const SUBMESH_TINTS = [
  [0.78, 0.76, 0.72],
  [0.6, 0.71, 0.8],
  [0.8, 0.69, 0.56],
  [0.64, 0.78, 0.66],
  [0.76, 0.66, 0.79],
  [0.8, 0.78, 0.58],
];
// --color-accent
const WIRE_COLOR = [0.886, 0.663, 0.31];
// Bones show through the mesh in a cool tone that the wood and skin tints lack.
const BONE_COLOR = [0.35, 0.85, 0.95];

const VERTEX_SHADER = `#version 300 es
in vec3 a_position;
in vec3 a_normal;
in vec2 a_uv;
uniform mat4 u_viewProjection;
out vec3 v_normal;
out vec2 v_uv;
void main() {
  v_normal = a_normal;
  v_uv = a_uv;
  gl_Position = u_viewProjection * vec4(a_position, 1.0);
}`;

// Lit from the camera, both faces alike: the meshes hold single-sided
// foliage and decals whose back faces the camera as often as not. A texel
// with alpha under one half is cut out: leaves are quads in an alpha mask,
// and overlay strips (moss, edge trim) are transparent where they are not
// drawn.
const FRAGMENT_SHADER = `#version 300 es
precision mediump float;
in vec3 v_normal;
in vec2 v_uv;
uniform vec3 u_color;
uniform vec3 u_toCamera;
uniform bool u_isLit;
uniform bool u_hasTexture;
uniform sampler2D u_texture;
out vec4 outColor;
void main() {
  if (!u_isLit) {
    outColor = vec4(u_color, 1.0);
    return;
  }
  vec4 texel = u_hasTexture ? texture(u_texture, v_uv) : vec4(u_color, 1.0);
  if (texel.a < 0.5) discard;
  vec3 base = texel.rgb;
  vec3 normal = normalize(v_normal);
  float facing = abs(dot(normal, u_toCamera));
  float sky = 0.5 + 0.5 * normal.y;
  outColor = vec4(base * (0.22 + 0.13 * sky + 0.65 * facing), 1.0);
}`;

const UNIFORMS = ["u_viewProjection", "u_color", "u_toCamera", "u_isLit", "u_hasTexture", "u_texture"];

export class WebGLUnavailableError extends Error {}

export class ModelRenderer {
  // `mesh.positions`: x, y, z per vertex; `mesh.uvs`: u, v per vertex, or
  // null; `mesh.indices`: triangle corners; `mesh.submeshes`: [first index,
  // index count, texture name] per part. `shading` is "textured", "solid"
  // or "wire".
  constructor(canvas, mesh, shading) {
    const gl = canvas.getContext("webgl2", { antialias: true });
    if (!gl) throw new WebGLUnavailableError("WebGL 2 is not available");
    const { positions, uvs, indices, submeshes } = mesh;
    this._canvas = canvas;
    this._gl = gl;
    this._indices = indices;
    this._submeshes = submeshes;
    this._shading = shading;
    // Texture name -> WebGL texture, as setTexture() gets them.
    this._textures = new Map();
    this._lineBuffer = null;
    // Bone lines: two x, y, z ends per bone, or null when hidden.
    this._boneLineCount = 0;
    this._isDrawQueued = false;
    this._isDisposed = false;
    this._bounds = meshBounds(positions);

    this._program = linkProgram(gl, VERTEX_SHADER, FRAGMENT_SHADER);
    this._uniforms = Object.fromEntries(
      UNIFORMS.map((name) => [name, gl.getUniformLocation(this._program, name)]),
    );
    this._vertexArray = gl.createVertexArray();
    gl.bindVertexArray(this._vertexArray);
    this._positionBuffer = this._attribute("a_position", positions, 3);
    this._normalBuffer = this._attribute("a_normal", vertexNormals(positions, indices), 3);
    this._uvBuffer = uvs ? this._attribute("a_uv", uvs, 2) : null;
    this._triangleBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this._triangleBuffer);
    gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indices, gl.STATIC_DRAW);

    this._boneArray = gl.createVertexArray();
    gl.bindVertexArray(this._boneArray);
    this._boneBuffer = this._attribute("a_position", new Float32Array(0), 3, gl.DYNAMIC_DRAW);
    gl.bindVertexArray(null);

    this.reset();
    this._listen();
    this._resizeObserver = new ResizeObserver(() => this._resize());
    this._resizeObserver.observe(canvas);
  }

  // Posed positions and normals, x, y, z per vertex, in place of the bind pose.
  setVertices(positions, normals) {
    if (this._isDisposed) return;
    const gl = this._gl;
    gl.bindBuffer(gl.ARRAY_BUFFER, this._positionBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, positions, gl.DYNAMIC_DRAW);
    gl.bindBuffer(gl.ARRAY_BUFFER, this._normalBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, normals, gl.DYNAMIC_DRAW);
    this._requestDraw();
  }

  // Line ends, x, y, z each, two per bone; null hides the bones.
  setBoneLines(ends) {
    if (this._isDisposed) return;
    const gl = this._gl;
    this._boneLineCount = ends ? ends.length / 3 : 0;
    if (ends) {
      gl.bindBuffer(gl.ARRAY_BUFFER, this._boneBuffer);
      gl.bufferData(gl.ARRAY_BUFFER, ends, gl.DYNAMIC_DRAW);
    }
    this._requestDraw();
  }

  // Fits the camera to `points` (x, y, z each) in place of the mesh: a view
  // with no triangles shows only its bones.
  fitPoints(points) {
    this._bounds = meshBounds(points);
    this.reset();
  }

  setShading(mode) {
    this._shading = mode;
    this._requestDraw();
  }

  // The decoded image of texture `name`, for every submesh that names it.
  setTexture(name, image) {
    if (this._isDisposed) return;
    const gl = this._gl;
    const texture = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, texture);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image);
    gl.generateMipmap(gl.TEXTURE_2D);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR);
    this._textures.set(name, texture);
    this._requestDraw();
  }

  // The three-quarter view that fits the whole mesh.
  reset() {
    const { center, radius } = this._bounds;
    this._target = [...center];
    this._yaw = START_YAW;
    this._pitch = START_PITCH;
    this._distance = (radius * FIT_MARGIN) / Math.sin(FIELD_OF_VIEW / 2);
    this._requestDraw();
  }

  dispose() {
    if (this._isDisposed) return;
    this._isDisposed = true;
    this._resizeObserver.disconnect();
    this._abort.abort();
    const gl = this._gl;
    [this._positionBuffer, this._normalBuffer, this._uvBuffer, this._triangleBuffer, this._lineBuffer,
      this._boneBuffer].forEach(
      (buffer) => {
        if (buffer) gl.deleteBuffer(buffer);
      },
    );
    this._textures.forEach((texture) => gl.deleteTexture(texture));
    gl.deleteVertexArray(this._vertexArray);
    gl.deleteVertexArray(this._boneArray);
    gl.deleteProgram(this._program);
    gl.getExtension("WEBGL_lose_context")?.loseContext();
  }

  _attribute(name, values, size, usage = this._gl.STATIC_DRAW) {
    const gl = this._gl;
    const buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.bufferData(gl.ARRAY_BUFFER, values, usage);
    const location = gl.getAttribLocation(this._program, name);
    gl.enableVertexAttribArray(location);
    gl.vertexAttribPointer(location, size, gl.FLOAT, false, 0, 0);
    return buffer;
  }

  _listen() {
    this._abort = new AbortController();
    const options = { signal: this._abort.signal };
    const canvas = this._canvas;
    let drag = null;

    canvas.addEventListener("pointerdown", (event) => {
      const isPan = event.button === MOUSE_SECONDARY || event.button === MOUSE_MIDDLE || event.shiftKey;
      if (event.button !== MOUSE_PRIMARY && !isPan) return;
      drag = { isPan, x: event.clientX, y: event.clientY };
      canvas.setPointerCapture(event.pointerId);
    }, options);
    canvas.addEventListener("pointermove", (event) => {
      if (!drag) return;
      const dx = event.clientX - drag.x;
      const dy = event.clientY - drag.y;
      drag.x = event.clientX;
      drag.y = event.clientY;
      if (drag.isPan) this._pan(dx, dy);
      else this._orbit(dx, dy);
    }, options);
    const endDrag = () => {
      drag = null;
    };
    canvas.addEventListener("pointerup", endDrag, options);
    canvas.addEventListener("pointercancel", endDrag, options);
    canvas.addEventListener("wheel", (event) => {
      event.preventDefault();
      this._zoom(Math.sign(event.deltaY));
    }, { ...options, passive: false });
    canvas.addEventListener("dblclick", () => this.reset(), options);
    canvas.addEventListener("contextmenu", (event) => event.preventDefault(), options);
  }

  _orbit(dx, dy) {
    this._yaw -= dx * ORBIT_RADIANS_PER_PIXEL;
    this._pitch = clamp(this._pitch + dy * ORBIT_RADIANS_PER_PIXEL, -MAX_PITCH, MAX_PITCH);
    this._requestDraw();
  }

  // Moves the target with the cursor: one pixel is one pixel's width of the
  // view at the target's distance.
  _pan(dx, dy) {
    const { right, up } = this._cameraAxes();
    const unitsPerPixel = (2 * this._distance * Math.tan(FIELD_OF_VIEW / 2)) / this._canvas.clientHeight;
    for (let axis = 0; axis < 3; axis += 1) {
      this._target[axis] += (-dx * right[axis] + dy * up[axis]) * unitsPerPixel;
    }
    this._requestDraw();
  }

  _zoom(direction) {
    const radius = this._bounds.radius;
    this._distance = clamp(
      this._distance * ZOOM_STEP ** direction,
      radius * MIN_DISTANCE_FACTOR,
      radius * MAX_DISTANCE_FACTOR,
    );
    this._requestDraw();
  }

  _resize() {
    if (!this._canvas.isConnected) {
      this.dispose();
      return;
    }
    const scale = window.devicePixelRatio || 1;
    this._canvas.width = Math.max(1, Math.round(this._canvas.clientWidth * scale));
    this._canvas.height = Math.max(1, Math.round(this._canvas.clientHeight * scale));
    this._requestDraw();
  }

  _requestDraw() {
    if (this._isDrawQueued || this._isDisposed) return;
    this._isDrawQueued = true;
    requestAnimationFrame(() => {
      this._isDrawQueued = false;
      if (!this._isDisposed) this._draw();
    });
  }

  // From the target towards the camera, unit length.
  _toCamera() {
    const flat = Math.cos(this._pitch);
    return [flat * Math.sin(this._yaw), Math.sin(this._pitch), flat * Math.cos(this._yaw)];
  }

  _cameraAxes() {
    const back = this._toCamera();
    const right = normalize(cross([0, 1, 0], back));
    return { right, up: cross(back, right) };
  }

  _draw() {
    const gl = this._gl;
    const toCamera = this._toCamera();
    const eye = this._target.map((value, axis) => value + toCamera[axis] * this._distance);
    const radius = this._bounds.radius;
    const near = radius * NEAR_FACTOR;
    const far = this._distance + radius * 2;
    const aspect = this._canvas.width / this._canvas.height;
    const viewProjection = multiply(perspective(FIELD_OF_VIEW, aspect, near, far), lookAt(eye, this._target));

    gl.viewport(0, 0, this._canvas.width, this._canvas.height);
    gl.clearColor(0, 0, 0, 0);
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
    gl.enable(gl.DEPTH_TEST);
    gl.useProgram(this._program);
    gl.bindVertexArray(this._vertexArray);
    gl.uniformMatrix4fv(this._uniforms.u_viewProjection, false, viewProjection);
    gl.uniform3fv(this._uniforms.u_toCamera, toCamera);

    if (this._shading === "wire") this._drawWire();
    else this._drawSolid();
    if (this._boneLineCount) this._drawBones();
  }

  // Over the mesh, depth test off, so the bones show through it.
  _drawBones() {
    const gl = this._gl;
    gl.disable(gl.DEPTH_TEST);
    gl.bindVertexArray(this._boneArray);
    gl.uniform1i(this._uniforms.u_isLit, 0);
    gl.uniform3fv(this._uniforms.u_color, BONE_COLOR);
    gl.drawArrays(gl.LINES, 0, this._boneLineCount);
    gl.bindVertexArray(this._vertexArray);
    gl.enable(gl.DEPTH_TEST);
  }

  // A part whose texture has not arrived (or does not exist) keeps its tint.
  _drawSolid() {
    const gl = this._gl;
    const isTextured = this._shading === "textured";
    gl.uniform1i(this._uniforms.u_isLit, 1);
    gl.uniform1i(this._uniforms.u_texture, 0);
    gl.activeTexture(gl.TEXTURE0);
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this._triangleBuffer);
    this._submeshes.forEach(([first, count, name], part) => {
      const texture = isTextured ? this._textures.get(name) : undefined;
      gl.uniform1i(this._uniforms.u_hasTexture, texture ? 1 : 0);
      if (texture) gl.bindTexture(gl.TEXTURE_2D, texture);
      gl.uniform3fv(this._uniforms.u_color, SUBMESH_TINTS[part % SUBMESH_TINTS.length]);
      gl.drawElements(gl.TRIANGLES, count, gl.UNSIGNED_INT, first * BYTES_PER_INDEX);
    });
  }

  // Each triangle's three edges as lines; a triangle's 3 corners become 6 line ends.
  _drawWire() {
    const gl = this._gl;
    if (!this._lineBuffer) {
      this._lineBuffer = gl.createBuffer();
      gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this._lineBuffer);
      gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, triangleEdges(this._indices), gl.STATIC_DRAW);
    }
    gl.uniform1i(this._uniforms.u_isLit, 0);
    gl.uniform3fv(this._uniforms.u_color, WIRE_COLOR);
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this._lineBuffer);
    gl.drawElements(gl.LINES, this._indices.length * 2, gl.UNSIGNED_INT, 0);
  }
}

function linkProgram(gl, vertexSource, fragmentSource) {
  const program = gl.createProgram();
  [[gl.VERTEX_SHADER, vertexSource], [gl.FRAGMENT_SHADER, fragmentSource]].forEach(([type, source]) => {
    const shader = gl.createShader(type);
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
      throw new Error(`shader: ${gl.getShaderInfoLog(shader)}`);
    }
    gl.attachShader(program, shader);
    gl.deleteShader(shader);
  });
  gl.linkProgram(program);
  if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
    throw new Error(`program: ${gl.getProgramInfoLog(program)}`);
  }
  return program;
}

function meshBounds(positions) {
  const min = [Infinity, Infinity, Infinity];
  const max = [-Infinity, -Infinity, -Infinity];
  for (let i = 0; i < positions.length; i += 3) {
    for (let axis = 0; axis < 3; axis += 1) {
      const value = positions[i + axis];
      if (value < min[axis]) min[axis] = value;
      if (value > max[axis]) max[axis] = value;
    }
  }
  if (positions.length === 0) return { center: [0, 0, 0], radius: 1 };
  const center = min.map((low, axis) => (low + max[axis]) / 2);
  const radius = Math.hypot(...max.map((high, axis) => high - min[axis])) / 2;
  return { center, radius: radius > 0 ? radius : 1 };
}

// Smooth normals: the area-weighted face normals around each vertex. A vertex
// on no triangle points up. model-rig.js skins these with the vertices.
export function vertexNormals(positions, indices) {
  const normals = new Float32Array(positions.length);
  for (let i = 0; i < indices.length; i += 3) {
    const a = indices[i] * 3;
    const b = indices[i + 1] * 3;
    const c = indices[i + 2] * 3;
    const u = [positions[b] - positions[a], positions[b + 1] - positions[a + 1], positions[b + 2] - positions[a + 2]];
    const v = [positions[c] - positions[a], positions[c + 1] - positions[a + 1], positions[c + 2] - positions[a + 2]];
    const face = cross(u, v);
    for (const corner of [a, b, c]) {
      normals[corner] += face[0];
      normals[corner + 1] += face[1];
      normals[corner + 2] += face[2];
    }
  }
  for (let i = 0; i < normals.length; i += 3) {
    const length = Math.hypot(normals[i], normals[i + 1], normals[i + 2]);
    if (length > 0) {
      normals[i] /= length;
      normals[i + 1] /= length;
      normals[i + 2] /= length;
    } else {
      normals[i + 1] = 1;
    }
  }
  return normals;
}

function triangleEdges(indices) {
  const lines = new Uint32Array(indices.length * 2);
  for (let i = 0, out = 0; i < indices.length; i += 3) {
    const [a, b, c] = [indices[i], indices[i + 1], indices[i + 2]];
    lines.set([a, b, b, c, c, a], out);
    out += 6;
  }
  return lines;
}
