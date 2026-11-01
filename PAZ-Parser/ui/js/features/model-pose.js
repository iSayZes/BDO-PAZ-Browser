"use strict";

// Posing the Model view: a .pab skeleton (Api.get_model_skeleton) and a
// .paa clip (Api.get_model_animation), as api/bdo_api_model_rigs.py sends
// them, turned into bone matrices, bone lines and skinned vertices.
//
// Matrices are 16 floats, row-major, acting on row vectors (v · M) as the
// files store them (docs/file-formats/other/skeleton_pab.md): the
// translation is the last row, and a bone's world matrix is its local
// matrix times its parent's. Times are milliseconds, lengths centimetres.

const MATRIX = 16;
// Per bone in `local`: scale x, y, z, rotation x, y, z, w, translation x, y, z.
const LOCAL = 10;
const SCALE_AT = 0;
const ROTATION_AT = 3;
const TRANSLATION_AT = 7;
const CHANNEL_SIZES = [3, 4, 3];
const BONES_PER_VERTEX = 4;

// The bytes of base64 `text` as a typed array of `ArrayType` (little-endian, as the API packs them).
export function decodeBase64(text, ArrayType) {
  const binary = atob(text);
  const bytes = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i += 1) bytes[i] = binary.charCodeAt(i);
  return new ArrayType(bytes.buffer);
}

export function decodeSkeleton(payload) {
  const ids = payload.ids;
  return {
    path: payload.path,
    isComplete: payload.isComplete,
    ids,
    names: payload.names,
    parents: payload.parents,
    world: decodeBase64(payload.world, Float32Array),
    inverseWorld: decodeBase64(payload.inverseWorld, Float32Array),
    local: decodeBase64(payload.local, Float32Array),
    indexById: new Map(ids.map((id, index) => [id, index])),
  };
}

// The clip's keys per skeleton bone: `tracks[bone]` is null for a bone the
// clip does not move, else [scale, rotation, translation], each
// { times, values } or null when that channel has no keys.
export function decodeClip(payload, skeleton) {
  const times = decodeBase64(payload.times, Uint16Array);
  const values = decodeBase64(payload.values, Float32Array);
  const tracks = new Array(skeleton.ids.length).fill(null);
  let timeAt = 0;
  let valueAt = 0;
  let movedBones = 0;
  for (const [boneId, ...counts] of payload.nodes) {
    const channels = counts.map((count, channel) => {
      const size = CHANNEL_SIZES[channel];
      const track = count
        ? { times: times.subarray(timeAt, timeAt + count), values: values.subarray(valueAt, valueAt + count * size) }
        : null;
      timeAt += count;
      valueAt += count * size;
      return track;
    });
    const bone = skeleton.indexById.get(boneId);
    if (bone !== undefined) {
      tracks[bone] = channels;
      movedBones += 1;
    }
  }
  return { path: payload.path, durationMs: payload.duration * 1000, tracks, movedBones };
}

// The world matrix of every bone at `timeMs` of `clip`, or the bind pose
// when `clip` is null, into `out` (bones x 16).
export function poseWorld(skeleton, clip, timeMs, out) {
  const { parents, local } = skeleton;
  const sample = new Float32Array(LOCAL);
  const own = new Float32Array(MATRIX);
  for (let bone = 0; bone < parents.length; bone += 1) {
    sample.set(local.subarray(bone * LOCAL, bone * LOCAL + LOCAL));
    const channels = clip?.tracks[bone];
    if (channels) {
      [SCALE_AT, ROTATION_AT, TRANSLATION_AT].forEach((at, channel) => {
        if (channels[channel]) sampleTrack(channels[channel], CHANNEL_SIZES[channel], timeMs, channel === 1, sample, at);
      });
    }
    composeLocal(sample, own);
    const parent = parents[bone];
    if (parent < 0) out.set(own, bone * MATRIX);
    else multiplyInto(own, 0, out, parent * MATRIX, out, bone * MATRIX);
  }
  return out;
}

// Two line ends per bone with a parent, from the parent's joint to its own.
export function boneLines(skeleton, world) {
  const { parents } = skeleton;
  const ends = [];
  for (let bone = 0; bone < parents.length; bone += 1) {
    const parent = parents[bone];
    if (parent < 0) continue;
    ends.push(...joint(world, parent), ...joint(world, bone));
  }
  return new Float32Array(ends);
}

// Every joint's position, x, y, z each, for fitting the camera.
export function jointPositions(world) {
  const count = world.length / MATRIX;
  const points = new Float32Array(count * 3);
  for (let bone = 0; bone < count; bone += 1) points.set(joint(world, bone), bone * 3);
  return points;
}

// The skeleton bone of each palette slot of a mesh, -1 for an id the
// skeleton lacks (the vertex keeps its bind position for that weight).
export function paletteBones(skeleton, palette) {
  return Int32Array.from(palette, (id) => skeleton.indexById.get(id) ?? -1);
}

// Linear blend skinning: each vertex's bind position and normal moved by
// the weighted bone matrices `inverseWorld · world`. `skin` holds the
// mesh's `positions`, `normals`, `boneIndices`, `boneWeights` and the
// `bones` of its palette slots; the result goes into `out.positions` and
// `out.normals`.
export function skinVertices(skeleton, world, skin, out) {
  const boneCount = skeleton.parents.length;
  const skinning = new Float32Array(boneCount * MATRIX);
  for (let bone = 0; bone < boneCount; bone += 1) {
    multiplyInto(skeleton.inverseWorld, bone * MATRIX, world, bone * MATRIX, skinning, bone * MATRIX);
  }
  const { positions, normals, boneIndices, boneWeights, bones } = skin;
  const vertexCount = positions.length / 3;
  for (let vertex = 0; vertex < vertexCount; vertex += 1) {
    const at = vertex * 3;
    const [x, y, z] = [positions[at], positions[at + 1], positions[at + 2]];
    const [nx, ny, nz] = [normals[at], normals[at + 1], normals[at + 2]];
    let [px, py, pz, qx, qy, qz, total] = [0, 0, 0, 0, 0, 0, 0];
    for (let k = 0; k < BONES_PER_VERTEX; k += 1) {
      const weight = boneWeights[vertex * BONES_PER_VERTEX + k];
      if (!weight) continue;
      total += weight;
      const bone = bones[boneIndices[vertex * BONES_PER_VERTEX + k]] ?? -1;
      if (bone < 0) {
        px += weight * x; py += weight * y; pz += weight * z;
        qx += weight * nx; qy += weight * ny; qz += weight * nz;
        continue;
      }
      const m = bone * MATRIX;
      px += weight * (x * skinning[m] + y * skinning[m + 4] + z * skinning[m + 8] + skinning[m + 12]);
      py += weight * (x * skinning[m + 1] + y * skinning[m + 5] + z * skinning[m + 9] + skinning[m + 13]);
      pz += weight * (x * skinning[m + 2] + y * skinning[m + 6] + z * skinning[m + 10] + skinning[m + 14]);
      qx += weight * (nx * skinning[m] + ny * skinning[m + 4] + nz * skinning[m + 8]);
      qy += weight * (nx * skinning[m + 1] + ny * skinning[m + 5] + nz * skinning[m + 9]);
      qz += weight * (nx * skinning[m + 2] + ny * skinning[m + 6] + nz * skinning[m + 10]);
    }
    if (!total) {
      out.positions.set([x, y, z], at);
      out.normals.set([nx, ny, nz], at);
      continue;
    }
    out.positions.set([px / total, py / total, pz / total], at);
    const length = Math.hypot(qx, qy, qz) || 1;
    out.normals.set([qx / length, qy / length, qz / length], at);
  }
}

function joint(world, bone) {
  const m = bone * MATRIX;
  return [world[m + 12], world[m + 13], world[m + 14]];
}

// The value of `track` at `timeMs` into `out` from `at`: the first key
// before the first time, the last after the last, and in between a linear
// blend (a normalised one for rotations, along the shorter arc).
function sampleTrack({ times, values }, size, timeMs, isRotation, out, at) {
  const last = times.length - 1;
  if (last === 0 || timeMs <= times[0]) {
    out.set(values.subarray(0, size), at);
    return;
  }
  if (timeMs >= times[last]) {
    out.set(values.subarray(last * size, last * size + size), at);
    return;
  }
  let low = 0;
  let high = last;
  while (high - low > 1) {
    const middle = (low + high) >> 1;
    if (times[middle] <= timeMs) low = middle;
    else high = middle;
  }
  const f = (timeMs - times[low]) / (times[high] - times[low]);
  const a = low * size;
  const b = high * size;
  let sign = 1;
  if (isRotation) {
    let dot = 0;
    for (let i = 0; i < size; i += 1) dot += values[a + i] * values[b + i];
    if (dot < 0) sign = -1;
  }
  for (let i = 0; i < size; i += 1) out[at + i] = values[a + i] * (1 - f) + sign * values[b + i] * f;
  if (isRotation) {
    const length = Math.hypot(out[at], out[at + 1], out[at + 2], out[at + 3]) || 1;
    for (let i = 0; i < size; i += 1) out[at + i] /= length;
  }
}

// Scale, rotation, translation (LOCAL floats) as a row-vector matrix: row i
// is scale i times column i of the rotation, the last row the translation.
function composeLocal(sample, out) {
  const [sx, sy, sz, x, y, z, w, tx, ty, tz] = sample;
  const [xx, yy, zz, xy, xz, yz, wx, wy, wz] = [x * x, y * y, z * z, x * y, x * z, y * z, w * x, w * y, w * z];
  out.set([
    sx * (1 - 2 * (yy + zz)), sx * 2 * (xy + wz), sx * 2 * (xz - wy), 0,
    sy * 2 * (xy - wz), sy * (1 - 2 * (xx + zz)), sy * 2 * (yz + wx), 0,
    sz * 2 * (xz + wy), sz * 2 * (yz - wx), sz * (1 - 2 * (xx + yy)), 0,
    tx, ty, tz, 1,
  ]);
}

// out[o..o+16] = a[ai..] · b[bi..]; `out` may be `b` at another offset.
function multiplyInto(a, ai, b, bi, out, o) {
  for (let row = 0; row < 4; row += 1) {
    for (let column = 0; column < 4; column += 1) {
      let sum = 0;
      for (let k = 0; k < 4; k += 1) sum += a[ai + row * 4 + k] * b[bi + k * 4 + column];
      out[o + row * 4 + column] = sum;
    }
  }
}
