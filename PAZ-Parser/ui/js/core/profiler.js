"use strict";

const DEFAULT_SLOW_MS = 16;

const PROFILED_METHODS = [
  "_loadTreeRoot",
  "_buildNode",
  "_toggleDir",
  "_selectFile",
  "switchTab",
  "_doSearch",
  "_gotoHexPage",
  "_gotoParsedPage",
  "_initTableSort",
  "_sortTable",
  "_doTabSearch",
  "_jumpToMatch",
  "_highlightHexOffset",
  "_highlightParsedRow",
];

function isEnabled() {
  const params = new URLSearchParams(window.location.search);
  return params.get("profile") === "1" || localStorage.getItem("bdoProfile") === "1";
}

function createStats() {
  return {
    calls: 0,
    totalMs: 0,
    maxMs: 0,
    lastMs: 0,
  };
}

function record(stats, name, duration) {
  const row = stats.get(name) ?? createStats();
  row.calls += 1;
  row.totalMs += duration;
  row.maxMs = Math.max(row.maxMs, duration);
  row.lastMs = duration;
  stats.set(name, row);
}

function formatReport(stats) {
  return [...stats.entries()]
    .map(([name, row]) => ({
      name,
      calls: row.calls,
      totalMs: Number(row.totalMs.toFixed(2)),
      avgMs: Number((row.totalMs / row.calls).toFixed(2)),
      maxMs: Number(row.maxMs.toFixed(2)),
      lastMs: Number(row.lastMs.toFixed(2)),
    }))
    .sort((a, b) => b.totalMs - a.totalMs);
}

export function installProfiler(app, options = {}) {
  if (!isEnabled() || window.appProfile) return;

  const slowMs = Number(options.slowMs ?? DEFAULT_SLOW_MS);
  const stats = new Map();

  for (const name of PROFILED_METHODS) {
    const fn = app[name];
    if (typeof fn !== "function") continue;

    app[name] = function profiledMethod(...args) {
      const start = performance.now();
      try {
        const result = fn.apply(this, args);
        if (result && typeof result.then === "function") {
          return result.finally(() => {
            const duration = performance.now() - start;
            record(stats, name, duration);
            if (duration >= slowMs) console.debug(`[profile] ${name}: ${duration.toFixed(2)} ms`);
          });
        }
        const duration = performance.now() - start;
        record(stats, name, duration);
        if (duration >= slowMs) console.debug(`[profile] ${name}: ${duration.toFixed(2)} ms`);
        return result;
      } catch (error) {
        const duration = performance.now() - start;
        record(stats, name, duration);
        throw error;
      }
    };
  }

  if ("PerformanceObserver" in window) {
    try {
      const observer = new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
          console.warn(`[profile] long task: ${entry.duration.toFixed(2)} ms`);
        }
      });
      observer.observe({ entryTypes: ["longtask"] });
    } catch {
      // Long Task API is best-effort and unavailable in some embedded Chromium builds.
    }
  }

  window.appProfile = {
    record(name, duration) {
      record(stats, name, duration);
      if (duration >= slowMs) console.debug(`[profile] ${name}: ${duration.toFixed(2)} ms`);
    },
    report() {
      const rows = formatReport(stats);
      console.table(rows);
      return rows;
    },
    reset() {
      stats.clear();
    },
  };

  console.info("[profile] BDO PAZ Browser JS profiler enabled. Use appProfile.report() for totals.");
}
