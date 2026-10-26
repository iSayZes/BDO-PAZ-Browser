"use strict";

// Vector and camera matrix helpers of the Model view (model-renderer.js).

export function clamp(value, low, high) {
  return Math.min(high, Math.max(low, value));
}

export function cross(a, b) {
  return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
}

export function normalize(vector) {
  const length = Math.hypot(...vector) || 1;
  return vector.map((value) => value / length);
}

// Column-major 4 x 4 matrices, as WebGL reads them.
export function perspective(fieldOfView, aspect, near, far) {
  const f = 1 / Math.tan(fieldOfView / 2);
  const depth = 1 / (near - far);
  return new Float32Array([
    f / aspect, 0, 0, 0,
    0, f, 0, 0,
    0, 0, (far + near) * depth, -1,
    0, 0, 2 * far * near * depth, 0,
  ]);
}

export function lookAt(eye, target) {
  const back = normalize(eye.map((value, axis) => value - target[axis]));
  const right = normalize(cross([0, 1, 0], back));
  const up = cross(back, right);
  const dot = (axis) => -(axis[0] * eye[0] + axis[1] * eye[1] + axis[2] * eye[2]);
  return new Float32Array([
    right[0], up[0], back[0], 0,
    right[1], up[1], back[1], 0,
    right[2], up[2], back[2], 0,
    dot(right), dot(up), dot(back), 1,
  ]);
}

export function multiply(a, b) {
  const out = new Float32Array(16);
  for (let column = 0; column < 4; column += 1) {
    for (let row = 0; row < 4; row += 1) {
      let sum = 0;
      for (let k = 0; k < 4; k += 1) sum += a[k * 4 + row] * b[column * 4 + k];
      out[column * 4 + row] = sum;
    }
  }
  return out;
}
